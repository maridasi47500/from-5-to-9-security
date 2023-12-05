#!/usr/bin/env python

import asyncio

import websockets
import json
import secrets
from radio1 import Radio1
JOIN = {}
WATCH = {}
MESSAGES = []


#message=""
async def start(websocket):
    """
    Handle a connection from the first player: start a new game.

    """
    # Initialize a Connect Four game, the set of WebSocket connections
    # receiving moves from this game, and secret access tokens.
    game = Radio1()
    connected = {websocket}

    join_key = secrets.token_urlsafe(12)
    JOIN[join_key] = game, connected

    watch_key = secrets.token_urlsafe(12)
    WATCH[watch_key] = game, connected

    try:
        # Send the secret access tokens to the browser of the first player,
        # where they'll be used for building "join" and "watch" links.
        event = {
            "type": "init",
            "join": join_key,
            "watch": watch_key,
        }
        await websocket.send(json.dumps(event))
        # Receive and process moves from the first player.
        await play(websocket, game, connected)
    finally:
        print("hey")
        #del JOIN[join_key]
        #del WATCH[watch_key]


async def replay(websocket,join_key):
        event = {
            "type": "play",
            "join": "azerty",
            "watch": "azerty"
        }
        await websocket.send(json.dumps(event))
async def replaywatch(websocket,join_key,connected):
        for message in MESSAGES:
            await websocket.send(json.dumps(message))
async def play(websocket,game, connected):
        event = {
            "type": "play",
            "join": "azerty",
            "watch": "azerty"
        }
        for connection in connected:
            await connection.send(json.dumps(event))
async def hey(websocket,join_key,text):
        game, connected = JOIN[join_key]
        event = {
                "text":text,
            "type": "discute",
            "join": "azerty",
            "watch": "azerty"
        }
        #await websocket.send(json.dumps(event))
        MESSAGES.insert(0,event)
        for connection in connected:
            await connection.send(json.dumps(event))
async def heyother(websocket,connected):
        event = {
            "type": "discute",
            "join": "azerty",
            "watch": "azerty"
        }
        for connection in connected:
            await connection.send(json.dumps(event))

async def join(websocket, join_key):
    """
    Handle a connection from the second player: join an existing game.

    """
    # Find the Connect Four game.
    try:
        print(JOIN)
        game, connected = JOIN[join_key]
    except KeyError:
        await error(websocket, "Game not found.")
        return

    # Register to receive moves from this game.
    connected.add(websocket)
    try:
        # Send the first move, in case the first player already played it.
        await replay(websocket, game)
        # Receive and process moves from the second player.
        await play(websocket, game, connected)
    finally:
        #connected.remove(websocket)
        print("hey")


async def watch(websocket, watch_key):
    """
    Handle a connection from a spectator: watch an existing game.

    """
    # Find the Connect Four game.
    try:
        game, connected = WATCH[watch_key]
    except KeyError:
        await error(websocket, "Game not found.")
        return

    # Register to receive moves from this game.
    connected.add(websocket)
    try:
        # Send previous moves, in case the game already started.

        await replaywatch(websocket, game,connected)
        await replay(websocket, game)
        # Keep the connection open, but don't receive any messages.
        await websocket.wait_closed()
    finally:
        connected.remove(websocket)


async def handler(websocket):
        websocket.send("CONNECT\naccept-version:1.0,1.1,2.0\n\n\x00\n")
        while True:

                    try:
                            #message="{}"
                            #try:
                            #       message=await websocket.recv()
                            #       await asyncio.sleep(0.5)
                            #       print(message,"message1")
                            #except websockets.ConnectionClosedOK:
                            #       print("error")#break
                            #print(message,"message2")
                            #try:
                            #       hey={"type":"play", "message":"HI !"}
                            #       await websocket.send(json.dumps(hey))
                            #       print("ok")
                            #       await asyncio.sleep(0.5)
                            #       #print(message,"message")
                            #except websockets.ConnectionClosedOK:
                            #       print("error")#break
                            message = await websocket.recv()
                            print(message, "mes")
                            event = json.loads(message)
                            print(event, "mes")

                            #assert event["type"] == "init"
                            print(("discute" in event), "discute")
                            if "type" in event and event["type"] == "discute":
                                   # Second player joins an existing game.

                                   await hey(websocket,event["join"],event["text"])

                            elif "join" in event:
                                   # Second player joins an existing game.
                                   print(event, event["join"])
                                   await join(websocket, event["join"])

                            elif "play" in event:
                                   # Second player joins an existing game.

                                   await play(websocket, Radio1(), "hey_joinkey")
                            elif "watch" in event:
                                   # Second player joins an existing game.
                                   await watch(websocket, event["watch"])
                            else:
                            # First player starts a new game.
                                   await start(websocket)
                    except websockets.ConnectionClosedOK:
                           print("error")#break
                           break

async def main():
        async with websockets.serve(handler, "", 8766):
                    await asyncio.Future()  # run forever



if __name__ == "__main__":
        asyncio.run(main())

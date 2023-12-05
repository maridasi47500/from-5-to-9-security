function showMessage(message) {
	  window.setTimeout(() => window.alert(message), 50);
}
function sendMove(websocket) {
	// Don't send moves for a spectator watching a game.
	   const params = new URLSearchParams(window.location.search);
	     if (params.has("watch")) {
	         return;
	           }
	
	             // When clicking a column, send a "play" event for a move in that column.
	                                         const event = {
	                                               type: "discute",
							 text: document.querySelector("#entry").value,
				               join: document.querySelector(".join").dataset.join,
	                                                     column: 1
	                                                         };
	                                                             websocket.send(JSON.stringify(event));
	                                                               }




	const websocket = new WebSocket("ws://localhost:8766/");
	   const board = document.querySelector(".board");
websocket.onopen = function(e) {
	  console.log("[open] Connection established");
	  console.log("Sending to server");


	     board.append("hey - yes");
		       const params = new URLSearchParams(window.location.search);
		           let event = { type: "init" };
		               if (params.has("join")) {
		                     // Second player joins an existing game.
		                           event.join = params.get("join");
				                document.querySelector(".join").dataset.join=params.get("join");
		                               } else if (params.has("watch")) {
		                                     // Spectator watches an existing game.
		                                           event.watch = params.get("watch");
		                                               } else {
		                                                     // First player starts a new game.
		                                                         }
		                                                             websocket.send(JSON.stringify(event));

};
	  websocket.onmessage = ({ data }) => {
		      console.log(data);
		      const event = JSON.parse(data);

		      switch (event.type) {
				    case "init":
				            // Create links for inviting the second player and spectators.
				               document.querySelector(".join").href = "?join=" + event.join;
				               document.querySelector(".join").dataset.join = event.join;
				                       document.querySelector(".watch").href = "?watch=" + event.watch;
				                       document.querySelector(".watch").dataset.watch = event.watch;
				                               break;
				      
			            case "discute":
				            // Update the UI with the move.
				               board.innerHTML += " - "+(event.text);
				                       break;
			            case "play":
				            // Update the UI with the move.
				               board.innerHTML += ("PLAY");
				                       break;
				                             case "win":
				                                     showMessage(`Player wins!`);
				                                             // No further messages are expected; close the WebSocket connection.
				                                                     websocket.close(1000);
				                                                             break;
				                                                                   case "error":
				                                                                           showMessage(event.message);
				                                                                                   break;
				                                                                                         default:
				                                                                                                 throw new Error(`Unsupported event type: ${event.type}.`);
				                                                                                                     }
				                                                                                                       };





$(function(){
	// Initialize the UI.





	     });

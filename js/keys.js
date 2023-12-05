// send keys to websocket and echo the response
	     const socket = new WebSocket('ws://localhost:8076/hello');

 $(function() {



	  
	  socket.addEventListener('open', function (event) {
	   
	       socket.send('Connection Established');
	        
	        });
	         
	          
	           
	           socket.addEventListener('message', function (event) {
	            
	                console.log(event.data);
	                 
	                 });

	                  
	                  const contactServer = () => {
	                   
	                       socket.send("Initialize");
	                        
	                        };

	                         
//	 function isOpen(ws) { return ws.readyState === ws.OPEN }
//     // create websocket
//         if (! ("WebSocket" in window)) WebSocket = MozWebSocket; // firefox
//             var socket = new WebSocket("ws://localhost:8076");
//
//                 // open the socket
//                     socket.onopen = function(event) {
//                         socket.send('connected\n');
//
//                             // show server response
//                                 socket.onmessage = function(e) {
//                                         $("#output").text(e.data);
//                                             }
//
//                                                 // for each typed key send #entry's text to server
//                                                     $("#entry").keyup(function (e) {
//							     if (!isOpen(socket)) return;
//                                                             socket.send($("#entry").attr("value")+"\n");
//                                                                 });
//                                                                     }
                                                                     });

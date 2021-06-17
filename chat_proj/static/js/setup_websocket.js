// WebSocket Connection Script
const roomName = JSON.parse(document.getElementById('room-name').textContent);   // collecte the JSON obj from the html-body tag
// JSON.parse() = Converts a JavaScript Object Notation (JSON) string into an object.
// JSON.parse() = JavaScript Object Notation (JSON) string  ->  JavaScript object

// [2nd Phase]
// collect the username which is sent back from the WS Server in the backend
const user_username = JSON.parse(document.getElementById('user_username').textContent);


// Creating the connection URL to the WebSocket
// websocket protocol
const ws_scheme = window.location.protocol == "https:" ? "wss" : "ws";
// host, that's been extracted from the browser
const ws_extracted_host_from_browser = window.location.host;
// consruct the URL set inside the app's (chatApp) "routing.py"
const ws_routing = '/ws/chat/';
// "roomName", the variable that collects the data from this pages "json_script" 
const roomName_collected_from_this_page_json_script = roomName;
// the entire URL value, that'll passed as param while creating new WebSocket obj
const ws_path =  ws_scheme + "://" + ws_extracted_host_from_browser + ws_routing + roomName_collected_from_this_page_json_script + "/";


// creating a new WebSocket obj, with different params; those param is CONSTRUCTING A URL 
// (but need to collect the "roomName", and we are sending back the roomName using the "room" view from "views.py", and the "room" view is getting that from the URL the users are typing after the "127.0.0.1:8080/chat/<user_inputed_chatroom_name>")
const chatSocket = new WebSocket(ws_path);


// Receives the that has been sent from the "chatApp/consumers.py" file's -> class "ChatRoomConsumer" -> func "tester_message"
// To receive a msg, we need to reference it via "chatSocket" created here
// "chatSocket.onmessage" gets running to receive the msg via "WS server"; DISPLAY MSG
chatSocket.onmessage = function (e) {
    const data = JSON.parse(e.data);    // whenver, we receive a msg, we're going to pull all the data that's received, then parsed it into JSON, then put inside the variable "data"
    console.log(data);
    // display the information/ msg that has been received in the "chatSocket.onmessage" func
    // default_msg_div = document.querySelector('#user-hello')  # don't need it after
    // default_msg_div.innerHTML = (data.tester)                # don't need it after

    // Display the message into the textarea, when the WS data got anything in the message in WS
    chat_msg_holder_div = document.querySelector('#chat-text-area')
    // chat_msg_holder_div.value += (data.message + '\n')   // updated LOC in next LOC

    // Display the username. sent from the backend
    chat_msg_holder_div.value += (data.username_backend + ': ' + data.message + '\n')
}
// Part-02 of "setup_websocket.js"
// js function to sending msg to the WebSocket Server

// a func for sending msg from the frontend will run after clicking the "send" btn
document.querySelector('#submit').onclick = (e) => {
    // collect the information from the "#input" field
    const messageInputDom = document.querySelector('#input');
    // get the value from messageInputDom (input text)
    const message = messageInputDom.value;
    // send the data into the WS server; 
    chatSocket.send(JSON.stringify({
        'message': message,
        "username": user_username,
    }));
    // after sending msg to WS server, clear the "#input" field
    messageInputDom.value = '';
};

// Now we need to handle our sent msg inside the consumer "ChatRoomConsumer" inside the "chatApp/consumers.py" file's 

// JSON.stringify() = Converts a JavaScript value to a JavaScript Object Notation (JSON) string
// JSON.stringify() = JavaScript object/ value  ->  JavaScript Object Notation (JSON) string
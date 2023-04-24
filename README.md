# Python-command-line-chat-application

 So far implements a simple command-line chat application using Python's built-in socket module and the select module for handling multiple client connections. This application allows multiple clients to connect to a single server and chat with each other.

<hr/>

> ### Run 
- `pipenv shell`
- `pipenv instal socket select`


> To implement:

Ability for clients to send messages to the server, which will then broadcast the message to all connected clients.
Ability for clients to choose a username, which will be displayed alongside their messages.
Ability for clients to send private messages to specific clients.
Ability for clients to see a list of currently connected clients.
Ability for clients to leave the chat room.
Add error handling for when a client disconnects unexpectedly.
Add security measures, such as password-protected rooms or encryption for messages.
Implement persistent storage of chat logs and client information.
Add the ability to send images or other files in addition to text messages.
Implement audio or video chat capabilities.

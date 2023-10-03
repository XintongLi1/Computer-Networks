# Overview

This program consists of a client and server implementation to demonstrate a two-stage communication process: a negotiation stage using TCP and a transaction stage using UDP.

### Techniques Used:

* **TCP (Transmission Control Protocol)**: Used in the negotiation stage for reliable, ordered and error-checked delivery of a stream of bytes between applications.
* **UDP (User Datagram Protocol)**: Used in the transaction stage for a simple transmission mechanism without guarantee of data delivery.
* **Socket Programming**: Provides the necessary methods and functionalities for communication between client and server.


### Network Knowledge Applied:

1. Understanding of TCP and its connection-oriented nature.
2. Understanding of UDP.
3. Basics of Socket Programming: How to create, bind, listen, and accept connections for server sockets and how to connect, send, and receive data for client sockets.


### How to Run:

#### Running the Server:

Run the following command:
`python server.py <req_code> <req_lim>`

* `<req_code>` is an integer that the client must send correctly to negotiate.
* `<req_lim>` is the limit of requests the server will handle in the UDP transaction stage before it sends a "LIMIT" response to the client.

The server will display its SERVER_PORT and will begin listening for incoming client connections. It will also display the negotiated `r_port` for each connection.

#### Running the Client:

Run the following command:
`python client.py <server_address> <n_port> <req_code> <message1> <message2> ...`

* `<server_address>` is the address (IP or hostname) of the server.
* `<n_port>` is the port on which the server is listening for TCP connections.
* `<req_code>` is the request code that should match with the server.
* `<message1>, <message2>, ...`  will be sent to the server in the transaction stage.

The client will display the negotiated `r_port` and then display the results for each request sent to the server in the UDP transaction stage.


# Microservices_APZ
Code for all tasks from apz, featuring a simple microservice

Additional tasks: retry, dublication, gRPC protocol

facade_service.py - facade service for client-server communication. Receives get or post requests from the client and manages them (runs on localhost: 8080)

logging_service.py - stores all messages that are snt by facade_service via grpc protocol, sends back all the messages when receives a GET request (runs on localhost: 8081)

messages_service - currently not implemented, sends back "not implemented" message when receives a GET request (runs on localhost: 8082)


logging.proto defines the gRPC service interface for the logging system.

It specifies the available RPC methods and message formats using Protocol Buffers (protobuf).

This file allows automatic generation of client and server code.

the rest of the files - logging_pb2.py and logging_pb2_grc.py where generated using this command:

`python -m grpc_tools.protoc -I=proto --python_out=. --grpc_python_out=. proto/messages.proto`

test_requests_get.sh - test file with bash code for sending a GET request

test_requests_post.sh - test file with bash code for sending POST request

Usage:

run all 3 microservices in separate terminals

facade:

![image](images/first.jpg)

logging:

![image](images/second.jpg)

messages:

![image](images/third.jpg)

than run the bash scripts:

first GET request, when logging hash map is empty:

![image](images/fifth.jpg)

facade service prints:

![image](images/fourth.jpg)

messages service prints:

![image](images/six.jpg)

A POST request:

![image](images/seven.jpg)

facade service prints:

![image](images/eights.jpg)

Now we'll do another GET request:

![image](images/nine.jpg)

facade service:

![image](images/tenth.jpg)


Now, let's try to send the same message, without changing anything:
![image](images/11.jpg)

facade service:
![image](images/12.jpg)

Now, a POST service with a different message:
![image](images/13.jpg)

facade service:

![image](images/14.jpg)

Now, let's check with GET:

![image](images/15.jpg)


To show that retry mechanism works, we'll shut down the logging server and try and post something there:

![image](images/16.jpg)

facade service:
![image](images/18.jpg)

as you can see, facade_service tried to send the message three times, but encountered a 

gRPC UNAVAILABLE error, only then did it state that the POST request failed and returned code 500:

![image](images/17.jpg)








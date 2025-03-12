# Microservices_APZ
Continuing the tasks, 
Code for task 3 from apz, featuring a simple microservice

Additional tasks: config service

facade_service.py - facade service for client-server communication. Receives get or post requests from the client and manages them (runs on localhost: 8080)

logging_service.py - stores all messages that are snt by facade_service via grpc protocol, sends back all the messages when receives a GET request (runs on localhost: 8082, 8083, 8084), stores data by running a hazelcast client

and storing everything in a distributed map

messages_service - currently not implemented, sends back "not implemented" message when receives a GET request (runs on localhost: 8081)

config_service.py - handles storing of ip addresses for instances of logging-services and messages-service

test_requests_get.sh - test file with bash code for sending a GET request

test_requests_post.sh - test file with bash code for sending POST request

config.txt - if you decide to change the ports in code for messages or logging service, modify this file too. Config example for stating the service addresses

Usage:

start hazelcast

run all 4 microservices in separate terminals

i fixed code a little bit while servers were running to check if duplicated messages still work for separate logging services, so msg1 was sent

multiple times

{./images/1.jpg}

{./images/2.jpg}

{./images/3.jpg}

{./images/4.jpg}











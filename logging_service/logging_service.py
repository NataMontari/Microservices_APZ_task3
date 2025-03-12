import grpc
from concurrent import futures
import logging
import hazelcast
from proto import logging_pb2
from proto import logging_pb2_grpc
import sys



class LoggingService(logging_pb2_grpc.LoggingServiceServicer):
    def __init__(self, port):
        self.hz_client = hazelcast.HazelcastClient()
        self.message_map = self.hz_client.get_map(f"messages_{port}").blocking()
    
    def LogMessage(self, request, context):

        if request.message in self.message_map.values():
            return logging_pb2.LogResponse(status="Duplicate message ignored")

        self.message_map.put(request.id, request.message)
        return logging_pb2.LogResponse(status="Message logged successfully")
    
    def GetMessages(self, request, context):
        return logging_pb2.MessagesResponse(messages = list(self.message_map.values()))
    
def serve(port):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers = 10))
    logging_pb2_grpc.add_LoggingServiceServicer_to_server(LoggingService(port), server)
    server.add_insecure_port(f'[::]:{port}')

    logging.info(f"Starting gRPC server on port {port}...")
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    if len(sys.argv) < 2:
        raise Exception("Please enter a port number from 8082 to 8084")
    port = int(sys.argv[1])  # Перетворюємо на int
    if port < 8082 or port > 8084:
       raise Exception("Please enter a port number from 8082 to 8084")
    serve(port)
import time
import grpc
from concurrent import futures

import grpc_concepts_pb2
import grpc_concepts_pb2_grpc

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class HelloWorldServicer(grpc_concepts_pb2_grpc.HelloServiceServicer):
    """Provide method functionalities for the hellowrold server"""

    def SayHello(self, request, context):
        greeting = request.greeting
        print("received: {}".format(greeting))
        return grpc_concepts_pb2.HelloResponse(reply="{} to you".format(greeting))

    def LotsOfReplies(self, request, context):
        for i in range(20):
            yield grpc_concepts_pb2.HelloResponse(
                reply="{} to you for the {} time".format(request.greeting, i)
            )
    def LotsOfGreetings(self, request, context):
        
        return grpc_concepts_pb2.HelloResponse(
            reply="Received all {} greetings".format(len([req for req in request]))
        )
    
    def BidiHello(self, request, context):
        for req in request:
            yield grpc_concepts_pb2.HelloResponse(
                reply="{} to you".format(req.greeting)
            )


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    grpc_concepts_pb2_grpc.add_HelloServiceServicer_to_server(
        HelloWorldServicer(), server
    )
    server.add_insecure_port("[::]:50051")
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == "__main__":
    serve()


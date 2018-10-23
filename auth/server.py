import time
import grpc
from concurrent import futures

import authentication_example_pb2, authentication_example_pb2_grpc


_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class HelloWorldServicer(authentication_example_pb2_grpc.HelloServiceServicer):
    """Provide method functionalities for the hellowrold server"""

    def SayHello(self, request, context):
        print(request)
        print("received: {}".format(greeting))
        return authentication_example_pb2.HelloResponse(reply="{} to you".format(request.greeting))


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    authentication_example_pb2_grpc.add_HelloServiceServicer_to_server(
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


import time
import grpc
from concurrent import futures

import ssl_grpc_pb2, ssl_grpc_pb2_grpc


_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class HelloWorldServicer(ssl_grpc_pb2_grpc.HelloServiceServicer):
    """Provide method functionalities for the hellowrold server"""

    def SayHello(self, request, context):
        metadata = context.invocation_metadata()
        print('metadata: {}'.format(metadata))
        print(request)
        print("received: {}".format(request))
        return ssl_grpc_pb2.HelloResponse(reply="{} to you".format(request.greeting))


def serve():
    # read certificate key
    with open("server.key", "rb") as f:
        private_key = f.read()
    with open("server.crt", "rb") as f:
        certificate_chain = f.read()

    # create server creds
    server_credentials = grpc.ssl_server_credentials(
        ((private_key, certificate_chain),)
    )
    # create server
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    ssl_grpc_pb2_grpc.add_HelloServiceServicer_to_server(HelloWorldServicer(), server)
    
    server.add_secure_port("[::]:50051", server_credentials)
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == "__main__":
    serve()


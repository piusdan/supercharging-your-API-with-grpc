import grpc
import ssl_grpc_pb2_grpc, ssl_grpc_pb2


def say_hello(stub):
    greeting = ssl_grpc_pb2.HelloRequest(greeting="Hello")
    metadata = [('api-key', 'my api key'),]
    resp = stub.SayHello(greeting, metadata=metadata)
    print(resp)


def main():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    # read cerificate
    with open('server.crt', 'rb') as f:
        trusted_certs = f.read()
    # create credentials

    creds = grpc.ssl_channel_credentials(root_certificates=trusted_certs)

    # create channel
    with grpc.secure_channel("localhost:50051", creds) as channel:
        stub = ssl_grpc_pb2_grpc.HelloServiceStub(channel)
        print("-------------- SayHello --------------")
        say_hello(stub)


if __name__ == "__main__":
    main()


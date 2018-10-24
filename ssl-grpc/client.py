import grpc
import ssl_grpc_pb2_grpc, ssl_grpc_pb2


def say_hello(stub):
    greeting = ssl_grpc_pb2.HelloRequest(greeting="Hello")
    resp = stub.SayHello(greeting)
    print(resp)


def main():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = ssl_grpc_pb2_grpc.HelloServiceStub(channel)
        print("-------------- SayHello --------------")
        say_hello(stub)


if __name__ == "__main__":
    main()


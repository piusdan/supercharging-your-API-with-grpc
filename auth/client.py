import grpc
import authentication_example_pb2, authentication_example_pb2_grpc
import header_manipulator_client_interceptor


def say_hello(stub):
    greeting = authentication_example_pb2.HelloRequest(greeting="Hello")
    resp = stub.SayHello(greeting)
    print(resp)


def main():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    header_adder_interceptor = header_manipulator_client_interceptor.header_adder_interceptor(
        "api_key", "42"
    )
    with grpc.insecure_channel("localhost:50051") as channel:
        intercept_channel = grpc.intercept_channel(channel, header_adder_interceptor)
        stub = authentication_example_pb2_grpc.HelloServiceStub(intercept_channel)
        print("-------------- SayHello --------------")
        say_hello(stub)


if __name__ == "__main__":
    main()


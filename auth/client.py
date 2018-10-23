import grpc
import authentication_example_pb2, authentication_example_pb2_grpc

def say_hello(stub):
    greeting = authentication_example_pb2.HelloRequest(greeting="Hello")
    metadata = [
            ('client', 'localhost-client'),
            ('apikey', 'myapikey')
        ]
    resp = stub.SayHello(greeting, metadata=metadata)
    print(resp)


def main():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = authentication_example_pb2_grpc.HelloServiceStub(channel)
        print("-------------- SayHello --------------")
        
        say_hello(stub)




if __name__ == '__main__':
    main()
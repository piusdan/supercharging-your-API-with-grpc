import grpc
import grpc_concepts_pb2
import grpc_concepts_pb2_grpc

def _make_greetings():
    return map(lambda x: grpc_concepts_pb2.HelloRequest(greeting="Hello {}".format(x)), list(range(10)))

def say_hello(stub):
    greeting = grpc_concepts_pb2.HelloRequest(greeting="Hello")
    resp = stub.SayHello(greeting)
    print(resp)

def many_replies(stub):
    greeting = grpc_concepts_pb2.HelloRequest(greeting="Hello")
    for resp in stub.LotsOfReplies(greeting):
        print(resp)

def many_greetings(stub):
    response = stub.LotsOfGreetings(_make_greetings())
    print(response)

def bidi_greetings(stub):
    responses = stub.BidiHello(_make_greetings())
    for response in responses:
        print(response)


def main():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = grpc_concepts_pb2_grpc.HelloServiceStub(channel)
        print("-------------- SayHello --------------")
        say_hello(stub)
        print("------------- Lotsof Replies ----------")
        many_replies(stub)
        print("------------- Lots of greetings  ----------")
        many_greetings(stub)
        print("------------- Bidirectional greetings  ----------")
        bidi_greetings(stub)




if __name__ == '__main__':
    main()
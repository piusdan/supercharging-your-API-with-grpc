Supercharging your APIs with gRPC
=============================

## Code walkthrough

#### Installation

Make a python virtual environment

```bash
$ python3 -m venv .venv && source .venv/bin/activate
```

Install the `grpcio-tools` package

```bash 
$ pip install grpcio-tools
```

Install the `googleapis-common-proto` package

```bash
$ pip install googleapis-common-protos
```

#### Generating python-code

```bash
$ python -m grpc_tools.protoc -I $SRC_dIR --python_out=$DEST_DIR --grpc_python_out=. $SRC_DIR/$proto_file
```

### working with examples

1. Generate stubs
```bash 
$ make stubs
```

2. Start client
```bash
$ make client
```

3. Start server
```bash
$ make server
```

4. Generate ssl certs
```bash
$ make gen_key
```

###### References

[gRPC documentation](https://grpc.io/docs/quickstart/python.html)
[Authetication](https://grpc.io/docs/guides/auth.html#python)
[Using SSL](https://www.sandtable.com/using-ssl-with-grpc-in-python)
LoadBalancing [gRPC blog](https://grpc.io/blog/)
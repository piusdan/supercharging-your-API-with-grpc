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
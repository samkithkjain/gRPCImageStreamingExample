# gRPC - Simple Server Streaming and Interceptors in Python

- The example simply generate 10 random images at the server side and streams them when a client call is made. 
- On the client side we have an interceptor which will log the time stamp of images received.

To regenerate python server/client code:

```bash
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. image_transfer.proto
```

To run server
```bash
python3 imageStreamingServer.py
```

To run client
```bash
python3 imageStreamingClient.py
```

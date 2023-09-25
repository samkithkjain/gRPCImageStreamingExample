# Comparing Protobuf based file storage vs JSON based file storage 

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
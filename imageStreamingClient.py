import grpc
import image_transfer_pb2
import image_transfer_pb2_grpc
from PIL import Image
import io
from datetime import datetime

class TimestampStreamInterceptor(grpc.UnaryStreamClientInterceptor):
    def intercept_unary_stream(self, continuation, client_call_details, request_iterator):
        response_iterator = continuation(client_call_details, request_iterator)
        for response in response_iterator:
            timestamp = datetime.now()
            print(f"Received Image at at timestamp: {timestamp}")
            yield response

def receive_images():
    # Create a gRPC channel with the server
    channel = grpc.insecure_channel('localhost:50051')
    
    # Add the interceptor to the channel
    channel = grpc.intercept_channel(channel, TimestampStreamInterceptor())

    # Create a gRPC stub
    stub = image_transfer_pb2_grpc.ImageTransferStub(channel)

    # Create an ImageRequest with an empty message (no request data needed)
    request = image_transfer_pb2.ImageRequest()

    try:
        # Call the getImage RPC to receive a stream of images
        for response in stub.getImage(request):

            image_data = response.image_data

            # Do whatever with the image data!
            # Display or Save, etc

    except grpc.RpcError as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    receive_images()

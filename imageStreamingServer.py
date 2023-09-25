import grpc
from concurrent import futures
import image_transfer_pb2
import image_transfer_pb2_grpc
import time
from randimage import get_random_image

class ImageTransferServicer(image_transfer_pb2_grpc.ImageTransferServicer):
    # Sending 10 random images
    def getImage(self, request, context):
        for i in range(10):  
            
            print('Generating Image Randomly')
            image_data = get_random_image((128,128)).tobytes()

            # Create an ImageResponse message with the image data
            response = image_transfer_pb2.ImageResponse(image_data = image_data)
            
            # Yield the response to the client
            yield response

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    image_transfer_pb2_grpc.add_ImageTransferServicer_to_server(ImageTransferServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Server started on port 50051")
    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()

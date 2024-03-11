import requests

class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def upload_image(self, image_path):
        try:
            url = f"{self.base_url}/upload"  # Replace '/upload' with the endpoint path
            files = {'image': open(image_path, 'rb')}
            response = requests.post(url, files=files)
            response.raise_for_status()  # Raise exception for HTTP errors (e.g., 404, 500)
            print("Image uploaded successfully.")
            return True
        except requests.exceptions.RequestException as e:
            print(f"Error uploading image: {e}")
            return False


if __name__ == "__main__":
    api_client = APIClient(base_url="http://example.com/api")  
    api_client.upload_image("path/to/image.jpg")

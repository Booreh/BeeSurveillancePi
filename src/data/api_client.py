import requests

class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url
        
    def retrieveDeviceId(self, userid, hiveid, ipadress):
        try:
            url = f"{self.base_url}/V1/camera/setup/"
            params = {'user_id': userid, 'hive_id': hiveid, 'ipadress': ipadress}

            response = requests.post(url, params= params)
            response.raise_for_status()
            response_json = response.json()
            
            if "camera_id" in response_json:
                deviceID = response_json["camera_id"]
                return deviceID
            else:
                print("Error: 'camera_id' not found in response JSON.")
                return None
        except requests.exceptions.RequestException as e:
            print(f"Error retrieving device id: {e}")
            return False



        

    def upload_image(self, user_id, device_id, image_path):
        try:
            url = f"{self.base_url}/V1/images/cameraupload/"
            params = {'user_id': user_id, 'camera_id': device_id}
            files = {'file': open(image_path, 'rb')}
            
            response = requests.post(url, files=files, params=params)
        
            response.raise_for_status()
            print(f"image uploaded successfully. Response: {response.text}") 
            return True
        except requests.exceptions.RequestException as e:
            print(f"Error uploading image: {e}")
            return False





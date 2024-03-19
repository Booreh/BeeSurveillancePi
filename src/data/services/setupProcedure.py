from data.services.jsonUtils import read_json, write_json
import os
import random
import subprocess
import cv2
class SetupProcedure:
    def __init__(self):
        self.device_folder = "device"
        self.device_file = os.path.join(self.device_folder, "device.json")
        
    

    def checkCameraConnection(self):
        device_data = self.getDeviceData()
        try:
            capture = cv2.VideoCapture(device_data["camera_id"])
            if not capture.isOpened():
                print(f"Unable to connect to camera with id: {device_data["camera_id"]}. Please check the device for issues.")
                return False
            else:
                print("Camera Found")
                capture.release()
                return True
        except Exception as e:
            # Handling for any exceptions (e.g., OpenCV errors)
            print(f"Error while checking camera connection: {e}")
            return False


    #Run IDE as admin, may also need to turn of firewall
    def checkInternetAccess(self):
        try:
            subprocess.check_output(["ping", "-c", "1", "8.8.8.8"])
            return True
        except subprocess.CalledProcessError:
            print("No internet access!")
            return False
    
    

    def checkServerConnection(self):
        return True
    

    def generateDeviceId(self):
        return random.randint(1000, 9999)
    
    def getDeviceData(self):
        return read_json(self.device_file)
        

    def setDeviceData(self, device_data):
        if not os.path.exists(self.device_folder):
            os.makedirs(self.device_folder)
        write_json(device_data, self.device_file)


    
    def checkDeviceData(self):
        device_data = self.getDeviceData()
        if device_data:
            print(f"Device Identification found. deviceID: {device_data['device_id']} cameraID: {device_data['camera_id']}")
        else:
            print("No device Identification found. Generating new ones...")
            device_data = {"device_id": self.generateDeviceId(), "camera_id": 0}
            self.setDeviceData(device_data)
            print(f"New device ID ({device_data['device_id']}) and camera ID ({device_data['camera_id']}) generated.")
        return device_data

    
    
    


    def runAllSetupProcedures(self):
        """
        Runs all setup procedures.
        
        Returns:
            bool: True if all setup procedures succeed, False otherwise.
        """
        check_deviceData = self.checkDeviceData()
        camera_connected = self.checkCameraConnection()
        internet_access = self.checkInternetAccess()
        # Add more setup procedures here
        
        # Return True if all setup procedures succeed, False otherwise
        return camera_connected and internet_access and check_deviceData is not None

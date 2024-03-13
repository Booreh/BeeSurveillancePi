from data.services.jsonUtils import read_json, write_json
import os
import random
import subprocess
import cv2
class SetupProcedure:
    def __init__(self, camera_id=0):
        self.device_folder = "device"
        self.device_id_file = os.path.join(self.device_folder, "device_id.json")
        self.camera_id = camera_id
        




    def checkCameraConnection(self):
        
        try:
            capture = cv2.VideoCapture(self.camera_id)
            if not capture.isOpened():
                print(f"Unable to connect to camera ({self.camera_id}). Please check the device for issues.")
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
    
    def getDeviceId(self):
        data = read_json(self.device_id_file)
        if data:
            return data.get("device_id")
        else:
            return None

    def setDeviceId(self, device_id):
        if not os.path.exists(self.device_folder):
            os.makedirs(self.device_folder)
        write_json({"device_id": device_id}, self.device_id_file)


    
    def checkDeviceId(self):
        device_id = self.getDeviceId()
        if device_id:
            print(f"Device ID: {device_id}")
        else:
            print("No device ID found. Generating a new one...")
            device_id = self.generateDeviceId()
            self.setDeviceId(device_id)
            print(f"New device ID generated: {device_id}")

    
    
    


    def runAllSetupProcedures(self):
        """
        Runs all setup procedures.
        
        Returns:
            bool: True if all setup procedures succeed, False otherwise.
        """
        camera_connected = self.checkCameraConnection()
        internet_access = self.checkInternetAccess()
        check_deviceID = self.checkDeviceId()
        # Add more setup procedures here
        
        # Return True if all setup procedures succeed, False otherwise
        return camera_connected and internet_access and self.getDeviceId() is not None

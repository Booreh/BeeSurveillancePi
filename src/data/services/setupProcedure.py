from data.services.jsonUtils import read_json, write_json
import os
import random
import subprocess
import cv2
class SetupProcedure:
    def __init__(self):
        self.records_folder = "records"
        self.device_file = os.path.join(self.records_folder, "device.json")
        self.user_file = os.path.join(self.records_folder, "user.json")
        self.hive_file = os.path.join(self.records_folder, "hive.json")
    
    def getDeviceData(self):
        return read_json(self.device_file)

    def checkCameraConnection(self):
        device_data = read_json(self.device_file)
        try:
            capture = cv2.VideoCapture(device_data["camera_id"])
            if not capture.isOpened():
                print(f'Unable to connect to camera with id: {device_data["camera_id"]}. Please check the device for issues.')
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
        #will be used to retrieve device id from API.
        return random.randint(1000, 9999)
    
    def retrieveUserId(self):
        #will be used to retrieve user id from API.
        return "udhawiuwdfhw4238rwdaw22ej2hfg"
    
    def retrieveHiveId(self):
        #will be used to retrieve hive id from API
        return random.randint(1000, 9999)
    
        

    def setRecordsFile(self, data, records_file):
        if not os.path.exists(self.records_folder):
            os.makedirs(self.records_folder)
        write_json(data, records_file)


    
    def checkDeviceData(self):
        device_data = read_json(self.device_file)
        if device_data:
            print(f"Device Identification found. deviceID: {device_data['device_id']} cameraID: {device_data['camera_id']}")
        else:
            print("No device Identification found. Generating new ones...")
            device_data = {"device_id": self.generateDeviceId(), "camera_id": 0}
            self.setRecordsFile(device_data, self.device_file)
            print(f"New Device ID ({device_data['device_id']}) and camera ID ({device_data['camera_id']}) generated.")
        return device_data
    
    def checkUserData(self):
        user_data = read_json(self.user_file)
        if user_data:
            print(f"User Identification found. userID: {user_data['user_id']}")
        else:
            print("No user Identification found. Trying to retrieve from API...")
            user_data = {"user_id": self.retrieveUserId()}
            self.setRecordsFile(user_data, self.user_file)
            print(f"New User ID ({user_data['user_id']}) retrieved.")
        return user_data
    

    def checkHiveData(self):
        hive_data = read_json(self.hive_file)
        if hive_data:
            print(f"Hive Identification found. HiveID: {hive_data['hive_id']}")
        else:
            print("No hive identification found. Trying to retrieve from API...")
            hive_data = {"hive_id": self.retrieveHiveId()}
            self.setRecordsFile(hive_data, self.hive_file)
            print(f"New Hive ID ({hive_data['hive_id']}) retrieved.")
        return hive_data


    

    
    
    


    def runAllSetupProcedures(self):

        setup_procedures = [
            self.checkDeviceData,
            self.checkUserData,
            self.checkHiveData,
            self.checkCameraConnection,
            self.checkInternetAccess
        ]

        return all(procedure() for procedure in setup_procedures)

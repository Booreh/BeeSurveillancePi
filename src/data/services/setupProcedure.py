from data.services.jsonUtils import read_json, write_json
from data.api_client import APIClient
import os
import subprocess
import cv2
import socket
from datetime import datetime
from pijuice import PiJuice

class SetupProcedure:
    def __init__(self):
        self.records_folder = "records"
        self.device_file = os.path.join(self.records_folder, "device.json")
        self.user_file = os.path.join(self.records_folder, "user.json")
        self.hive_file = os.path.join(self.records_folder, "hive.json")
        self.pijuice = PiJuice(1, 0x14)

    def getlocalIpAdress(self):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.connect(("8.8.8.8", 80))
            local_ip = sock.getsockname()[0]
            sock.close()
            print(f"This is your ip: {str(local_ip)}")
            return str(local_ip)
        
        except Exception as e:
            print("Error:", e)
            return None

    
    def getDeviceData(self):
        return read_json(self.device_file)
    
    def getUserData(self):
        return read_json(self.user_file)
    
    def getHiveData(self):
        return read_json(self.hive_file)

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
            print(f"Error while checking camera connection: {e}")
            return False



    def checkInternetAccess(self):
        try:
            subprocess.check_output(["ping", "-c", "1", "8.8.8.8"])
            return True
        except subprocess.CalledProcessError:
            print("No internet access!")
            return False
    
    

    def checkServerConnection(self):
        return True
    
    def retrieveUserId(self):
        #will be used to retrieve user id from API.
        return "udhawiuwdfhw4238rwdaw22ej2hfg"
    
    def retrieveHiveId(self):
        #will be used to retrieve hive id from API
        return "123"
    

    
        

    def setRecordsFile(self, data, records_file):
        if not os.path.exists(self.records_folder):
            os.makedirs(self.records_folder)
        write_json(data, records_file)


    def shutDownSchedule(self):
        try:
            currentTime = datetime.now()
            if 0 <= currentTime.hour < 1:
                self.pijuice.power.SetPowerOff(5)
        except Exception as e:
            print(f"Error occurred during shutdown: {str(e)}")




    
    def checkDeviceData(self):
        device_data = read_json(self.device_file)
        if device_data:
            print(f"Device Identification found. deviceID: {device_data['device_id']} cameraID: {device_data['camera_id']}")
        else:
            print("No Device Identification found. Retrieving from API....")
            api = APIClient("http://158.39.162.139:8007")
            deviceIdCall = api.retrieveDeviceId(userid=self.getUserData()["user_id"], hiveid=self.getHiveData()["hive_id"], ipadress= self.getlocalIpAdress())

            device_data = {"device_id": deviceIdCall, "camera_id": 0}
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
            self.checkUserData,
            self.checkHiveData,
            self.checkDeviceData,
            self.checkCameraConnection,
            self.checkInternetAccess
        ]

        return all(procedure() for procedure in setup_procedures)

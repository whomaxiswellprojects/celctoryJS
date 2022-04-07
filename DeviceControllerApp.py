import random
import getpass
import socket
import time
import os

class DeviceControllerApp:
    @classmethod
    def createDeviceController(cls, ref: str, req: int):
        if req != 8080:
            exit(0)

        ref += ":" + str(req)
        dev = ref + "-|-Device_" + str(random.randint(1 , 9999))

        return DeviceControllerApp(dev)

    def __init__(self, devName):
        self.devName = devName
        self.devices: dict(str, str) = {}
        self.masters: dict(str, str) = {}
        self.files: dict(str, str) = {}

    def loaddevices(self):
        self.devices[socket.gethostname()] = "8080-" + str(random.randint(1 , 9999)) + "-|-Incoding=UTF8-|-Device_" + str(random.randint(1 , 9999)) + "-|-SocketPort=8080-|-Rendered=true-|-" + str(getpass.getuser()) + "-|-" + str(socket.gethostname())
        print("Added Device! Host: " + socket.gethostname() + " Port: 8080")
        print(self.devices[socket.gethostname()])

    def integrateDevices(self):
        
        self.loaddevices()
        self.includeMasters()
        self.addBuildFile()

        print("looping Through Devices Reloading")
        while True:
            time.sleep(1)
            os.system("clear")
            self.loaddevices()
            self.includeMasters()
            self.addBuildFile()
            print("looping Through Devices Reloading")

    def includeMasters(self):
        self.masters[socket.gethostname() + "-|-" + getpass.getuser()] = {
            "Format": "UTF8",
            "INTERPUTER": "Builf-Interputer",
            "DEVICE": socket.gethostname(),
            "URLS": [
                "https://celctory.js/address/" + socket.gethostname() + "/" + getpass.getuser() + "/socketurl.url.txt",
                "https://celctory.js/address?port=8080/" + socket.gethostname() + "/" + getpass.getuser() + "/socketport.txt",
                "https://celctory.js/hosts/definehost?name=" + socket.gethostname(),
                "https://celctory.js/address/load.db",
                "https://celctory.js/hosts/cport",
                "https://celctory.js/gjit/piece/code?=8080/indecator=0/host.aspx?loadable=true,server=https://celctory.js/server/hosts/gjitserver.srv",
                f"""https://celctory.js/gjit/piece/code?=8080/indecator=0/databaseAllocator/host.aspx?dbpath=https://celctory.js/address/load.db,dbdebug=false,parser=true,socket={socket.gethostname()},user={getpass.getuser()},pass=true,allocator=2048kb,compress=true,supress=true,debug=false,storesupress=true"""
            ]
        }
        print("[" + socket.gethostname() + "-|-" + getpass.getuser() + "]: " + str(self.masters[socket.gethostname() + "-|-" + getpass.getuser()]))

    def addBuildFile(self):
        self.files["BuildFile"] = {
            'Name': "BuildFile",
            'Stream': True,
            'Debug': False,
            'decoderUrl': 'https://celctorydecoder.net/decoder/decode.aspx?format=UTF-8'
        }
        self.files[".BuildDebug"] = {
            'Name': ".BuildDebug",
            'Stream': True,
            'Debug': True,
            'decoderUrl': 'https://celctorydecoder.net/decoder/decode.aspx?format=UTF-8'
        }

        print(self.files["BuildFile"])
        print(self.files[".BuildDebug"])
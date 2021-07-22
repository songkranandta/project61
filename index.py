import automatic 
import automatic_2
from record import RecordVideo
from record_2 import RecordVideo_2
import time
import threading



def a():
    while True:
        RecordVideo('rtsp://192.168.1.140:8554/unicast' ,'came1'  ,30)
def b():
    while True:
        RecordVideo_2('rtsp://192.168.1.192:8554/unicast' ,'came2'  ,30)
def c():    
    while True:
        automatic.GoogleDriveUpload('/came1')
        automatic_2.GoogleDriveUpload_2('/came2')
        time.sleep(300)
    

threading.Thread(target=a).start()
threading.Thread(target=b).start()
threading.Thread(target=c).start()
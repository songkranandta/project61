from os import name
import cv2
import calendar
import sched,time

ts = calendar.timegm(time.gmtime())
s = sched.scheduler(time.time, time.sleep)
record_status = True 
fourcc=cv2.VideoWriter_fourcc(*'XVID')
name = ts
time_stamp_static = ts




def write_video_name(message):
        f = open("recording_video.txt", "w")
        f.write(message)
        f.close()

class RecordVideo:
    write_video_name('Video_'+str(name)+'.avi')
    def record_interupts(self,sec):
        global time_stamp_static 
        global record_status
        if(time_stamp_static+sec <= calendar.timegm(time.gmtime())): 
            time_stamp_static = calendar.timegm(time.gmtime()); 
            record_status = False 
            print("interruts_1")

    def write_video_name(self,message):
        f = open("recording_video.txt", "a")
        f.write(message)
        f.close()       
    def __init__(self,ip,path,sec):
        cap = cv2.VideoCapture(ip)
        out=cv2.VideoWriter(path+'/Video_'+str(name)+'.avi',fourcc,25.0,(int(cap.get(3)), int(cap.get(4))))
        global record_status
        while(cap.isOpened()):
            ret, frame = cap.read()
            if(ret==True):
                self.record_interupts(sec) 
                if(record_status == True):
                    cv2.imshow('Camera_1',frame)
                    out.write(frame)
                else:
                    write_video_name('Video_'+str(calendar.timegm(time.gmtime()))+'.avi')

                    out=cv2.VideoWriter(path+'/Video_'+str(calendar.timegm(time.gmtime()))+'.avi',fourcc,25.0,(int(cap.get(3)), int(cap.get(4))))
                    record_status = True 
                if(cv2.waitKey(1) & 0xFF == ord('q')):
                    break
            else:
                break
        cap.release()
        cv2.destroyAllWindows()

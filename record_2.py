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

class RecordVideo_2:
    write_video_name('Video_'+str(name)+'.avi')
    def record_interupts(self,sec):
        global time_stamp_static 
        global record_status
        if(time_stamp_static+sec <= calendar.timegm(time.gmtime())): 
            time_stamp_static = calendar.timegm(time.gmtime()); 
            record_status = False 
            print("interruts_2")

    def write_video_name(self,message):
        f = open("recording_video.txt", "a")
        f.write(message)
        f.close()       
    def __init__(self,ip_2,path_2,sec):
        cap_2 = cv2.VideoCapture(ip_2)
        out=cv2.VideoWriter(path_2+'/Video_'+str(name)+'.avi',fourcc,25.0,(int(cap_2.get(3)), int(cap_2.get(4))))
        global record_status
        while(cap_2.isOpened()):
            ret, frame_2 = cap_2.read()
            if(ret==True):
                self.record_interupts(sec) 
                if(record_status == True):
                    cv2.imshow('Camera_2',frame_2)
                    out.write(frame_2)
                else:
                    write_video_name('Video_'+str(calendar.timegm(time.gmtime()))+'.avi')

                    out=cv2.VideoWriter(path_2+'/Video_'+str(calendar.timegm(time.gmtime()))+'.avi',fourcc,25.0,(int(cap_2.get(3)), int(cap_2.get(4))))
                    record_status = True 
                if(cv2.waitKey(1) & 0xFF == ord('q')):
                    break
            else:
                break
        cap_2.release()
        cv2.destroyAllWindows()

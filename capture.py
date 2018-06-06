import cv2
import os
import time

class ShashinVideoCapture():
    def __init__(self):
        cam = cv2.VideoCapture(0)
        cv2.namedWindow("Shashin VideoCapture")

        while True:
            ret, frame = cam.read()
            cv2.imshow("Shashin VideoCapture", frame)
            if not ret:
                break
            k = cv2.waitKey(1) & 0xFF
            os.popen("./standby")

            if k%256 == 27:
                # ESC pressed
                print("Escape hit, closing...")
                break
            elif k%256 == 32:
                # SPACE pressed
                img_name = "input.png"
                cv2.imwrite(img_name, frame)
                print("Photo written!")
                os.popen("./blink")
                break

        
        cam.release()
        for i in range(4):
            cv2.destroyAllWindows()
            cv2.waitKey(1)
        

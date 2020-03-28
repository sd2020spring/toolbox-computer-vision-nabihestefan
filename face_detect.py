""" Experiment with face detection and image filtering using OpenCV """
import numpy as np
import cv2

#face detector algorithm
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')

#blurring numpy matrix
kernel = np.ones((21, 21), 'uint8')

#screen capturer (video thigamagig)
cap = cv2.VideoCapture(0)

run = True
while run:
    #Capture frame-by-frame
    ret, frame = cap.read()
    #run face detector
    faces = face_cascade.detectMultiScale(frame, scaleFactor=1.2, minSize=(20, 20))
    for (x, y, w, h) in faces:
        #put rectangle over face
        frame[y:y+h, x:x+w, :] = cv2.dilate(frame[y:y+h, x:x+w, :], kernel)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255))

        """
        put red rectangle over each face
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255))
        """

        #Draw the face over the faces
        #Right Eye (from user perspective)
        cv2.circle(frame, (int(x+(5*w/16)), int(y+(h/3))), 20, (255, 255, 255), thickness=-1)
        cv2.circle(frame, (int(x+(5*w/16)+5), int(y+(h/3)+5)), 6, 255, thickness=-1)

        #Left Eye (from user perspective)
        cv2.circle(frame, (int(x+(11*w/16)), int(y+(h/3))), 20, (255, 255, 255), thickness=-1)
        cv2.circle(frame, (int(x+(11*w/16)-5), int(y+(h/3)+5)), 6, 255, thickness=-1)

        #mouth
        cv2.circle(frame, (int(x+(w/2)), int(y+(5*h/6))), 30,  (0, 0, 0), thickness = -1)

        # Display the resulting frame
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("Done")
            run = False




# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

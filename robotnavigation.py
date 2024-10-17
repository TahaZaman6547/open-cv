import cv2 as cv

capture = cv.VideoCapture('robot_lawn_navigation.mp4')  

while True:
    isTrue, frame = capture.read()
    
    if isTrue:
       
        frame_resized = cv.resize(frame, (640, 480))
        cv.imshow('Lawn Robot Navigation', frame_resized)

    
        if cv.waitKey(20) & 0xFF == ord('d'):
            break
    else:
        break

capture.release()
cv.destroyAllWindows()

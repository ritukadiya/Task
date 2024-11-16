import cv2

# Open the webcam
video_cap = cv2.VideoCapture(0)

while True:
    # Capture each frame
    ret, video = video_cap.read()
    
    # Show the video in a window
    cv2.imshow("video_live", video)
    
    # Exit the loop when the 'a' key is pressed
    if cv2.waitKey(10) == ord("a"):
        break

# Release the video capture object and close all OpenCV windows
video_cap.release()
cv2.destroyAllWindows()  
# Media Tech Assignment - Emily Fletcher 18410839
# Import Statements
import cv2
import numpy as np
import cvlib
from cvlib.object_detection import draw_bbox


def motion_detection(video):
    # video location
    videopath = video

    # Uncomment to change feed to webcam
    # feed = cv2.VideoCapture(0)
    feed = cv2.VideoCapture(videopath)

    # Prints whether connection to camera or video is correct
    ret, frame = feed.read()

    if ret:
        print('Video Source Found')
    else:
        print('Video Source Not Found')

    # Placeholder function
    def capture_frames():
        print("Save Video Test")

    # While camera or video is running
    while feed.isOpened():
        # defining two frames to compare
        ret, frame1 = feed.read()
        ret, frame2 = feed.read()
        # Finding the absolute difference between the two frames
        diff = cv2.absdiff(frame1, frame2)

        # prints when video is finished and closes window
        if not ret:
            print("End of Frames")

        # Converts Feed to Grey and adds a Blur then a Dilation (makes it easier to detect motion)
        gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)

        blur = cv2.GaussianBlur(gray, (5, 5), 0)
        # change 2nd parameter for changes to detection range
        _, thresh = cv2.threshold(blur, 35, 255, cv2.THRESH_BINARY)
        dilated = cv2.dilate(thresh, None, iterations=3)
        contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        for c in contours:
            # 5000 Threshold removes smaller detection objects
            if cv2.contourArea(c) < 5000:
                continue
            # defining values to create a rectangle
            x, y, w, h = cv2.boundingRect(c)

            # Saves a frame everytime motion is detected
            capture_frames()
            print("Motion Detected")

        # Applying to detect common objects
        # Only detects objects the module has 85% confidence or above in
        (bbox, label, conf) = cvlib.detect_common_objects(frame, confidence=0.85)
        objects_detected = label
        print(objects_detected)

        # creating a new video with bbox on each frame
    video_with_detection = draw_bbox(frame, bbox, label, conf)
    
    #Returns to main class so it can be applied to video sources
    return video_with_detection



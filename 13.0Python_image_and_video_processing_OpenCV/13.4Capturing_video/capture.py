import cv2, time

"""
    'VideoCapture()' - Method that triggers video capture
    For parameters 'VideoCapture(0|1|2)' will be external web cams and for dir file 'VideoCapture("...")'
"""
video = cv2.VideoCapture(0)

# to know number or frames generated;
f = 0

while True:
    f = f+1

    # create frame that captures imgs
    check, frame = video.read()

    print(check)
    print(frame)

    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # time.sleep(3)
    cv2.imshow("Capturing...", gray_frame)

    # time to capture each frame = 1 millisec
    wkey = cv2.waitKey(1)
    print(gray_frame)

    # break the loop
    if wkey == ord('q'):
        break

print(f"Number of frames generated are: {f} iterations")
video.release()
cv2.destroyAllWindows

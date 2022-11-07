import cv2
vidcap = cv2.VideoCapture('sample.mp4')
success,image = vidcap.read()
count = 0
r_count=0
success = True
while success:
    success,image = vidcap.read()
    if count%45 ==0:
        img180 = cv2.rotate(image, cv2.ROTATE_180)
        cv2.imwrite("image/image%s.jpg" %format(r_count,'04'),img180)
        r_count+=1
    count += 1
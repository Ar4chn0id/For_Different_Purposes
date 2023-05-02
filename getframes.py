import cv2

video = cv2.VideoCapture('video4.mp4')
path = 'frames4/'
count = 0

while True:
    success, image = video.read()
    if not success:    # Video sonuna geldiyseniz döngüyü sonlandırın
        break
    cv2.imwrite(path + 'frame%d.jpg' % count, image)    # Kareleri JPEG formatında kaydedin
    count += 1 # Kare sayacını artırın

video.release()# Video işlemi tamamlandıktan sonra işlemi serbest bırakın

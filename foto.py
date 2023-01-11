import cv2


kamera=cv2.VideoCapture(0)
while True:
    kontrol,frame=kamera.read()
   # gri=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
   # cv2.imshow("siyahbeyaz Goruntu",gri)
    cv2.imshow("orjinal",frame)
    cv2.imwrite("aaaa.png",frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
kamera.relase()
cv2.destroyAllWindows()
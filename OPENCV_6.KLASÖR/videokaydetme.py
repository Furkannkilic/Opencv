import cv2

cap = cv2.VideoCapture(0,cv2.CAP_DSHOW) # VideoCapture, videoyu webcamden mi yoksa dosyadan mı okuyacağımızı belirtmek için kullanılır. 0, burada webcamden okuyacağımızı gösterir.
filename="webcam.avi"
videofileoutput=cv2.VideoWriter(filename)
while True:  # Sonsuz döngü
    ret, frame = cap.read()  # Videoda yakaladığımız kareleri tek tek okumaya yarar. cap.read(), framelerin değerini doğru okuduysa ret True, yanlış okunduysa False olur.
    frame = cv2.flip(frame, 1)  # Her görüntüyü istediğimiz eksenlere göre yansıtır. Girilen ilk değişken yönünü değiştirmek istediğimiz frame, ikincisi ise hangi yönde değiştirmek istediğimiz. 1 girersek her bir frame, Y ekseninde yansıtılarak gösterilir.
    videofileoutput.write(frame)
    cv2.imshow("WEBCAM FİLE",frame)  # Okuduğumuz frameleri tek tek göreceğiz.
    if cv2.waitKey(1)  & 0xFF==ord("q"):# Videodaki framelerin her birini ekranda 15 milisaniye görmek istiyoruz.
      break


cap.release()  # Yaptığımız işlemi durdurur.
cv2.destroyAllWindows()  # Açık olan tüm pencereyi kapatır.
import cv2  


cap = cv2.VideoCapture(0)

# Sonsuz döngü 
while 1:
    
    ret, frame = cap.read()

    
    if not ret:
        break

    # Görüntüyü yatay olarak aynala (sağa-sol ters çevirme)
    frame = cv2.flip(frame, 1)

    # Canny kenar algılama yöntemi ile kenarları tespit et
    # 100: Düşük eşik değeri, 500: Yüksek eşik değeri
    edges = cv2.Canny(frame, 100, 500)

    # Orijinal görüntüyü göster
    cv2.imshow("Frame", frame)

    # Kenar algılanmış görüntüyü göster
    cv2.imshow("Edges", edges)

   
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break


cap.release()

cv2.destroyAllWindows()

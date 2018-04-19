import cv2
import sys

yuzTanim = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# resim dosyasını oku
resim=cv2.imread("news.jpg")
gri = cv2.cvtColor(resim, cv2.COLOR_BGR2GRAY) # arkaplan gri

yuzler = yuzTanim.detectMultiScale(
    gri,
    scaleFactor=1.01,
    minNeighbors=5,
    minSize=(30, 30)
)

print("Bulunan {0} yüz! ".format(len(yuzler)))

# Draw a rectangle around the faces
#for (x, y, w, h) in faces:
#    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

cv2.imshow("Yüz Bulundu", resim)
cv2.waitKey(0)

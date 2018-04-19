import cv2
import glob


resimler = glob.glob("*.jpg")

for r in resimler:
    gri = cv2.imread(r,0)
    r100 = cv2.resize(gri,(200,200)) # yeniden boyutlandır
    cv2.imshow("100X100",r100) # görüntüleme
    cv2.waitKey(1000) # bekleme
    cv2.destroyAllWindows()
    cv2.imwrite("100x100" + r,r100)  # fiziksel olarak dosyayı kaydet

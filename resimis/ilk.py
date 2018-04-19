import cv2


res1 = cv2.imread("galaxy.jpg",0)

print(type(res1))
print(res1.shape)
print(res1.ndim)
print(res1)

rs1_b = cv2.resize(res1,(int(res1.shape[0]/2), int(res1.shape[1]/2)))
cv2.imwrite("galaksi%50.jpg",rs1_b)

cv2.imshow("Galaksi",rs1_b)
cv2.waitKey(2000)

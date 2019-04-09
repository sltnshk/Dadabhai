import cv2
img = cv2.imread("C:\\Users\\abc\\Desktop\\penguins.jpg",1)
img1 = cv2.imread("C:\\Users\\abc\\Desktop\\penguins.jpg",0)
resized = cv2.resize(img,(int(img.shape[1]/2),int(img.shape[0]/2)))
print(img)

print("----------------------------------------------------")
print(type(img1))

cv2.imshow("penguins",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
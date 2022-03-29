import cv2
filePath = 'cat.jpg'
windowTitle = 'Wow awesome di ba'
readCvImage = cv2.imread(filePath, 1)
cv2.imshow(windowTitle, readCvImage)
cv2.waitKey(0)
cv2.destroyAllWindows()

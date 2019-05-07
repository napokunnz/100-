import cv2
img = cv2.imread("imori.jpg")
red = img[:, :, 2].copy()

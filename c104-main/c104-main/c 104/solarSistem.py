import cv2

img = cv2.imread('solar-system.jpg')


cv2.putText(img, "Sol", (100, 80), cv2.FONT_HERSHEY_SIMPLEX, 200, (0, 0, 255), )
cv2.putText(img, "mercúrio", (150, 80), cv2.FONT_HERSHEY_SIMPLEX, 200, (0, 0, 255), )
cv2.putText(img, "vênus", (200, 80), cv2.FONT_HERSHEY_SIMPLEX, 200, (0, 0, 255), )
cv2.putText(img, "Terra", (250, 80), cv2.FONT_HERSHEY_SIMPLEX, 200, (0, 0, 255), )
cv2.putText(img, "Marte", (300, 80), cv2.FONT_HERSHEY_SIMPLEX, 200, (0, 0, 255), )
cv2.putText(img, "Júpiter", (350, 80), cv2.FONT_HERSHEY_SIMPLEX, 200, (0, 0, 255), )
cv2.putText(img, "Saturno", (400, 80), cv2.FONT_HERSHEY_SIMPLEX, 200, (0, 0, 255), )
cv2.putText(img, "Urano", (450, 80), cv2.FONT_HERSHEY_SIMPLEX, 200, (0, 0, 255), )
cv2.putText(img, "Netuno", (500, 80), cv2.FONT_HERSHEY_SIMPLEX, 200, (0, 0, 255), )

cv2.imshow("solar-system.jpg", img)

cv2.waitKey(0)
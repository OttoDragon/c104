import cv2

img = cv2.imread('solar-system.jpg')

cv2.waitKey(0)
cv2.putText(img, 
            "Sol", 
            (100, 80), 
            cv2.FONT_HERSHEY_SIMPLEX, 
            2, 
            (0, 0, 255), 
            )
cv2.imshow("solar system", img)
#prof, quando eu testo a imagem ela pisca e depois sai, mesmo com o waitKey sendo 0.... não consigo terminar o projeto assim
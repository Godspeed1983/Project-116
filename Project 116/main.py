import cv2

img = cv2.imread("C:/Users/Adit Kadiyan/Downloads/Project 116/sun.jpg")

text_to_show = "Sun"


cv2.putText(img,  
           text_to_show,
           (20, 300),  
           cv2.FONT_HERSHEY_COMPLEX_SMALL,
           0.5,  
           (0,0,255)
           )

cv2.imshow("output",img)

cv2.waitKey(0)

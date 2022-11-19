import cv2

img = cv2.imread("solar-system.jpg")

rocket = img[120:360,400:500]



text_to_show = "Mercury"
text_to_show2 = "Venus"
text_to_show3 = "Earth"
text_to_show4 = "Mars"
text_to_show5 = "Jupiter"
text_to_show6 = "Saturn"
text_to_show7 = "Uranus"
text_to_show8 = "Neptune"






cv2.putText(img,
            text_to_show,
            (125,175),
            fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
            fontScale=0.5,
            color=(255,255,255))

cv2.putText(img,
            text_to_show2,
            (195,275),
            fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
            fontScale=0.5,
            color=(255,255,255))
cv2.putText(img,
            text_to_show3,
            (295,275),
            fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
            fontScale=0.5,
            color=(255,255,255))
cv2.putText(img,
            text_to_show4,
            (395,275),
            fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
            fontScale=0.5,
            color=(255,255,255))
cv2.putText(img,
            text_to_show5,
            (495,75),
            fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
            fontScale=0.5,
            color=(255,255,255))
cv2.putText(img,
            text_to_show6,
            (695,105),
            fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
            fontScale=0.5,
            color=(255,255,255))
cv2.putText(img,
            text_to_show7,
            (975,275),
            fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
            fontScale=0.5,
            color=(255,255,255))
cv2.putText(img,
            text_to_show2,
            (1125,275),
            fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
            fontScale=0.5,
            color=(255,255,255))

cv2.imshow("Output", img)

cv2.waitKey(0)
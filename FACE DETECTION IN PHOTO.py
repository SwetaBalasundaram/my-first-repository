
# FACE DETECTION


import cv2 #installed je-open-cv from python package Numpy. get numpyby + button
#cv2 can see only in grayscale

img=cv2.imread(r"C:\Users\sweta\Downloads\beautiful-young-people-jeans-looking-260nw-390053596.jpg")  # must include r ( converts as a raw)

resized_img = cv2.resize(img,(200,200))

gray_img=cv2.cvtColor(resized_img,cv2.COLOR_BGR2GRAY)
#cv2.imshow('gray',gray_img)


face_cascade= cv2.CascadeClassifier(r"C:\Users\sweta\PycharmProjects\pythonProject2\haarcascade_frontalface_default.xml")

#to detect multiple faces
faces=face_cascade.detectMultiScale(gray_img,scaleFactor=1.05,minNeighbors=5)

print(faces) # gives 2 matrices if 2 face found. [x,y,width,height]

#w-width,h-height,(x,y) is position and adding w & h gives another position coordinate
for x,y,w,h in faces:
    cv2.rectangle(resized_img,(x,y),(x+w,y+h),(0,255,0),3) #rgb color 0,255,0 and thickness 3
#before code got square due to point given by us


#resized = cv2.resize(img,(int(img.shape[1]*0.5),int(img.shape[0]*0.5)))

#show the image to the user

cv2.imshow('image',resized_img)
cv2.waitKey() # 0 millisecond means user has to press the key to close the window
#cv2.destroyAllWindows() #destroys window depending on waitkey



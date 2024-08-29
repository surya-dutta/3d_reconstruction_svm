import cv2
from matplotlib import pyplot as plt
import math

#Read input image and calculate size
img = cv2.imread('img1.png')
rows,cols,temp = img.shape

#Assign co-ordinates of object's vertices
P1 = [2077,2810,1]
P2 = [3164,2140,1]
P3 = [2085,2217,1]
P4 = [3209,1727,1]
P5 = [667,1559,1]
P6 = [1734,1335,1]
P7 = [675,1923,1]

#Draw annotation lines along object's edges
cv2.line(img,(P1[0],P1[1]),(P3[0],P3[1]),(255,0,0),10)     #Red (Z)
cv2.line(img,(P2[0],P2[1]),(P4[0],P4[1]),(255,0,0),10)
cv2.line(img,(P7[0],P7[1]),(P5[0],P5[1]),(255,0,0),10)

cv2.line(img,(P1[0],P1[1]),(P7[0],P7[1]),(0,255,0),10)     #Green (Y)
cv2.line(img,(P3[0],P3[1]),(P5[0],P5[1]),(0,255,0),10)
cv2.line(img,(P4[0],P4[1]),(P6[0],P6[1]),(0,255,0),10)

cv2.line(img,(P1[0],P1[1]),(P2[0],P2[1]),(0,0,255),10)     #Blue (X)
cv2.line(img,(P3[0],P3[1]),(P4[0],P4[1]),(0,0,255),10)
cv2.line(img,(P5[0],P5[1]),(P6[0],P6[1]),(0,0,255),10)

#Initialize ref axes
refx = P2
refy = P7
refz = P3
wo = P1

#Calculate xyz distances
distance_x = math.sqrt( ((wo[0]-refx[0])**2)+((wo[1]-refx[1])**2) )
distance_y = math.sqrt( ((wo[0]-refy[0])**2)+((wo[1]-refy[1])**2) )
distance_z = math.sqrt( ((wo[0]-refz[0])**2)+((wo[1]-refz[1])**2) )

plt.imshow(img)
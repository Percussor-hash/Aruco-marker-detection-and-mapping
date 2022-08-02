import cv2 
import cv2.aruco as aruco
import numpy as np
import os 
import time
import math
import turtle
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()

def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()


  
t = turtle.Turtle()
t.left(90)
t.color("white")
t.setpos(-100,-100)


# Opens the inbuilt camera of laptop to capture video.
cap = cv2.VideoCapture("megamax.mp4")
i = 0
 
while(cap.isOpened()):
    ret, frame = cap.read()
     
    # This condition prevents from infinite looping
    # incase video ends.
    if ret == False:
        break
     
    # Save Frame by Frame into disk using imwrite method
    cv2.imwrite('Frame'+str(i)+'.jpg', frame)
    i += 1
 
cap.release()
cv2.destroyAllWindows()

def findAruco(img, marker_size=6,total_markers=250,draw=True):
  gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
  key = getattr(aruco,f'DICT_{marker_size}X{marker_size}_{total_markers}')
  arucoDict=aruco.Dictionary_get(key)
  arucoParam=aruco.DetectorParameters_create()
  bbox,ids,_=aruco.detectMarkers(gray,arucoDict,parameters=arucoParam)  
  t.forward(0.35) 
  if ids!=None:    
    t.width(4)
    t.color("red")     
  else:
    t.color("blue") 
    t.width(1)     
  if ids == [[15]]:
    t.right(5.625)
  if ids == [[17]]:
    t.right(2.8125)    
  print(ids)
  if draw:
    aruco.drawDetectedMarkers(img,bbox)
  return bbox,ids


j = 1  
arr = [] 
flag = 0
while i!=j:
    sonic =  'Frame'+str(j)+'.jpg'
    img = cv2.imread(sonic)
    img = cv2.resize(img,(0,0),fx=0.5,fy=0.5)        
    bbox,ids = findAruco(img) 
    if ids !=None and flag==0:
        t.width(2)
        t.color("black")
        t.write(ids)
        flag = flag + 1
    elif ids == None:
        flag = 0    
    if ids not in arr and ids!=None and ids!=[[16]]:
        arr.append(ids)
    os.unlink(sonic) 
    time.sleep(0.01)    
    j = j + 1 
    if cv2.waitKey(1)==113:
        break
    cv2.imshow("img",img)

cv2.destroyAllWindows()



#lis = [[id, x, y]]

lis = [[[[11]], 0, 0], [[[12]], 0, 0.35],[[[13]], 0, 0.7],[[[14]], 0, 1.050],[[[15]], 0, 1.300],[[[17]], 1.027, 1.300],[[[18]], 1.027, 1.050],[[[19]], 1.027, 0.700],[[[20]], 1.027, 0.350],[[[21]], 1.027, 0]]

#arr =[[[11]], [[12]],[[13]],[[14]],[[15]],[[17]],[[18]],[[19]],[[20]],[[21]]]


sum = 0
for i in arr:
    y = 0
    q = 0
    p =[]
    r =[]
    while y==0:
        a = lis[q][0] 
        if i == a and i !=[[11]]:
            p.append(lis[q][1])
            p.append(lis[q][2])  
            r.append(lis[q-1][1])
            r.append(lis[q-1][2])
            m = math.sqrt(((p[0]-r[0])**2)+((p[1]-r[1])**2))
            sum = sum + m        
            print('In front of room id',i)
            print('after moving a distance', sum)
            print()
            y = 1
        elif i == lis[q][0] and i==[[11]]:
            print('In front of room id',i) 
            print()
            y = 1   
        else:
            q = q + 1
            
        
root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()    
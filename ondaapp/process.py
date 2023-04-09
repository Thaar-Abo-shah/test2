import cv2
import numpy as np
import random
import string




def im_pro(url,level):
# Load the image
    img = cv2.imread(url)
    height1, width1, channels = img.shape
    
    

    dim = (900, 1350)
    img = cv2.resize(img, dim, interpolation = cv2.INTER_LINEAR)
    # cv2.imshow('Destina', img)

    x, y, w, h = 300, 550, 300, 250


    height, width = img.shape[:2]
    img_array = np.array(img)
    a=[]
    if level=='0' :
       a=[1,1,2,3,4,5,6,7,8,9,11,12,12,13,13,14,14,14,15,15,16,17,16,15,15,14,14,13,13,12,12,11,9,8,7,6,5,4,3,2,1,1]

    if level=='1' :
       a=[1,1,2,3,4,5,6,7,8,9,11,12,14,15,16,17,18,18,19,20,20,21,20,19,18,17,16,15,14,13,12,11,9,8,7,6,5,4,3,2,1,1]

    if level=='2' :
       a=[1,1,2,3,4,5,6,7,9,10,12,13,14,15,16,18,19,21,22,23,24,23,22,21,20,19,17,16,15,14,13,11,9,8,7,6,5,4,3,2,1,1]
    n=0
    z=0;
    m=0;
    # print(h/23)
    for i in range(y,y+h):

        # if(i<(y+int((h)/2))):
        #     print(y+int((h)/2)-i)
        #     print('+++++++')
        # else:
        #     print('-------')
        if(n == int(h/(len(a)-4))):
            # print(z)
            m=a[z];
            z+=1;
            n=0
        n += 1
        for j in range(x+int(w/2),x,-1):

            for k in range(m):
                img_array[i][j+k+1] = img_array[i][j+k]
        for j in range(x+int(w/2),x+w,1):

            for k in range(m):
                img_array[i][j-k-1] = img_array[i][j-k]
    random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    img_name=str('media/images/'+random_string+'.jpg')
    

    newdim=(width1 , height1)
    img_array = cv2.resize(img_array, newdim, interpolation = cv2.INTER_LINEAR)

    cv2.imwrite(img_name,img_array )
    return img_name
    # Save the result
    # cv2.imshow('Destination_image', img_array)
    # cv2.waitKey(0)







def im_pro_side(url,level):
# Load the image
    img = cv2.imread(url)
    height1, width1, channels = img.shape
    
    

    dim = (900, 1350)
    img = cv2.resize(img, dim, interpolation = cv2.INTER_LINEAR)
    # cv2.imshow('Destina', img)

    x, y, w, h = 300, 550, 300, 250


    height, width = img.shape[:2]
    img_array = np.array(img)
    a=[]
    if level=='0' :
       a=[1,1,2,3,4,5,6,7,8,9,11,12,12,13,13,14,14,14,15,15,16,17,16,15,15,14,14,13,13,12,12,11,9,8,7,6,5,4,3,2,1,1]

    if level=='1' :
       a=[1,1,2,3,4,5,6,7,8,9,11,12,14,15,16,17,18,18,19,20,20,21,20,19,18,17,16,15,14,13,12,11,9,8,7,6,5,4,3,2,1,1]

    if level=='2' :
       a=[1,1,2,3,4,5,6,7,9,10,12,13,14,15,16,18,19,21,22,23,24,23,22,21,20,19,17,16,15,14,13,11,9,8,7,6,5,4,3,2,1,1]
    n=0
    z=0;
    m=0;
    # print(h/23)
    for i in range(y,y+h):

        # if(i<(y+int((h)/2))):
        #     print(y+int((h)/2)-i)
        #     print('+++++++')
        # else:
        #     print('-------')
        if(n == int(h/(len(a)-4))):
            # print(z)
            m=a[z];
            z+=1;
            n=0
        n += 1
        # for j in range(x+int(w/2),x,-1):

        #     for k in range(m):
        #         img_array[i][j+k+1] = img_array[i][j+k]
        for j in range(x+int(w/2),x+w,1):

            for k in range(m):
                img_array[i][j-k-1] = img_array[i][j-k]
    random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    img_name=str('media/images/'+random_string+'.jpg')
    

    newdim=(width1 , height1)
    img_array = cv2.resize(img_array, newdim, interpolation = cv2.INTER_LINEAR)

    cv2.imwrite(img_name,img_array )
    return img_name
    # Save the result
    # cv2.imshow('Destination_image', img_array)
    # cv2.waitKey(0)
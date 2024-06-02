#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
img=cv2.imread('sample.jpg')


# In[ ]:


cv2.imshow('Our Image',img) #image is just a name/title of GUI application
cv2.waitKey(0) #won't respond without this


# In[2]:


import matplotlib.pyplot as plt
plt.imshow(img)
plt.show()


# In[3]:


# we first run the matplotlib and then the openCV one so that the kernel does not die
# we then see the difference between the color combinations
# openCV uses different colorspace than matplotlib
# RGB-most systems
# BGR-openCV(reverse of it)
#each image has pixels, each pixel has a color value and alot of pixels create images
#we need to change the colorspace used by openCV to RGB so that it matches with that of the system and doesn't lead to any inconsistency


# In[4]:


rgb_img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB) #convert color


# In[5]:


plt.imshow(rgb_img)


# In[6]:


img_bw=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
plt.imshow(img_bw) #when run thru openCV this will give Black and White
#similarly we can change RGB to Gray as well by passing that rgb image


# In[ ]:


cv2.imshow("BW",img_bw)
cv2.waitKey(0)


# In[ ]:





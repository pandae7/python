#!/usr/bin/env python
# coding: utf-8

# In[20]:


def dodge(front,back):
    result=front*255/(255-back) 
    result[result>255]=255
    result[back==255]=255
    return result.astype('uint8')


# In[21]:


import numpy as np
def grayscale(rgb):
    return np.dot(rgb[...,:3], [0.299, 0.587, 0.114])


# In[22]:


img ="https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcQ35eoopg-v5Asx8B4GBx46RrjUNIOaFWiPd5NvwNhQUqMdP3Px&usqp=CAU"


# In[23]:


import imageio
s = imageio.imread(img)
g=grayscale(s)
i = 255-g
import scipy.ndimage
b = scipy.ndimage.filters.gaussian_filter(i,sigma=10)
r= dodge(b,g)


# In[24]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
plt.imshow(r, cmap="gray")


# In[25]:


plt.imsave('img2.png', r, cmap='gray', vmin=0, vmax=255)


# In[ ]:

#!/usr/bin/env python
# coding: utf-8

# In[4]:


a=10
var1=20
x="monday"

print(a)
print(var1)
print(x)
type(x)


# In[5]:


var1=10
var2=20
var3=30
list_int=[10,20,30]
print(list_int)


# In[6]:


list_int[0]


# In[7]:


list_int[-1]


# In[8]:


list_int[0:3]


# In[9]:


list_int.append(25)
print(list_int)


# In[10]:


list_int.remove(25)
print(list_int)


# In[11]:


list_int.reverse()
print(list_int)


# In[12]:


list_int.sort()
print(list_int)


# In[14]:


x=10
for each in list_int:
    if(each>x):
        x=each
    else:
        continue
print(x)


# In[15]:


i=0
while(i<5):
    print(i)
    i=i+1


# In[17]:


def cember_cevre(r,pi=3.14):
    result=2*pi*r
    return result
cember_cevre(2)


# In[18]:


def hesapla(x):
    result=x*x
    return result
hesapla(5)


# In[19]:


result=lambda x:x*x
print(result(5))


# In[20]:


dictionary={"tugce":23,"kagan":16,"coco":3}
print(dictionary)


# In[21]:


type(dictionary)


# In[22]:


dictionary.keys()


# In[23]:


dictionary.values()


# In[24]:


b=dictionary.keys()

if "tugce" in b:
    print("yes")
else:
    print("no")


# In[ ]:






# coding: utf-8

# In[1]:


def func(x,y,sign):
    
    if sign=="+" :
        print(plus(x,y))    
    elif sign=="-" :
        print(minus(x,y))
    elif sign=="*" :
        print(multiply(x,y))
    elif sign=="/" :
        print(divide(x,y))
        
def plus(a,b):
    return a+b
def minus(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b



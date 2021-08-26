# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 10:02:50 2021

@author: hoang
"""


a=[]
class x:
    def __init__(self,name,age):
        self.name=name
        self.age=age

p1=x('hai',4)
p2=x('hssssai',24)

a.append(p1)
print(a[0].name)
a.append(p2)
print(a[1].age)

print(a)
for i in range(3,8):
    print(i)






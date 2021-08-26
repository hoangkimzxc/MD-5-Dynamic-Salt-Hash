# -*- coding: utf-8 -*-
"""
Created on Tue Jul 20 21:22:54 2021

@author: hoang
6
"""

import InputAdjust
import SaltGen
import SaltPlace
import SaltInsert
import HashOutput

pwd=InputAdjust.adjust()
print("Mat khau ma` nguoi` dung` phai? ghi nho' la`:",pwd,"\n")

salt=SaltGen.genChars()
print("Gia tri salt dc tao la`:",salt,"\n")

saltPlace=SaltPlace.placement(pwd)
print("da~ thuc hien thiet lap vi tri cho salt!\n")

print("da~ tao mat khau duoc chen` salt!\n")
new_pwd=SaltInsert.insert(pwd,salt,saltPlace)
print("Mat khau duoc chen salt la`:",new_pwd,"\n")

last_hashed_pwd=HashOutput.dynamicSaltHash(new_pwd)
print("MD-5 DYNAMIC SALT PASSWORD:",last_hashed_pwd,"\n")




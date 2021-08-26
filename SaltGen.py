# -*- coding: utf-8 -*-
"""
Created on Tue Jul 20 20:05:09 2021

@author: hoang
2
"""

import random

def genChars():
    while True:
        saltAmount=int(input("Nhap kich co Salt toi thieu tu 10-32 ky tu(nhap so^'):"))
        if saltAmount<10:
             print("Yeu cau nhap gia tri lon hon 10 va nho hon 32")
        elif saltAmount>32:
            print("Yeu cau nhap gia tri nho hon 32 va lon hon 10")
        else:
            break
        
    letters=""
    combination="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789∼!@$#%ˆ&∗()_-+={}|[]\:“<>?;’,./"
    for i in range(saltAmount):
        letters+=random.choice(combination)    
    return letters

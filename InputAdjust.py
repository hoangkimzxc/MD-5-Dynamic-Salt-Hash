# -*- coding: utf-8 -*-
"""
Created on Tue Jul 20 19:12:58 2021

@author: hoang
1
"""

import random
from md5 import MD5

def adjust():
    lower_chars="abcdefghijklmnopqrstuvwxyz"
    upper_chars="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    num_chars="0123456789"
    special_chars="∼!@$#%ˆ&∗()_-+={}|[]\:“<>?;’,./"
    while True:
        pwd=input("Nhap mat khau it nhat tu` 8 den 32 ky tu:")
        # pwd=input()
        if len(pwd)<8:
            print("Mat khau ban nhap k du 8 ky tu, vui long nhap lai!\n")
        elif len(pwd)>32:
            print("Mat khau ban nhap vuot qua 32 ky tu, vui long nhap lai!\n")
        else:
            print("\n'"+pwd+"' la mat khau ban dau cua ban\n")
            hashed_pwd=MD5.hash(pwd)
            print("Gia tri bam MD-5:",hashed_pwd,"thu duoc tu mat khau ban dau se co kha nang cao nam trong bang cau^` vong^`(tra [link] https://md5.gromweb.com/)\n")
            
            a_lower=random.choice(lower_chars)
            a_upper=random.choice(upper_chars)
            a_num=random.choice(num_chars)
            a_spec=random.choice(special_chars)
            c1=0
            c2=0
            c3=0
            c4=0
            
            for i in pwd:
                if i in lower_chars:
                    break
                else:
                    c1+=1 # pwd k bao gom du char can phai bo sung
            if c1==len(pwd) and len(pwd)<32:
                pwd=pwd+a_lower
                print("Mat khau cua ban thieu ky tu viet thuong, 1 ky tu viet thuong'"+a_lower+"' se duoc them vao!\n")
            
            for i in pwd:
                if i in upper_chars:
                    break
                else:
                    c2+=1 # pwd k bao gom du char can phai bo sung
            if c2==len(pwd) and len(pwd)<32:
                pwd=pwd+a_upper
                print("Mat khau cua ban thieu ky tu viet hoa, 1 ky tu viet hoa '"+a_upper+"' se duoc them vao!\n")
                
            for i in pwd:
                if i in num_chars:
                    break
                else:
                    c3+=1 # pwd k bao gom du char can phai bo sung
            if c3==len(pwd) and len(pwd)<32:
                pwd=pwd+a_num
                print("Mat khau cua ban thieu ky tu so, 1 ky tu so '"+a_num+"' se duoc them vao!\n")
                    
            for i in pwd:
                if i in special_chars:
                    break
                else:
                    c4+=1 # pwd k bao gom du char can phai bo sung
            if c4==len(pwd) and len(pwd)<32:
                pwd=pwd+a_spec
                print("Mat khau cua ban thieu ky tu dac biet, 1 ky tu dac biet '"+a_spec+"' se duoc them vao!\n")
            return pwd
        
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 20 21:17:23 2021

@author: hoang
3
"""

from md5 import MD5

def pwd2Bin(pwd):
    result=[] #list luu bin
    bits="" #bien luu chuoi bit bin
    for i in range(len(pwd)):
        bits=format(ord(pwd[i]),'08b') #doi ky tu sang nhi phan dang str
        result.append(bits)
    print("Mat khau doi sang nhi phan: ",result,"\n")
    return result

def hashPwd2Bin(pwd):
    hex_result=[] #list luu kq hex
    hashed_pwd=MD5.hash(pwd) #str ma hoa md5 cua pwd
    k=0 #bien nhay?
    s="" #bien tach chuoi thanh chuoi con co 2 ky tu
    for i in range(int(len(hashed_pwd)/2)):
        s=hashed_pwd[k]+hashed_pwd[k+1]
        hex_result.append(s)
        k+=2
    print("Gia tri bam cua mat khau o he 16: ",hashed_pwd,"\n")
    print(hex_result,"\n")
    
    
    bin_result=[] #list luu bin
    bits="" #bien luu chuoi bit bin
    for i in range(len(hex_result)):
        bits=format(int(hex_result[i],16),'08b')#chuyen hex sang bin
        bin_result.append(bits)
    print("Gia tri bam cua mat khau duoc doi sang nhi phan: ",bin_result,"\n")
    return bin_result

def placement(pwd):
    bin_pwd=pwd2Bin(pwd)
    a=[] #list luu bit ngoai cung ben phai cua pwd
    for i in range(len(bin_pwd)):
        a.append(bin_pwd[i][7])
    print("Bit ngoai cung ben phai cua mat khau: ",a,"\n")
    
    bin_hashed_pwd=hashPwd2Bin(pwd)
    b=[] #list luu bit ngoai cung ben phai cua hash_pwd
    for j in range(len(bin_hashed_pwd)):
        b.append(bin_hashed_pwd[j][7])
    print("Bit ngoai cung ben phai cua gia tri bam: ",b,"\n")
        
    xor_rslt=[] #list luu kq xor cua 2 list tren
    if len(a)>len(b): #neu list a nhieu hon list b thi them bit 0 vao b
        for i in range(len(a)-len(b)):
            b.append('0')
        print("Neu nhu mat khau dai hon gia tri bam thi chen them bit 0 vao: ",b,"\n")
            
    for i in range(len(a)): #neu it hon hoac bang thi duyet theo a roi xor
        temp=int(a[i])^int(b[i])
        xor_rslt.append(temp) #xor
    print("Gia tri sau khi XOR: ",xor_rslt,"\n")
    return xor_rslt
       
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 11:50:28 2021

@author: hoang
4
"""
#kich co salt nho hon hoac bang vi tri 1 thi chac chan se chen` het
def insert(pwd,salt,saltPos):
    new_pwd=""
    temp=""
    c=0 #bien dem de nhay? ky tu trong salt va check vi tri bit 1
    d=len(salt) #bien dem de thoat lap khi chen het gia tri salt, neu k co thi se bi loi vi ngoai mang salt
    for i in range(len(saltPos)):
        if saltPos[i]==1: #neu vi tri la 1 thi chen tung ki tu pwd r theo sau la salt
            new_pwd=new_pwd+(pwd[i]+salt[c])
            c+=1#tang bien dem len
            print(new_pwd)
            d-=1#giam d di toi khi nao=0 thi thoat lap va chen not ky tu con lai
            if(d==0):
                for j in range(i+1,len(pwd)):#+1 la vi i chua thoat lap nen chua dc tang len
                    temp=temp+pwd[j]
                    print("phan mat khau con` lai: ",temp)
                new_pwd=new_pwd+temp;
                break;
        elif saltPos[i]==0:#neu la 0 thi k chen salt chi chen ki tu pwd
            new_pwd=new_pwd+pwd[i]
            print(new_pwd)
        
    if len(salt)>c:#vi mang k the nao full 1 nen se thua ra nhung vi tri cua 0
        for i in range(c,len(salt)):#duyet tu vi tri luc truoc dang chen do?
            temp=temp+salt[i] #tao chuoi rong de cho phan con lai cua salt chua dc chen
            c+=1
        new_pwd=new_pwd+temp#ghep not vao duoi pwd moi'
    return new_pwd

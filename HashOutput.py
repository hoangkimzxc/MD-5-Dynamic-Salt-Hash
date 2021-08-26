# -*- coding: utf-8 -*-
"""
Created on Thu Jul 22 14:16:52 2021

@author: hoang
5
"""

from md5 import MD5

def dynamicSaltHash(saltedPwd):
    result=MD5.hash(saltedPwd)
    return result

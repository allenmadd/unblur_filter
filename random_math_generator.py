# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 20:55:41 2018

@author: madel
"""
import random
import matplotlib.pyplot as plt
import numpy as np
import string
import operator

ops = ['+', '-', '*', '/']

latex_scripts= ['\leq', '\times', '\infty',  '\prime', '\approx', '']

                
greek_letters=['\theta', '\lambda', '\delta', '\alpha', '\beta', '\epsilon', '\pi', '\omega', 
               '\Psi', '\Pi', '\tau', '\xi']

math_mode= ['^', '_', '\prod_{k=1}^n', '\dot', '\sum_{k=1}^']

takes_entries=['\sqrt[n]{', '\frac{']
after_frac1=['}']
after_frac2=['{']



#buddy bois

for i in range(10):
    num1 = random.randint(0,120)
    num2 = random.randint(0,120)
    operation = random.choice(ops)
    takes=random.choice(takes_entries)
    scripts=random.choice(latex_scripts)
    greek=random.choice(greek_letters)  
    math=random.choice(math_mode)

    random_egn= ['$',num1, operation, greek, scripts, greek, math, num1, num2, '$']
    print(random_egn)


#need to turn it into a string and rremove the delimiter  ,
    
    
   # random_string=' '.join(random_egn)
    
    #random_egn.replace(',', '')
    #print(random_string)









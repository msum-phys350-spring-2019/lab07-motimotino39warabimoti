# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 21:24:03 2019

谷桜子

"""
#import necessary function

import numpy as np
#import matplotlib.pyplot as plt

"""
PART-1

Make a function that will return frequency and eigenvectors:)
frequency is normally squrt(k/m)


The result with k_over_m as 1

frequency: 1.0
Eigen value1: [-2.23606798] 
Eigen value2: [2.23606798]
Eigen Vector1: [[ 0.22975292 -0.97324899]] 
Eigen vector2: [[-0.97324899 -0.22975292]]

looks like their out put is correct

Qなんかｗのん　のん　なってるエラーはなんぞｗ

"""

#check the function with k_over_m=1

k_over_m=1
matrix=np.array([[2,-1],[1,-2]])


def calc_frequencies_and_modes(matrix,k_over_m):
    frequency=np.sqrt(k_over_m)
    val,vec=np.linalg.eigh(matrix)
    
    """
    ここはただの整数だからいい
    val1=val[0]
    val2=val[1]
    ここのをmodesにしないでこうやってカットしてしまうと、
    あとでmodesとしたときに　ふたつのarrayがひとつのarrayにぶっちこまれたように
    なってしまって
    計算ちゃんとしてくれなかったのよね。。。
    だからmode として I called bothe vec1,vec2 and returned.
    vec1=vec[:,0:1]
    vec2=vec[:,1:2]
    """
    
    
    
    return frequency, vec

#freq, va1, va2, ve1, ve2= calc_frequencies_and_modes(matrix,k_over_m)

#print ("frequency: ", freq, "val1: ", va1,"val2: ", va2,"vect1: ", ve1,"vect2: ", ve2)

freq, modes= calc_frequencies_and_modes(matrix,k_over_m)
print ("frequency: ", freq, "vect1: ", modes[0,:], "vect2: ", modes[1,:])

"""
PART-2
Make function that will calc 
a, and  b


"""

def calc_components_from_initial_conditions_(x_int,modes):
    
    a=np.dot(x_int,modes[0,:])
    b=np.dot(x_int,modes[1,:])
    
    return a,b

#this is checking vec1*vec1,Vec1*Vec2
#x_int= modes[1,:]

#try with vec[1,0]    
x_int=np.array([1,0])

a,b= calc_components_from_initial_conditions_(x_int,modes)
print ("a: ", a, "b: ", b)

"""


This is answer a=vec1*vec1 has to be about 1(dot product)
vec1*vec2=is perpendicular =0

a:  0.9999999999999998 b:  0.0

#this is make sence, that is opposite 
a:  0.0 b:  0.9999999999999998


calculation with [1,0]
a:  0.22975292054736116 b:  -0.9732489894677301





"""
    
    
"""
PART3

"""
t=0

while t<=100:
    #updating time by 1
    t+=1
    
    def time_dependence(t,frequency,a,b,modes):
        
        #この振動数１，２ってどうやってもとめるんだろうかな？
        
        
        return a*np.cos(frequency*t)*(modes[0,:])+a*np.cos(frequency*t)*(modes[1,:])
    



























    

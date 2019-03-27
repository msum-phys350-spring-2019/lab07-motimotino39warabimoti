# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 21:24:03 2019

谷桜子

"""
#import necessary function

import numpy as np
import matplotlib.pyplot as plt

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
matrix=np.array([[2,-1],[-1,2]])


def calc_frequencies_and_modes(matrix,k_over_m):
    val,vec=np.linalg.eigh(matrix)
    frequency=np.sqrt(k_over_m)*val
    
    
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

    
    
    return frequency, vec,val

#freq, va1, va2, ve1, ve2= calc_frequencies_and_modes(matrix,k_over_m)

#print ("frequency: ", freq, "val1: ", va1,"val2: ", va2,"vect1: ", ve1,"vect2: ", ve2)

freq, modes,val= calc_frequencies_and_modes(matrix,k_over_m)
print ("frequency: ", freq, "vect1: ", modes[:,0], "vect2: ", modes[:,1],'val1:',val[0],'val2:',val[1])

"""
PART-2
Make function that will calc 
a, and  b


"""

def calc_components_from_initial_conditions_(x_int,modes):
    
    a=np.dot(x_int,modes[:,0])
    b=np.dot(x_int,modes[:,1])
    
    return a,b

#this is checking vec1*vec1,Vec1*Vec2
#x_int= modes[:,1]

#try with vec[1,0]    
x_int=np.array([0,1])

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
    





def time_dependence(a, b, t,freq,modes):
        
        #この振動数１，２ってどうやってもとめるんだろうかな？
        #omega is resoance frequency=eigenvalue
        
        #define the function that will calculate position
        
        
        pos=a*np.cos((freq[0])*t)*(modes[:,0])+b*np.cos((freq[1])*t)*(modes[:,1])
        
        return pos


print ('ANSWER:',time_dependence(a, b, 2,freq,modes))



"""
ANSWER: [1. 0.]

initial position as 
x_int=np.array([1,0])
when I set up t=0, that returned pos [1,0]
So I can say that function is working well

"""



t_init = 0
t_end = 10

N_times = 100



time = np.linspace(t_init, t_end, num=N_times)
pos1= np.empty_like(time)
pos2=np.empty_like(time)



for t in range (N_times):
    
    
    pos1[t],pos2[t]=time_dependence(a,b,time[t],freq, modes)
  
    
    #updating time by 1
    
    #position is calculated by increasing time
    
    #DO NOT FORGET
    #pos is whole array, if I want to update the pos by time
    #I need to update array!pos[t]アレイをかっとしながらこまこまアップデート！
    
    
def plot_motion_of_masses(x, time, title='mass'):
    """
    Function to make a plot of motion of masses as a function of time. The time
    should be on the vertical axis and the position on the horizontal axis.
    Parameters
    ----------
    x : array of position, N_times by 2 elements
        The array of positions, set up so that x[:, 0] is the position of mass
        1 relative to equilibrium and x[:, 1] is the position of mass 2.
    time : array of times
        Times at which the positions have been calculated.
    title : str
        A descriptive title for the plot to make grading easier.
    """
    # Nothing special about these, but they look nice
    x1_equilibrium_pos = 3
    x2_equilibrium_pos = 6

    x1 = x[:, 0] + x1_equilibrium_pos
    x2 = x[:, 1] + x2_equilibrium_pos

    plt.plot(x1, time, label='Mass 1')
    plt.plot(x2, time, label='Mass 2')
    plt.xlim(0, 9)
    plt.legend()
    plt.title(title)


## YOU FILL IN THE REST! 
x = np.zeros([N_times, 2])
x[:, 0] = pos1
x[:, 1] = pos2
plot_motion_of_masses(x, time)
"""    
print(posx.shape)
plt.plot(time,posx,'r-',label='motion1')
plt.legend()
plt.xlabel('time')
plt.ylabel('displacement')
plt.show()


plt.plot(time,posy,'b-',label='motion2')
plt.legend()
plt.show()




plt.plot(time,posx,'r-')
plt.plot(time,posy,'b-')

"""


    
    


    
   
   
    
   
    
    
   
 
    
    
    
    
    
  
    









    



























    

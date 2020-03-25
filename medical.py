# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random
import pandas


df = pd.read_csv("C:/Users/Jeet Das/Desktop/medical-college.csv",encoding="utf-8")

print("\n----------------------- output data :---------------------\n")
print("Project - 17 : Numbers of Medical Colleges and MBBS Seats in India (using Python)");
print("\n------------------------------------------------------------\n")


# Question – A : get row and column numbers 

print('---------------------------------------------')
print("Dimension of the data frame = ",df.shape)
print('---------------------------------------------')

# Question – B : print column names :

print('------------------------\n Column names as follows :')
print('------------------------\n')
count = 0
for col in df.columns: 
        print(count,"-->",col)
        count = count+1
print("\n-----------------------------\n")

# Question - C : print available states/UT and State and Outside the ambit of MCI 

df0 = df['State and Outside the ambit of MCI']

print('---------------------------------------------')
print('Available data for following State and UT / State and Outside the ambit of MCI : ')
print('---------------------------------------------')
print(df0)
print('---------------------------------------------')


# Question - D : Medical colleges in india

df1 = df['No of Government Colleges-(status as on 23.8.2013)']
df2 = df['No of Private Colleges-(status as on 23.8.2013)']
df3 = df['Total no of colleges-(status as on 23.8.2013)']

plt.title('Question - D : Medical colleges in india')
plt.xlabel("State sl. no. --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(df1,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="[1] No of Government Colleges-(status as on 23.8.2013)")

plt.plot(df2,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="[2] No of Private Colleges-(status as on 23.8.2013)")

plt.plot(df3,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="[3] Total no of colleges-(status as on 23.8.2013)")
            
          
plt.legend()
plt.show()

# Question - E : MBBS seats

df4 = df['MBBS seats in Government Colleges-(status as on 23.8.2013)']
print('-------- States/UT --------')
print(df0)
print('-------- Seats Govt medical colleges --------')
print(df4)

df5 = df['MBBS seats in Private Colleges-(status as on 23.8.2013)']
print('-------- States/UT --------')
print(df0)
print('-------- Seats Private medical colleges --------')
print(df5)


df6 = df['Total MBBS seats in Colleges-(status as on 23.8.2013)']
print('-------- States/UT --------')
print(df0)
print('-------- Total (Private + Govt ) Seats medical colleges --------')
print(df6)



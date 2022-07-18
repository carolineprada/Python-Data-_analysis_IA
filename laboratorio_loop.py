# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 22:16:57 2021

@author: Caroline
"""

#Ejercicios Bucles

#PARTE 1 → For 
for x in range(-5,5):
    print(x)
    

#PARTE 2 → For
genres=[ 'rock', 'R&B', 'Soundtrack', 'R&B', 'soul', 'pop']    

for y in genres:
    print(y)
    
    
#PARTE 3 → For
squares=['red', 'yellow', 'green', 'purple', 'blue']

for z in squares:
    print(z)
    
#PARTE 4 → While
PlayListRatings = [10, 9.5, 10, 8, 7.5, 5, 10, 10]

#Variables iniciales
i=0
vali = PlayListRatings[0]

#Loop
while (vali >= 6):
    
    vali= PlayListRatings[i]
    i=i+1
    print(vali)
    
print("It took", i, "Repetitions")    


#PARTE 5 → While
squa = ['orange', 'orange', 'purple', 'blue ', 'orange']

#Variables
new_squares = []
j = 0

#Loop
while (squa[j] == "orange"):
    new_squares.append(squa[j])
    j= j+1
    
print(new_squares)    
    
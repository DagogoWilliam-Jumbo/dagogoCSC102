#!/usr/bin/env python
# coding: utf-8

# In[ ]:


str = input("Enter your state of origin")

print ("Your state of origin is: ", str)
print ("The first character is: ", str[0])
print ("The characters starting from 3rd and 5th are: ", str[2:5])
print ("The string starting from 3rd character is: ", str[2:])
print ("State of origin two times", str * 2)


# In[ ]:


# Input from user
m = float(input("Enter mass in kilograms: "))

# Constant value for the speed of light in m/s
c = 299792458

# Calculating energy using Einstein's equation
energy = m * c ** 2

# Displaying the result 
print(f"The energy equivalent to {m} kg of mass is {energy} joules.")


# In[ ]:


list = [ 'Anaconda, 786 , 2.23, 'Jupyter', 70.2 ]
shortlist = [321, 'Python']
        
print(list)               ''' Prints complete list '''
print(list[0])            # Prints first element of the list
print(list[1:3])          # Prints elements starting from 2nd till 3rd 
print(list[2:])           ''' Prints elements starting from 3rd element'''
print(shortlist * 2)      # Prints list two times
print(list + shortlist)   # Prints concatenated lists
        
        


# In[ ]:


tuple = ("Ekiti", 750, 'Oshogbo', 250, "Akure", 500)
s_tuple = ("Abeokuta", 300, "Ogbomoso")

# Prints the complete tuple
print (tuple)

# Prints last element of the tuple
print (tuple[-1])

# Prints elements of the tuple starting from 2nd till 3rd
print (tuple[2:4])

# Prints elements of the tuple starting from 3rd element
print (tuple[3:])

# Prints contents of the tuple twice
print (s_tuple * 3)

# Prints concatenated tuples
print (tuple + s_tuple)


# In[ ]:


# Returns false as game_1 is not equal to game_2
game_1 = 2
game_2 = 4
print(bool(game_1 == game_2)
# Or
print(game_1 == game_2)
    
# Returns False as val is None
val = None
print(bool(val))

# Returns false as num is empty sequence 
num = ()
print(bool(num))
      
# Returns true as age is boolean
age = True
print(bool(age))


# In[ ]:


# Convert to int 

grade = int(70)        # grade will be 70
gpa = int(4.9)         # gpa will be 4.9
cgpa = int("4")        #cgpa will be 4

print(f"Grade = {grade}")
print(f"GPA = {gpa}")
print(f"CGPA = {cgpa}")


# In[ ]:


# Convert to float

grade = float(97)
gpa = float(5)
cgpa = float("4.7")

print(f"Grade = {grade}")
print(f"GPA = {gpa}")
print(f"CGPA = {cgpa}")


# In[ ]:





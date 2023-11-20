#!/usr/bin/env python
# coding: utf-8

# In[162]:


# Checking working directory 
import os 
import pandas as pd 

current_directory = os.getcwd()
print(current_directory)


# In[163]:


# Changing working directory 
new_directory_path = r'C:\Users\aimemagana\HealthDataAnalytics'


# In[164]:


file_path = "Week13Assignment.txt"
try:
    with open(file_path, "r") as file: 
        content = file.read()
        print (content)
except FileNotFoundError: 
        print(f"File '{file_path}' not found.")
except IOError: 
        print("An error has occured while reading this file.")


# In[165]:


# Average age of patients 
df = pd.read_csv(file_path)
print(df)


# In[166]:


print(df.columns)


# In[167]:


# Average age 
average_age = df[' Age'].mean()
print(average_age)


# In[168]:


# Number of male and female patients 
male = (df[' Gender'] == ' Male').sum()
female = (df[' Gender'] == ' Female').sum()
print(f"The number of male patients is {male} and the number of feamle patients is {female}.")


# In[169]:


# Get the highest blood pressure 
max_bp = max(df[' BloodPressure'])
print(f"The highest blood pressure is {max_bp}.")


# In[170]:


# Get the lowest blood pressure 
low_bp = min(df[' BloodPressure'])
print(f"The lowest blood pressure is {low_bp}.")


# In[171]:


# Find the average body tempreature of the patients
average_temp = df[' Temperature'].mean()
print(f"The average tempreature is {average_temp}.")


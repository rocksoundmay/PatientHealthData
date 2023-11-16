#!/usr/bin/env python
# coding: utf-8

# In[3]:


# Checking working directory
import os
import pandas as pd

current_directory = os.getcwd()
print(current_directory)


# In[5]:


# Change working directory
new_directory_path = "/Users/kenzie/Downloads"
os.chdir(new_directory_path)

updated_dir = os.getcwd()
print(updated_dir)


# In[6]:


file_path = "Week13Assignment.txt"

try: 
    with open(file_path, "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("File '{file_path}' Not Found.")
except IOError:
    print("An error occured while reading the file.")


# In[10]:


# Average age of patients
df = pd.read_csv(file_path)
print(df)
print(df.columns)


# In[12]:


# Average age
average_age = df[' Age'].mean()
print(average_age)


# In[13]:


# Number of male and female patients
male = (df[' Gender'] == ' Male').sum()
female = (df[' Gender'] == ' Female').sum()
print(f"The number of male patients is {male} and the number of female patients is {female}.")


# In[14]:


# Get the highest blood pressure
max_bp = max(df[' BloodPressure'])
print(f"The highest blood pressure is {max_bp}.")


# In[15]:


# Get the lowest blood pressure
min_bp = min(df[' BloodPressure'])
print(f"The lowest blood pressure is {min_bp}.")


# In[16]:


# Average body temperature of all patients
mean_body_temperature = (df[' Temperature']).mean()
print(mean_body_temperature)


# In[ ]:





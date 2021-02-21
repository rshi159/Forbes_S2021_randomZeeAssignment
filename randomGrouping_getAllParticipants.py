#!/usr/bin/env python
# coding: utf-8

# In[192]:


import numpy as np
import pandas as pd
import logging
import sys


# In[197]:


# Set parameters

# Column index of data. Col 0 should be datetime of submission
NAME_IDX = 1
EMAIL_IDX = 2
STATUS_IDX = 3
ACTION_IDX = 4

# Rename if option strings change. Order matters since we make new columns with numerical values.
STATUS_OPTIONS = ["Yes", "No", "In testing protocol, but off campus"]
STATUS_ENCODING = [0,1,2]

ACTION_OPTIONS = ["Put me on the list!","Take me off of the list!"]
ACTION_ENCODING = [0,1]

# Set group size. We will probably have people left over so we can assign them by hand.
GROUP_SIZE = 4

# filepath to save output as
FILEPATH = "./groupings.xlsx"

# create logger for debug and useful output. Print to stdout
root = logging.getLogger()
root.setLevel(logging.DEBUG)

handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)


# In[204]:


logging.debug(">>Starting<<")
# read data into df
df = pd.read_csv('submissions.csv')
# new df for list of unique students. Column headers are same as imported df
df_students = pd.DataFrame(columns=df.columns)
# yes = 0, no = 1, near campus = 2.
df['status'] = df.iloc[:,STATUS_IDX].replace(STATUS_OPTIONS,STATUS_OPTIONS)
# 0 = add to list. 1 = remove from list
df['action'] = df.iloc[:,ACTION_IDX].replace(ACTION_OPTIONS,ACTION_ENCODING)

# we will assume students won't make any spelling errors. However names might be weird with spacing and capitalization
# the code will identify unique students by their email.

# get array of unique emails
uniq_email = df['Email'].unique()

# fill dataframe of unique students
for name in uniq_email:
#     details of most recent sumbission
    recent_sub = df.loc[df['Email'] == name].iloc[-1,:]
#     print(recent_sub)
    if recent_sub['action'] == 0:
        df_students = df_students.append(recent_sub)


# randomize ordering to avoid anything dumb like roomdraw.
logging.debug(">>Randomizing students into groups of size: %d <<" % GROUP_SIZE)
# get number of rows in dataframe
num_students = df_students.shape[0]
logging.debug(">>Expect %d groups<<" % np.ceil(num_students/GROUP_SIZE))
# create an incremental array of length equal to number of students
index = np.arange(num_students)
# shuffle the array, the function scrambles the input array. No return, probably passes the pointer as input.
np.random.shuffle(index)
df_students = df_students.iloc[index, :]

# create array of emails with each column having number of students in a group.
# the last row will have placeholders. Please insert those folks in other groups
emails = df_students['Email']
# gets number of placeholders we need to add in order to get number of students to be a multiple of GROUP_SIZE
padding_len = GROUP_SIZE - num_students % GROUP_SIZE
logging.debug(">>Number of ungrouped students = %d<<" % (num_students % GROUP_SIZE))
emails_padded = np.append(emails, np.repeat("placeholder@placeholder.edu",padding_len))

# Reshape array so it can easily be pasted into recipients bar of gmail
output_arr = emails_padded.reshape(-1,GROUP_SIZE)
# Make the output a dataframe and save as excel file
logging.debug(">>Writing to Excel Document at: %s <<" % FILEPATH)
pd.DataFrame(output_arr).to_excel(FILEPATH, index=False)


# In[206]:


# # Save the code to a python script. copy and paste into terminal
# !jupyter nbconvert --to python randomGrouping_getAllParticipants.ipynb


# In[ ]:





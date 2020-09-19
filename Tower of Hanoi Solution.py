#!/usr/bin/env python
# coding: utf-8

# This script is to build a recursion function for Tower of Hanoi
# 
# We take the towers to be labelled as "A", "B" & "C"
# 
# Disk are number from 1 as the smallest disk to 2 to the next smallest, so on and so forth
# 
# ![slide_28.jpg](attachment:slide_28.jpg)

# In[70]:


#Function to create the instruction in string form

def Instruction(n,fr,to):
    print ('Move disk '+str(n)+ ' from column '+str(fr)+' to '+str(to))
    
Instruction(5,"A","B")


# In[73]:


#Function to instruct you how to finish the Tower of Hanoi in the least amount of steps

#Function name is SolveHanoi()
#It takes in the input of (Number of Disks, Original Position, Auxiliary Position, Target Position)

def SolveHanoi(n,OG,AX,Tar):
    if n==0:
        pass
    else :
        SolveHanoi(n-1,OG,Tar,AX)  #To move n-1 disks to the Auxiliary position so that the bottom Disk can move to the Target Position
        Instruction(n,OG,Tar)
        SolveHanoi(n-1,AX,OG,Tar)
        
        
        
SolveHanoi(4,"A","B","c") 


# In[ ]:





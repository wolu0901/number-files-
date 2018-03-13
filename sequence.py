# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 21:43:12 2018

@author: wolu0
"""
import os
import time
import tkinter.filedialog as t

def choosefile():
    t.Tk().withdraw()
    path= t.askdirectory()
    return path

path = choosefile()

    
def changename(path):
    filelist = os.listdir(path)
    i = 1
    for file in filelist:
        odddir = path + '/' + file
        newdir = path + '/' + str(i) + '.' + file
        os.rename(odddir,newdir)
        i+=1
    return i -1


if __name__ == '__main__':
    start = time.time()  
    print('process %s file'%(changename(path)))  
    c = time.time() - start  
    print('take:%0.2f seconds'%(c))  

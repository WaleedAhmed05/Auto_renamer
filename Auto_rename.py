import os
import time

Path = input("Please enter the Directory Path: ")
#Here User have to provide full folder path
#Eg: W:\python codes\randomtextfiles

print("---------------------------------")
print("Please write '1' for mp3 files ")
print("Please write '2' for image files ")
print("Please write '3' for text files ")
print("Please write '4' for mp4 files ")
print("---------------------------------")


Extension=int(input("Choose the number: "))

if (Extension>0 and Extension<=4):
    print("You have Choosed, no: "+str(Extension))
    if Extension==1:
       Ext=".mp3"
       
    if Extension==2:
       Ext=".jpg"
       
    if Extension==3:
       Ext=".txt"
       
    if Extension==4:
       Ext=".mp4"
else:
    print("Wrong Selection of Extension, Program Closed! ")
    print("Choose from '1','2','3','4' ")
    time.sleep(3)
    
       

fileNumber = 1
print("Old Files Name")
print(os.listdir(Path))
os.chdir(Path)
files=os.listdir(Path)

for file in files:
    os.rename(file, str(fileNumber)+str(Ext))
    fileNumber = fileNumber+1
print("----------------------")
print("New File Names")
print(os.listdir(Path))
time.sleep(3)
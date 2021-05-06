# -*- coding: utf-8 -*-
"""
Created on Wed May  5 13:28:40 2021

@author: Hadar
"""
######file= input("enter file name: ")
file='�צאט WhatsApp עם יום הולדת בנות לנויה.txt'
openFile= open(file, 'r', encoding= 'utf-8')
fileRead=openFile.read()
fileLines=fileRead.split('\n')

##part 1##
#find contact list
contacts=list()
for line in fileLines:
    line=line.strip()
    if line.count(":")<2:
       continue
    if line[0].isdigit():
       help=line.find("-")
       start=line.find(" ",help)
       end=line.find(":",help)
       contact=line[start:end]
    if contact not in contacts:
      contacts.append(contact)
#give each contact an id     
index={}
n=1
for contact in contacts:
    index[contact]=n
    n=n+1

##part 2,3##
infoList=list() 
metadata=dict()    
extraTxt=""  
info={}
num=0
for line in fileLines:
    line=line.strip()
    if "הקבוצה" and "נוצרה" in line:
        start=line.find("הקבוצה")+6
        end=line.find("נוצרה")
        metadata["chat_name"]=line[start+2:end-2]
        metadata["creation_date"]=line.split("-")[0]
        metadata["num_of_participants"]=len(contacts)
        metadata["creator"]=line.split("נוצרה על ידי")[1]         
    if line.count(":")>=2 and line[0].isdigit():
        place=line.find("-")
        info["datetime"]=line[:place]
        start=line.find(" ",place)
        end=line.find(":",place)
        x=line[start:end]
        info["id"]= index[x]
        info["text"]=line[end+2:]
        infoList.append(info) 
        info={}
    if line.count(":")<2 and line.count("-")<1:
        extraTxt=" "+line
        infoList[num-1]["text"]+=extraTxt


##part 4##
milon4=dict()
milon4["messages"]=infoList    
milon4["metadata"]=metadata
chatName=metadata["chat_name"]+".txt"
import json
file=open(chatName, "w", encoding="utf-8")
json.dump(milon4, file, ensure_ascii=False, indent=4)
file=open(chatName, "r", encoding="utf-8")
print(json.load(file))     

       

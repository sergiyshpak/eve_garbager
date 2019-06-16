# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 19:56:29 2019

@author: sergiy
"""

import webbrowser


from tkinter import *

import requests
import json
import time 
import sys
import math

systemDict= {} 
typesDict=  {}
locDict=  {}
systemSec= {} 

sleepTime=3

sys_sys={}
with open("sys_sys_topo1.txt", "r") as ins:
    for line in ins:
        line = line[:-1]
        my_list = line.split(",")
        sys_sys[my_list[0]] = my_list[1]

with open("mapSolarSystems100.csv", "r") as ins:
    for line in ins:
        my_list = line.split(",")
        #print(my_list[2]+"   " +my_list[3])
        systemDict[my_list[2]] = my_list[3]
        systemSec[my_list[2]] = my_list[4]

with open("invTypes.csv", "r") as ins:
    for line in ins:
        my_list = line.split(",")
        typesDict[my_list[0]] = my_list[2]

with open("loc.csv", "r") as ins:
    for line in ins:
        line = line[:-1]
        my_list = line.split(",")
        locDict[my_list[0]] = my_list[1]
        


koraba_w_sys="Ohkunen"
jumpLimit=10
minCost=0


class App():
    def __init__(self):
        self.root = Tk()
        self.root.title("GDSFDSADS EREF EA")
        
        self.top_frame = Frame(self.root)
        self.bottom_frame = Frame(self.root)
        self.top_frame.grid(row=0) 
        self.bottom_frame.grid(row=1) 

        self.e1 = Entry(self.top_frame ) 
        self.e2 = Entry(self.top_frame) 
        self.e1.grid(row=0, column=0) 
        self.e2.grid(row=1, column=0) 

        self.btn1 = Button(self.top_frame, text = "Set Home",  command = self.set_home)
        self.btn2 = Button(self.top_frame, text = "Set Dist",  command = self.set_dist)
        self.btn1.grid(row=0, column=1)  
        self.btn2.grid(row=1, column=1)  
        
        self.T = Text( self.bottom_frame, height=40, width=190)
        self.T.grid(row=0)
        
        self.update_clock()
        self.root.mainloop()

    def set_dist(self):
        jumpLimit=14
        
    def set_home(self):    
        koraba_w_sys="M-OEE8"

    def openHLink(self, urik):
        #print ("Going to .."+urik)
        #####print (webbrowser._browsers)
        new = 2 # open in a new tab, if possible
        #url = "http://docs.python.org/library/webbrowser.html"
        webbrowser.get(using='windows-default').open(urik,new=new)        

    def update_clock(self):
       
        url = 'https://redisq.zkillboard.com/listen.php?queueID=pipea1023'   
        headers = {'user-agent': 'my-app-test/0.0.1'}
        r = requests.get(url, headers=headers)
        if r.text!='{"package":null}':
            parsed_json = json.loads(r.text)
            datka=parsed_json['package']
            killid=str(datka['killID'])
            print("--------- "+killid)
            sysa=str(datka['killmail']['solar_system_id'])
            totaldeneg='${:,.2f}'.format(datka['zkb']['totalValue'])
            shipp=str(datka['killmail']['victim']['ship_type_id'])
            zkillLocationID=str(datka['zkb']['locationID'])
            timestamp=str(datka['killmail']['killmail_time'])
            
            xc=0.2
            yc=0.2
            zc=0.2
            xc=datka['killmail']['victim']['position']['x']
            yc=datka['killmail']['victim']['position']['y']
            zc=datka['killmail']['victim']['position']['z']
            
            dista=math.sqrt(xc**2+yc**2+zc**2) /1000
            dista=dista/149597870.7
    
            #print(sysa)
            dist_to_fly=100500
            if systemDict.get(sysa,"figgevoznaet_sysa")[0]!="J":
                distURL="http://everest.kaelspencer.com/jump/"+koraba_w_sys+"/"+systemDict.get(sysa,"figgevoznaet_sysa")+"/"
                #print(distURL)
                rdis = requests.get(distURL, headers=headers)
                #print(rdis.text)
                try:
                    self.parsed_dist_json = json.loads(rdis.text)
                except:
                    print('--=kakasraka=--')    
             #   print("Distance to fly from "+systemDict.get(koraba_w_sys,"figgevoznaet_sysa")+" is "+str(parsed_dist_json["count"]))
                dist_to_fly=self.parsed_dist_json["jumps"]
    
            if (int(dist_to_fly)<int(jumpLimit) 
                and int(datka['zkb']['totalValue'])>int(minCost)):
                
                
#                    self.T.insert(END, 'GeeksforGeeks  BEST WEBSITE\n')
#        self.T.tag_configure("hlink", foreground='blue', underline=1)
        #self.T.tag_bind("hlink", "<Control-Button-1>", self.openHLink)
#        self.T.tag_bind("hlink", "<Control-Button-1>",   lambda  e:self.openHLink("www.google.com"))
#        self.T.insert(END, "This is a link\n")
#        self.T.insert(END, "ZKILLBOARD", "hlink")
#        self.T.insert(END, "\nAnd text goes on...\n")

              # print("ddddddd---"+totaldeneg)
            

                lololo=timestamp  + ' Jumps_to_loc ' +str(dist_to_fly) + ' total$$$ '+totaldeneg+ ' system  '+systemDict.get(sysa,"figgevoznaet_sysa")                 + ' security ' +systemSec.get(sysa,"_____")                  + ' ship ' + typesDict.get(shipp,"figgevoznaet_ship") + ' Location ' + locDict.get(zkillLocationID,"GDETO")                + ' DistFromSUN '+str(dista)
                
                
                #+ '      '+UREL1+killid+'/'
                
               # print("dddd"+lololo)
                
                
                self.T.tag_configure("hlink", foreground='blue', underline=1)
                self.T.tag_bind("hlink", "<Control-Button-1>",   lambda  e:self.openHLink('https://zkillboard.com/kill/'+killid+'/'))
                self.T.insert(END, "ZKILLBOARD", "hlink")
                self.T.insert(END, '   ' +lololo+'\n\n')
            
            
            else:
                print("-=skip=-dist-"+str(dist_to_fly)+"--")
         
        
        
        
        self.root.after(2000, self.update_clock)

app=App()
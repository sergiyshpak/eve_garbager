# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 13:06:20 2017

@author: g705586
"""
            
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

"""
gategate={}
gatosys={}

#50000001,30000777
#50000002,30000777
with open("gate_sys.txt", "r") as ins:
    for line in ins:
        line = line[:-1]
        my_list = line.split(",")
        gatosys[my_list[0]] = my_list[1]
        
        
#50000004,50001270
#50000005,50002266
with open("mapJumps.csv", "r") as ins:
    for line in ins:
        line = line[:-1]
        my_list = line.split(",")
        gategate[my_list[0]] = my_list[1]

inta1=0
f = open('sys_sys_topo.txt', 'a')        
for gata1,gata2 in gategate.items():
    inta1=inta1+1
    f.write(gatosys[gata1]+","+gatosys[gata2]+"\n")
f.close

"""




UREL1='https://zkillboard.com/kill/'

# JITA  https://zkillboard.com/system/30000142/
# UEDAMA  https://zkillboard.com/system/30002768/



koraba_w_sys="Jita"
jumpLimit=1000
minCost=0

for pair in sys.argv:

    my_list = pair.split(":")
    if my_list[0]=='jumpLimit':
        jumpLimit=my_list[1]
    if my_list[0]=='minCost':
        minCost=my_list[1]
    if my_list[0]=='sysa':
        koraba_w_sys=my_list[1]
    

print ("---= start --- jumpLimit:"+str(jumpLimit)
       +"  minCost:"+str(minCost)
       +"  sysa:"+koraba_w_sys)


while 1==1:
    url = 'https://redisq.zkillboard.com/listen.php' #?queueID=pipetka1023'   
    headers = {'user-agent': 'my-app-test/0.0.1'}
    r = requests.get(url, headers=headers)
    #print(r.text)
    if r.text!='{"package":null}':
        parsed_json = json.loads(r.text)
     #   f_hours_from_now = datetime.now() + timedelta(hours=4)
        datka=parsed_json['package']
        killid=str(datka['killID'])
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
            distURL="http://everest.kaelspencer.com/route/"+koraba_w_sys+"/"+systemDict.get(sysa,"figgevoznaet_sysa")+"/"
            #print(distURL)
            rdis = requests.get(distURL, headers=headers)
            #print(rdis.text)
            parsed_dist_json = json.loads(rdis.text)
         #   print("Distance to fly from "+systemDict.get(koraba_w_sys,"figgevoznaet_sysa")+" is "+str(parsed_dist_json["count"]))
            dist_to_fly=parsed_dist_json["count"]

        if int(dist_to_fly)<int(jumpLimit) and int(datka['zkb']['totalValue'])>int(minCost):
            print(timestamp
                + ' Jumps_to_loc '+str(dist_to_fly)
                + ' total$$$ '+totaldeneg
                + ' system  '+systemDict.get(sysa,"figgevoznaet_sysa") 
                + ' security ' +systemSec.get(sysa,"_____")  
                + ' ship ' + typesDict.get(shipp,"figgevoznaet_ship") 
                + ' Location ' + locDict.get(zkillLocationID,"GDETO")
                + ' DistFromSUN '+str(dista)
                + '      '+UREL1+killid+'/')
        else:
            print("-=skip=-")
 
        #f = open('workfile', 'a')            
        #f.write(timestamp+'   totaldeneg '+totaldeneg+'  sysa  '+systemDict.get(sysa,"figgevoznaet_sysa") 
        #    + ' ship ' + typesDict.get(shipp,"figgevoznaet_ship") 
        #    + ' Location ' + locDict.get(zkillLocationID,"GDETO")
        #    + '      '+UREL1+killid+'/' + '\n')
        #f.close
        


            
    time.sleep(sleepTime)
    
    
    
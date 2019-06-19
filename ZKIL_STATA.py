# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 13:06:20 2017

@author: g705586


sobiray statu of fresh kill, 
group by sysa,  
 dist to jump
 
to find active battles 

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


stata_dict = {}

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

printocount=0
printolimit=5

while 1==1:
    url = 'https://redisq.zkillboard.com/listen.php' #?queueID=pipetka1023'   
    headers = {'user-agent': 'my-app-test/0.0.1'}
    r = requests.get(url, headers=headers)
    if r.text!='{"package":null}':
        parsed_json = json.loads(r.text)
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

        if systemDict.get(sysa,"figgevoznaet_sysa")[0]!="J":
            
            countessa=0
            countessa=stata_dict.get(sysa,0)
            countessa=countessa+1
            stata_dict[sysa]=countessa
            
            printocount=printocount+1
            if printocount>printolimit:
                printocount=0
                for siska in stata_dict: 
                    dist_to_fly=100500
                    dist_to_fly=sys_sys.get(koraba_w_sys+systemDict.get(siska,"ololo"),100500)
                    if dist_to_fly==100500:
                        distURL="http://everest.kaelspencer.com/jump/"+koraba_w_sys+"/"+systemDict.get(siska,"figgevoznaet_sysa")+"/"
                        rdis = requests.get(distURL, headers=headers)
                        try:
                            parsed_dist_json = json.loads(rdis.text)
                            dist_to_fly=parsed_dist_json["jumps"]
                            sys_sys[koraba_w_sys+systemDict.get(siska,"ololo")]=dist_to_fly
                        except:
                            print("shit happend "+distURL)
                    sseka=str(systemSec.get(siska,11))
                    ssiska=systemDict.get(siska)
                    sdist=str(dist_to_fly)
                    sstatka=str(stata_dict[siska])
                    print(siska+"   seka- "+sseka +" -=- "+ssiska+" ---dist--" +sdist+ "   kills --- "+sstatka)
                print(" --------- " )                    

    time.sleep(sleepTime)
    
    
    
import yaml
import time
from datetime import datetime

file=open("Milestone1A.yaml")
data = yaml.load(file, Loader=yaml.FullLoader)
out=open("log.txt",'w')
def seq(dictionary,x,y):
    for key,val in dictionary.items():
        if y=="":
            out.write(str(datetime.now())+";"+x+"." +key+" Entry"+"\n")
            if val["Type"]=="Task":
                if val["Function"]=="TimeFunction":
                    out.write(str(datetime.now())+";" +x+"." +key +" Executing " + val["Function"]+ " (" + key+"_Input" + ", " + val["Inputs"]["ExecutionTime"]+")"+"\n")
                    time.sleep(int(val["Inputs"]["ExecutionTime"]))
                    #out.write(str(datetime.now())+";"+key+" Exit"+"\n")
            if val["Type"]=="Flow":
                if val["Execution"]=="Sequential":
                    seq(val["Activities"],x,key)
            out.write(str(datetime.now())+";"+x+"." +key+" Exit"+"\n")
        
        else:    
            out.write(str(datetime.now())+";"+x+"."+y+"." +key+" Entry"+"\n")
            if val["Type"]=="Task":
                if val["Function"]=="TimeFunction":
                    out.write(str(datetime.now())+";" +x+"."+y+"." +key +" Executing " + val["Function"]+ " (" + key+"_Input" + ", " + val["Inputs"]["ExecutionTime"]+")"+"\n")
                    time.sleep(int(val["Inputs"]["ExecutionTime"]))
                    #out.write(str(datetime.now())+";"+key+" Exit"+"\n")
            if val["Type"]=="Flow":
                if val["Execution"]=="Sequential":
                    seq(val["Activities"],x,key)
            out.write(str(datetime.now())+";"+x+"."+y+"." +key+" Exit"+"\n")
                        
for key,val in data.items():
    y=""
    out.write(str(datetime.now())+";"+key+" Entry"+"\n")
    if val["Type"]=="Flow":
        if val["Execution"]=="Sequential":
            seq(val['Activities'],key,y)
    out.write(str(datetime.now())+";"+key+" Exit"+"\n")
out.close()
print("exit")
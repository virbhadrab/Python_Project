import os
import datetime
import hashlib
import schedule
from sys import *

def hashfile(path,blocksize=1024):
    file = open(path,"rb")
    hasher = hashlib.md5()
    
    buf = file.read(blocksize)
    
    while len(buf) > 0:
        hasher.update(buf)
        buf = file.read(blocksize)
    
    file.close()
    
    return hasher.hexdigest()

def travelDir():
    
    path = argv[1]
    unique = {}
    
    flag = os.path.isabs(path)
    
    if flag == False:
        path = os.path.abspath(path)
        
    exists = os.path.isdir(path) 
    
    if exists:
        fd = open("Log.txt","a")
        fd.write(str(datetime.datetime.now()))
        
        for dirName,subdirs,fileList in os.walk(path):
            for filename in fileList:
                path = os.path.join(dirName,filename)
                
                file_hash = hashfile(path)
                
                if file_hash not in unique:
                    unique[file_hash] = filename
                else:
                    os.remove(path)
                    fd.write("\n")
                    fd.write(filename)
                    fd.write("\n")
                    print("Remove Successfully.")
        fd.close()
    else:
        print("Invalide Path :")

def main():
    
    print("------ Application Start -------")
    
    schedule.every(30).seconds.do(travelDir)
    
    while True:
        schedule.run_pending()
        
if __name__=="__main__":
    main()
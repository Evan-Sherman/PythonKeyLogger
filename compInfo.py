import socket
import uuid
import psutil
import sys
import os


def runCommand(comm):
    os.system(comm)

def get_files(startpath):
    fileStr = ""
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 2 * (level)
        fileStr += '{}{}/'.format(indent, os.path.basename(root)) + '\n'
        subindent = ' ' * 2 * (level + 1)
        for f in files:
            fileStr += '{}{}'.format(subindent, f) + '\n'

        return fileStr
    
def print_files(startpath):
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 2 * (level)
        print('{}{}/'.format(indent, os.path.basename(root)))
        subindent = ' ' * 2 * (level + 1)
        for f in files:
            print('{}{}'.format(subindent, f))


def getInfo(root):

    hostname = socket.gethostname()
    ip_addr = socket.gethostbyname(hostname)

    mac_str = ':'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff)
    for ele in range(0,8*6,8)][::-1])

    sys_name = sys.platform

    #[total, avalilable, percentUsed, used, free, active, inactive, buffers, caches, shared]
    mem = psutil.virtual_memory()
    total_mem = int(mem[0] / 1000000000)

    #[total, used, free, percent]
    disk= psutil.disk_usage('/')
    total_disk = int(disk[0] / 1000000000)
    info = ""
    info += f"Hostname: {hostname} \n"
    info += f"IP Address: {ip_addr}\n"
    info += f"MAC Address: {mac_str}\n"
    info += f"OS Name: {sys_name}\n"
    info += f"Total RAM: {total_mem} GB\n"
    info += f"Total Disk Space on this partition: {total_disk} GB\n"
    # fileHierarch = getAllFiles(root)

    return info, ""

def getAllFiles(fileName):
    files = ""
    for dirpath, dirnames, filenames in os.walk(fileName):
        for name in filenames:
            files += os.path.join(dirpath, name) + '\n'
        for name in dirnames:
            files += os.path.join(dirpath, name) + '\n'
    return files


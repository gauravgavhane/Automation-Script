import os
import psutil
import time
from sys import*
import os

def ProcessDisplay(log_dir = "LOgFile"):
    listprocess = []

    if not os.path.exists(log_dir):
        try:
            os.mkdir(log_dir)
        except:
            pass

    seperator = "-"*80
    log_path = os.path.join(log_dir, "Log%s.log"%(time.ctime()))
    f = open(log_path, 'w')
    f.write(seperator + "\n")
    f.write("Process Logger with Log Report Facility :"+time.ctime() + "\n")
    f.write(seperator + "\n")

    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['pid', 'name', 'username'])
            pinfo['vms'] = proc.memory_info().vms / (1024 * 1024)

            listprocess.append(pinfo);

        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    for element in listprocess:
        f.write("%s\n" %element)

def main():
    print("----LOG FILE----")
    print("Application Name : "+argv[0])

    if len(argv)!=2:
        print("Error:Invalid number of arguments")
        exit()
    if argv[1]=="H" or argv[1]=="h":
        print("This Script is used log record of running processes")
        exit()

    if argv[1]=="U" or argv[1]=="u":
        print("usage:Application AbsolutePath_of_Directory")
        exit()

    try:
        ProcessDisplay(argv[1])
    except ValueError:
        print("Error : Invalid datatype of input")
    except Exception:
        print("Error: Invalid Input")

if __name__ == "__main__":
    main()

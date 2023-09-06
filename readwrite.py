
from datetime import datetime
from log import Log

today = datetime.utcnow()
date = today.strftime("%Y-%m-%d")

# class Log:
#     def __init__(self, time, message):
#         self.time = time
#         self.message = message
    
#     def __str__(self) -> str:
#         return f"{self.time}: {self.message}"
        

def readfile(date=date):

    """

    Reads log file for date, if specified. Defaults to current date.

    """

    logs = []

    with open(f"./logs/{date}.txt", 'r') as f:
        file = [x.strip() for x in f.readlines()]
    
    for f in file:
        f = f.split("::")
        logs.append(Log(f[0], f[1]))
    
    print("Logs read")
    return logs



def writefile(data):

    '''

    Writes activity to the logfile for current date

    '''

    today = datetime.utcnow()
    d_time = today.strftime("%d/%m/%Y %H:%M:%S")
    date = today.strftime("%Y-%m-%d")
     
    try:
        new = open(f"./logs/{date}.txt", 'x')
        new.write(f"{data['payload']}\n")
        new.close()
    except FileExistsError:
        new = open(f"./logs/{date}.txt", 'a')
        new.write(f"{data['payload']}\n")
        new.close()



writefile({"topic": "hello", "payload": "Motion "})

# readfile("2023-09-06")

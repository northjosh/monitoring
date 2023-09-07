
from datetime import datetime
from log import Log


def get_date():
    today = datetime.utcnow()
    date = today.strftime("%Y-%m-%d")

    return date

# class Log:
#     def __init__(self, time, message):
#         self.time = time
#         self.message = message
    
#     def __str__(self) -> str:
#         return f"{self.time}: {self.message}"
        

def readfile(date=get_date()):

    """

    Reads log file for date, if specified. Defaults to current date.

    """

    print()

    logs = []

    with open(f"./logs/{date}.txt", 'r') as f:
        file = [x.strip() for x in f.readlines()]
    
    if len(file) != 0:
        for f in file:
            f = f.split("::")
            logs.append(Log(f[0], f[1]))
    else:
        logs = [f":: No Activities for {date} "]

    
    print("Logs read")
    print(logs)
    logs.reverse()
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


# writefile({"topic": "hello", "payload": "Motion "})
# readfile("2023-09-06")

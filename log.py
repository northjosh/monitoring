class Log:
    def __init__(self, time, message):
        self.time = time
        self.message = message
    
    def __str__(self) -> str:
        return f"{self.time}: {self.message}"
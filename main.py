from datetime import datetime 
def time_convert(time):
    t = datetime.strptime(time, '%I:%M:%S %p')
    return t.strftime('%H:%M:%S')
    
print(time_convert('02:20:00 PM'))    

from collections import namedtuple
from datetime import datetime
import psutil

def log(inter):
    f = open('log.txt', 'a')
    log = namedtuple('log', ['timedate', 'cpu', 'memory'])
    timedate = datetime.now()
    cpu = psutil.cpu_percent(interval=inter)
    svmem = psutil.virtual_memory()
    memory = svmem.percent
    string = str(log(timedate, cpu, memory))
    f.write(string + '\n')
    f.close

count = int(input('Введите число логов: '))
interval = int(input('Введите интервал логов: '))
for i in range(count):
    log(interval)

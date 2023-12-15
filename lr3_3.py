from collections import namedtuple
from datetime import datetime
import psutil
import platform
import argparse
import matplotlib.pyplot as plt
x = []
y = []
z = []

def log():
    f = open('log.txt', 'a')
    log = namedtuple('log', ['timedate','cpu', 'memory'])
    timedate = datetime.now()
    cpu = psutil.cpu_percent(interval=1)
    svmem = psutil.virtual_memory()
    memory = svmem.percent
    string = str(log(timedate, cpu, memory))
    f.write(string + '\n')
    f.close

count = int(input('Введите число логов: '))
for i in range(count):
    cpu = psutil.cpu_percent(interval=1)
    svmem = psutil.virtual_memory()
    memory = svmem.percent
    x.append(i+1)
    y.append(cpu)
    z.append(memory)
plt.plot(x, y)
plt.plot(x, z)
plt.show()

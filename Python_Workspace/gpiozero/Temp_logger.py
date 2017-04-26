from gpiozero import CPUTemperature
from time import sleep, strftime, time
import matplotlib.pyplot as plt

cpu = CPUTemperature()

plt.ion()
x = []
y = []
dtemp = 20

def write_temp(temp):
    with open("cpu_temp.csv", "a") as log:
        log.write("{0},{1}\n".format(strftime("%Y-%m-%d %H:%M:%S"),str(temp)))

def graph(temp):
    y.append(temp)
    x.append(time())
    plt.clf()
    plt.scatter(x,y)
    plt.title('Live Temp Log', fontsize=20)
    plt.xlabel('Time', fontsize=16)
    plt.ylabel('Temp', fontsize=16)
    plt.plot(x,y, color="red",  linewidth=2.5, linestyle="-")
    plt.ylim(0,100)
    plt.draw()
    
while True:
    temp = cpu.temperature
    write_temp(temp-dtemp)
    graph(temp-dtemp)
    sleep(1)

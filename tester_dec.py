
proc = 'AMD Ryzen 5 3550H (2.1 - 3.7 GHz)'
speed = proc.split("(")[1].replace(')', '').split("ГГц")[0]
try:
    print(type(float(speed)))
except:
    speed = proc.split("(")[1].replace(')', '').split("GHz")[0].split('-')[0]
cpu_serial = proc.split(' ')[0] + ' ' + proc.split(' ')[1] + ' ' + proc.split(' ')[2]
print(type(float(speed)))
print(cpu_serial)
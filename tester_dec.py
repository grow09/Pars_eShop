
proc = 'AMD Ryzen 5 3550H (2.1 - 3.7 GHz)'
speed = proc.split("(")[1].replace(')', '').split("ГГц")[0]
try:
    print(type(float(speed)))
except:
    speed = proc.split("(")[1].replace(')', '').split("GHz")[0].split('-')[0]
print(type(float(speed)))
print(speed)
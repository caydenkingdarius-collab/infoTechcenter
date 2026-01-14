#Welcome Branch

# Libraries imported here
import sys
import time

print("\nWelcome Branch - Developer: Cayden Johnson")
print("\nWelcome to infotech center V.1.0")


x = 0
ellipsis = 0

while x != 20:
    x += 1
    ellipsisMessage = ("InfoTechCenter OS Booting" + "."* ellipsis)
    ellipsis += 1
    sys. stdout.write("\r" + ellipsisMessage +"   ")
    sys.stdout.flush()
    time.sleep(.5)
    if ellipsis == 4:
        ellipsis = 0
    if x == 20:
        print("\nOperating system Booted up - Retina scammd - Acces Granted")  
# Welcome Branch
# Libraries imported here
import sys
import time
import os

# Enable ANSI escape codes on Windows
if os.name == "nt":
    os.system("")

# ANSI color codes
GREEN = "\033[92m"
BLACK_BG = "\033[40m"
RESET = "\033[0m"

# Clear screen and set colors
print(BLACK_BG + GREEN, end="")

print("\nWelcome Branch - Developer: Cayden Johnson")
print("\nWelcome to infotech center V.1.0")

x = 0
ellipsis = 0

while x != 20:
    x += 1
    ellipsisMessage = "InfoTechCenter OS Booting" + "." * ellipsis
    ellipsis += 1

    sys.stdout.write("\r" + ellipsisMessage + "   ")
    sys.stdout.flush()
    time.sleep(0.5)

    if ellipsis == 4:
        ellipsis = 0

    if x == 20:
        print("\nOperating system Booted up - Retina scammed - Access Granted")

# Reset colors at the end
print(RESET)
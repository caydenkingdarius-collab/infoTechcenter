#betatestdev

# ============================================
# Welcome Branch
# Developer: Cayden Johnson
# Program: InfoTechCenter OS Boot Screen
# Version: 1.0
# ============================================

# Import required standard libraries
import sys      # Used for writing output without a newline
import time     # Used for delays (sleep)
import os       # Used for operating system interactions

# Enable ANSI escape codes on Windows terminals
# This allows color codes to work properly
if os.name == "nt":
    os.system("")

# ANSI color codes for terminal styling
GREEN = "\033[92m"      # Green text color
BLACK_BG = "\033[40m"   # Black background color
RESET = "\033[0m"       # Reset colors back to default

# Clear screen styling and apply colors
print(BLACK_BG + GREEN, end="")

# Display welcome messages
print("\nWelcome Branch - Developer: Cayden Johnson")
print("\nWelcome to infotech center V.1.0")

# Initialize counters
x = 0           # Controls how long the boot loop runs
ellipsis = 0    # Controls the number of dots in the loading animation

# Boot-up animation loop
while x != 20:
    x += 1

    # Create loading message with animated dots
    ellipsisMessage = "InfoTechCenter OS Booting" + "." * ellipsis
    ellipsis += 1

    # Overwrite the same line in the terminal
    sys.stdout.write("\r" + ellipsisMessage + "   ")
    sys.stdout.flush()

    # Pause to create animation effect
    time.sleep(0.5)

    # Reset dots after reaching three
    if ellipsis == 4:
        ellipsis = 0

    # Final boot message when loop completes
    if x == 20:
        print("\nOperating system Booted up - Retina scammed - Access Granted")

# Reset terminal colors before exiting
print(RESET)

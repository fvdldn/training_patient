"""deze module laat zien hoeveel regels input er zijn op de commandline
lines in de standard input
Input: any string from the system standard input"""

import sys

count = 0

for line in sys.stdin:
    count += 1

print(count, "lines in de standaard input")

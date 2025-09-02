import random
import sys
import os

# Change the current working directory to the script's directory
script_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
os.chdir(script_dir)

N = 100000

arr = []
s = "abcdefghijklmnopqrstuvwxyz"
for _ in range(N):
    i = random.randrange(0, 25)
    arr.append(s[i])

arrStr = ''.join(arr)

with open('1917-B.in', 'w') as f:
    f.write('1\n')
    f.write('1000000\n')
    f.write(f'{arrStr}\n')

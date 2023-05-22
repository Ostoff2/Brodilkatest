import os

a="st"
b=a+"\n"


with open('Settings.txt', 'r') as f1, open('Settings.txt', 'w') as f2:
    lines = f1.readlines()

    for line in lines:
        line = line.strip()
        if line == '1':
            f2.write('2')
        else:
            f2.write(line)

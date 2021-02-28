import os
import subprocess


for file in os.listdir('templates'):
    file = os.path.join('templates', file)
    print(file)
    BOOL = 0
    STRINGS = []
    with open(file, 'r') as f:
        string = ""
        for char in f.read():
            if char == '"':
                BOOL = (BOOL + 1) % 2
                if string != "":
                    STRINGS.append(string)
                string = ""
            if BOOL:
                if char != '"':
                    string += char
    with open(file, 'r') as f:
        strings = [string for string in STRINGS if string.startswith('http') and "uploads-ssl" in string]
        print(strings)
        read = f.read()
        temp = "{{ url_for('static', filename='imgs/%s') }}"
        for string in strings:
            name = string.split('_')[-1]
            proc = subprocess.Popen(['wget', '-O', 'static/imgs/' + name, string])
            print(name)
            proc.wait()
            read = read.replace(string, temp % name)
    
    with open(file, 'w') as f:
        f.write(read)

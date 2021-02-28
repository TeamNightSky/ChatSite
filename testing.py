from utils.stats import find_files
import subprocess


for file in find_files('templates'):
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

        strings = [string for string in STRINGS if string.startswith('http') and "uploads-ssl" in string]
        temp = "{{ url_for('static', filename='img/%s'"
        file = f.read()
        for string in strings:
            name = string.split('_')[-1]
            file = file.replace(string, temp % name)
            subprocess.Popen(['wget', '-O', 'static/imgs/' + name, string]).wait()

    

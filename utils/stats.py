import os


def find_files(directory=os.getcwd()):
    for file in os.listdir(directory):
        path = os.path.join(directory, file)
        if os.path.isfile(path):
            try:
                open(path, encoding='UTF-8').read() 
                yield path
            except:
                pass
        elif os.path.isdir(path):
            yield from find_files(path)


def total_files():
    return len(list(find_files()))

def total_lines():
    return sum([len(open(file, 'r').readlines()) for file in find_files()])

def total_chars():
    return sum([len(open(file, 'r').read()) for file in find_files()])
    
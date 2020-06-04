index = {
    'time' : 0,
    'date' : 1,
    'storage' : 2
}

def get_def(prop):
    f = open("defaults.txt")
    props = f.readlines()
    f.close()
    req = props[index[prop]]
    req = req.replace("\n", "")
    return req

def mod_def(prop, new_def):
    new = new_def + '\n'
    fr = open("defaults.txt", "r")
    props = fr.readlines()
    fr.close()
    fw = open("defaults.txt", "w")
    del props[index[prop]]
    props.insert(index[prop], new)
    for pro in props:
        fw.write(pro)
    fw.close()

if __name__ == '__main__':
    pass
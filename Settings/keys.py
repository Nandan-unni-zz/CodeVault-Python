# key = imp.load_souce('default', './Settings/keys.py')
import time
default = {
    'time' : 0,
    'date' : 1,
    'storage' : 2
}

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
    print(req)
    return req

def mod_def(prop, new_def):
    new = new_def + '\n'
    fr = open("defaults.txt", "r")
    props = fr.readlines()
    fr.close()
    fw = open("defaults.txt", "w")
    print(index[prop], props)
    del props[index[prop]]
    props.insert(index[prop], new)
    for pro in props:
        fw.write(pro)
    fw.close()

months = {
    1 : 'Jan',
    2 : 'Feb',
    3 : 'March',
    4 : 'April',
    5 : 'May',
    6 : 'June',
    7 : 'July',
    8 : 'Aug',
    9 : 'Sept',
    10 : 'Oct',
    11 : 'Nov',
    12  : 'Dec'
}
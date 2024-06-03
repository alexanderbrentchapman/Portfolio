import json

x = open("data.json", 'r')
jsondata = x.read()
x.close()

print(x)
print(type(jsondata))
ddict = dict(jsondata)
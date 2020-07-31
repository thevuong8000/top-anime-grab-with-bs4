import json

# f = open('../data/HanNom.json', 'w')
# data = "鴻"
# data = data.encode('utf-16')
# print(data.decode('utf-16'))
# f.write(str(data))
# f.close()
link = "../data/HanNom.json"
with open(link) as file:
    data = json.load(file)
for (key, value) in data.items():
    # print(key, value)
    print(key + " ->", key.encode('utf-8'), ord(key))
    # print(key.encode('iso-8859-1').decode('utf-8') + ": " + value[0].encode('iso-8859-1').decode('utf-8'))
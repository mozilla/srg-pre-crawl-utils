import json
import matplotlib.pyplot as plt

jsonfile = open('final.json')
jsonstr = jsonfile.read()
jsondata = json.loads(jsonstr)

finaltld = {}

def parse(string):
  return string.split("/")[2]
  #for other understanding of TLD+1, use the below return function
  #return "".join([str.split("/")[2], "/", str.split("/")[3]])

for i in range(len(jsondata)):
  for j in jsondata[i][1]:
    if j.startswith("http"):
      tld = parse(j)
      finaltld[tld] = finaltld.get(tld, 0) + 1

sort = sorted(finaltld.items())
x, y = zip(*sort)

xvals = range(len(x))

plt.figure(figsize=(20,10))
plt.xticks(xvals, x, rotation="vertical")
plt.plot(xvals, y)
#plt.show()
plt.savefig('plot.png')

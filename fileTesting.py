f = open("CST_3112_Tutorial_Grades.csv","r+")
for line in f:
    lines = f.readline()
    oneLine=lines.split(",")
    print(oneLine[0],oneLine[1])
    toText=oneLine[0]+"\t" +oneLine[1] +"\n"
    g = open("hell.txt","a")
    g.write(toText)
f.close()
g.close()

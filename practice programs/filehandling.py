f=open('myfile.txt','r')
i=0
while True:
    i=i+1
    line = f.readline()
    if not line:
        break
        m1= line.split(",")[0]
        m2=line.split(",")[1]
        m3=line.split(",")[3]
        print(f"marks of student {i} is {m1}")
        print(f"marks of student {i} is {m2}")
        print(f"marks of the student {i} is {m3}")
        print(line)
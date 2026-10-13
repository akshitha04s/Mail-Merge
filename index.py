check="[name]"
c=1
with open("names.txt",'r') as names:
    nnames=names.readlines()
with open("letterformat.txt",'r') as format:
    contents=format.read()
for name in nnames:
    name=name.strip()
    with open(f"{c}.txt",'w') as curr:
        curr.write(contents.replace(check,name))
        print(curr)
        c+=1
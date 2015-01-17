print sum((i+1)*sum(ord(c)-ord('A')+1 for c in name) for i,name in enumerate(sorted(open("names.txt","r").readline().replace('"',"").split(","))))

rf = open('dutchWordList.txt','r')
w = open('formattedWL.txt','w')

nl = rf.readline()
i = 0
while nl != "":
	nl = nl.replace('\t','')
	nl = nl.replace('\n','')
	nl = nl.split('.')[1]
	dutch = str(nl.split(" ")[0])
	w.write(dutch + "$_{")
	trans = nl.split(" ")[1:]
	for i in range(len(trans)):
		if i>0:
			w.write(" ")
		w.write(trans[i])
	

	w.write("}$")
	if( i == 1):
		w.write("\\\\ \n")
	else:
		w.write("&")
	i = (i+1)%2
	nl=rf.readline()

print "Done"

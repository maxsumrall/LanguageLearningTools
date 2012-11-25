readF = open('wordList.txt','r')
writeTo = open('swedishWords.txt','w')
line = readF.readline().split("\t")
while len(line)> 1:
	swedishWord = len(line)
	swedishWord = line[swedishWord-1]#the last elemet
	print swedishWord
	writeTo.write(swedishWord + "")
	line = readF.readline().split("\t")
print "Done!"
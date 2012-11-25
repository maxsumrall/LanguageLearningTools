swedishWord = open("swedishWords.txt",'r')
englishWord = open("englishTrans.txt",'r')
tex = open("texOutput.txt",'w')

i = 1
while i < 51:
	tex.write(swedishWord.readline().rstrip())
	tex.write("$_{")
	tex.write(englishWord.readline().rstrip())
	tex.write("}$")
	if(i%2 == 0):
		tex.write("\\\\ \n")
	else:
		tex.write(" & ")
	i+=1

swedishWord.close()
englishWord.close()
tex.close()
print "Done"
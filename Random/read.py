fw = open("example.txt", 'a')
fw.write("Writing some stuffs in my text file\n")
fw.write("I like to Code and Pray\n")
fw.close()

fr = open("example.txt", "r")
text = fr.read()
print (text)
fr.close()
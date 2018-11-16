import time as t

greetings = ["great", "good", "fine"]
name1 = "Keenah"

'''
if name == "Keenah":
    print("Hello, ", name)
else:
    print("Oh, well what is your name then?")
'''

def checkName(name):
    confirm = input(str("Is your name " + name + "? "))
    confirm = confirm.lower()

    if confirm == "yes":
        print("Hello,", name)
	ans1 = input("How are you? ")
	if ans1 in greetings:
                    print("That's great")
    	else:
                    print("What went wrong?")
	    t.sleep(3)
    else:
        print("We're sorry about that.")
        t.sleep(3)

checkName(name1)

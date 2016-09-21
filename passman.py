import random
import atexit

uppercase_letters = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z".split()
lowercase_letters = [x.lower() for x in uppercase_letters]
numbers = [0,1,2,3,4,5,6,7,8,9]
special_chars = ['!','$','%','@','#']
character_classes = [uppercase_letters, lowercase_letters, numbers, special_chars]

entries = []

def generatePassword(allowed_classes, length):
    pw = ""
    for x in xrange(length):
        char_class = int(random.choice(allowed_classes))
        char = random.choice(character_classes[char_class])
        pw = pw + str(char)
    return pw



class Entry:
    username = ""
    password = ""
    website = ""

    def __init__(self, username, website, password=None, len=None, allowed_chars=None):
        self.username = username
        self.website = website
        pw = ""

        if password != None:
            self.password = password
        else:
            for x in xrange(len):
                char_class = int(random.choice(allowed_chars)) - 1
                char = random.choice(character_classes[char_class])
                pw = pw + str(char)
            self.password = pw


    def toString(self):
        return self.username + '\t' + self.website + '\t' + self.password


def listAll():
    for entry in entries:
        print entry.toString()
    # git test


def create():
    username = ""
    website = ""
    len = ""
    allowed_chars = ""
    print "Enter the username."
    username = raw_input()
    print "Enter the website."
    website = raw_input()
    print "Enter the desired length."
    len = int(raw_input())
    print "Enter the numbers corresponding to which character classes you would like to include."
    print "e.g. Enter '123' if you want to include uppercase letters, lowercase letters, and numbrers."
    print "1. Uppercase letters (A-Z)"
    print "2. Lowercase letters (a-z)"
    print "3. Numbers (0-9)"
    print "4. Special characters (!$%@#)"
    allowed_chars = raw_input()

    entry = Entry(username=username, website=website, len=len, allowed_chars=allowed_chars)

    entries.append(entry)


def loadList():
    f = open("pw.txt", "r")
    for line in f:
        stuff = line.split('\t')

        if (stuff[0] != "" and stuff[1] != "" and stuff[2] != ""):
            entry = Entry(username=stuff[0], website=stuff[1], password=stuff[2])
            entries.append(entry)
    f.close()


#@atexit.register
#def saveList():
#    f = open("pw.txt", "w")
#    for entry in entries:
#        f.write(entry.toString())
#    f.close()


def main():
    choice = 0

    loadList()

    while (True):
        print "Please select an option.\n\r"
        print "1. List entries"
        print "2. Create new entry"
        print "3. Quit"

        choice = raw_input()

        if choice == "1":
            listAll()
        elif choice == "2":
            create()
        elif choice == "3":
            exit()
        else:
            print "You have chosen an invalid option. Please try again."


if __name__ == "__main__": main()
# line.rstrip() is used to strip the whitespace at the end of the file
# casefold() is used to turn the string into all lowercases so I used this to match
# Some titles were very long so this required them to be shortened when displaying them.

def sortYear():
    year = ""
    listofFile = []
    linesofFile = []
    listofYears = []
    yearstart = input("Enter start year : ")
    yearend = input("Enter end year : ")

    f = open("booklist.txt", 'r')
    if yearstart not in f.read():
        print("\nNo entries found")
        f.close()

    else:
        with open("booklist.txt", 'r') as file:
            for line in file:
                linesofFile.append(line.rstrip())
            for entry in linesofFile:
                listofFile.append(entry.split(','))

            for line in listofFile:
                if int(line[-2]) >= int(yearstart) and int(line[-2]) <= int(yearend):
                    listofYears.append(line)

            print('{0}                                         | {1:<44}| {2:<20}'.format('Title', 'Author',
                                                                                          'Publication Year'))
            print('{0:-<117}'.format(''))
            for line in listofYears:
                print("{0:<44}|{1:<20}                           |{2:<25}".format(line[0][:44], line[1], line[-2]))


def showRating():
    occ = 0
    rating = ""
    listofFile = []
    linesofFile = []
    ratingEntries = []
    rating = input("\nEnter rating : ")

    with open("booklist.txt", 'r') as file:
        for line in file:
            linesofFile.append(line.rstrip())
        for entry in linesofFile:
            listofFile.append(entry.split(','))
        for line in listofFile:
            if line[2] == rating:
                ratingEntries.append(line)
                occ += 1
        if occ < 1:
            print("\nEntry not found")
        else:
            print('{0}                                         | {1:<44}| {2:<20}'.format('Title', 'Author',
                                                                                          'Publication Year'))
            print('{0:-<117}'.format(''))
            for line in ratingEntries:
                print("{0:<44}|{1:<20}                           |{2:<25}".format(line[0][:44], line[1], line[-2]))


def showAuthor():
    occ = 0
    listofFile = []
    linesofFile = []
    authorEntries = []
    author = input("\nEnter an author's name (or part of a name): ")
    with open("booklist.txt", 'r') as file:
        for line in file:
            linesofFile.append(line.rstrip())
        for entry in linesofFile:
            listofFile.append(entry.split(','))
        for line in listofFile:
            if author.casefold() in line[1].casefold():
                authorEntries.append(line)
                occ += 1
        if occ >= 1:
            print('{0}                                         | {1:<44}| {2:<20}'.format('Title', 'Author',
                                                                                          'Publication Year'))
            print('{0:-<117}'.format(''))
            for line in authorEntries:
                print("{0:<44}|{1:<20}                           |{2:<25}".format(line[0][:44], line[1], line[-2]))
        else:
            print("\nEntry not found")


def showTitle():
    occ = 0
    listofFile = []
    linesofFile = []
    titleEntries = []
    title = input("\nEnter a Title name (or part of a Title): ")
    with open("booklist.txt", 'r') as file:
        for line in file:
            linesofFile.append(line.rstrip())
        for entry in linesofFile:
            listofFile.append(entry.split(','))
        for line in listofFile:
            if title.casefold() in line[0].casefold():
                titleEntries.append(line)
                occ += 1
        if occ >= 1:
            print('{0}                                         | {1:<44}| {2:<20}'.format('Title', 'Author',
                                                                                          'Publication Year'))
            print('{0:-<117}'.format(''))
            for line in titleEntries:
                print("{0:<44}|{1:<20}                           |{2:<25}".format(line[0][:44], line[1], line[-2]))
        else:
            print("\nEntry not found")


def menu():
    print("\n1 Enter year range")
    print("\n2 Enter minimum rating")
    print("\n3 Search for author")
    print("\n4 Search for title")
    print("\nQ Quit")


choice = ''
while choice != 'Q':
    menu()
    choice = input("\nEnter a choice > ")
    if choice == '1':
        sortYear()
    elif choice == '2':
        showRating()
    elif choice == '3':
        showAuthor()
    elif choice == '4':
        showTitle()
    elif choice == 'Q':
        break
    else:
        print("\nPlease try again the format of the menu and enter one of the following:")



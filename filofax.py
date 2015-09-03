# BUGGFIX
#
# månadsvy
#
# bläddra över årsgränser antingen genom exception handling eller förfinad bläddringsfunktion

# Titel: Filofax
# Författare: Tobias Mattsson
# Datum: 2015-09-03
#
# Det här är ett program som försöker härma en filofax.
# Programmet lagrar datum och minnesanteckningar på fil.

from time import *
from Catalog import *

# -------- Hjälpfunktioner --------

# Gör om en textsträng till en datum.
def str2date(date_str):
    return strptime(date_str, '%Y-%m-%d')

# Gör om ett datum till en textsträng.
def date2str(date):
    return strftime('%Y-%m-%d', date)

# Genererar en lista med månadens dagar.
def daysOfMonth(year, month):
    days = []
    for day in range(0, 32):
        days.append(day)
        try:
            strptime(str(year) + '-' + str(month) + '-' + str(day), '%Y-%m-%d')
        except ValueError:
            days.remove(day)
    return days

# -------- Funktioner för gränssnitt --------

# Skriver ut valmenyn.
def printMenu():
    print()
    print('Main menu >')
    print('(N)ext page')
    print('(P)revious page')
    print('A(d)d a note')
    print('R(e)move a note')
    print('(A)dd page')
    print('(R)emove page')
    print('(S)how pages')
    print('(F)lip to page')
    print('(C)heck date')
    print('(Q)uit')

# Skriver ut valda datumets aktivitet.
def printCurrent(filofax):
    print()
    print("Current page(" + date2str(filofax.current_date) + "):")
    if filofax.findPage(filofax.current_date) == None:
        print('N/A')
    else:
        print(filofax.findPage(filofax.current_date).note, end = '')

# Läser in och returnerar första bokstaven i användarens val som stor bokstav.
def choose():
    choice = ''
    while choice == '':
        choice = input('What do you want to do? ')
    print()
    return choice[0].upper()

# Läser in och returnerar ett datum som användaren skriver in.
def chooseDate():
    while True:
        choice = input('Which date(YYYY-MM-DD)? ')
        # Denna kontroll är för att t.ex. 8 är en giltig månad, men formatet skall vara 08.
        if len(choice) == 10:
            # Kontrollerar att det är ett giltigt datum.
            try:
                strptime(choice, "%Y-%m-%d")
            except ValueError:
                pass
            return strptime(choice, '%Y-%m-%d')
        else:
            print('Not a valid date! Please try again')

def chooseIndex():
    while True:
        choice = input('Which note do you want to remove(Index)? ')
        try:
            int(choice)
            break
        except:
            print('Try again!')
    return int(choice)

# Läser in och returnerar en aktiviet som användaren skriver in.
def typeNote():
    note = input('Type in you text: ')
    return note

# Lägger till en sida.
def addPage(filofax):
    if filofax.newPage(filofax.current_date):
        print('Page added!')
    else:
        print('Page already exists!')

# Tar bort en sida.
def removePage(filofax):
    if filofax.isPage(filofax.current_date):
        filofax.removePage(filofax.current_date)
        print('Page removed!')
    else:
        print('There is no page to remove.')

# Lägger till en anteckning.
def addNote(filofax):
    if filofax.isPage(filofax.current_date):
        note = typeNote()
        filofax.addNote(note)
        print('Note added!')
    else:
        print('There is no page!')

# Tar bort en anteckning.
def removeNote(filofax):
    if filofax.numNotes(filofax.current_date) == 1:
        filofax.removeNote(0)
        print('Note removed!')
    elif filofax.numNotes(filofax.current_date) == -1:
        print('There is no page with this date.')
    elif filofax.numNotes(filofax.current_date) == 0:
        print('There is no note on this page.')
    else:
        while True:
            index = chooseIndex()
            if filofax.removeNote(index):
                print('Note removed!')
                break
            else:
                print('Wrong index!')

# Visar alla sidors aktivitet(er).
def showPages(filofax):
    print("Overview of all sheets:")
    for page in filofax.pages:
        print(date2str(page.date) + ': ')
        for text in page.note:
            print(text, end = '')
            print()

# Visar dagens aktivitet.
def showPage(filofax, date):
    if filofax.numNotes(date) >= 0:
        print("Notes found at " + strftime('%Y-%m-%d', date) + ':')
        print(filofax.findPage(date).note)
    else:
        print("No page found!")

# Returnerar dagens datum som en sträng.
def todaysDate():
    return localtime()

# -------- Huvudprogram --------

def mainProgram():
    print("- Welcome to version 0.6 of Filofax")
    print("- Type the first letter of the alternative in the menu to execute it.")
    try:
        filofax = Catalog(FILENAME)
    except UnboundLocalError:
        print('File ' + FILENAME + ' not found!')
    printCurrent(filofax)
    printMenu()
    choice = choose()
    while choice != 'Q':
        if choice == 'N':
            filofax.changeDate(1)
        if choice == 'P':
            filofax.changeDate(-1)
        if choice == 'D':
            addNote(filofax)
        if choice == 'E':
            removeNote(filofax)
        if choice == 'A':
            addPage(filofax)
        if choice == 'R':
            removePage(filofax)
        if choice == 'S':
            showPages(filofax)
        if choice == 'F':
            date = chooseDate()
            filofax.setDate(date)
        if choice == 'C':
            date = chooseDate()
            showPage(filofax, date)
        printCurrent(filofax)
        printMenu()
        choice = choose()
    filofax.save(FILENAME)

FILENAME = 'filofax.txt'
mainProgram()

# findPage och isPage är väldigt lika. Fix it! :D
# addPage och removePage bör fungera på liknande sätt, men det gör de inte. Den ena returnerar och den andra inte.

from time import *
from Page import *

# -------- En klass som beskriver en katalog. --------
# Attribut:
#   pages - en lista som innehåller samtliga sidor.
#   current_date - aktuellt datum (uppslaget), består endast av år-månad-dag.
#
class Catalog:
    # Skapar en katalog över de sidor som finns lagrade på fil.
    def __init__(self, filename):
        self.pages = []
        self.current_date = strptime(str(localtime()[0]) + '-' + str(localtime()[7]), '%Y-%j')
        file = open(filename, 'rU')
        for line in file:
            parts = line.strip().split('/')
            iteration = 0
            note = []
            for part in parts:
                # Hoppa över första delen av raden.
                if iteration == 0:
                    iteration = 1
                    pass
                # Lägg inte till tomma anteckningar.
                elif part != '':
                    note.append(part)
            # Tar med rader som är rätt formatterade.
            if len(parts) >= 2:
                page = Page(strptime(parts[0], '%Y-%m-%d'), note)
                self.pages.append(page)
        file.close()
    
    # Sparar hela katalogen på fil.
    # Format: <date>/<note>(/<note>/<note>...)\n
    def save(self, filename):
        file = open(filename, 'w')
        for page in sorted(self.pages, key = lambda page: page.date):
            file.write(strftime('%Y-%m-%d', page.date) + '/' + '/'.join(page.note) + '\n')
        file.close()

    # Returnerar en sida med ett visst datum.
    def findPage(self, date):
        for page in self.pages:
            if page.date == date:
                return page
        return None

    # Returnerar True om sidan finns, annars returneras False.
    def isPage(self, date):
        is_page = False
        for page in self.pages:
            if page.date == date:
                is_page = True
                break
        return is_page

    # Skapar en ny sida.
    def newPage(self, date):
        page_created = False
        if not self.isPage(date):
            page = Page(date, [])
            self.pages.append(page)
            page_created = True
        return page_created
    
    # Lägger till en anteckning till en sida.
    def addNote(self, note):
        note_added = False
        if self.isPage(self.current_date):
            self.findPage(self.current_date).addNote(note)
            note_added = True
        return note_added

    # Tar bort en anteckning med ett givet index från ett blad.
    def removeNote(self, index):
        note_removed = False
        page = self.findPage(self.current_date)
        if index + 1 <= len(page.note):
            page.removeNote(index)
            note_removed = True
        return note_removed

    # Läser in och returnerar användarens val.
    #def choose(self):
    #    return

    # Ändrar aktuellt datum i katalogen.
    def changeDate(self, change):
        year = self.current_date[0]
        day = self.current_date[7]
        new_date = strptime(str(year) + '-' + str(day + change), '%Y-%j')
        self.current_date = new_date

    # Sätter aktuellt datum i katalogen.
    def setDate(self, date):
        self.current_date = date

    # Tar bort en sida.
    def removePage(self, date):
        for page in self.pages:
            if page.date == date:
                self.pages.remove(page)

    # Returnerar antalet anteckningar för en given sida.
    def numNotes(self, date):
        num_notes = -1
        if self.isPage(date):
            page = self.findPage(date)#self.current_date)
            num_notes = len(page.note)
        return num_notes

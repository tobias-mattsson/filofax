from time import *

# -------- En klass som beskriver en sida. --------
# Attribut:
#   date - datumet för minnesanteckningen
#   note - minnesanteckningen
#
class Page:
    # Skapar en ny sida
    def __init__(self, date, note):
        self.date = date
        self.note = note

    # Returnerar en sträng som beskriver sidan
    # Format: <date>: <note>
    def __str__(self):
        self.note = ''
        for each in self.note:
            self.note.append(each)
        return strftime('%Y-%m-%d', self.date) + ': ' + self.note

    # Lägger till en ny anteckning till listan över anteckningar.
    def addNote(self, new_note):
        self.note.append(new_note)

    # Tar bort en anteckning med ett givet index.
    def removeNote(self, index):
        self.note.pop(index)

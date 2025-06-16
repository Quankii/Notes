
from ToolsDB import ToolsDB
from ToolsHTML import ToolsHTML

class Menu:
    def __init__(self):
        with open('menu.txt') as file:
            self.menu = file.read()
        
        self.tdb = ToolsDB()
        self.thtm = ToolsHTML()
        self.StartMenu()

    # Виводить меню
    def printMenu(self):
        notes = self.tdb.returnNotes(None)
        for note in notes:
            print(f"№ {note[0]}.\nName: {note[1]}\nPriority: {note[3]}\n\tDescription: {note[2]}")
            input("\nНаступна (Enter)..")

#Запускає меню
    def StartMenu(self):
        while True:
            print(self.menu)
            try:
                WhoDo = int(input("\n\t\tЩо робим?: "))
            except ValueError:
                print("Виберіть номер дії")
                continue

            if WhoDo == 6:
                break
            elif WhoDo == 1:
                self.printMenu()
            elif WhoDo == 2:
                self.tdb.WriteNewNote()
            elif WhoDo == 3:
                self.printMenu()
                self.tdb.DeleteNote()
            elif WhoDo == 4:
                self.printMenu()
                self.tdb.ChangeNote()
            elif WhoDo == 5:
                self.thtm.LoadHtmlPage()



m = Menu()
m.StartMenu()
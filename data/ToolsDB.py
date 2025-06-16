
import sqlite3 as sq



class ToolsDB:

    def __init__(self):
        self.__db_path = 'db/notes.db'
        self.__createDB()


    # Створює БД
    def __createDB(self):
        with sq.connect(self.__db_path) as con:
            cur = con.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS notes (id_note INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, description TEXT, priority TEXT)")

    # Вставновлює приорітет
    @classmethod
    def __change_priority(self):
        PriorityNote = input("Дайте приорітет нотатці[Low - 1; Default - 2; High - 3] (Enter якщо Default): ")

        if PriorityNote.lower() in ('3', 'high'):
            PriorityNote = 'High'
        elif PriorityNote.lower() in ('1', 'low'):
            PriorityNote = 'Low'
        else:
            PriorityNote = 'default'

        return PriorityNote

    # Збирає данні про нотатку
    @classmethod
    def __ask_info_note(self):

        NameNote = input("Введіть ім'я нотатці: ")
        DescriptionNote = input("Введіть саму нотатку: ")
        PriorityNote = self.__change_priority()

        return (NameNote, DescriptionNote, PriorityNote)

    # Записує нотатку в БД
    def WriteNewNote(self):
        info = self.__ask_info_note()
        with sq.connect(self.__db_path) as con:
            cur = con.cursor()
            cur.execute("INSERT INTO notes(name, description, priority) VALUES (?, ?, ?)", info)

    # Збирає данні з БД
    def __read_bd(self, type_search=None):
        list_priority = ("Low", "Default", "High")

        if type_search == 'L':
            priority_search = list_priority[0]
        elif type_search == 'D':
            priority_search = list_priority[1]
        elif type_search == 'H':
            priority_search = list_priority[2]
        else:
            priority_search = 'all'

        with sq.connect(self.__db_path) as con:
            cur = con.cursor()

            if priority_search == 'all':
                cur.execute("SELECT * FROM notes")
                return cur.fetchall()
            else:
                cur.execute("SELECT * FROM notes WHERE priority == ? ", (priority_search, ))
                return cur.fetchall()

    # Вертає нотатки з БД
    def returnNotes(self, type_r = 'a'):
        if type_r == 'a':
            HowRead = input("Які нотатки по приорітетах читати [Low - 1; Default - 2; High - 3] (Enter якщо всі)?: ")

        HowRead = 'non'

        # L - Low; D - Default; H - High; A - All
        if HowRead.lower() in ('1', 'low'):
            return self.__read_bd("L")
        elif HowRead.lower() in ('2', 'default'):
            return self.__read_bd('D')
        elif HowRead.lower() in ('3', "H"):
            return self.__read_bd("H")
        else:
            return self.__read_bd()

    # Видаляє нотатки з БД
    def DeleteNote(self):
        notes = self.__read_bd()

        try:
            number = int(input("Введіть номер нотатки яку хочеш видалити: "))
        except ValueError:
            print("Номер має бути цифрою")

        for note in notes:
            if note[0]== number:
                with sq.connect(self.__db_path) as con:
                    cur = con.cursor()

                    cur.execute("DELETE FROM notes WHERE id_note == ?", (number, ))
                    print(f"{note[2]} видалено!")
    
    def ChangeNote(self):
        notes = self.__read_bd()
        try:
            number = int(input("\nВведіть номер нотатки яку хочеш редагувати: "))
        except ValueError:
            print("Номер має бути цифрою")
            self.ChangeNote()
            return 

        for note in notes:
            if note[0] == number:
                with sq.connect(self.__db_path) as con:
                    cur = con.cursor()

                    result = self.__ask_info_note()

                    cur.execute("UPDATE notes SET name = ?, description = ?, priority = ? WHERE id_note == ?", (result[0], result[1], result[2], number, ))
                    print(f"{note[2]} видалено!")


        


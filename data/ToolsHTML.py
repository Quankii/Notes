from ToolsDB import ToolsDB
from jinja2 import Environment, FileSystemLoader

class ToolsHTML:

    def __init__(self):
        self.tdb = ToolsDB()

    def LoadHtmlPage(self):
        
        res = self.tdb.returnNotes('n')
        fs = FileSystemLoader("Html/HTML")
        env = Environment(loader=fs)

        tm = env.get_template('FullPage.html')
        msg = tm.render(notes = res)
        
        with open("FileSite/index.html", 'w') as file:
            file.write(msg)

            print("Сайт з списком нотаток збережено по шляху ./FileSite/index.html :)")

t = ToolsHTML()
t.LoadHtmlPage()


import cmd
import sqlite3

class KanbanApp(cmd.Cmd):
    #code for all functions and commands

    def __init__(self):
        super(KanbanApp, self).__init__()

    def do_todo(self,item_name):
        conn = sqlite3.connect('kanban_app.db')
        c = conn.cursor()
        item_name = input("input new item: ")
        c.execute("INSERT INTO task VALUES(NULL,?);", [item_name])
        c.execute("")
        conn.commit()
        conn.close()



    def do_EOF (self, line):
        return True



if __name__ == '__main__':
    KanbanApp().cmdloop()


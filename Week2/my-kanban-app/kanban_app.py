import cmd
import sqlite3

class KanbanApp(cmd.Cmd):
    #code for all functions and commands
    conn = sqlite3.connect('kanban_app.db')
    c = conn.cursor()
    def __init__(self):
        super(KanbanApp, self).__init__()

    def do_todo(self,item_name):
        item_name = input("input new item: ")
        self.c.execute("INSERT INTO task VALUES(NULL,?);", [item_name])
        self.c.execute("")
        self.conn.commit()
        self.conn.close()



    def do_EOF (self, line):
        return True



if __name__ == '__main__':
    KanbanApp().cmdloop()


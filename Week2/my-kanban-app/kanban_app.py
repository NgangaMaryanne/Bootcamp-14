import cmd
import sqlite3
from clint.textui import colored, columns, puts
from datetime import datetime


class KanbanApp(cmd.Cmd):
    # code for all functions and commands

    def __init__(self):
        super(KanbanApp, self).__init__()

    def do_todo(self, item_name):
        conn = sqlite3.connect('kanban_app.db')
        c = conn.cursor()
        item_name = input("input new item: ")
        starttime = datetime.now()
        c.execute("INSERT INTO task VALUES(NULL,?,?,?,? );", (item_name, "todo", starttime, 0))
        conn.commit()
        conn.close()

    def do_doing(self, task_id):
        conn = sqlite3.connect('kanban_app.db')
        c = conn.cursor()
        c.execute("UPDATE task SET stage = ?, start_time = ? WHERE task_id = ?", ("doing",datetime.now(), task_id))
        conn.commit()
        conn.close()

    def do_done(self, task_id):
        conn = sqlite3.connect('kanban_app.db')
        c = conn.cursor()
        c.execute("SELECT stage FROM task WHERE task_id = ?",task_id)
        check_id = c.fetchone()
        if check_id[0]=="todo":
            print(colored.magenta("This item is in the todo section, It has to pass through the doing section before it can be considered done."))
        elif check_id[0]=="done":
            print(colored.magenta("Task has already been done"))
        else:
            c.execute("UPDATE task SET stage = ?, end_time = ? WHERE task_id = ?", ("done",datetime.now(), task_id))
        conn.commit()
        conn.close()

    @staticmethod
    def do_list_todo(self):
        conn = sqlite3.connect('kanban_app.db')
        c = conn.cursor()
        c.execute('SELECT task_id, task_name FROM task WHERE stage=?', ['todo'])
        todo_tasks = c.fetchall()
        print('to do tasks: ')
        for item in todo_tasks:
            print(colored.red(item))
        conn.close()

    @staticmethod
    def do_list_doing(self):
        conn = sqlite3.connect('kanban_app.db')
        c = conn.cursor()
        c.execute('SELECT task_id, task_name FROM task WHERE stage=?', ['doing'])
        doing_tasks = c.fetchall()
        print('tasks in progress : ')
        for item in doing_tasks:
            print(colored.yellow(item))
        conn.close()

    @staticmethod
    def do_list_done(self):
        conn = sqlite3.connect('kanban_app.db')
        c = conn.cursor()
        c.execute('SELECT task_id, task_name FROM task WHERE stage=?', ['done'])
        done_tasks = c.fetchall()
        print('Done tasks : ')
        for item in done_tasks:
            print(colored.cyan(item))
        conn.close()

    @staticmethod
    def do_list_all(self):
        conn = sqlite3.connect('kanban_app.db')
        c = conn.cursor()
        c.execute('SELECT task_id,task_name FROM task WHERE stage=?', ['todo'])
        todo_tasks = c.fetchall()
        c.execute('SELECT  task_id,task_name FROM task WHERE stage=?', ['doing'])
        doing_tasks = c.fetchall()
        c.execute('SELECT  task_id,task_name FROM task WHERE stage=?', ['done'])
        done_tasks = c.fetchall()

        print(colored.red(todo_tasks), colored.yellow(doing_tasks), colored.cyan(done_tasks))

    def do_del(self, task_id):
        conn = sqlite3.connect('kanban_app.db')
        c = conn.cursor()
        c.execute("DELETE FROM task WHERE task_id=?",[task_id])
        conn.commit()
        conn.close()


    def do_edit(self, task_id):
        conn = sqlite3.connect('kanban_app.db')
        c = conn.cursor()
        new_task = input("Please input the new task name: ")
        c.execute("UPDATE task SET task_name = ? WHERE task_id = ?", (new_task, task_id))
        conn.commit()
        conn.close()

    def do_EOF(self, line):
        return True


if __name__ == '__main__':
    KanbanApp().cmdloop()


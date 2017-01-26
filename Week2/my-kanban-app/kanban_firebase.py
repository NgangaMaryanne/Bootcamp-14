import cmd
import sqlite3
import clint
from clint.textui import colored, columns, puts
from datetime import datetime
from pyfirebase import Firebase
from prettytable import PrettyTable
import pprint
from requests.exceptions import ConnectionError


class KanbanApp(cmd.Cmd, object):
    # code for all functions and commands
    firebase = Firebase('https://my-kanban-app.firebaseio.com')
    tasks_ref = firebase.ref()
    def __init__(self):
        super(KanbanApp, self).__init__()
        def banner_message(text, ch='=', length = 150):
            spaced_text = '%s'%text
            banner_message =spaced_text.center(length, ch)
            return banner_message 
        print colored.green(banner_message('WELCOME TO KANBAN APPLICATION'))

    def do_todo(self, item_name):
        conn = sqlite3.connect('kanban_app.db')
        conn.text_factory = str
        c = conn.cursor()
        item_name = str(raw_input("input new item: "))
        payload = {'task_id':'NULL', 'task_name':item_name, 'stage':'todo', 'start-time':str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")), 'end-time':0}
        task = (self.tasks_ref).push(payload)
        c.execute("INSERT INTO task VALUES(NULL,?,?,?,? );", (item_name, "todo", str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")), 0))
        conn.commit()
        conn.close()
        print colored.green ("Task added successfully")

    def do_doing(self, task_id):
        conn = sqlite3.connect('kanban_app.db')
        conn.text_factory = str
        c = conn.cursor()
        c.execute("UPDATE task SET stage = ?, start_time = ? WHERE task_id = ?", ("doing", datetime.now().strftime("%Y-%m-%d %H:%M:%S"), task_id))
        conn.commit()
        print colored.green("Task moved to doing section")
        conn.close()


    def do_done(self, task_id):
        conn = sqlite3.connect('kanban_app.db')
        conn.text_factory = str
        c = conn.cursor()
        c.execute("SELECT stage FROM task WHERE task_id = ?",task_id)
        check_id = c.fetchone()
        if check_id[0]=="todo":
            print colored.magenta("This item is in the todo section, It has to pass through the doing section before it can be considered done.")
        elif check_id[0]=="done":
            print(colored.magenta("Task has already been done"))
        else:
            c.execute("UPDATE task SET stage = ?, end_time = ? WHERE task_id = ?", ("done",str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")), task_id))
        conn.commit()
        conn.close()
        print colored.green('Task completed')

    @staticmethod
    def do_list_todo(self):
        conn = sqlite3.connect('kanban_app.db')
        conn.text_factory = str
        c = conn.cursor()

        

        c.execute('SELECT task_id, task_name FROM task WHERE stage=?', ['todo'])
        todo_tasks = c.fetchall()

        print 'to do tasks from sqlite are: '
        for item in todo_tasks:
            print(colored.red (item))

        # code to get to do items from firebase.
        conn.close()

        '''
        try:
            firebase = Firebase('https://my-kanban-app.firebaseio.com')
            tasks_ref = firebase.ref()
            new_todo_task = tasks_ref.get()
            fireb_todo_tasks = []
            for k, v in new_todo_task.iteritems():
                innerdict = v
                for k, v in innerdict.iteritems():
                    if v =='todo':
                        task_name = innerdict.get('task_name')
                        fireb_todo_tasks.append(task_name)
                    else:
                        pass
            print colored.magenta('the to do items from firebase are:')
            for i in fireb_todo_tasks:
                print i
        except ConnectionError as e:
            print colored.red( 'Cannot print items from firebase because there is no internet connection')
        '''
       

    @staticmethod
    def do_list_doing(self):
        conn = sqlite3.connect('kanban_app.db')
        conn.text_factory = str
        c = conn.cursor()
        c.execute('SELECT task_id, task_name FROM task WHERE stage=?', ['doing'])
        doing_tasks = c.fetchall()
        print 'tasks in progress : '
        for item in doing_tasks:
            print colored.yellow(str(item))
        conn.close()

    @staticmethod
    def do_list_done(self):
        conn = sqlite3.connect('kanban_app.db')
        conn.text_factory = str
        c = conn.cursor()
        c.execute('SELECT task_id, task_name FROM task WHERE stage=?', ['done'])
        done_tasks = c.fetchall()
        print 'Done tasks : '
        for item in done_tasks:
            print colored.cyan(item)
        conn.close()

    @staticmethod
    def do_list_all(self):
        conn = sqlite3.connect('kanban_app.db')
        conn.text_factory = str
        c = conn.cursor()
        c.execute('SELECT task_id,task_name FROM task WHERE stage=?', ['todo'])
        todo_tasks_results = c.fetchall()
        c.execute('SELECT task_id,task_name, start_time FROM task WHERE stage=?', ['doing'])
        doing_tasks_results = c.fetchall()
        c.execute('SELECT  task_id,task_name, start_time, end_time FROM task WHERE stage=?', ['done'])
        done_tasks_results = c.fetchall()

        todo_tasks = []
        doing_tasks = []
        done_tasks = []

        #todo tasks, transform tuples to lists
        for item in todo_tasks_results:
            item = list(item)
            todo_tasks.append(item)

        #doing tasks

        for item in doing_tasks_results:
            item = list(item)
            doing_tasks.append(item) 

        #done tasks
        for item in done_tasks_results:
            item = list(item)
            done_tasks.append(item)
        #format data for table.
        all_tasks = []

        #check whether all lists are equal
        if len(todo_tasks)==len(doing_tasks)==len(done_tasks):
            for index, value in enumerate(todo_tasks):
                all_tasks.append([value,doing_tasks[index], done_tasks[index]])

        elif (len(todo_tasks)==len(doing_tasks)!=len(done_tasks)) or(len(todo_tasks)==len(done_tasks)!=len(doing_tasks)) or (len(doing_tasks)==len(done_tasks)!=len(todo_tasks)) :
            if len(todo_tasks)==len(doing_tasks)!=len(done_tasks):
                if len(todo_tasks)<len(done_tasks):
                    for index, value in enumerate(done_tasks):
                        if index< len (todo_tasks):
                            all_tasks.append([todo_tasks[index], doing_tasks[index],value])
                        else:
                            all_tasks.append(['','',value])
                else:
                    for index, value in enumerate(todo_tasks):
                        if index<len(done_tasks):
                            all_tasks.append([value, doing_tasks[index],done_tasks[index]])
                        else:
                            all_tasks.append([value, doing_tasks[index], ''])

            elif len(todo_tasks)==len(done_tasks)!=len(doing_tasks):
                if len(todo_tasks)<len(doing_tasks):
                    for index, value in enumerate(doing_tasks):
                        if index<len(done_tasks):
                            all_tasks.append([todo_tasks[index],value,done_tasks[index]])
                        else:
                            all_tasks.append(['', value, ''])
                else:
                    for index, value in enumerate(todo_tasks):
                        if index<len(doing_tasks):
                            all_tasks.append([value, doing_tasks[index],done_tasks[index] ])
                        else:
                            all_tasks.append([value, '', done_tasks[index]])

            elif len(doing_tasks)==len(done_tasks)!=len(todo_tasks):
                if len(doing_tasks)< len(todo_tasks):
                    for index, value in enumerate(todo_tasks):
                        if index<len(doing_tasks):
                            all_tasks.append([value,doing_tasks[index],done_tasks[index]])
                        else:
                            all_tasks.append([value, '', ''])
                else:
                    for index, value in enumerate(doing_tasks):
                        if index<len(todo_tasks):
                            all_tasks.append([todo_tasks[index], value, done_tasks[index]])
                        else:
                            all_tasks.append(['',value, done_tasks[index]])

        else:
            listlengths = [len(todo_tasks), len(doing_tasks),len(done_tasks)]

            #Get the length of longer list with o for todo_tasks, 1 for doing_tasks and 2 for done_tasks
            longer_list_length= max(listlengths)
            #Get position of longer list
            longer_list_pos = listlengths.index(longer_list_length)
            print longer_list_pos

            if longer_list_pos == 0:
                for index, value in enumerate(todo_tasks):
                    if index<len(doing_tasks) and index<len(done_tasks):
                        all_tasks.append([value, doing_tasks[index], done_tasks[index]])
                    elif index<len(doing_tasks) and index>=len(done_tasks):
                        all_tasks.append([value,doing_tasks[index], ''])
                    elif index >=len(doing_tasks) and index<len(done_tasks):
                        all_tasks.append([value, '', done_tasks[index]])
                    elif index >=len(doing_tasks)and index>=len(done_tasks):
                        all_tasks.append([value, '',''])
                    else:
                        print 'please recheck todo tasks'


            elif longer_list_pos ==1:
                for index, value in enumerate(doing_tasks):
                    if index<len(todo_tasks) and index<len(done_tasks):
                        all_tasks.append([todo_tasks[index], value, done_tasks[index]])
                    elif index<len(todo_tasks) and index >= len(done_tasks):
                        all_tasks.append([todo_tasks[index], value, ''])
                    elif index >= len(todo_tasks) and index< len(done_tasks):
                        all_tasks.append(['', value, done_tasks[index]])
                    elif index>= len(todo_tasks) and index>= len(done_tasks):
                        all_tasks.append(['', value, ''])
                    else:
                        print 'please recheck doing tasks'

            else:
                for index, value in enumerate (done_tasks):
                    if index<len(todo_tasks) and index<len(doing_tasks):
                        all_tasks.append([todo_tasks[index], doing_tasks[index], value])
                    elif index<len(todo_tasks) and index>=len(doing_tasks):
                        all_tasks.append([todo_tasks[index], '', value])
                    elif index>=len(todo_tasks) and index<len(doing_tasks):
                        all_tasks.append(['', doing_tasks[index], value])
                    elif index>=len(todo_tasks) and index>=len(doing_tasks):
                        all_tasks.append (['','', value])
                    else:
                        print 'please recheck done tasks'

        print colored.green("Doing section has start time of the task, date and time. Done section has task start time and task end time respectively.")
        #CREATE DISPLAY TABLE
        t = PrettyTable()
        t.field_names = ["TO DO", "DOING", "DONE"]
        for i in all_tasks:
            t.add_row(i)
        print t
                
        #firebase get all item:
        try:
            firebase = Firebase('https://my-kanban-app.firebaseio.com')
            tasks_ref = firebase.ref()
            all_fireb_tasks = tasks_ref.get()

            print
            print  
            print ('all items in firebase are: ')
            for k, v in all_fireb_tasks.iteritems():
                firebase_tasks=v
                for k, v in firebase_tasks.iteritems():
                    if k == 'task_name':
                        print colored.magenta(v)
               
        except ConnectionError as e:
            print "cannot print firebase all items, no internet connection"


    def do_del(self, task_id):
        conn = sqlite3.connect('kanban_app.db')
        conn.text_factory = str
        c = conn.cursor()
        c.execute("DELETE FROM task WHERE task_id=?",[task_id])
        conn.commit()
        conn.close()


    def do_edit(self, task_id):
        conn = sqlite3.connect('kanban_app.db')
        conn.text_factory = str
        c = conn.cursor()
        new_task = raw_input("Please input the new task name: ")
        c.execute("UPDATE task SET task_name = ? WHERE task_id = ?", (new_task, task_id))
        conn.commit()
        conn.close()

    def do_EOF(self, line):
        return True


if __name__ == '__main__':
    KanbanApp().cmdloop()


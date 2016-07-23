#Benjamin Garness
#CS 0008
#hw 5

import tkinter

import murder

import pickle

class Application:

    def __init__(self):
        self.__window = tkinter.Tk()
        self.__window.title('Murder Database')
        self.__murders = []
        self.__selected_index = -1
        self.__selected_murder = None
        self.__weapon = tkinter.StringVar()
        self.__location = tkinter.StringVar()
        self.__suspect = tkinter.StringVar()
        self.__victim = tkinter.StringVar()
        self.build_input_frame('Victim: ', self.__victim)
        self.build_input_frame('Suspect: ', self.__suspect)
        self.build_input_frame('Weapon: ', self.__weapon)
        self.build_input_frame('Location: ', self.__location)
        
        frame = tkinter.Frame(self.__window)
        self.__add_button = tkinter.Button(frame, text='Add Murder',
            anchor=tkinter.W, command=self.add_murder)
        self.__add_button.pack(side='top')
        self.__save_button = tkinter.Button(frame, text='Save Murder',
            anchor=tkinter.W, command=self.save, state=tkinter.DISABLED)
        self.__save_button.pack(side='left')
        self.__delete_button = tkinter.Button(frame, text='Delete Murder',
            anchor=tkinter.W, command=self.delete, state=tkinter.DISABLED)
        self.__delete_button.pack(side='right')
        frame.pack()


        frame = tkinter.Frame(self.__window)
        label = tkinter.Label(frame, text='Murders')
        self.__murder_list = tkinter.Listbox(frame, width=60,
            selectmode=tkinter.SINGLE)
        self.__murder_list.bind('<<ListboxSelect>>', self.select_murder)
        label.pack()
        self.__murder_list.pack()
        frame.pack()

        '''frame = tkinter.Frame(self.__window)
        self.__save_file = tkinter.Button(frame, text='Save file',
            anchor=tkinter.W, command=self.save_file)
        self.__file_name = tkinter.StringVar()
        self.build_input_frame('File name?', self.__file_name)
        self.__save_file.pack(side='left')
        self.__open_file = tkinter.Button(frame, text='Open file',
            anchor=tkinter.W, command=self.open_file)
        self.__open_file.pack(side='right')
        frame.pack()'''

    def open_file(self):
        self.__murders = pickle.load( open(self.__save_file_name, 'rb'))

    def build_input_frame(self, label, textvariable):
        frame = tkinter.Frame(self.__window)
        label = tkinter.Label(frame, text=label, width=10, anchor=tkinter.W)
        entry = tkinter.Entry(frame, textvariable=textvariable, width=20)
        label.pack(side='left')
        entry.pack(side='right')
        frame.pack()

    def save_file(self):
        pickle.dump(self.__murders, open(self.__file_name, 'wb'))
            
    def start(self):
        tkinter.mainloop()
        
    def add_murder(self):
        c = murder.Murder(self.__suspect.get(), self.__victim.get(),
                            self.__weapon.get(), self.__location.get())
        self.__murders.append(c)
        self.__murder_list.insert(tkinter.END, str(c))

    def save(self):
        self.__selected_murder.set_suspect(self.__suspect.get())
        self.__selected_murder.set_victim(self.__victim.get())
        self.__selected_murder.set_weapon(self.__weapon.get())
        self.__selected_murder.set_location(self.__location.get())

        self.__murder_list.delete(self.__selected_index)
        self.__murder_list.insert(self.__selected_index,
            str(self.__selected_murder))
        self.after_selected_operation()

    def after_selected_operation(self):
        self.__selected_index = -1
        self.__selected_murder = None

        self.__suspect.set('')
        self.__victim.set('')
        self.__weapon.set('')
        self.__location.set('')
        self.__save_button.config(state=tkinter.DISABLED)
        self.__delete_button.config(state=tkinter.DISABLED)

    def delete(self):
        if 0 <= self.__selected_index < len(self.__murders):
            del self.__murders[self.__selected_index]
            self.__murder_list.delete(self.__selected_index)
            self.after_selected_operation()

    def select_murder(self, event):
        current_selection = self.__murder_list.curselection()
        if current_selection:
            self.__selected_index = current_selection[0]
            self.__selected_murder = self.__murders[self.__selected_index]
            self.__suspect.set(self.__selected_murder.get_suspect())
            self.__victim.set(self.__selected_murder.get_victim())
            self.__weapon.set(self.__selected_murder.get_weapon())
            self.__location.set(self.__selected_murder.get_location())
            self.__save_button.config(state=tkinter.NORMAL)
            self.__delete_button.config(state=tkinter.NORMAL)
        
def main():
    app = Application()
    app.start()

main()

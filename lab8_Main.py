import tkinter

import contact

class Application:

    def __init__(self):
        self.__contacts = []
        self.__selected_index = -1
        self.__selected_contact = None
        self.__window = tkinter.Tk()
        self.__window.title('Contact Manager')
        self.__first_name = tkinter.StringVar()
        self.__last_name = tkinter.StringVar()
        self.__email = tkinter.StringVar()
        self.__phone = tkinter.StringVar()
        self.build_input_frame('First Name: ', self.__first_name)
        self.build_input_frame('Last Name: ', self.__last_name)
        self.build_input_frame('Email: ', self.__email)
        self.build_input_frame('Phone: ', self.__phone)

        frame = tkinter.Frame(self.__window)
        self.__add_button = tkinter.Button(frame, text='Add Contact',
            anchor=tkinter.W, command=self.add_contact)
        self.__add_button.pack(side='left')
        frame.pack()

        frame = tkinter.Frame(self.__window)
        label = tkinter.Label(frame, text='Your Contacts')
        self.__contacts_list = tkinter.Listbox(frame, width=120,
            selectmode=tkinter.SINGLE)
        label.pack()
        self.__contacts_list.pack()
        frame.pack()

    def start(self):
        tkinter.mainloop()

    def build_input_frame(self, label, textvariable):
        frame = tkinter.Frame(self.__window)
        label = tkinter.Label(frame, text=label, width=15, anchor=tkinter.W)
        entry = tkinter.Entry(frame, textvariable=textvariable, width=30)
        label.pack(side='left')
        entry.pack(side='right')
        frame.pack()

    def add_contact(self):
        c = contact.Contact(self.__first_name.get(), self.__last_name.get(),
                            self.__email.get(), self.__phone.get())
        self.__contacts.append(c)
        self.__contacts_list.insert(tkinter.END, str(c))


def main():
    app = Application()
    app.start()

main()

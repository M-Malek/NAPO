import tkinter.filedialog
from tkinter import *
from tkinter import messagebox
from core.file_manager import *
from core.password_manager import *
import webbrowser


class MainWindow:

    def __init__(self):
        self.user_password_input = ""
        self.window = Tk()
        self.window.title("NAPO v.1")
        self.window.config(width=200, height=400, padx=20, pady=20)
        self.window.resizable(False, False)
        self.start_picture = PhotoImage(file="core/new_logo.png")
        self.data_to_show = {}
        self.data = None

        self.init_screen()

        self.window.mainloop()

    def init_screen(self):
        canvas = Canvas(self.window, width=200, height=200)
        canvas.create_image(100, 100, image=self.start_picture)
        canvas.grid(row=0, column=0)
        canvas.update()

        button_new = Button(self.window, text="New", command=self.create_new_password_file, width=30)
        button_new.grid(row=1, column=0)

        button_open = Button(self.window, text="Open", command=self.open_password_file, width=30)
        button_open.grid(row=2, column=0)

        button_settings = Button(self.window, text="Author", command=self.author_screen, width=30)
        button_settings.grid(row=3, column=0)

        button_author = Button(self.window, text="Quit", command=self.window.destroy, width=30)
        button_author.grid(row=4, column=0)

    @staticmethod
    def create_new_password_file():
        data = File()
        data.save_file()

    def open_password_file(self):
        self.data = File()
        file_path = self.file_location_messagebox()
        self.data.load_file(file_path)

        self.clear_window()
        self.save_new_password_frame()
        self.load_all_passwords_frame()
        self.settings_frame()

    def save_new_password_frame(self):
        def random_password():
            new_password = generate_password()
            entry_password.delete(0, END)
            entry_password.insert(0, new_password)

        def add_password():
            website = entry_website.get()
            login = entry_user.get()
            password = entry_password.get()
            self.data.all_passwords[website] = {"login": login, "password": password}
            self.load_all_passwords_frame()

        new_password_frame = LabelFrame(self.window, text="Add a new password")
        new_password_frame.grid(row=0, column=0)

        label_website = Label(new_password_frame, text="Website:")
        label_website.grid(row=1, column=0)

        label_user = Label(new_password_frame, text="Email/Username:")
        label_user.grid(row=2, column=0)

        label_password = Label(new_password_frame, text="Password:")
        label_password.grid(row=3, column=0)

        entry_website = Entry(new_password_frame, width=35)
        entry_website.grid(row=1, column=1, sticky="ew", columnspan=2)

        entry_user = Entry(new_password_frame, width=35)
        entry_user.grid(row=2, column=1, columnspan=2, sticky="ew")

        entry_password = Entry(new_password_frame, width=20)
        entry_password.grid(row=3, column=1, sticky="ew")

        button_password = Button(new_password_frame, command=random_password, text="Generate password")
        button_password.grid(row=3, column=2, sticky="ew")

        button_add = Button(new_password_frame,command=add_password, text="Add", width=36)
        button_add.grid(row=4, column=1, columnspan=2, sticky="ew")

    def load_all_passwords_frame(self):
        def show_website_info():
            website_entry.delete(0, END)
            user_entry.delete(0, END)
            password_entry.delete(0, END)
            selected_web = listbox_websites.get(listbox_websites.curselection())
            website_entry.insert(0, selected_web)
            user_entry.insert(0, self.data.all_passwords[selected_web]["login"])
            password_entry.insert(0, self.data.all_passwords[selected_web]["password"])

        frame_all_passwords = LabelFrame(self.window, text="All saved passwords")
        frame_all_passwords.grid(row=0, column=3, sticky="n", rowspan=2)

        listbox_websites = Listbox(frame_all_passwords, height=10, width=30)
        all_websites = list(self.data.all_passwords.keys())
        for item in all_websites:
            listbox_websites.insert(all_websites.index(item), item)
        listbox_websites.bind("<<ListboxSelect>>", lambda e: show_website_info())
        listbox_websites.grid(row=1, column=3)

        frame_password_data = LabelFrame(self.window, text="Password data")
        frame_password_data.grid(row=0, column=4, sticky="n", rowspan=4)

        website_label = Label(frame_password_data, text="Website")
        website_label.grid(row=1, column=4)
        website_entry = Entry(frame_password_data, width=22)
        website_entry.grid(row=1, column=5)

        user_label = Label(frame_password_data, text="Login/Email")
        user_label.grid(row=2, column=4)
        user_entry = Entry(frame_password_data, width=22)
        user_entry.grid(row=2, column=5)

        password_label = Label(frame_password_data, text="Password")
        password_label.grid(row=3, column=4)
        password_entry = Entry(frame_password_data, show="*", width=22)
        password_entry.grid(row=3, column=5)

        button_copy = Button(frame_password_data, text="Copy password to clipboard", width=22)
        button_copy.grid(row=4, column=5)

        button_delete = Button(frame_password_data, text="Delete website from list", width=22)
        button_delete.grid(row=5, column=5)

    def settings_frame(self):
        frame_settings = LabelFrame(self.window, text="Settings")
        frame_settings.grid(row=1, column=0, columnspan=3, sticky="snew")

        button_back = Button(frame_settings, text="Back", command=self.app_restart, width=20)
        button_back.grid(row=1, column=0, columnspan=3, sticky="ew")

    @staticmethod
    def ask_user_file_password():
        def test():
            print(password_window_entry.get())
            password_window.destroy()

        password_window = Tk()
        password_window.config(width=50, height=40)
        password_window.title("Password required")
        password_window_label = Label(text="Please, enter password to your password's data file:")
        password_window_label.grid(row=0, column=0)

        password_window_entry = Entry(width=40, show="*")
        password_window_entry.grid(row=0, column=1)

        password_window_button = Button(text="Submit password", command=test, width=70)
        password_window_button.grid(row=1, column=0, columnspan=2)

        password_window.mainloop()

    def clear_window(self):
        for widget in self.window.winfo_children():
            widget.destroy()

    def app_restart(self):
        self.data_to_show.clear()
        self.clear_window()
        self.init_screen()

    def author_screen(self):
        def course_callback():
            webbrowser.open_new \
                ("https://www.udemy.com/share/103IHM3@VBQYo05_-WD9j0wSKiukqeS490POl0L7ZnHd_Ya6gOSvyxuoNjVmaZIcEGQjMtmc/")

        self.clear_window()
        canvas = Canvas(self.window, width=200, height=200)
        canvas.create_image(100, 100, image=self.start_picture)
        canvas.grid(row=0, column=0)
        canvas.update()

        author_label = Label(self.window, text="Created by Michal Malek\n Based on Password Manager created during "
                                               "100 days of Code Challenge:")
        author_label.grid(row=1, column=0)
        course_web_label = Label(self.window, text=r"https://www.udemy.com/share/103IHM3@VBQYo05_-WD9j0wSKiukqeS490POl0L7ZnHd_Ya6gOSvyxuoNjVmaZIcEGQjMtmc/")
        course_web_label.grid(row=2, column=0, sticky="ew")
        course_web_label.bind("<Button-1>", lambda e: course_callback())

        button_back = Button(self.window, text="Back", command=self.app_restart)
        button_back.grid(row=3, column=0, sticky="ew")

    @staticmethod
    def file_location_messagebox():
        file = tkinter.filedialog.askopenfilename(title="Choose your data file")
        return file


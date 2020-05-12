import csv
import random
import pyperclip
import tkinter as tk
import tkinter.scrolledtext as st
from tkinter import messagebox
from tkinter.filedialog import askopenfilename, asksaveasfile

INSTRUCTIONS = """1. Enter a message into the message center and click 'Encode'

2. To decode a message into coded message into message center and click 'Decode'

3. Upload a message from .txt file by clicking 'Upload'

4. Save message to .txt file by clicking 'Save'

5. To view key, click 'Key Menu' and then 'View Key'

6. To create new key, click 'Key Menu' and then 'Create Key'"""


class MessageKey:
    _alphaNumSym = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                   'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
                   'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8',
                   '9', '0', '~', '`', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '=', '_', '+', '[', ']',
                   "\\", ';', "'", ',', '.', '/', '{', '}', '|', ':', '"', '<', '>', '?', "’", ' ']

    master_key = {}

    def __init__(self):

        if MessageKey.master_key:
            pass
        else:
            try:
                key = open('key.csv', 'r')
                reader = csv.reader(key)

                for row in reader:
                    MessageKey.master_key[row[0]] = row[1]

                key.close()
            except FileNotFoundError:
                messagebox.showwarning('File Error', 'Unable to locate key file')

    def create_key(self):
        random.shuffle(MessageKey._alphaNumSym)
        val = 1

        for char in MessageKey._alphaNumSym:
            MessageKey.master_key[str(val)] = char
            val += 1

        self.save_key()

    def save_key(self):
        self.key = csv.writer(open('key.csv', 'w', newline=''))
        for k, v in MessageKey.master_key.items():
            self.key.writerow([k, v])

    def view_key(self):
        self.key = []
        for k, v in MessageKey.master_key.items():
            self.key.append(k + ': ' + str(v))
        return self.key


class Messages(MessageKey):

    def __init__(self):
        super().__init__()
        self.text = []

    def encoder(self, message):
        k_list = list(self.master_key.keys())
        v_list = list(self.master_key.values())
        split_msg = (list(message))

        self.text.clear()

        for letter in split_msg:
            if letter not in v_list:
                tk.messagebox.showerror("Value Not Found", f"'{letter}' is not in key")
            else:
                num_letter = (k_list[v_list.index(letter)])
                self.text.append(num_letter)

        return self.text

    def decoder(self, message):
        self.text.clear()

        msg = message.split(' ')
        for num in msg:
            if num not in self.master_key:
                tk.messagebox.showerror("Key Not Found", f"'{num}' is not in key")
            else:
                self.text.append(self.master_key.get(num))

        decode_str = ''.join(self.text)
        return decode_str


class App:
    # create instance of other classes
    msg_key = MessageKey()
    msg = Messages()

    # GUI window
    def __init__(self, main):
        self.main = main
        self.main.title("Message Encoder App")
        self.main.minsize(550, 500)

        # Top frame of GUI window
        self.msg_frame = tk.LabelFrame(
            main, text="Message Center", labelanchor=tk.N, width=400, height=200, bg='white', bd=5
        )
        self.msg_text = tk.Text(self.msg_frame, height=15, width=60, wrap='word')
        self.msg_text.pack(fill=tk.BOTH)

        # Middle frame of GUI window
        self.info_frame = tk.LabelFrame(
            main, text="Information Center", labelanchor=tk.N, width=475, height=100, bg='white smoke'
        )
        self.info_txt = st.ScrolledText(self.info_frame, height=10, width=60, state='normal', wrap='word', bg='grey88')
        self.info_txt.insert('end', INSTRUCTIONS)
        self.info_txt.pack()
        self.info_txt.config(state='disabled')

        # Bottom frame of GUI window
        self.options_frame = tk.Frame(
            main, width=500, height=50, bg='grey25'
        )

        lft_btns = self.lft_btns()
        rt_btns = self.rt_btns()

        # Left buttons on bottom frame
        for name, comm in lft_btns.items():
            frame = tk.Frame(self.options_frame, relief=tk.GROOVE, borderwidth=5, bg='grey25')
            frame.pack(side=tk.LEFT)
            btn = tk.Button(master=frame, text=name, command=comm)
            btn.pack()

        # Right buttons on bottom frame
        for name, comm in rt_btns.items():
            frame = tk.Frame(self.options_frame, relief=tk.GROOVE, borderwidth=5, bg='grey25')
            frame.pack(side=tk.RIGHT)
            btn = tk.Button(master=frame, text=name, command=comm)
            btn.pack()

        # File options on menu bar
        file_opt = self.file_opts()

        self.menu_bar = tk.Menu(self.main)
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)

        for opt, comm in file_opt.items():
            self.file_menu.add_command(label=opt, command=comm)

        self.menu_bar.add_cascade(label='File', menu=self.file_menu)

        # Key options on menu bar
        key_opt = self.key_opts()

        self.key_menu = tk.Menu(self.menu_bar, tearoff=0)

        for opt, comm in key_opt.items():
            self.key_menu.add_command(label=opt, command=comm)
        self.menu_bar.add_cascade(label='Key Menu', menu=self.key_menu)

        # Packing all frames and menu bar onto GUI window
        self.msg_frame.pack(fill=tk.BOTH, expand=True)
        self.info_frame.pack()
        self.options_frame.pack(fill=tk.BOTH, expand=True)
        self.main.config(menu=self.menu_bar)

    # left and right buttons and commands
    def lft_btns(self):
        opt = {
            "Encode": self.encode_btn,
            "Decode": self.decode_btn,
            "Copy": self.copy_btn,
            "Clear": self.clear_btn,
        }
        return opt

    def rt_btns(self):
        opt = {
            "Exit": self.exit,
            "Save": self.save_msg,
            "Load": self.load_msg
        }
        return opt

    # functions of buttons
    def encode_btn(self):
        message = self.msg_text.get('1.0', tk.END)
        message = message.replace('\n', '')
        self.info_update(self.msg.encoder(message))

    def decode_btn(self):
        message = self.msg_text.get('1.0', tk.END)
        message = message.replace('\n', '')
        self.info_update(self.msg.decoder(message))

    def copy_btn(self):
        message = self.info_txt.get('1.0', tk.END)
        pyperclip.copy(message)

    def clear_btn(self):
        self.msg_text.delete('1.0', tk.END)
        self.info_update(INSTRUCTIONS)

    # Menu items and commands for File
    def file_opts(self):
        opts = {
            "Open": self.load_msg,
            "Save": self.save_msg,
            "Exit": self.exit
        }
        return opts

    def load_msg(self):
        file = askopenfilename(filetypes=[("Text Files", "*.txt")])

        if not file:
            return

        self.msg_text.delete('1.0', tk.END)

        with open(file, 'r') as input_file:
            text = input_file.read()
            text = text.splitlines()

            if text[0].isdecimal():
                self.msg_text.insert(tk.END, text)
            else:
                t = text[0]
                self.msg_text.insert(tk.END, t)

    def save_msg(self):
        file = asksaveasfile(mode='w', defaultextension='.txt')
        if file:
            file.write(self.info_txt.get('1.0', tk.END))
            file.close()

    def exit(self):
        self.main.destroy()

    # Menu items and commands for Keys Menu
    def key_opts(self):
        opts = {
            "Create New Key": self.create_key,
            "View Key": self.view_key
        }
        return opts

    def view_key(self):
        self.info_txt.config(state='normal')
        self.info_txt.delete('1.0', tk.END)

        for item in self.msg_key.view_key():
            self.info_txt.insert('end', (item + '\n'))

        self.info_txt.config(state='disabled')

    def create_key(self):
        self.msg_key.create_key()
        messagebox.showinfo("Information", "Key has been created.")

    # Changes display of text inside info_txt widget
    def info_update(self, text):
        self.info_txt.config(state='normal')
        self.info_txt.delete('1.0', tk.END)
        self.info_txt.insert('end', text)
        self.info_txt.config(state='disabled')


window = tk.Tk()
window.resizable(width=False, height=False)
my_app = App(window)
window.mainloop()

# TODO display errors in Information Center or messagebox
# TODO create option to load a key

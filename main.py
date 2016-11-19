version = 1.0
build = 24
connected = False
print("PythonSSH Version: " + str(version) + " Build: " + str(build))
import paramiko
import tkinter as tk
import cmd
host = input("Hostname or IP: ")
client = paramiko.SSHClient()
client.set_missing_host_key_policy(
    paramiko.AutoAddPolicy())
def make_entry(parent, caption, width=None, **options):
    tk.Label(parent, text=caption).pack(side=tk.TOP)
    entry = tk.Entry(parent, **options)
    if width:
        entry.config(width=width)
    entry.pack(side=tk.TOP, padx=10, fill=tk.BOTH)
    return entry
def login():
    usrname = user.get()
    passwd = password.get()
    print("Attempting connection...")
    root.quit()
    root.destroy()
    client.connect(host, port=22, username=usrname, password=passwd)
    connected = True
    print("Sign in success, use 'exit' to close connection...")
    while connected:
        cmd = input("command> ")
        if cmd == "exit":
            client.close()
        stdin, stdout, stderr = client.exec_command(cmd)
        stdin.close()
        for line in stdout.read().splitlines():
            print(line)
    else:
        client.close()
root = tk.Tk()
root.geometry('300x160')
root.title('PythonSSH | Sign in')
#frame for window margin
parent = tk.Frame(root, padx=10, pady=10)
parent.pack(fill=tk.BOTH, expand=True)
#entrys with not shown text
user = make_entry(parent, "Username:", 16)
password = make_entry(parent, "Password:", 16, show="*")
#button to attempt to login
b = tk.Button(parent, borderwidth=4, text="Login", width=10, pady=8, command=login)
b.pack(side=tk.BOTTOM)

user.focus_set()
parent.mainloop()
print("Exit.")

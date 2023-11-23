import tkinter as tk
import socket
import threading
import json
from datetime import datetime

root  = tk.Tk()
label_name = tk.Label(root)
username = 'default'


# ------------ Send message from Client -----------
def send_message():
    print("sending message")
    message = {
        "text": entry.get(),
        "user": username
    }
    entry.delete(0,"end")
    json_data = json.dumps(message)
    client.send(json_data.encode('utf-8'))
    listbox_outgoing.insert("end", message["text"])
    write_in_file(message)



# -------------- save userName ----------------

def save_name():
    name = name_entry.get()
    global username
    username = name
    name_entry.destroy()
    save_username.destroy()
    label_name = tk.Label(frame1, text="Username: {}".format(name))
    label_name.pack(pady=10)

#--------------- Recive Message --------------
def receive_messages():
    while True:
        # Receive and display messages from the server
        message = client.recv(1024).decode('utf-8')
        json_data = json.loads(message)
        listbox_incoming.insert("end", json_data["text"]+' from: ' + json_data["user"] )
        write_in_file(json_data, json_data['user'])


def write_in_file(message, from_user='me'):
    with open("client.txt", "a") as file:
        file.write(f"message: {message['text']}; from:{from_user}; time: {datetime.now().time()}\n")




message_placeholder = "Enter text here"
name_placeholder = "Enter your name"
placeholder_color = "grey"

# Handlers for placeholder in entry field
def on_entry_click(event):
    if event.widget.get() != "":
        event.widget.delete(0, "end")  
        event.widget.config(fg='black')  # Set text color to black

def on_focus_out(event):
    if event.widget.get() == "":
        if(event.widget == entry):
            entry.insert(0, message_placeholder)  
        if(event.widget == name_entry):
            name_entry.insert(0, name_placeholder)  
        event.widget.config(fg='grey') 





# =============== User Interface =============
root["bg"] = 'white'
root.config(pady=30, padx=10)
frame1 = tk.Frame(root, bd = 40, bg='grey', width=600, height=200)
frame2 = tk.Frame(root, bd=20, bg='yellow', width=600, height=200)
frame1.pack(pady=20)
frame2.pack()



#Entry
entry_var = tk.StringVar()
name_var = tk.StringVar()

entry = tk.Entry(frame1, width=40, textvariable=entry_var)
entry.insert(0, message_placeholder)  # Insert the placeholder text
entry.bind('<FocusIn>', on_entry_click)
entry.bind('<FocusOut>', on_focus_out)

name_entry = tk.Entry(frame1, width=40, textvariable=name_var)
name_entry.insert(0, name_placeholder)
name_entry.bind('<FocusIn>', on_entry_click)
name_entry.bind('<FocusOut>', on_focus_out)


#Send Button
save_username = tk.Button(frame1, text="Save UserName", width=33, bd=5, font="Arial 9", command=save_name)
send_btn = tk.Button(frame1, text="Send Message", width=33, bd=5, font="Arial 9", command=send_message)

# incoming messages and outcoming messages
label_incoming = tk.Label(frame2, text="Incoming Messages")
label_outgoing = tk.Label(frame2, text="Outgoing Messages")

listbox_incoming = tk.Listbox(frame2, width=50, height=10)
listbox_outgoing = tk.Listbox(frame2, width=50, height=10)

label_incoming.grid(row=0, column=0, pady=5)
listbox_incoming.grid(row=1, column=0, padx=10, pady=5)

label_outgoing.grid(row=0, column=1, pady=5)
listbox_outgoing.grid(row=1, column=1, padx=10, pady=5)


#Pack
name_entry.pack(pady=10)
save_username.pack()
entry.pack(pady=15)
send_btn.pack()

frame1.grid_rowconfigure(1, weight=1)
frame1.grid_columnconfigure(0, weight=1)
frame1.grid_columnconfigure(1, weight=1)
frame2.grid_rowconfigure(1, weight=1)  
frame2.grid_columnconfigure(0, weight=1) 
frame2.grid_columnconfigure(1, weight=1) 



# Main
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 12345))
receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()
root.mainloop()


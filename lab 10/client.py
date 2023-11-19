import tkinter as tk
import socket
import threading


incoming_messages = ["hello", "bro", "really", "I do not think so"]

# ------------ Send message from Client -----------
def send_message():

    print("sending message")
    message = entry.get()
    entry.delete(0,"end")
    client.send(message.encode())
    listbox_outgoing.insert("end", message)

#--------------- Recive Message --------------
def receive_messages():
    while True:
        # Receive and display messages from the server
        message = client.recv(1024).decode('utf-8')
        print("received message: ", message)
        listbox_incoming.insert("end", message)



# Handlers for placeholder in entry field
def on_entry_click(event):
    if entry.get() == placeholder:
        entry.delete(0, "end")  # Remove the placeholder text
        entry.config(fg='black')  # Set text color to black

def on_focus_out(event):
    if entry.get() == "":
        entry.insert(0, placeholder)  # Insert the placeholder text
        entry.config(fg='grey')  # Set text color to grey

placeholder = "Enter text here"
placeholder_color = "grey"



# =============== User Interface =============
root  = tk.Tk()
root["bg"] = 'white'

frame1 = tk.Frame(root, bd = 40, bg='grey', width=600, height=200)
frame2 = tk.Frame(root, bd=20, bg='yellow', width=600, height=200)
frame1.pack()
frame2.pack()


#Entry
entry_var = tk.StringVar()

entry = tk.Entry(frame1, width=40, textvariable=entry_var)
entry.insert(0, placeholder)  # Insert the placeholder text
entry.bind('<FocusIn>', on_entry_click)
entry.bind('<FocusOut>', on_focus_out)

#Send Button
send_btn = tk.Button(frame1, text="Send Message", width=33, bd=5, font="Arial 9", command=send_message)

# incoming messages and outcoming messages
label_incoming = tk.Label(frame2, text="Incoming Messages")
label_outgoing = tk.Label(frame2, text="Outgoing Messages")

listbox_incoming = tk.Listbox(frame2, width=50, height=10)
listbox_outgoing = tk.Listbox(frame2, width=50, height=10)

# for message in incoming_messages:
#     listbox_incoming.insert("end", message)


label_incoming.grid(row=0, column=0, pady=5)
listbox_incoming.grid(row=1, column=0, padx=10, pady=5)

label_outgoing.grid(row=0, column=1, pady=5)
listbox_outgoing.grid(row=1, column=1, padx=10, pady=5)


#Pack
entry.pack(pady=15)
send_btn.pack()




# Main
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 12345))
receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()
root.mainloop()


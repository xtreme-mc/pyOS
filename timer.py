from main import *

def countdown():
    try:
        count = int(entry.get())
    except ValueError:
        pass
 
    for i in range(count, 0, -1):
        label.config(text=i)
        root.update()
        sleep(1)
    label.config(text="finish")

root = tk.Tk()
root.title(f"timer for {user}")
icon(root)

label = tk.Label(root, text="enter time:")
label.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="start", command=countdown)
button.pack()

root.mainloop()

sys.exit

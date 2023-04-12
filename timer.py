from main import *

def countdown():
    while True:
        try:
            count = int(entry.get())
            break
        except ValueError:
            continue
        
    for i in range(count, 0, -1):
        label.config(text=i)
        root.update()
        sleep(1)
    label.config(text="finish")

root = tk.Tk()
root.title("Countdown Timer")

label = tk.Label(root, text="enter time:")
label.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="start", command=countdown)
button.pack()

root.mainloop()
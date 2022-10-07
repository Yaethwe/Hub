from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import tkinter as tk
app = Ursina()
player = FirstPersonController()
Sky()

boxes = []
for i in range(20):
  for j in range(20):
    for k in range(3):
      box = Button(color=color.white, model='cube', position=(j,k,i),
            texture='grass.png', parent=scene, origin_y=0.5)
      boxes.append(box)

def input(key):
  for box in boxes:
    if box.hovered:
      if key == 'left mouse down':
        new = Button(color=color.white, model='cube', position=box.position + mouse.normal,
                    texture='grass.png', parent=scene, origin_y=0.5)
        boxes.append(new)
      if key == 'right mouse down':
        boxes.remove(box)
        destroy(box)
        
  if key == 'escape':
    win = tk.Tk()
    win.title('Exit')
    win.geometry('500x300')
    f = tk.Frame(win)
    y = tk.Button(f, text="Yes", command=exit, bg='red', fg='white')
    n = tk.Button(f, text="No", command=win.destroy, bg='green', fg="white")
    t = tk.Label(win, text="Are you sure that you want to exit?", fg="blue", font=("sans-serif", 16))
    
    t.pack()
    f.pack()
    y.grid(row=0, column=0)
    n.grid(row=0, column=1)
    win.mainloop()

app.run()

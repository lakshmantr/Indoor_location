import tkinter as tk
import requests
import json

root = tk.Tk()
root.title("Location Indicator")
room_list = []

height = 500
width = 820
canvas = tk.Canvas(root, width=width, height=height, relief=tk.SUNKEN, bd=10)

def room_door(x1, y1):
    canvas.create_arc(x1-20, y1-20, x1+20, y1+20, start=0, extent=90, outline="black", width=2)

class room:
    def __init__(self, canvas, x1, y1, x2, y2, name=""):
        self.rect = canvas.create_rectangle(x1, y1, x2, y2, outline="black", width=2, fill="lightgray")
        self.name = name
        center_x = (x1 + x2) / 2
        center_y = (y1 + y2) / 2
        self.label = canvas.create_text(center_x, center_y, text=name, font=("Arial", 8, "bold"), fill="black")
    
    def coordinates_translation(self, x, y, z):
        a = canvas.coords(room_list[z].rect)[0]
        b = canvas.coords(room_list[z].rect)[1]
        x = x + a
        y = y + b
        return x, y

room_list = []
room_data = [
    (20, 20, 158, 158, "Labor\nRoom"),     
    (158, 20, 226, 89, "Toilet 1"),        
    (20, 158, 158, 296, "ICU"),          
    (20, 296, 89, 365, "Sterilization"),  
    (89, 296, 158, 365, "Changing\nRoom"),  
    (158, 158, 296, 296, "Lobby"),         
    (388, 20, 526, 89, "Doctor's\nCabin"), 
    (388, 89, 526, 226, "Waiting"),     
    (526, 20, 664, 226, "Reception"),      
    (158, 365, 296, 479, "Room 4"),  
    (296, 365, 433, 479, "Room 3"),            
    (433, 365, 572, 479, "Room 1"),        
    (572, 365, 664, 479, "Room 2"),        
]
for room_info in room_data:
    r = room(canvas, *room_info)
    room_list.append(r)
i = 0
def hello():
    global coordinates, i
    canvas.delete("dots")
    if i >= 3:
        return
    else:
        for employee_id, color in [(1, "red"), (2, "blue")]:
            response = requests.get(f"http://127.0.0.1:5000/launch?employee_id={employee_id}")
            data = response.json()
            zl = int(data["Room"])
            xl = int(data["x coordinates"])
            yl = int(data["y coordinates"])
            
            x, y = room_list[zl-1].coordinates_translation(xl, yl, zl-1)
            
            canvas.create_oval(x, y, x + 10, y + 10, fill=color, tags="dots")
        
        i += 1
        root.after(1000, hello)

button = tk.Button(root, text="Start", command=hello)
room_door(158, 227)  # ICU → Lobby (connection added)
room_door(157, 350)  #Corridor → Changong room
room_door(89, 330)   # Changing Room → Sterilization
room_door(250, 158)  #Lobby → Corridor (connection to main corridor)
room_door(388, 54)   #Lift → Doctor's Cabin
room_door(158,54)    #Tiolet 1 -> Cooridor
room_door(157,120)   #Labour Room -> Cooridoor
room_door(663,125)   #Entrance
room_door(388, 157)  # Recovery → Corridor
room_door(527,200)
room_door(595, 226)  # Reception → Waiting
room_door(227, 365)  # Lobby → Pre/Post OT
room_door(364, 365)  # Pre/Post OT → OT
room_door(502, 365)  # OT → Room 1
room_door(618, 365)  # Room 1 → Room 2
room_door(69,296)
# Add corridor line
canvas.create_line(200, 20, 500, 20, width=2)
canvas.create_line(664, 200, 664, 400, width=2)  # Vertical corridor line
button.pack()
canvas.pack()
root.mainloop()
import tkinter as tk,requests,json
root=tk.Tk()
root.title("Location Indicater")
room_list=[] 
height=500
widht=500
canvas=tk.Canvas(root,width=widht,height=height,relief=tk.SUNKEN,bd=10) 
class room:
    def __init__(self,canvas,x1,y1,x2,y2):
        self.rect = canvas.create_rectangle(x1, y1, x2, y2, outline="black", width=5)    
    def coordinates_translation(self,x,y,z):
        a=canvas.coords(room_list[z].rect)[0]
        b=canvas.coords(room_list[z].rect)[1]
        x=x+a
        y=y+b           
        return x,y
room_list=[]
room_coords = [
    (0, 250, 250, 0),
    (0, 250, 500, 500),
    (250, 0, 500, 250)]
for coords in room_coords:
    r=room(canvas,*coords)
    room_list.append(r) 
i=0    
def hello():
    global i
    global coordinates
    canvas.delete("dots")
    if i>=3:
       return
    else:  
         employee_id=1
         response=requests.get(f"http://127.0.0.1:5000/launch?employee_id={employee_id}")
         data=response.json()
         zl=int(data["Room"])
         xl=int(data["x coordinates"])
         yl=int(data["y coordinates"])    
         i+=1
         x,y=room_list[zl-1].coordinates_translation(xl,yl,zl-1)       
         canvas.create_oval(x, y, x + 10, y + 10, fill="red",tags="dots")   
         root.after(1000,hello)
button=tk.Button(root,text="Start",command=hello)
button.pack()   
canvas.pack()   
root.mainloop()    

     
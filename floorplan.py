import tkinter as tk,json
import requests
root=tk.Tk()
canvas=tk.Canvas(root,width=500,height=500,relief=tk.SUNKEN,bd=10)
room1=canvas.create_rectangle(0,250,250,0,outline="black",width=5)
room2=canvas.create_rectangle(0,250,500,500,outline="black",width=5)
room3=canvas.create_rectangle(250,0,500,250,outline="black",width=5)
coordinates={}
i=0
def hello():
    global i
    global coordinates
    canvas.delete("dots")
    coordinates={}
    if i>=3:
       return
    else:  
         employee_id=1
         response=requests.get(f"http://127.0.0.1:5000/launch?employee_id={employee_id}")
         data=response.json()
         x=int(data["x coordinates"])
         y=int(data["y coordinates"])       
         coordinates[(x, y)] = True
         canvas.create_oval(x, y, x + 10, y + 10, fill="red",tags="dots")   
         i+=1
         root.after(1000,hello)
button=tk.Button(root,text="Start",command=hello)
button.pack()
canvas.pack()
root.mainloop()
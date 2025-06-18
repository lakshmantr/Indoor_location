from flask import Flask,request ,jsonify
app = Flask(__name__)
list_of_coordinates = {1:{"room":1,"x":45,"y":120},2:{"room":1,"x":200,"y":60},3:{"room":3,"x":125,"y":90}}
counter=1
@app.route('/launch')
def launch_gui():
    cdn=request.args.get('employee_id',type=int)
    global counter
    if cdn==1:
      if counter<4:
         if list_of_coordinates[counter]["room"]==1:
               x=list_of_coordinates[counter]["x"]
               y=list_of_coordinates[counter]["y"]
               counter+=1
               return jsonify({"x coordinates":x,
                               "y coordinates":y})
               
         elif list_of_coordinates[counter]["room"]==2:
                x=list_of_coordinates[counter]["x"]
                y=list_of_coordinates[counter]["y"]
                x=0+x
                y=250+y
                counter+=1
                return jsonify({"x coordinates":x,
                               "y coordinates":y})
                 
         elif  list_of_coordinates[counter]["room"]==3:
                x=list_of_coordinates[counter]["x"]
                y=list_of_coordinates[counter]["y"]
                x=x+250
                y=y+0
                counter+=1
                return jsonify({"x coordinates":x,
                               "y coordinates":y})
                
      else:
           counter=1
           x=list_of_coordinates[counter]["x"]
           y=list_of_coordinates[counter]["y"]
           return jsonify({"x coordinates":x,
                           "y coordinates":y})
           
    else:
            return jsonify({"error": "Invalid employee_id"}), 400
                   
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask,request ,jsonify
app = Flask(__name__)
list_of_coordinates = {1:{"room":1,"x":45,"y":120},2:{"room":1,"x":200,"y":60},3:{"room":3,"x":125,"y":90}}
counter = 1
@app.route('/launch')
def launch_gui():
    cdn=request.args.get('employee_id',type=int)
    global counter
    if cdn==1:
           z=list_of_coordinates[counter]["room"]
           x=list_of_coordinates[counter]["x"]
           y=list_of_coordinates[counter]["y"]
           counter+=1
           return jsonify({"Room":z,
                           "x coordinates":x,
                           "y coordinates":y})
    else:
          return jsonify({"error": "Invalid employee_id"}), 400                  
if __name__ == '__main__':
    app.run(debug=True)
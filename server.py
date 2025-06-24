from flask import Flask,request ,jsonify
app = Flask(__name__)
emp_1_list_of_coordinates = {1:{"room":1,"x":45,"y":120},2:{"room":1,"x":200,"y":60},3:{"room":3,"x":125,"y":90}}
emp_2_list_of_coordinates = {1:{"room":1,"x":60,"y":180},2:{"room":2,"x":420,"y":200},3:{"room":3,"x":190,"y":80}}
emp_counter={1:1,2:1}
@app.route('/launch')
def launch_gui():
    cdn=request.args.get('employee_id',type=int)
    global counter
    if cdn is None or cdn>3 or cdn<1:
           return jsonify({"error": "Invalid employee_id"}), 400 
    else: 
          counter=emp_counter[cdn]
          list_of_coordinates= emp_1_list_of_coordinates if cdn == 1 else emp_2_list_of_coordinates
          z=list_of_coordinates[counter]["room"]
          x=list_of_coordinates[counter]["x"]    
          y=list_of_coordinates[counter]["y"]
          emp_counter[cdn]+=1
          return jsonify({"Room":z,
                           "x coordinates":x,
                           "y coordinates":y})                         
if __name__ == '__main__':
    app.run(debug=True)
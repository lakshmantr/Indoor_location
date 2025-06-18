from flask import Flask,request ,jsonify
app = Flask(__name__)
list_of_coordinates = [
    (15, 60,), 
     (105, 225),
     (195,300)]
@app.route('/launch')
def launch_gui():
    cdn=request.args.get('coordinates_index',type=int)
    if cdn is None or cdn<0 or cdn>2:        
         return jsonify('Invalid Coordibates Index'),400
    else:
         x=list_of_coordinates[cdn][0]
         y=list_of_coordinates[cdn][1]
         return jsonify({"x coordinates":x,
                         "y coordinates":y})
if __name__ == '__main__':
    app.run(debug=True)
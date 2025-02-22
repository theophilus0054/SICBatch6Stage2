from flask import Flask, request, jsonify

app = Flask(__name__)

data_saved = {}

@app.route('/data', methods = ['POST', 'GET'])
def recieve_data():
    global data_saved
    if request.method == 'POST':
        data = request.json
        print(f"Received Data: {data}")
        data_saved = data
        return {"status": "success"}, 200   
    else:
        return jsonify(data_saved), 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=7000, debug=True)
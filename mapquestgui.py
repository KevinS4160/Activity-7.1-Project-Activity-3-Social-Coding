from flask import Flask, render_template, request, jsonify
import urllib.parse
import requests

app = Flask(__name__)

main_api = "https://www.mapquestapi.com/directions/v2/route?" 
key = "arhaArR8A7wX8lxvSKao4iF2rZm5STjM"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_directions', methods=['POST'])
def get_directions():
    orig = request.form['origin']
    dest = request.form['destination']
    url = main_api + urllib.parse.urlencode({"key": key, "from": orig, "to": dest})
    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]

    if json_status == 0:
        directions = {
            "status": "success",
            "formattedTime": json_data["route"]["formattedTime"],
            "distance": "{:.2f}".format(json_data["route"]["distance"] * 1.61),
            "narrative": [
                f"{each['narrative']} ({'{:.2f}'.format(each['distance'] * 1.61)} km)"
                for each in json_data["route"]["legs"][0]["maneuvers"]
            ]
        }
        return jsonify(directions)
    else:
        return jsonify({"status": "error", "code": json_status})

if __name__ == "__main__":
    app.run(debug=True)

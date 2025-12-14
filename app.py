from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/calculate", methods=["POST"])
def calculate_bmi():
    data = request.get_json()

    weight = float(data["weight"])   # in kg
    height = float(data["height"])   # in meters

    bmi = round(weight / (height ** 2), 2)

    if bmi < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi < 25:
        category = "Normal weight"
    elif 25 <= bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"

    return jsonify({
        "bmi": bmi,
        "category": category
    })

if __name__ == "__main__":
    app.run(debug=True)

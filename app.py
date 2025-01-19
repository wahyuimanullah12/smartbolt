from flask import Flask, request, render_template, jsonify
import random

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/process-payment", methods=["POST"])
def process_payment():
    meter_number = request.form.get("meterNumber")
    amount = request.form.get("amount")

    if not meter_number or not amount:
        return "Input tidak valid", 400

    # Simulasi token listrik (gunakan API sebenarnya untuk produksi)
    token = "".join([str(random.randint(0, 9)) for _ in range(20)])

    return render_template("success.html", meter_number=meter_number, amount=amount, token=token)

if __name__ == "__main__":
    app.run(debug=True)

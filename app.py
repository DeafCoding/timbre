from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("ring.html")

@app.route("/ring", methods=["POST"])
def ring():
    category = request.form["category"]
    print(f"🔔 Someone rang: {category}")
    return "Thanks! The resident has been notified."
def home():
    return render_template("ring.html")

if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, render_template, request, abort
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from dotenv import load_dotenv
import os
import requests

load_dotenv()

MESSAGES = {
    "delivery": "📦 A delivery is waiting at your door",
    "family": "👋 Your family member/s came to visit you",
    "other": "❓ Seems that someone is waiting for you",
}
NTFY_TOPIC = os.environ["NTFY_TOPIC"]
RING_ID = os.environ["RING_ID"]

app = Flask(__name__)
limiter = Limiter(get_remote_address, app=app)

@app.route("/ring/<ring_id>", methods=["GET", "POST"])
@limiter.limit("3 per minute", methods=["POST"])
def ring(ring_id):
    if ring_id != RING_ID:
        abort(404)

    if request.method == "POST":
        category = request.form["category"]
        if category not in MESSAGES:
            abort(400)
        print(f"🔔 Someone rang: {category}")
        requests.post(
            f"https://ntfy.sh/{NTFY_TOPIC}",
            data=MESSAGES[category].encode("utf-8"),
            headers={"Title": "Timbre", "Priority": "urgent", "Tags": "bell"},
        )
        return "Thanks! The resident has been notified."

    return render_template("ring.html")
@app.errorhandler(429)
def too_many(e):
    return "You rang way too many, let that cool down please"
@app.errorhandler(400)
def bad_request(e):
    return "Invalid request.", 400

if __name__ == "__main__":
    app.run(debug=True)

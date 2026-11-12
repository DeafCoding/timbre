from flask import Flask, render_template, request, abort   # ← agregué abort
import os
import requests

MESSAGES = {
    "delivery": "📦 A delivery is waiting at your door",
    "family": "👋 Your family member/s came to visit you",
    "other": "❓ Seems that someone is waiting for you",
}
NTFY_TOPIC = os.environ["NTFY_TOPIC"]
RING_ID = os.environ["RING_ID"]                                 # ← nuevo

app = Flask(__name__)

@app.route("/ring/<ring_id>", methods=["GET", "POST"])    # ← una sola ruta
def ring(ring_id):
    if ring_id != RING_ID:                                      # ← ¿coincide con el secreto?
        abort(404)

    if request.method == "POST":                             # ← ¿tocaron un botón?
        category = request.form["category"]
        print(f"🔔 Someone rang: {category}")
        requests.post(
            f"https://ntfy.sh/{NTFY_TOPIC}",
            data=MESSAGES[category].encode("utf-8"),
            headers={"Title": "Timbre", "Priority": "urgent", "Tags": "bell"},
        )
        return "Thanks! The resident has been notified."

    return render_template("ring.html")                     # ← si no, muestra los botones

if __name__ == "__main__":
    app.run(debug=True)
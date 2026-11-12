# Timbre 🔔
A free, no-install doorbell for Deaf people. Visitors scan a QR code
on the door, tap a button, and the resident gets an urgent push notification.

## Why
Video doorbells need mounting, wiring, and Wi-Fi at the door. Timbre is a
printed QR code: renters, dorms, and temporary homes can use it today.

## How it works
1. Visitor scans the QR code on the door
2. Picks a reason: 📦 Delivery · 👋 Family & Friends · ❓ Other
3. The resident gets an urgent push notification via [ntfy](https://ntfy.sh)

## MVP (Phase 1) ✅
- [x] Visitor page with 3 buttons: Delivery, Family & Friends, Other
- [x] Urgent push notification via ntfy
- [x] Random, unguessable ID in the URL (`/ring/<id>`)
- [x] Printable QR code generator

## Phase 2
- [ ] User registration, one QR per user
- [ ] Optional visitor photo
- [ ] Deployment with HTTPS on a custom subdomain

## Setup
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Create a `.env` file (never commit it):
```
NTFY_TOPIC=your-random-topic
RING_ID=your-random-id
```

Generate random values with:
```bash
python3 -c "import secrets; print(secrets.token_urlsafe(16))"
```

Run the app:
```bash
python app.py
```

Generate the QR code:
```bash
python make_qr.py http://localhost:5000
```

## Threat model (living section)
Built first, then attacked by me. Each finding lists the threat and its mitigation.

| Threat | Impact | Mitigation | Status |
|---|---|---|---|
| Guessable ntfy topic | Anyone can read or spam notifications | Random topic stored in `.env`, not in code | ✅ |
| Guessable doorbell URL | Strangers can ring any doorbell | Secret random ID in the URL, 404 otherwise | ✅ |
| Secrets in a public repo | Topic and ID leak via GitHub | `.env` and QR images in `.gitignore` | ✅ |
| Unvalidated `category` input | Server crash (500) leaking source code and file paths | Allow-list of categories, generic 400 handler | ✅ |
| Doorbell spam from a photographed QR | Endless notifications | Rate limit: 3 rings/minute per IP, generic 429 handler | ✅ |
| Default error pages leak details | Reveals stack traces and rate limits | Custom generic handlers for 400 and 429 | ✅ |
| Flask debug mode in production | Remote code execution via Werkzeug debugger | Never deploy with `debug=True` | ⏳ before deploy |
| QR swapping (fake sticker over the real one) | Visitors sent to a phishing page | Tamper-evident sticker, show the domain on the printout | ⏳ |

## Ideas
- Silent doorbell for new parents (no waking the baby), night-shift workers, homes with dogs

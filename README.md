# Timbre 🔔
A free, no-install doorbell for Deaf people. Visitors scan a QR code
on the door, tap a button, and the resident gets a push notification.

## Why
Video doorbells need mounting, wiring, and Wi-Fi at the door. Timbre is a
printed QR code: renters, dorms, and temporary homes can use it today.

## MVP (Phase 1)
- [x] Visitor page with 3 buttons: Delivery, Family & Friends, Other
- [x] Push notification via ntfy
- [x] Random, unguessable ID in the URL (/ring/<id>)
- [x] Printable QR code

## Phase 2
- [ ] User registration, one QR per user
- [ ] Optional visitor photo

## Threat model (living section)
- Guessable ntfy topic → anyone can read or spam notifications → use random IDs
- QR swapping (a fake sticker over the real one) → visitors sent to a phishing page
- Spam from a photographed QR → rate limiting, presence check

# AirPulse+ Prototype

A beginner-friendly software prototype for:

**AI-Powered Contactless Vital Sign Detection Using Wi-Fi Signals**

## What this prototype does

- Simulates a Wi-Fi/CSI sensing stream.
- Lets you change a person's pose.
- Changes simulated heart rate, respiration, motion, signal quality and status based on pose.
- Shows a live synthetic signal.
- Requires no ESP32, Cognitum Seed, camera or other hardware.

## Important

This is a **software demonstration using simulated data**. It is not a medical device and does not measure real vital signs.

## Windows setup

Open CMD in this folder:

```cmd
cd backend
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python -m uvicorn main:app --host 127.0.0.1 --port 8000
```

Then open:

http://127.0.0.1:8000

Stop the server with `Ctrl+C`.

## Architecture

Pose selection -> simulated CSI waveform -> synthetic vital estimation -> dashboard.

The simulator is intentionally simple so it can later be replaced by a real CSI processing pipeline.

import math
import random
import time

POSES = {
    "standing": {
        "label": "Standing",
        "heart": 72,
        "resp": 15,
        "motion": 8,
        "quality": 94,
        "color": "green",
        "description": "Stable upright posture"
    },
    "sitting": {
        "label": "Sitting",
        "heart": 68,
        "resp": 14,
        "motion": 4,
        "quality": 96,
        "color": "green",
        "description": "Low-motion seated posture"
    },
    "walking": {
        "label": "Walking",
        "heart": 92,
        "resp": 21,
        "motion": 48,
        "quality": 88,
        "color": "blue",
        "description": "Moderate dynamic movement"
    },
    "running": {
        "label": "Running",
        "heart": 128,
        "resp": 30,
        "motion": 82,
        "quality": 76,
        "color": "orange",
        "description": "High-intensity movement"
    },
    "lying": {
        "label": "Lying",
        "heart": 64,
        "resp": 13,
        "motion": 2,
        "quality": 97,
        "color": "green",
        "description": "Resting horizontal posture"
    },
    "sleeping": {
        "label": "Sleeping",
        "heart": 58,
        "resp": 11,
        "motion": 1,
        "quality": 98,
        "color": "purple",
        "description": "Low-motion resting state"
    },
}

current_pose = "standing"
started = time.time()

def set_pose(pose: str):
    global current_pose
    pose = pose.lower()
    if pose not in POSES:
        return {"error": f"Unknown pose. Choose one of: {', '.join(POSES)}"}
    current_pose = pose
    return get_state()

def get_state():
    p = POSES[current_pose]
    t = time.time() - started

    # Small deterministic-looking changes make the dashboard feel live.
    heart = p["heart"] + round(2.0 * math.sin(t / 4.0) + random.uniform(-1.2, 1.2))
    resp = p["resp"] + round(0.5 * math.sin(t / 5.0) + random.uniform(-0.3, 0.3), 1)
    quality = max(60, min(99, p["quality"] + round(math.sin(t / 7.0))))
    motion = max(0, min(100, p["motion"] + round(4 * math.sin(t / 2.5))))

    if heart < 60:
        status = "Resting"
    elif heart < 100:
        status = "Normal"
    elif heart < 120:
        status = "Active"
    else:
        status = "High activity"

    # Synthetic CSI-like waveform for visualization only.
    samples = []
    for i in range(90):
        x = i / 8.0
        breathing = math.sin(x * (1.0 + resp / 80.0) + t * 1.3) * (0.45 + motion / 250)
        heartbeat = math.sin(x * 4.7 + t * 2.0) * 0.12
        noise = random.uniform(-0.08, 0.08)
        samples.append(round(breathing + heartbeat + noise, 4))

    return {
        "pose": current_pose,
        "poseLabel": p["label"],
        "description": p["description"],
        "heartRate": int(heart),
        "respirationRate": float(resp),
        "motion": int(motion),
        "signalQuality": int(quality),
        "status": status,
        "samples": samples,
        "timestamp": time.time(),
        "simulation": True
    }

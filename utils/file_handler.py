import os
import json
from datetime import datetime

DATA_DIR = "data"

def buat_batch_harian(tanggal: str):
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)

    path = os.path.join(DATA_DIR, f"{tanggal}.json")
    if not os.path.exists(path):
        batch_data = {
            "tanggal": tanggal,
            "waktu_mulai": datetime.now().isoformat(),
            "donatur": []
        }
        with open(path, "w") as f:
            json.dump(batch_data, f, indent=2)
    else:
        with open(path) as f:
            batch_data = json.load(f)

    return batch_data, path

def load_batch_data(tanggal: str):
    path = os.path.join(DATA_DIR, f"{tanggal}.json")
    if os.path.exists(path):
        with open(path) as f:
            return json.load(f)
    return None

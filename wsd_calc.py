import json
import soundfile as sf
import numpy as np
import uuid
import numpy as np
from pathlib import Path

thresholds_filename = 'thresholds.json'

def get_threshold(id):
    if id is None:
        return -1
    try:
        thresholds = json.load(open(thresholds_filename, 'r'))
    except Exception:
        thresholds = {}
    return thresholds.get(id, -1)

def post_threshold(audio_track):
    data, _ = sf.read(audio_track)
    t = np.percentile(np.abs(data), 99.9)
    try:
        thresholds = json.load(open(thresholds_filename, 'r'))
    except Exception:
        thresholds = {}
    id = str(uuid.uuid4())
    thresholds[id] = t
    json.dump(thresholds, open(thresholds_filename, 'w+'))
    return id

def _max_pool(data, pool_size=20):
    pooled = data.copy()
    for i in range(pool_size, len(data) - pool_size):
        pooled[i] = np.max(np.abs(data[i - pool_size: i + pool_size]))
    return pooled

def get_wsd(id, audio_track, num_syllables, backup_percentile=88):
    data, sr = sf.read(audio_track)

    pooled = _max_pool(data)

    t = get_threshold(id)
    if t == -1:
        t = np.percentile(np.abs(data), backup_percentile)

    pooled = np.where(pooled > t, 1, 0)
    word_duration = np.sum(pooled) / sr * 1000 # Reduces to seconds then scales to ms
    wsd = word_duration / num_syllables
    return wsd
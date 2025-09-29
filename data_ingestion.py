import json
from typing import List, Dict

def load_activity_log(path: str) -> List[Dict]:
    """Load a JSON array of daily activity logs."""
    with open(path, 'r') as f:
        data = json.load(f)
    if not isinstance(data, list):
        raise ValueError('Input JSON must be a list of daily records.')
    return data

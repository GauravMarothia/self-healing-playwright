import json
import os
from datetime import datetime

def log_healing_event(old_selector, new_selector, status="Success"):
    """
    Records the healing event to the reports directory for audit.
    """
    log_path = "reports/healing_logs.json"
    
    # Ensure the directory exists
    os.makedirs(os.path.dirname(log_path), exist_ok=True)
    
    event = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "original_selector": old_selector,
        "healed_selector": new_selector,
        "status": status
    }
    
    # Append to existing log or create new list
    logs = []
    if os.path.exists(log_path):
        with open(log_path, "r") as f:
            try:
                logs = json.load(f)
            except json.JSONDecodeError:
                pass
                
    logs.append(event)
    
    with open(log_path, "w") as f:
        json.dump(logs, indent=4, fp=f)
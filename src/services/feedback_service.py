# Saves agent feedback, one JSON line per record.
import json
from datetime import datetime, timezone
 
from src.core import config
 
 
def save_feedback(ticket: str, reply: str, rating: str, edited_reply: str | None = None) -> None: #type: ignore
    record = {
        "time": datetime.now(timezone.utc).isoformat(),
        "ticket": ticket,
        "reply": reply,
        "rating": rating,
        "edited_reply": edited_reply,
    }
    with open(config.FEEDBACK_FILE, "a", encoding="utf-8") as f:
        f.write(json.dumps(record, ensure_ascii=False) + "\n")

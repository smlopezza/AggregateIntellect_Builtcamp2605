import os
from fastapi import APIRouter, Header, HTTPException
from app.utils import is_sendable, local_hour

router = APIRouter()

SECRET = os.getenv("CLOUD_SCHEDULER_SECRET", "")


def _verify(secret: str):
    if secret != SECRET:
        raise HTTPException(status_code=403, detail="Forbidden")


@router.post("/jobs/pre-chat-nudge")
async def pre_chat_nudge(x_scheduler_secret: str = Header(...)):
    _verify(x_scheduler_secret)
    # Query Firestore: contacts where scheduled_chat_at in (now+12h, now+36h)
    # and pre_nudge_sent_at is null
    # For each: skip if not is_sendable() or local_hour() != 20
    # Send nudge via Claude (Haiku) + Twilio, write pre_nudge_sent_at
    return {"status": "ok"}


@router.post("/jobs/post-chat-checkin")
async def post_chat_checkin(x_scheduler_secret: str = Header(...)):
    _verify(x_scheduler_secret)
    # Query Firestore: contacts where scheduled_chat_at in (now-3h, now-1h)
    # and post_nudge_sent_at is null
    # For each: skip if not is_sendable()
    # Send check-in via Claude (Sonnet) + Twilio, write post_nudge_sent_at
    return {"status": "ok"}


@router.post("/jobs/thank-you-nudge")
async def thank_you_nudge(x_scheduler_secret: str = Header(...)):
    _verify(x_scheduler_secret)
    # Query Firestore: contacts where scheduled_chat_at in (now-36h, now-12h)
    # and thank_you_nudge_sent_at is null and post_nudge_sent_at is not null
    # For each: skip if local_hour() != 7
    # Send thank-you nudge via Claude (Haiku) + Twilio, write thank_you_nudge_sent_at
    return {"status": "ok"}


@router.post("/jobs/reset-rate-limits")
async def reset_rate_limits(x_scheduler_secret: str = Header(...)):
    _verify(x_scheduler_secret)
    # Batch query Firestore: all users where message_count_reset_at < now
    # Reset message_count_today = 0 for each
    return {"status": "ok"}

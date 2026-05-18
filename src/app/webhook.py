from fastapi import APIRouter, BackgroundTasks, Request
from fastapi.responses import Response

router = APIRouter()


@router.post("/webhook/twilio")
async def twilio_webhook(request: Request, background_tasks: BackgroundTasks):
    form = await request.form()
    phone = str(form.get("From", "")).replace("whatsapp:", "")
    text = str(form.get("Body", ""))
    message_sid = str(form.get("MessageSid", ""))

    background_tasks.add_task(process_message, phone, text, message_sid)
    return Response(content="", media_type="text/xml")


async def process_message(phone: str, text: str, message_sid: str):
    # TODO: implement full message processing pipeline
    # 1. Idempotency check (MessageSid)
    # 2. Load or create user doc from Firestore
    # 3. Check rate limit
    # 4. Load active contact doc
    # 5. Build context + call Claude
    # 6. Handle update_state tool use
    # 7. Save messages to Firestore
    # 8. Send reply via Twilio
    pass

import os
from google.cloud import firestore
from app.models import UserDoc, ContactDoc

_db = None


def get_db():
    global _db
    if _db is None:
        _db = firestore.Client(project=os.getenv("FIRESTORE_PROJECT_ID"))
    return _db


def load_user(phone: str) -> UserDoc:
    doc = get_db().collection("users").document(phone).get()
    if doc.exists:
        return UserDoc(phone=phone, **doc.to_dict())
    return UserDoc(phone=phone)


def save_user(user: UserDoc):
    data = {k: v for k, v in user.__dict__.items() if k != "phone"}
    get_db().collection("users").document(user.phone).set(data, merge=True)


def load_contact(phone: str, contact_id: str) -> ContactDoc | None:
    doc = get_db().collection("users").document(phone)\
        .collection("contacts").document(contact_id).get()
    if doc.exists:
        return ContactDoc(**doc.to_dict())
    return None


def save_contact(phone: str, contact_id: str, contact: ContactDoc):
    get_db().collection("users").document(phone)\
        .collection("contacts").document(contact_id).set(contact.__dict__, merge=True)


def is_duplicate(message_sid: str) -> bool:
    doc = get_db().collection("processed_messages").document(message_sid).get()
    if doc.exists:
        return True
    get_db().collection("processed_messages").document(message_sid).set({"processed": True})
    return False

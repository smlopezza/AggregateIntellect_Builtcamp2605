from dataclasses import dataclass
from typing import Optional


@dataclass
class ContactDoc:
    name: str
    role: str
    company: str
    connection_context: str
    scheduled_chat_at: Optional[str] = None
    pre_nudge_sent_at: Optional[str] = None
    post_nudge_sent_at: Optional[str] = None
    thank_you_nudge_sent_at: Optional[str] = None
    post_call_notes: Optional[str] = None
    depth_signals: Optional[str] = None
    topics_of_interest: Optional[list] = None
    linkedin_url: Optional[str] = None
    created_at: Optional[str] = None

    def __post_init__(self):
        if self.topics_of_interest is None:
            self.topics_of_interest = []


@dataclass
class UserDoc:
    phone: str
    name: str = ""
    field: str = ""
    language: str = "es"
    time_in_canada: str = ""
    city: str = ""
    country_of_origin: str = ""
    timezone: str = "America/Toronto"
    current_challenge: str = ""
    application_stage: str = "exploring"
    has_contacts: bool = False
    about_me: Optional[str] = None
    conversation_summary: Optional[str] = None
    current_state: str = "onboarding"
    messages: Optional[list] = None
    last_active: Optional[str] = None
    tier: str = "free"
    message_count_today: int = 0
    message_count_reset_at: Optional[str] = None
    contributed_at: Optional[str] = None

    def __post_init__(self):
        if self.messages is None:
            self.messages = []

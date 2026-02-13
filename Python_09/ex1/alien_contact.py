from pydantic import Field, model_validator, BaseModel, ValidationError
from datetime import datetime
from typing import Optional
from enum import Enum


class ContactType(str, Enum):
    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: Optional[str] = Field(max_length=500, default=None)
    is_verified: bool = False

    @model_validator(mode="after")
    def validate(self):
        if not self.contact_id.startswith("AC"):
            raise ValueError('Contact ID must start with "AC"')

        if self.contact_type == ContactType.PHYSICAL and not self.is_verified:
            raise ValueError('Physical contact reports must be verified')

        if (
             self.contact_type == ContactType.TELEPATHIC
             and self.witness_count < 3):
            raise ValueError('Telepathic contact require at least 3 witnesses')

        if self.signal_strength > 7.0 and self.message_received is None:
            raise ValueError('Strong signals should include received messages')

        return self


def display_contact_info(contact: AlienContact) -> None:
    print(
          "Valid contact report:\n"
          f"ID: {contact.contact_id}\n"
          f"Type: {contact.contact_type.value}\n"
          f"Location: {contact.location}\n"
          f"Signal: {contact.signal_strength}/10\n"
          f"Duration: {contact.duration_minutes} minutes\n"
          f"Witnesses: {contact.witness_count}")
    if contact.message_received:
        print(f"Message: '{contact.message_received}'\n")


def main() -> None:
    print("Alien Contact Log Validation")
    try:
        print("======================================")
        contact1 = AlienContact(
            contact_id="AC_2024_001",
            timestamp=datetime.now(),
            contact_type=ContactType.RADIO,
            location="Area 51, Nevada",
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=5,
            message_received="Greetings from Zeta Reticuli",
            is_verified=True
        )
        display_contact_info(contact1)

    except ValidationError as e:
        print("Expected validation error:")
        for err in e.errors():
            if 'error' in err['ctx']:
                print(err['ctx']['error'])
            else:
                print(err['msg'])

    try:
        print("======================================")
        contact2 = AlienContact(
            contact_id="AC_2024_001",
            timestamp=datetime.now(),
            contact_type=ContactType.TELEPATHIC,
            location="Area 51, Nevada",
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=1,
            message_received="Greetings from Zeta Reticuli",
            is_verified=True
        )
        display_contact_info(contact2)

    except ValidationError as e:
        print("Expected validation error:")
        for err in e.errors():
            if 'error' in err['ctx']:
                print(err['ctx']['error'])
            else:
                print(err['msg'])


if __name__ == "__main__":
    main()

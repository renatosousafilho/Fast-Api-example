from pydantic import BaseModel, field_validator, ValidationError
from datetime import datetime as dt
from pytz import timezone as tz

class NoteSchema(BaseModel):
    title: str
    description: str
    completed: str
    created_date: str

    @field_validator("title")
    def validate_title(cls, value):
        if not value:
            raise ValueError("field required")
        if len(value) < 3:
            raise ValueError("Title should have at least 3 characters")
        if len(value) > 20:
            raise ValueError("Title should have at most 20 characters")
        return value

        


class NoteDB(NoteSchema):
    id: int

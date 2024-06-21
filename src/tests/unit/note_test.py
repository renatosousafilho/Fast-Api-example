import pytest
import logging
from app.api.models import NoteSchema

logger = logging.getLogger(__name__)

def test_should_create_valid_note():
  # Arrange
  payload = {
    "title": "Test Title",
    "description": "Test Description",
    "completed": "False",
    "created_date": "2021-01-01T00:00:00",
  }
  # Act
  note = NoteSchema(**payload)
  # Assert
  assert note.title == payload["title"]
  assert note.description == payload["description"]
  assert note.completed == payload["completed"]
  assert note.created_date == payload["created_date"]

def test_should_raise_error_when_title_is_too_short():
  # Arrange
  payload = {
    "title": "T",
    "description": "Test Description",
    "completed": "False",
    "created_date": "2021-01-01T00:00:00",
  }
  logger.error("payload: %s", payload)
  # Act & Assert
  with pytest.raises(ValueError) as error:
    NoteSchema(**payload)
  assert "Title should have at least 3 characters" in str(error)
  
def test_should_raise_error_when_title_is_too_long():
  # Arrange
  payload = {
    "title": "Title with more than 20 characters",
    "description": "Test Description",
    "completed": "False",
    "created_date": "2021-01-01T00:00:00",
  }
  logger.error("payload: %s", payload)
  # Act & Assert
  with pytest.raises(ValueError) as error:
    NoteSchema(**payload)
  assert "Title should have at most 20 characters" in str(error)

def test_should_raise_error_when_title_is_missing():
  # Arrange
  payload = {
    "title": "",
    "description": "Test Description",
    "completed": "False",
    "created_date": "2021-01-01T00:00:00",
  }
  logger.error("payload: %s", payload)
  # Act
  with pytest.raises(ValueError) as error:
    NoteSchema(**payload)
  assert "field required" in str(error)

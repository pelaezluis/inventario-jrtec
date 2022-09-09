from pydantic import BaseModel
from typing import Optional

class AudioConverter(BaseModel):
    id: Optional[str]
    audio_in: str
    audio_out: str
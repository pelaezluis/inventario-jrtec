from fastapi import APIRouter, HTTPException, File, UploadFile
from uuid import uuid4 as uuid
from app.schemas.response import GetResponse, PostResponse, PutResponse, DeleteResponse
from app.schemas.audio_converter import AudioConverter
from pydub import AudioSegment
from pydub.utils import which

router = APIRouter()

@router.get('/audio')
async def get_audio():
    pass


def convert_audio_to_opus(audio_in: str, audio_out: str): # convert to 48kHz
    AudioSegment.converter = which("ffmpeg")
    sound = AudioSegment.from_mp3(audio_in)
    sound.export(audio_out, format="opus")
    print(f'File {audio_in} Converted')


@router.post('/audio')
async def create_audio(file: UploadFile = File(...)):
    path: str = 'app/static/audio'
    ext: str = file.filename.split('.')[-1]
    out: str = file.filename.replace(ext, 'opus')
    
    with open(f'{path}/{file.filename}', 'wb') as audio:
        cont = await file.read()
        audio.write(cont)
        audio.close()
    convert_audio_to_opus(f'{path}/{file.filename}', f'{path}/{out}')
    return {"filename": file.filename}
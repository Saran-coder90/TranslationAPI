from fastapi import FastAPI, HTTPException, Response
from pydantic import BaseModel
from deep_translator import GoogleTranslator

app = FastAPI()

class TranslationRequest(BaseModel):
    text: str
    to: str

@app.post("/{from_language}")
async def get_translated_text(from_language: str, request: TranslationRequest):
    try:
        translated = GoogleTranslator(source=from_language, target=request.to).translate(request.text)
        return {"translated_text": translated, "statusCode" : 200}
    except Exception as e:
        return Response(
            statusCode=500,
            translated_text = None
        )
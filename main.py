from fastapi import FastAPI, HTTPException
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
        return {"original_text": request.text, "translated_text": translated}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Translation failed: {str(e)}")

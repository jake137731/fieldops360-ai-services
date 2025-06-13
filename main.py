from fastapi import FastAPI, Request
import openai, os

app = FastAPI()
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.post("/generate")
async def generate(request: Request):
    data = await request.json()
    prompt = data.get("prompt")
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return {"proposal": response.choices[0].message.content}

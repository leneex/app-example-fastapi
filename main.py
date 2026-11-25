from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

app = FastAPI()

@app.get("/", response_class=PlainTextResponse)
async def root():
    return "Hello world"


if __name__ == "__main__":
    import os

    import uvicorn

    # Local run: port from PORT, 8000 by default
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("PORT", "8000")))


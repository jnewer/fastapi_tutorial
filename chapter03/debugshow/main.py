from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
import uvicorn


app = FastAPI(debug=True)


@app.get("/")
def index():
    1992 / 0
    return PlainTextResponse("Hello, world!")


if __name__ == "__main__":
    uvicorn.run(app="main:app", host="127.0.0.1", port=65535, reload=True, debug=True)

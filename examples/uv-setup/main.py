import os
import air
from fastapi import FastAPI
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()


@app.get("/", response_class=air.TagResponse)
async def index():
    message = os.getenv("MESSAGE", "Hello, World!")
    
    return air.Html(
        air.Head(air.Title("UV Example")),
        air.Body(
            air.H1(message),
            air.P("This is a minimal FastAPI app with Air tags."),
            air.P("Edit MESSAGE in .env to change the greeting.")
        )
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
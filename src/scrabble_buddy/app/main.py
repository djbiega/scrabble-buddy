import base64

from fastapi import FastAPI, File, UploadFile, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.responses import FileResponse

from src.scrabble_buddy import TEMPLATES_DIR

app = FastAPI()
templates = Jinja2Templates(directory=TEMPLATES_DIR)

@app.post("/upload")
async def upload(request: Request, file: UploadFile = File(...)):
    try:
        contents = file.file.read()
        with open(f"uploaded_{file.filename}", "wb+") as f:
            f.write(contents)
    except:
        return {"message": "There was an error uploading the file"}
    finally:
        file.file.close()

    encoded_image = base64.b64encode(contents).decode("utf-8")
    return templates.TemplateResponse("display.html", {"request": request, "uploadedImage": encoded_image})


@app.get("/")
async def main(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", port=5000, log_level="info")

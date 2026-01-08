from fastapi import FastAPI, UploadFile
from app.backend.ocr import run_ocr
from app.backend.extract import extract_items

app = FastAPI()

@app.post("/process_menu")
async def process_menu(file: UploadFile):
    path = "datas/tmp/menu.png"
    with open(path, "wb") as f:
        f.write(await file.read())

    lines = run_ocr(path)
    items = extract_items(lines)

    return {"items": items}

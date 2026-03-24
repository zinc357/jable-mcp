import uvicorn
from fastapi import FastAPI, HTTPException
from jable_downloader import download_by_code

app = FastAPI()

@app.get("/download/{code}")
def download(code: str):
    try:
        path = download_by_code(code)
        return {"status": "success", "file": path}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

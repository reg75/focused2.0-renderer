from fastapi import FastAPI, Body, Response, HTTPException
from pydantic import BaseModel
from weasyprint import HTML

app = FastAPI()

class RenderReq(BaseModel):
    html: str

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/render", response_class=Response)
def render(req: RenderReq):
    try:
        pdf = HTML(string=req.html).write_pdf()
        return Response(content=pdf, media_type="application/pdf")
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

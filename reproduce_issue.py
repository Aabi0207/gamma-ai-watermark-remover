
import os
import tempfile
import logging
from fastapi import FastAPI, File, UploadFile, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from starlette.exceptions import HTTPException as StarletteHTTPException
from werkzeug.utils import secure_filename
from utils.processors import PDFProcessor, PPTXProcessor

app = FastAPI(title="Gamma AI Watermark Remover")
templates = Jinja2Templates(directory="templates")

# Initialize processors
pdf_processor = PDFProcessor()
print("PDFProcessor initialized")
pptx_processor = PPTXProcessor()
print("PPTXProcessor initialized")

if __name__ == "__main__":
    import uvicorn
    print("Success uvicorn import inside main")

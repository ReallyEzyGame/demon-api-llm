# -*- coding: utf-8 -*-
"""[W2 - NOTEBOOK] API.ipynb


Original file is located at
    https://colab.research.google.com/drive/11RIrVMiR5foC0x8R15i9RCkf1-4aujhz

# Source code structure:
# Import Libraries( in the requirements.txt)
# Build Model
# Build & Initialize API
# 
# Install Libraries
"""

# Cài đặt các thư viện cho Model và API

"""# Import Libraries"""

# Import thư viện xử lý bất đồng bộ và API
import nest_asyncio
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
import torch
# Import thư viện AI
from transformers import pipeline
from transformers import AutoTokenizer, AutoModelForCausalLM
# Import thư viện hỗ trợ chạy tunneling ngầm
import subprocess
import threading
import time

"""# Build Model"""

model_id = "Qwen/Qwen2.5-3B-Instruct"

print("Đang tải Tokenizer và Model...")
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    device_map="auto",
    torch_dtype=torch.float16,
)
print("Tải thành công!")

"""# Initialize API"""

app = FastAPI(title="Qwen LLM API")

# Lớp định nghĩa dữ liệu đầu vào
class QueryRequest(BaseModel):
    prompt: str
    max_new_tokens: int = 256
    temperature: float = 0.7

@app.get("/")
def detail():
    return {"detail": "This is text generation API service using Qwen-2.5-3B LLM model"}

@app.get("/health")
def health_check():
    return {"status": "Qwen API is running on Colab"}

@app.post("/generate")
def generate_text(req: QueryRequest):
    # Chuẩn bị đầu vào cho model
    inputs = tokenizer(req.prompt, return_tensors="pt").to(model.device)

    # Sinh văn bản
    outputs = model.generate(
        **inputs,
        max_new_tokens=req.max_new_tokens,
        temperature=req.temperature,
        do_sample=True
    )

    # Giải mã kết quả (bỏ phần prompt ban đầu đi nếu muốn)
    response_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return {"response": response_text}

# Cho phép uvicorn chạy ngầm trong Colab cell
nest_asyncio.apply()

# # Hàm khởi động server
# def run_server():
#     uvicorn.run(app, host="127.0.0.1", port=8000, log_level="warning")

# # Khởi động Server
# server_thread = threading.Thread(target=run_server, daemon=True)
# server_thread.start()
# for running non-stop and giving API to outside cell
if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000)
# Mô phỏng Server khởi động
time.sleep(3)
print("Server đã chạy tại http://127.0.0.1:8000")
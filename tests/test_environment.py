
import torch
import open_clip
import faiss
import numpy as np
from PIL import Image
import fastapi

print("=" * 45)
print("TEXT-TO-IMAGE SEARCH ENGINE")
print("=" * 45)

print("PyTorch:", torch.__version__)
print("CUDA:", torch.cuda.is_available())
print("OpenCLIP: Successfully imported")
print("FAISS:", faiss.__version__)
print("NumPy:", np.__version__)
print("Pillow: Successfully imported")
print("FastAPI: Successfully imported")

print("=" * 45)
print("ENVIRONMENT READY")
print("=" * 45)

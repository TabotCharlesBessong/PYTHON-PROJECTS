from fastapi import APIRouter
import base64
from io import BytesIO
from apps.calculator.utils import analyze_image
from schema import ImageData
from PIL import Image

router = APIRouter()

@router.post('')
async def run(data: ImageData):
  image_data = base64.b64decode(data.image.split(",")[1])  # Assumes data:image/png;base64,<data>
  image_bytes = BytesIO(image_data)
  image = Image.open(image_bytes)
  responses = analyze_image(image, dict_of_vars=data.dict_of_vars)
  processed_responses = []
  for response in responses:
      processed_responses.append({
          "expr": response["expr"],
          "result": response["result"],
          "assign": True  # You can modify this based on your requirements
      })
  return {"message": "Image processed", "data": processed_responses, "status": "success"}
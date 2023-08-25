from django.shortcuts import render
from django.views import View
from PIL import Image
import cv2
import pytesseract
import os
import numpy as np

class ImageToTextView(View):
    template_name = 'imgtotext/upload.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        if 'image' in request.FILES:
            image_file = request.FILES['image']
            img = Image.open(image_file)

            # Convert PIL Image to OpenCV image
            img_cv2 = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)

            # Set the Tesseract executable path
            pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

            # Perform OCR using Tesseract
            extracted_text = pytesseract.image_to_string(img_cv2)

            return render(request, 'imgtotext/results.html', {'extracted_text': extracted_text})

        return render(request, self.template_name)

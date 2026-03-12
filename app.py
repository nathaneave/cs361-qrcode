import qrcode, base64
from io import BytesIO
from PIL import Image
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/qrcode")
def generate_qr_code(url: str, brand: str = None):
    qr = qrcode.QRCode(box_size=10, border=2)
    qr.add_data(url)
    qr.make(fit=True)

    qr_code_image = qr.make_image(fill_color="black", back_color="white")
    qr_code_image = qr_code_image.resize((861, 861))

    if brand == "envite":
        background_image_original = Image.open(r"images/template.png")
        background_image = background_image_original.copy()

        paste_box =  (112, 109)
        background_image.paste(qr_code_image, paste_box)

        buffered = BytesIO()
        background_image.save(buffered, format="PNG")
        image_string = base64.b64encode(buffered.getvalue()).decode('utf-8')
    else:
        buffered = BytesIO()
        qr_code_image.save(buffered, format="PNG")
        image_string = base64.b64encode(buffered.getvalue()).decode('utf-8')

    
    return {"base_64_image": image_string}

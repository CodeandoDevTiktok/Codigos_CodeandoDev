#utils.py

from PIL import Image
import io
import base64

def convertir_imagen_a_base64(avatar_data):
    try:
        imagen = Image.open(io.BytesIO(avatar_data))
        buffered = io.BytesIO()
        imagen.save(buffered, format="JPEG")
        return base64.b64encode(buffered.getvalue()).decode()
    except Exception as e:
        print(f"Error al convertir imagen: {e}")
        return None
    


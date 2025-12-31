import requests
from PIL import Image, ImageEnhance, ImageFilter
from io import BytesIO
from config import HF_API_KEY
def generate_image_from_text(prompt):
    """
    Generates an image from a text prompt using the Stable Diffusion API.
    """
    API_URL = "https://router.huggingface.co/hf-inference/models/stabilityai/stable-diffusion-3-medium-diffusers"
    headers = {
        "Authorization": f"Bearer {HF_API_KEY}"
    }
    payload = {"inputs": prompt}
    response = requests. post(API_URL, headers=headers, json=payload)
    if response.status_code == 200:
        image = Image.open(BytesIO(response.content))
        return image
    else:
        raise Exception(
            f"Request failed with status code {response.status_code}: {response.text}"
        ) 
def post_process_image(image):
    """
    Applies post-processing effects to the image.
    """
    enhancer = ImageEnhance. Brightness(image)
    bright_image = enhancer.enhance(1.2)

    enhancer = ImageEnhance.Contrast(bright_image)
    contrast_image = enhancer.enhance(1.3)

    soft_focus_image = contrast_image.filter(
        ImageFilter.GaussianBlur(radius=2)

    )

    return soft_focus_image

def main():
    print("Welcome to the Post-Processing Magic Workshop!")
    print("Type 'exit' to quit. \n")

    while True:
        user_input = input("Enter a description for the image: \n")
        if user_input.lower() == "exit":
            break

        try:
            image = generate_image_from_text(user_input)
            processed_image = post_process_image(image)
            processed_image. show()

        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ =="__main__":
    main()

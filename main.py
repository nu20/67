import requests
from PIL import Image
from io import BytesIO
from config import HF_API_KEY

API_URL = "https://api-inference.huggingface.co/models/CompVis/stable-diffusion-v1-4"


def generate_image_from_text(prompt: str) -> Image.Image:
    """
    Sends a text prompt to Hugging Face Inference API
    and returns a generated PIL Image.
    """
    headers = {
        "Authorization": f"Bearer {HF_API_KEY}"
    }

    payload = {
        "inputs": prompt
    }

    try:
        response = requests.post(
            API_URL,
            headers=headers,
            json=payload,
            timeout=60
        )
        response.raise_for_status()

        # Check if response is image
        if "image" in response.headers.get("Content-Type", ""):
            image = Image.open(BytesIO(response.content))
            return image
        else:
            raise Exception("Response is not an image. Possibly model loading or API error.")

    except requests.exceptions.RequestException as e:
        raise Exception(f"Request failed: {e}")


def main():
    print("🎨 Text-to-Image Generator (Stable Diffusion 1.5)")
    print("Type 'exit' to quit.\n")

    while True:
        prompt = input("Enter image description:\n").strip()

        if prompt.lower() == "exit":
            print("Goodbye 👋")
            break

        print("\n⏳ Generating image...\n")

        try:
            image = generate_image_from_text(prompt)
            image.show()

            save_choice = input("Save image? (yes/no): ").strip().lower()
            if save_choice == "yes":
                filename = input("Enter filename (without extension): ").strip()
                filename = filename or "generated_image"
                filename = "".join(c for c in filename if c.isalnum() or c in "_-")

                image.save(f"{filename}.png")
                print(f"✅ Image saved as {filename}.png\n")

        except Exception as error:
            print(f"❌ Error: {error}\n")

        print("-" * 80 + "\n")


if __name__ == "__main__":
    main()
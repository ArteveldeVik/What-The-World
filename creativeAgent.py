import requests
from PIL import Image
from io import BytesIO
import json

def generate_art(description):
    print("Starting art generation...")
    headers = {
        "Authorization": "Bearer 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",
        "Content-Type": "application/json"
    }
    API_URL = "https://api-inference.huggingface.co/models/nimocodes/FinetunedSDXL"
    payload = {"inputs": description}

    response = requests.post(API_URL, headers=headers, json=payload)
    if response.status_code == 200:
        try:
            # Check if the response is JSON containing an image URL
            response_data = response.json()
            if 'generated_image_url' in response_data:
                image_url = response_data['generated_image_url']
                image_response = requests.get(image_url)
                if image_response.status_code == 200:
                    image = Image.open(BytesIO(image_response.content))
                    image.save("art.png")
                    print("\033[92mArt successfully and saved as 'art.png'\033[0m")  # Green text
                else:
                    print("\033[91mFailed to download image, status code: {}\033[0m".format(image_response.status_code))  # Red text
            else:
                print("\033[91mUnexpected response content: {}\033[0m".format(response_data))  # Red text
        except json.JSONDecodeError:
            # If response is not JSON, it might be an image directly
            image = Image.open(BytesIO(response.content))
            image.save("art.png")
            print("\033[92mArt successfully and saved as 'art.png'\033[0m")  # Green text
    else:
        print("\033[91mFailed to generate art, status code: {}, response: {}\033[0m".format(response.status_code, response.text))  # Red text


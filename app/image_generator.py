
import os
from diffusers import StableDiffusionPipeline
import torch

# Hugging Face API key 
HF_TOKEN = ""  
def generate_image(prompt: str, output_path="outputs/generated_image.png") -> str:
    """
    Generate an image from a prompt using Hugging Face Stable Diffusion.
    """
    os.makedirs("outputs", exist_ok=True)

    # Load Stable Diffusion pipeline
    pipe = StableDiffusionPipeline.from_pretrained(
        "runwayml/stable-diffusion-v1-5",
        use_auth_token=HF_TOKEN,
    )

    # Sending pipeline to CPU or GPU if available
    device = "cuda" if torch.cuda.is_available() else "cpu"
    pipe = pipe.to(device)

    #Generate image with size
    image = pipe(prompt, height=256, width=256).images[0]

    # Save image
    image.save(output_path)
    return output_path
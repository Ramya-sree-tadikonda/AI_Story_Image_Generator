# AI Story + Image Generator

Create magical stories and bring them to life with AI-generated images!  
Enter a story idea, and the app generates both a captivating story and a visual scene.
# How It Works

1. Story Generation – Uses an LLM (Hugging Face Transformers) to generate a story based on your prompt.  
2. Key Scene Extraction – Automatically selects the first 1–2 sentences of the story to create a scene.  
3. Image Generation – Stable Diffusion (Hugging Face Diffusers) transforms the key scene into a vivid AI-generated image.
   
# Flow: 
`User Prompt → LLM generates story → Extract key scene → Stable Diffusion generates image → Display on app`
# Tech Stack & Tools
Python – Programming language  
Streamlit – Web app interface  
Hugging Face Transformers – LLM for story generation  
Hugging Face Diffusers / Stable Diffusion – AI image generation  
Torch (PyTorch) – Handles GPU/CPU computation  
Requests – API calls  

# Libraries Installed
```bash
pip install streamlit
pip install torch
pip install diffusers
pip install transformers
pip install requests

## Run the Streamlit app
streamlit run app/app_interface.py
Browser:
Local URL: http://localhost:8501



"""
from transformers import AutoModelForCausalLM, AutoTokenizer

# Load model(llm like gpt-2) and tokenizer
tokenizer = AutoTokenizer.from_pretrained("gpt2")
model = AutoModelForCausalLM.from_pretrained("gpt2")

def generate_story(prompt: str, max_length=300) -> str:
    inputs = tokenizer.encode(prompt, return_tensors="pt")
    outputs = model.generate(inputs, max_length=max_length, do_sample=True, temperature=0.7)
    story = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return story

"""





import google.generativeai as genai


GEMINI_API_KEY = ""

# ConfigureAPI
genai.configure(api_key=GEMINI_API_KEY)

# Load model
model = genai.GenerativeModel("gemini-1.5-flash")

def generate_story(prompt: str) -> str:
    """
    Generate story using Gemini API.
    """
    response = model.generate_content(prompt)
    return response.text
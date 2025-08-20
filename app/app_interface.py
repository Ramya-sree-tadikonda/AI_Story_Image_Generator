import streamlit as st
from story_generator import generate_story
from image_generator import generate_image

st.set_page_config(page_title="AI Story + Image Generator", layout="wide")
st.title("AI Story + Image Generator")

prompt = st.text_input("Enter your story idea:")

if st.button("Generate"):
    if not prompt.strip():
        st.warning("Please enter a story prompt!")
    else:
        try:
            # story generating
            story = generate_story(prompt)
            st.subheader("Generated Story")
            st.write(story)

            # Extract key scene for image generation
            key_scene = ". ".join(story.split(".")[:2])
            image_prompt = f"{key_scene}, fantasy art, cinematic, detailed, digital painting"

            # Generate image
            img_path = generate_image(image_prompt)
            st.subheader("Generated Image")
            st.image(img_path)

        except Exception as e:
            st.error(f"Error: {e}")

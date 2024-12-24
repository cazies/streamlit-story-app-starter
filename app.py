import streamlit as st
import openai

# Title and description
st.title("AI Story Creation App")
st.write("Create story outlines with AI. Enter your inputs below!")

# Input fields
title = st.text_input("Story Title")
genre = st.selectbox("Genre", ["Adventure", "Fantasy", "Sci-Fi", "Mystery"])
characters = st.text_area("Characters (comma-separated)")

# API Key Input
openai_api_key = st.text_input("Enter your OpenAI API Key", type="password")

# Generate Story
if st.button("Generate Story"):
    if not openai_api_key:
        st.warning("Please enter your OpenAI API key.")
    else:
        openai.api_key = openai_api_key
        prompt = f"Write a story outline for a {genre} story titled '{title}' with these characters: {characters}."
        try:
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=prompt,
                max_tokens=150
            )
            story_outline = response.choices[0].text.strip()
            st.subheader("Your Story Outline")
            st.write(story_outline)
        except Exception as e:
            st.error(f"Error: {e}")

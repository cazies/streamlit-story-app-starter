import streamlit as st
import openai

# Title and description
st.title("AI Story Generator")
st.write("Enter details about your story to generate an outline.")

# Input fields
story_title = st.text_input("Enter the story title")
genre = st.selectbox("Select the genre", ["Adventure", "Fantasy", "Sci-Fi", "Mystery"])
characters = st.text_area("Enter the main characters (comma-separated)")

# OpenAI API Key input
openai_api_key = st.text_input("Enter your OpenAI API Key", type="password")

if st.button("Generate Story Outline"):
    if not openai_api_key:
        st.warning("Please enter your OpenAI API Key.")
    else:
        openai.api_key = openai_api_key
        prompt = f"Write a story outline for a {genre} story titled '{story_title}' with these characters: {characters}."
        try:
            response = openai.chat.completions.create(
                         model="gpt-4",  # Use the specified model
                    messages=[
                        {"role": "user", "content": prompt},
                    ],
                    temperature=0.5,  # Adjust creativity as needed
                     max_tokens=800
                )

            story_outline = response.choices[0].message.content.strip()
            st.subheader("Generated Story Outline")
            st.write(story_outline)
        except Exception as e:
            st.error(f"Error: {e}")

import re
import tempfile
import shutil
import streamlit as st
from embedchain import App
import time

# Define the embedchain_bot function
def embedchain_bot(db_path, api_key):
    return App.from_config(
        config={
            "llm": {"provider": "openai", "config": {"model": "gpt-4-turbo", "temperature": 0.5, "api_key": api_key}},
            "vectordb": {"provider": "chroma", "config": {"dir": db_path}},
            "embedder": {"provider": "openai", "config": {"api_key": api_key}},
        }
    )

def extract_video_id(url):
    """
    Extract the video ID from a YouTube URL using a more comprehensive regex pattern.
    """
    video_id_match = re.search(r"((?<=(v|V)/)|(?<=be/)|(?<=(\?|\&)v=)|(?<=embed/))([\w-]+)", url)
    if video_id_match:
        return video_id_match.group(0)
    return None

def close_app(app):
    """
    Close the embedchain app to release any resources.
    """
    if hasattr(app, 'close'):
        app.close()

# Streamlit App
st.title("Chat with YouTube Video 📺")
st.caption("This app allows you to chat with a YouTube video using the OpenAI API")

openai_access_token = st.text_input("OpenAI API Key", type="password")

if openai_access_token:
    # Manage database setup and cleanup within the session
    if 'db_path' not in st.session_state:
        st.session_state.db_path = tempfile.mkdtemp()
    if 'app' not in st.session_state:
        st.session_state.app = embedchain_bot(st.session_state.db_path, openai_access_token)

    video_url = st.text_input("Enter YouTube Video URL")
    
    if video_url:
        video_id = extract_video_id(video_url)
        if video_id:
            full_video_url = f"https://www.youtube.com/watch?v={video_id}"
            try:
                st.session_state.app.add(full_video_url, data_type="youtube_video")
                st.success(f"Added {full_video_url} to knowledge base!")
                
                prompt = st.text_input("Ask any question about the YouTube Video")
                if prompt:
                    answer = st.session_state.app.chat(prompt)
                    st.write(answer)
            except Exception as e:
                st.error(f"Error processing video: {e}")
        else:
            st.error("Invalid YouTube URL. Please enter a valid URL.")

    # Clean up resources when done
    cleanup_button = st.button("Clean Up Resources")
    if cleanup_button:
        if 'app' in st.session_state:
            close_app(st.session_state.app)
            del st.session_state.app
        if 'db_path' in st.session_state:
            shutil.rmtree(st.session_state.db_path, ignore_errors=True)
            del st.session_state.db_path

from pytube import YouTube
import streamlit as st
from PIL import Image
from io import BytesIO
import requests
import os
import re

# Use HTML to center the title and add padding at the bottom
st.markdown("""
    <h1 style='text-align: center; padding-bottom: 40px;'>TubeFetch</h1>
""", unsafe_allow_html=True)

# Initial text for the input box
video_link = st.text_input("Enter your link here......🥲")

# Function to sanitize filename
def sanitize_filename(filename):
    return re.sub(r'[^a-zA-Z0-9 -]', '', filename)

def download_video(stream, title, suffix):
    sanitized_title = sanitize_filename(title)
    download_path = os.path.join(os.path.expanduser("~"), "Downloads", f"{sanitized_title}_{suffix}.mp4")
    stream.download(output_path=download_path)
    st.success(f"Downloaded :  Check Downloads in your Device")

# Function to download the thumbnail
def download_thumbnail(url, title):
    sanitized_title = sanitize_filename(title)
    response = requests.get(url)
    thumbnail_path = os.path.join(os.path.expanduser("~"), "Downloads", f"{sanitized_title}_thumbnail.jpg")
    with open(thumbnail_path, 'wb') as file:
        file.write(response.content)
    st.success(f"Thumbnail downloaded : Check Downloads in your Device")

# Centered button without key attribute
satyam =False
if st.button('Search Video 🔍 ', type="primary", help="Click to search for video"):
    satyam  = True
    # Check if a valid YouTube video link is provided

# Check if the link is a YouTube link and process it
if ("youtube.com" in video_link or "youtu.be" in video_link):
    try:
        # Fetching YouTube video details
        yt_video = YouTube(video_link)
        st.session_state['yt_video'] = yt_video

        # Displaying video details
        title = yt_video.title
        thumbnail_url = yt_video.thumbnail_url
        st.write(f"**Video Title:** {title}")
      

        # Display the video thumbnail
        thumbnail = Image.open(BytesIO(requests.get(thumbnail_url).content))
        resized_thumbnail = thumbnail.resize((400, 250))  # Adjust the size as needed
        col1, col2, col3 = st.columns([1, 2, 1])
        col2.image(resized_thumbnail, caption="Video Thumbnail", use_column_width=True)


        # Buttons for downloading videos in different resolutions
        col1, col2 = st.columns(2)
        col1.write("**Highest Resolution Video** 1080" )
        if col2.button('⬇️ Download '):
            highest = yt_video.streams.get_highest_resolution()
            download_video(highest, title, "high")

            

        col1, col2 = st.columns(2)
        col1.write("**Medium Resolution Video** 720")
        if col2.button('⬇️ Download'):
            medium = yt_video.streams.get_by_resolution("480p")
            if medium:
                download_video(medium, title, "medium")
            else:
                st.error("Medium resolution not available.")

        col1, col2 = st.columns(2)
        col1.write("**Low Resolution Video** 360")
        if col2.button('⬇️ Download   '):
            lowest = yt_video.streams.get_lowest_resolution()
            download_video(lowest, title, "low")

        col1, col2 = st.columns(2)
        col1.write("**Audio Only**")
        if col2.button('⬇️  Download'):
            audio = yt_video.streams.get_audio_only()
            download_video(audio, title, "audio")

        # Button for downloading the video thumbnail
        col1, col2 = st.columns(2)
        col1.write("**Download Thumbnail**")
        if col2.button('⬇️ Download     '):
            download_thumbnail(thumbnail_url, title)

    except Exception as e:
        st.error(f"An error occurred: {str(e)}")

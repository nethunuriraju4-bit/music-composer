import streamlit as st
from music_backend import generate_music

st.set_page_config(
    page_title="AI Music Generator",
    page_icon="🎵",
    layout="wide"
)

# Styling (Dark UI)
st.markdown("""
<style>

.stApp {
background-color:#0f172a;
}

.title{
font-size:40px;
font-weight:bold;
color:white;
}

.subtitle{
color:#cbd5e1;
font-size:18px;
}

.stButton>button{
background-color:#22c55e;
color:white;
font-size:18px;
border-radius:8px;
padding:10px 20px;
}

</style>
""", unsafe_allow_html=True)

st.markdown('<p class="title">🎵 AI Music Generator</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Create music using AI</p>', unsafe_allow_html=True)

st.write("")

col1, col2 = st.columns([2,1])

with col1:
    prompt = st.text_area(
        "Describe your music",
        placeholder="Example: energetic electronic dance music"
    )

with col2:

    mood = st.selectbox(
        "Mood",
        ["happy","sad","calm","energetic","epic"]
    )

    genre = st.selectbox(
        "Genre",
        ["electronic","lofi","classical","ambient","game music"]
    )

st.write("")

if st.button("Generate Music 🎶"):

    if prompt == "":
        st.warning("Please enter music description")

    else:

        with st.spinner("AI is composing music..."):

            music_file = generate_music(prompt, mood, genre)

        st.success("Music Generated!")

        audio_file = open(music_file, "rb")

        st.audio(audio_file.read(), format="audio/wav")

        with open(music_file, "rb") as file:
            st.download_button(
                "Download Music",
                file,
                "ai_music.wav"
            )
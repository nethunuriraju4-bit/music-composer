import torch
from transformers import MusicgenForConditionalGeneration, AutoProcessor
import scipy.io.wavfile as wavfile
import tempfile

# Load model once
processor = AutoProcessor.from_pretrained("facebook/musicgen-small")
model = MusicgenForConditionalGeneration.from_pretrained("facebook/musicgen-small")

def generate_music(prompt, mood, genre):

    text_prompt = f"{mood} {genre} {prompt}"

    inputs = processor(
        text=[text_prompt],
        padding=True,
        return_tensors="pt"
    )

    audio_values = model.generate(**inputs, max_new_tokens=256)

    sampling_rate = model.config.audio_encoder.sampling_rate

    audio = audio_values[0,0].cpu().numpy()

    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".wav")

    wavfile.write(temp_file.name, sampling_rate, audio)

    return temp_file.name
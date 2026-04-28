import gradio as gr
import torch
from transformers import pipeline

def transcript_audio(audio):
    pipe = pipeline(
        "automatic-speech-recognition",
        model="openai/whisper-tiny.en",
        chunk_length_s=30,
    )

    result = pipe(audio)["text"]
    return result 

audio_input = gr.Audio(sources="upload", type="filepath")  
output_text = gr.Textbox()

iface = gr.Interface(fn=transcript_audio, 
                    inputs=audio_input, outputs=output_text, 
					title="Audio Transcription App",
					description="Upload the audio file")

iface.launch()
import torch
from transformers import pipeline

def get_pipe():
    pipe = pipeline(
        "automatic-speech-recognition",
        model="openai/whisper-tiny.en",
        chunk_length_s=30,
    )

    return pipe


import os
import gradio as gr
from langchain_groq import ChatGroq
from services.llm import product_assistant,get_chain
from services.pipeline import get_pipe

def transcript_audio(audio_file):
    pipe = get_pipe()
    raw_transcript = pipe(audio_file, batch_size=8)["text"]
    adjusted_transcript = product_assistant(raw_transcript)
    chain = get_chain()
    result = chain.invoke({"context": adjusted_transcript})

    # Write the result to a file for downloading
    output_file = "meeting_minutes_and_tasks.txt"
    with open(output_file, "w") as file:
        file.write(result)

    # Return the textual result and the file for download
    return result, output_file

audio_input = gr.Audio(sources="upload", type="filepath", label="Upload your audio file")
output_text = gr.Textbox(label="Meeting Minutes and Tasks")
download_file = gr.File(label="Download the Generated Meeting Minutes and Tasks")

iface = gr.Interface(
    fn=transcript_audio,
    inputs=audio_input,
    outputs=[output_text, download_file],
    title="AI Meeting Assistant",
    description="Upload an audio file of a meeting. This tool will transcribe the audio, fix product-related terminology, and generate meeting minutes along with a list of tasks."
)

iface.launch()
import requests

url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/hTqGqoC-LrW6S79HjuJUkg/trimmed-02.wav"
response = requests.get(url)

audio_file_path = "audio_sample.wav"

if response.status_code==200:
    with open (audio_file_path,"wb") as f:
        f.write(response.content)
        print("Audio file successfully downloaded.")
else:
    print("Error downloading audio file.")


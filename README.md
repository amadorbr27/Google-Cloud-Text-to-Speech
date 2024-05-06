
# Text-to-Speech Synthesis Function Documentation

This documentation covers the use of the `synthesize_text` function, which enables converting text to speech using the Google Cloud Text-to-Speech API.

## Requirements

- Python 3.6 or higher
- `google-cloud-text-to-speech` library
- `google-auth` library
- Google Cloud Platform API credentials (JSON file)

## Setup

1. **Installing Dependencies**: Ensure you have installed the necessary libraries using pip:

   ```bash
   pip install google-cloud-text-to-speech google-auth
   ```

2. **Credentials**: To authenticate the API, you will need a JSON credentials file from Google Cloud. You can set an environment variable for the credentials file location:

   ```bash
   export GOOGLE_APPLICATION_CREDENTIALS="/path/to/your/google-credentials.json"
   ```

   Alternatively, you can load the credentials directly in the code, as shown in the usage example below.

## Function Usage

The `synthesize_text` function converts the provided text into audio, saving the result in an MP3 file. Below is an example of how to use the function:

```python
from google.cloud import texttospeech
from google.oauth2 import service_account

def synthesize_text(text, output_file, credentials_path):
    # Loading credentials
    credentials = service_account.Credentials.from_service_account_file(credentials_path)
    # Initializing the client with credentials
    client = texttospeech.TextToSpeechClient(credentials=credentials)

    # Setting up the text to be synthesized
    synthesis_input = texttospeech.SynthesisInput(text=text)

    # Configuring the voice parameters
    voice = texttospeech.VoiceSelectionParams(
        language_code="pt-BR",  # Language code for Brazilian Portuguese
        ssml_gender=texttospeech.SsmlVoiceGender.MALE  # Male voice
    )

    # Configuring the audio settings
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3  # MP3 audio format
    )

    # Making the request to synthesize speech
    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )

    # Saving the synthesized speech to a file
    with open(output_file, "wb") as out:
        out.write(response.audio_content)
        print(f'Audio saved in "{output_file}"')  # Confirmation message

# Example text to be converted into speech
text = "Example of text to be converted into speech."

# Path for the output audio file
output_file = "converted_text.mp3"

# Path to the JSON credentials file
credentials_path = "client_secret.json"

# Synthesizing the text into speech
synthesize_text(text, output_file, credentials_path)
```

## Function Parameters

- **text (str)**: The text that will be converted into speech.
- **output_file (str)**: The path of the file where the audio will be saved.
- **credentials_path (str)**: The path to the JSON credentials file.

## Output

The result will be an MP3 audio file containing the speech generated from the provided text, saved at the location specified in the `output_file` parameter.

For more information on additional settings and voice options, refer to the [official Google Cloud Text-to-Speech API documentation](https://cloud.google.com/text-to-speech/docs).

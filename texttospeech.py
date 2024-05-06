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
texto = "Example of text to be converted into speech."

# Path for the output audio file
output_file = "converted_text.mp3"

# Path to the JSON credentials file
credentials_path = "client_secret.json"

# Synthesizing the text into speech
synthesize_text(texto, output_file, credentials_path)

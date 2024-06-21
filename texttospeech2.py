from google.cloud import texttospeech
import os


os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "client_secret.json"

# Configuração do cliente
client = texttospeech.TextToSpeechClient()

# Texto que você deseja converter em fala
text = "Olá Mundo!"

# Configuração da síntese de fala
synthesis_input = texttospeech.SynthesisInput(text=text)

# Seleção da voz
voice = texttospeech.VoiceSelectionParams(
    language_code="pt-BR", name="pt-BR-Standard-B"
)
''' 
Vozes Wavenet:
pt-BR-Wavenet-A: Feminina
pt-BR-Wavenet-B: Masculina
pt-BR-Wavenet-C: Feminina
pt-BR-Wavenet-D: Masculina
pt-BR-Wavenet-E: Masculina
Vozes Standard:
pt-BR-Standard-A: Feminina
pt-BR-Standard-B: Masculina
pt-BR-Standard-C: Feminina
pt-BR-Standard-D: Masculina
'''

# Configuração do áudio
audio_config = texttospeech.AudioConfig(
    audio_encoding=texttospeech.AudioEncoding.MP3
)

# Solicitação de síntese
response = client.synthesize_speech(
    input=synthesis_input, voice=voice, audio_config=audio_config
)

# Salvando o áudio em um arquivo
with open("output.mp3", "wb") as out:
    out.write(response.audio_content)
    print("Áudio salvo como output.mp3")

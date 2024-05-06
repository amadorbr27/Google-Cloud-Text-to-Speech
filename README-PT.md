
# Documentação da Função de Sintetização de Texto em Fala

Esta documentação abrange o uso da função `synthesize_text`, que permite converter texto em fala usando a API Google Cloud Text-to-Speech.

## Requisitos

- Python 3.6 ou superior
- Biblioteca `google-cloud-text-to-speech`
- Biblioteca `google-auth`
- Credenciais de API do Google Cloud Platform (arquivo JSON)

## Configuração

1. **Instalação de Dependências**: Certifique-se de ter instalado as bibliotecas necessárias usando o pip:

   ```bash
   pip install google-cloud-text-to-speech google-auth
   ```

2. **Credenciais**: Para autenticar a API, você precisará de um arquivo de credenciais JSON do Google Cloud. Você pode definir uma variável de ambiente para a localização do arquivo de credenciais:

   ```bash
   export GOOGLE_APPLICATION_CREDENTIALS="/path/to/your/google-credentials.json"
   ```

   Ou pode carregar as credenciais diretamente no código, como mostrado no exemplo de uso abaixo.

## Uso da Função

A função `synthesize_text` converte o texto fornecido em áudio, salvando o resultado em um arquivo MP3. Abaixo está um exemplo de como usar a função:

```python
from google.cloud import texttospeech
from google.oauth2 import service_account

def synthesize_text(text, output_file, credentials_path):
    credentials = service_account.Credentials.from_service_account_file(credentials_path)
    client = texttospeech.TextToSpeechClient(credentials=credentials)

    synthesis_input = texttospeech.SynthesisInput(text=text)

    voice = texttospeech.VoiceSelectionParams(
        language_code="pt-BR",
        ssml_gender=texttospeech.SsmlVoiceGender.MALE
    )

    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )

    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )

    with open(output_file, "wb") as out:
        out.write(response.audio_content)
        print(f'Audio salvo em "{output_file}"')

# Exemplo de texto a ser convertido
texto = "Exemplo de texto para ser convertido em fala."

# Caminho do arquivo de saída de áudio
output_file = "exemplo_audio.mp3"

# Caminho para o arquivo JSON de credenciais
credentials_path = "/path/to/your/google-credentials.json"

# Chamada da função
synthesize_text(texto, output_file, credentials_path)
```

## Parâmetros da Função

- **text (str)**: Texto que será convertido em fala.
- **output_file (str)**: Caminho do arquivo onde o áudio será salvo.
- **credentials_path (str)**: Caminho para o arquivo de credenciais JSON.

## Resultado

O resultado será um arquivo de áudio MP3 contendo a fala gerada a partir do texto fornecido, salvo no local especificado no parâmetro `output_file`.

Para mais informações sobre configurações adicionais e opções de voz, consulte a [documentação oficial da API Google Cloud Text-to-Speech](https://cloud.google.com/text-to-speech/docs).

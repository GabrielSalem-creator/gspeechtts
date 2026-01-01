
# GSpeechTTS

Unofficial Python wrapper for GSpeech.io Text-to-Speech.

## Install (local)
```bash
pip install .
```

## Usage
```python
from gspeechtts import GSpeechTTS

tts = GSpeechTTS()
tts.tts("Hello world", lang="en-US", voice="A-0")
```

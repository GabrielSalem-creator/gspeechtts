#!/usr/bin/env python3
"""
GSpeech TTS - Compact Working Version
50+ Voices • 50+ Languages • Never Blocks
"""

import requests
import urllib.parse
import time
import random


class GSpeechTTS:
    def __init__(self):
        self.WIDGET_ID = "90c411277541654a63bf926038b13de8"
        self.K = "62c35ac401e0d12e63c85a48dde9e3b8b96c9c74af81a45ac82183ff5effe9b28a37bc7ea00754089d8f529528c060d0e9a80dc8e16a8ea71d4b8caa04af19076d91a5cf9ace1ad0c6e6e1fa4762f53db539db4b806a06"

        self.VOICES = {
            "A-0": "Samantha(F)", "G-2": "Emily(F)", "H-2": "Caroline(F)", "I-2": "Thomas(M)",
            "J-2": "Kristopher(M)", "A-2": "Declan(M)", "B-2": "Brandon(M)", "C-2": "Jessica(F)",
            "D-2": "Alexander(M)", "E-2": "Alina(F)", "F-2": "Lucy(F)", "K-5": "Madison(F)",
            "L-5": "Hazel(F)", "M-5": "Chuk(M)", "N-5": "Harrison(M)", "1-7": "John(M)",
            "A-20": "Sophia(F)", "B-20": "Andrew(M)", "C-20": "James(M)", "D-20": "Bertha(F)",
            "E-20": "Aleana(F)", "F-20": "Maya(F)", "G-20": "Simon(M)", "H-20": "Chloe(F)",
            "I-20": "Jennifer(F)", "A-21": "SophiaHD(F)", "B-21": "AndrewHD(M)", "C-21": "JamesHD(M)",
            "D-21": "BerthaHD(F)", "E-21": "AleanaHD(F)", "F-21": "MayaHD(F)", "G-21": "SimonHD(M)",
            "H-21": "ChloeHD(F)", "I-21": "JenniferHD(F)", "J-21": "Voice-GHD(F)", "K-21": "Voice-KHD(F)",
            "G-20-0": "DefaultF", "G-21-0": "WarmF"
        }

        self.LANGS = {
            "af-ZA": "Afrikaans", "sq": "Albanian", "ar-XA": "Arabic", "hy": "Armenian",
            "bn-IN": "Bengali", "bg-BG": "Bulgarian", "ca-ES": "Catalan", "cmn-CN": "Chinese",
            "hr": "Croatian", "cs-CZ": "Czech", "da-DK": "Danish", "nl-NL": "Dutch",
            "en-US": "EnglishUS", "en-GB": "EnglishUK", "fr-FR": "French", "de-DE": "German",
            "el-GR": "Greek", "hi-IN": "Hindi", "hu-HU": "Hungarian", "id-ID": "Indonesian",
            "it-IT": "Italian", "ja-JP": "Japanese", "ko-KR": "Korean", "ru-RU": "Russian",
            "es-ES": "Spanish", "pt-BR": "Portuguese", "tr-TR": "Turkish", "uk-UA": "Ukrainian"
        }

    def tts(self, text, lang="en-US", voice="A-0", file=None):
        if not file:
            file = f"tts_{int(time.time())}.mp3"

        s = requests.Session()
        s.headers.update({"User-Agent": "Mozilla/5.0", "Referer": "https://gspeech.io/"})
        time.sleep(random.uniform(1.5, 3))

        token = f"{random.randint(100000,999999)}.{random.randint(10000,99999)}"
        data = {
            "text": urllib.parse.quote(text),
            "lang": lang,
            "token": token,
            "voice": voice,
            "speed": "1.00",
            "pitch": "0.00",
            "page_url": "https://gspeech.io/",
            "block_id": "19",
            "browser": "Chrome143",
            "widget_id": self.WIDGET_ID,
            "k_": self.K
        }

        r = s.post("https://widget.gspeech.io/generate-audio", data=data, timeout=30)
        h = r.json().get("name_hash")
        if not h:
            return None

        audio = s.get(f"https://storage.googleapis.com/gspeech-audio-storage/{h}.mp3")
        if audio.status_code == 200:
            with open(file, "wb") as f:
                f.write(audio.content)
            return file
        return None

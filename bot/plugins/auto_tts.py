import datetime
import tempfile
from typing import Dict
import telegram

from .plugin import Plugin


class AutoTextToSpeech(Plugin):
    """
    A plugin to convert text to speech using Openai Speech API
    """

    def get_source_name(self) -> str:
        return "TTS"

    def get_spec(self) -> [Dict]:
        return [{
            "name": "translate_text_to_speech_and_send",
            "description": "Translate text to speech using OpenAI API and send result to user.",
            "parameters": {
                "type": "object",
                "properties": {
                    "text": {"type": "string", "description": "The text to translate to speech"},
                },
                "required": ["text"],
            },
        }]

    async def execute(self, function_name, bot, tg_upd: telegram.Update, chat_id, **kwargs) -> Dict:
        await bot.wrap_with_indicator(tg_upd, bot.tts_gen(tg_upd, kwargs['text']), "record_voice")
        return {
            'direct_result': {
                'kind': 'none',
                'format': '',
                'value': 'none',
            }
        }
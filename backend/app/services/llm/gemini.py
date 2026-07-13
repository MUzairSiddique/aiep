from backend.app.services.llm.base import BaseLLMProvider


class GeminiProvider(BaseLLMProvider):

    def generate(self, prompt: str) -> str:
        """
        Temporary implementation.

        In the next sprint this will call Gemini API.
        """

        return f"[Gemini] {prompt}"
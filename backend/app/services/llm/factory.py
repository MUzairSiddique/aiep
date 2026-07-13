from backend.app.core.config import settings

from backend.app.services.llm.gemini import GeminiProvider


class LLMFactory:

    @staticmethod
    def create():
        """
        Return the configured LLM provider.
        """

        if settings.llm_provider.lower() == "gemini":
            return GeminiProvider()

        raise ValueError(
            f"Unsupported provider: {settings.llm_provider}"
        )
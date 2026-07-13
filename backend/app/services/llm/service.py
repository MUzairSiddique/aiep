from backend.app.services.llm.factory import LLMFactory


class LLMService:

    def __init__(self):
        self.provider = LLMFactory.create()

    def generate(self, prompt: str) -> str:
        return self.provider.generate(prompt)
from abc import ABC, abstractmethod


class BaseLLMProvider(ABC):
    """
    Every LLM provider in AIEP must inherit this class.
    """

    @abstractmethod
    def generate(self, prompt: str) -> str:
        """
        Generate a response from the LLM.
        """
        pass
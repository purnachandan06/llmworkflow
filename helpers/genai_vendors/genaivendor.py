from abc import ABC, abstractmethod

class GenAiVendor(ABC):
    """
    Class to define the basic structure for GenAiVendor workflows implementation
    """
    def __init__(self):
        pass

    @abstractmethod
    def chat(self, message: str, model: str):
        """
        Method to perform chat request
        """
        pass

    @abstractmethod
    def embeddings(self, message: str, model: str):
        """
        Method to perform embeddings request
        """
        pass
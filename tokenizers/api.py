"""
Interface for Tokenizers
"""

from abc import ABC, abstractmethod


class TokenizersInterface(ABC):

    @abstractmethod
    def tokenize(self, s):
        """
        :return: the list of tokens in s
        """
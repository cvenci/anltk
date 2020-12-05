"""
Regular expression Tokenizer

This module use regular expression to tokenize a string
"""

import re

from tokenizers.api import TokenizersInterface


class RegexTokenizer(TokenizersInterface):
    """
    Class of tokenizers that use regular expressions to slice the entry string,
    the regex could either specify the separators between tokens or the tokens themselves
    """

    def __init__(self, pattern, sep=False, no_empty=True):
        self._pattern = pattern
        self._sep = sep
        self._no_empty = no_empty
        self._regex = None

    def _is_regex(self):
        # Converting pattern to a regex object
        if self._regex is None:
            re.compile(self._pattern)

    def tokenize(self, s):
        self._is_regex()
        if self._sep:
            if self._no_empty:
                return [token for token in self._regex.split(s) if token]
            else:
                return self._regex.split(s)

        else:
            return self._regex.findall(s)
from typing import List

def tokenize(text: str) -> List[str]:
    """
    Tokenize a text into words.
    
    Args:
        text: The text to tokenize.

    Returns:
        A list of word token.
    """
    return text.split()
# src/preprocess.py

import re
import string

def preprocess(text : str) -> str:
    """
    Preprocess the text data by lowecasing,
    removing special characters, digits, and
    extra spaces.

    Args:
        text (str): input text data

    Returns:
        str: preprocessed text data
    """

    # Lowercasing the text
    text = text.lower()

    # Removing sepcial chars, keep only a-z, 0-9, and some special chars
    text = re.sub(r'[^a-z0-9\s\.\,\!\?]', '', text)

    # Replace multiple spaces with a single space
    text = re.sub(r'\s+', ' ', text)

    return text
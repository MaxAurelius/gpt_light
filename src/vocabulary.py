from typing import List, Dict
from collections import Counter

def build_vocabulary(tokenized_text : List[str], min_freq : int = 1) -> Dict[str, int]:
    """
    Build a vocabulary from token to unique indices.
    
    Args:
        tokenized_text (List[str]): list of tokenized text data
        min_freq (int): minimum frequency of words to be included in the vocabulary

    Returns:
        Dict[str, int]: a dictionary mapping token to unique indices
    """

    token_counts = Counter(tokenized_text)
    
    # filter tokens by minimum frequency
    tokens = [token for token, freq in token_counts.items() if freq >= min_freq]

    # add special tokens
    vocab = {"<PAD>": 0, "<UNK>": 1}

    # add the rests of the tokens to the vocabulary, assign idx
    for idx, token in enumerate(tokens, 2):
        vocab[token] = idx

    return vocab
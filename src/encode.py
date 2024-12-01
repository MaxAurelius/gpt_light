from typing import List
from typing import Dict

def encode_tokens(tokenized_text: List[str], vocab: Dict[str, int]) -> List[int]:
    """
    Encode a list of tokens into a list of indices.
    
    Args:
        tokenized_text (List[str]): list of tokenized text data
        vocab (Dict[str, int]): vocabulary mapping token to unique indices

    Returns:
        List[int]: a list of indices
    """
    return [vocab.get(token, vocab['<UNK>']) for token in tokenized_text]

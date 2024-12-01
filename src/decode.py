from typing import List
from typing import Dict

def decode_tokens(encoded_text: List[int], vocab: Dict[str, int]) -> List[str]:
    """
    Decode a list of indices into a list of token.
    
    Args:
        encoded_text (List[int]): list of encoded indices
        vocab (Dict[str, int]): vocabulary mapping token to unique indices

    Returns:
        List[str]: a list of token
    """
    
    # invert the vocabulary
    inv_vobab = {idx : token for token, idx in vocab.items()}
    return [inv_vobab.get(idx, '<UNK>') for idx in encoded_text]
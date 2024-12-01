import numpy as np
from typing import List
from typing import Tuple

def create_sequence(encoded_text: List[str], seq_length: int) -> Tuple[np.array, np.array]:
    """
    Create input otput pairs for training.

    Args:
        encoded_text (List[str]): list of encoded text data
        seq_length (int): length of the sequence

    Returns:
        Tuple[np.array, np.array]: a tuple of input and output pairs
    """
    inputs = []
    targets = []
    for i in range(len(encoded_text) - seq_length):
        inputs.append(encoded_text[i:i+seq_length])
        targets.append(encoded_text[i+1:i+seq_length+1])
    return np.array(inputs), np.array(targets)
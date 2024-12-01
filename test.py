# import all modules
from preprocess import preprocess
from tokenize import tokenize
from vocabulary import build_vocabulary
from encode import encode_tokens
from decode import decode_tokens
from sequence import create_sequence

test_str = "Hello, World! This is a test string. Let's see how well the encoding works with a longer sentence. This test string includes some repeating words. Repeating words help test the encoding process."

print("Original text:")
print(test_str)

print("\nPreprocessing the text...")
preprocess_str = preprocess(test_str)
print(preprocess_str)

print("\nTokenizing the preprocessed text...")
tokenized_text = tokenize(preprocess_str)
print(tokenized_text)

print("\nBuilding the vocabulary from tokenized text...")
vocab = build_vocabulary(tokenized_text)
print(vocab)

print("\nEncoding the tokenized text...")
encoded_text = encode_tokens(tokenized_text, vocab)
print(encoded_text)

print("\nDecoding the encoded text...")
decoded_text = decode_tokens(encoded_text, vocab)
print(decoded_text)

print("\nCreate sequences...")
inputs, targets = create_sequence(encoded_text, 5)

print("Inputs:\n", inputs)
print("Targets:\n", targets)

print(inputs[0], " -> ", targets[0])
from engine import *
text = 'BEEP'
tree_root = build_tree(text)
huffman_codes = get_codes(tree_root)

print(f'original text: {text}')
print(f'huffman codes: {huffman_codes}')

encoded_text = "".join([huffman_codes[char] for char in text])
print(f'encoded text: {encoded_text}')
import heapq
from collections import Counter

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_tree(text):
    frequencies = Counter(text)

    heap = [Node(char, freq) for char, freq in frequencies.items()]

    heapq.heapify(heap)
    while len(heap) > 1:
        node1 = heapq.heappop(heap)
        node2 = heapq.heappop(heap)

        merged = Node(None, node1.freq + node2.freq)
        merged.left = node1
        merged.right = node2

        heapq.heappush(heap, merged)

    return heap[0]

def get_codes(node, current_code = "", codes = {}):
    if node is None:
        return
    if node.char is not None:
        codes[node.char] = current_code

    get_codes(node.left, current_code + "0", codes)
    get_codes(node.right, current_code + "1", codes)

    return codes
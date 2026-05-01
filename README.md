# Huffman Archiver (BitSqueeze) 📂

**BitSqueeze** is a high-performance, lossless data compression utility engineered to implement the classic **Huffman Coding** algorithm. The project provides an end-to-end pipeline for converting standard datasets into optimized binary archives, focusing on information theory and bit-level data manipulation.



## 🏗️ System Architecture & Engineering
The architecture is modular, separating the analytical engine from the I/O layer to ensure maintainability and high processing speed.

### 1. Frequency Analysis & Modeling
The system initiates a single-pass scan of the input file to generate a frequency distribution map. By utilizing a hash map (dictionary) for $O(1)$ lookups, the engine identifies the statistical weight of every character in the source data.

### 2. Min-Heap & Binary Tree Construction
To ensure optimal compression, the algorithm constructs a Huffman tree from the bottom up.
* **Priority Queueing:** A Min-Heap (`heapq`) is utilized to maintain nodes ordered by frequency.
* **Greedy Merging:** The algorithm iteratively extracts the two nodes with the lowest frequencies and merges them into a parent node. This process continues until a singular root node remains, forming the foundation of the optimal prefix-free code.

### 3. Tree Serialization & Metadata
A critical challenge in decompression is reconstructing the tree without external data. BitSqueeze addresses this by serializing the tree structure as metadata within the archive's header. This makes the archive **self-contained**, allowing the decompression module to reconstruct the exact pathing required to retrieve the original data.

### 4. Bit-Packing Engine
Standard file systems operate at the byte level, while Huffman codes operate at the bit level. The engine utilizes custom **bitwise operations** (`<<`, `&`, `|`) to pack variable-length Huffman codes into 8-bit sequences (bytes). This ensures that the final file is as dense as mathematically possible.

## ⚙️ Technical Complexity
* **Time Complexity:** * Compression: $O(n \log k)$ where $n$ is the file size and $k$ is the alphabet size.
    * Decompression: $O(n)$, allowing for rapid restoration.
* **Space Complexity:** $O(k)$ to maintain the character weight map and tree structure.

## 🧪 Rigorous Verification & Testing
The project implements a comprehensive unit testing suite to guarantee data integrity. Automated tests verify that the checksum of the decompressed output matches the source file identically.

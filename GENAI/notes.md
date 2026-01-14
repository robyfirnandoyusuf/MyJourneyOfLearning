
## 2. Transformers
Transformer itu backbone nya GENAI, transformer punya 2 block:
a. self attention, yang gunanya untuk mempertimbangkan pentingnya tiap token sehingga membantu model untuk memahami hubungan antar token dalam input
contoh:
Kalimat “The cat sat on the mat because it was tired.”
→ Model perlu tahu bahwa “it” mengacu ke “cat”, bukan “mat”.
Self-attention membantu menemukan hubungan ini tanpa urutan berulang seperti pada RNN.

b. feed forward, output dari self attention akan di masukkan ke dalam feed forward untuk menyempurnakan kembali representasi dari urutan input


Tokenizing Teks
Tokenizing itu penting dalam NLP dan GenAI, karena dengan model tidak bisa menerima teks secara langsung maka diperlukan input data numerik.proses untuk mengubah teks menjadi angka ini disebut Tokenizing

ada 3 pendekatan umumnya:
    
    1. Character level: 
    2. Word level
    3. Subword level

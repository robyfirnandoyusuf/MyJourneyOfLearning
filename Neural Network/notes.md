# Neural Network dari Nol: Dari Dataset sampai `model.compile()`

Dokumen ini berisi konsep neural network paling dasar. Alurnya: mulai dari **data mentah**, lewat **forward → loss → backprop → gradient descent**, sampai **training, evaluasi (confusion matrix)**, dan terakhir versi **framework Keras yang di-`compile`**. Semua angka di sini sudah dihitung beneran, bukan kira-kira.

---

## 0. Peta Besar (baca ini dulu)

Semua machine learning supervised - dari neuron tunggal sampai LLM - mengikuti 8 langkah yang sama:

```
1. DATASET        →  kumpulan (input, jawaban benar)
2. FORWARD PASS   →  model menebak (prediksi)
3. LOSS           →  ukur seberapa salah tebakannya
4. BACKPROP       →  cari "siapa penyebab error" (gradient)
5. GRADIENT DESC  →  geser weight sedikit ke arah yang benar
6. ULANGI 2–5     →  ribuan kali sampai loss kecil  (= TRAINING)
7. TESTING        →  coba ke data baru yang belum pernah dilihat
8. EVALUATION     →  confusion matrix, accuracy, precision, recall, F1
```

Yang berubah antar model cuma **skala** (1 neuron vs miliaran) dan **arsitektur** (cara neuron disusun). Mesinnya identik. Kalau sudah paham 8 langkah ini di neuron tunggal, artinya kita sudah pegang fondasinya.

---

## 1. Tiga Istilah yang Wajib Dibedakan

Ini sumber kebingungan nomor satu pemula. Bedakan dengan tegas:

| Simbol | Nama | Siapa yang kasih | Contoh |
|---|---|---|---|
| $x$ | **input** / fitur | dataset | jam belajar = 2 |
| $y$ | **label** / target / ground truth / jawaban asli | dataset | lulus? = 0 (tidak) |
| $\hat{y}$ | **prediksi** ("y-hat") | model | 0.73 |

Poin kunci: **$x$ dan $y$ dua-duanya datang dari dataset.** Dataset itu seperti buku soal yang sudah ada kunci jawabannya. $x$ adalah soalnya, $y$ adalah kunci jawabannya. Model cuma menghasilkan $\hat{y}$ - tebakan dia atas soal itu. Belajar = membuat $\hat{y}$ makin dekat ke $y$.

**Analogi guru–murid:**
- Dataset = soal + kunci jawaban.
- Neural network = murid yang menebak.
- Loss = nilai merah dari guru ("kamu salah sebesar ini").
- Backpropagation = guru menunjukkan bagian mana yang salah.
- Gradient descent = murid memperbaiki caranya.

Kalau tidak ada $y$ (kunci jawaban), model tidak tahu dia benar atau salah - itu sebabnya supervised learning **butuh** label.

---

## 2. Dataset Konkret Kita

Kita pakai kasus klasik dan kecil: **memprediksi apakah seorang siswa lulus berdasarkan jam belajar.** Aturan dunia nyatanya: makin lama belajar, makin besar peluang lulus.

ML tidak suka teks, jadi "Lulus/Tidak" diubah jadi angka (0 = tidak lulus, 1 = lulus):

| Jam belajar ($x$) | Lulus? ($y$) |
|---|---|
| 1 | 0 |
| 2 | 0 |
| 3 | 0 |
| 6 | 1 |
| 7 | 1 |
| 8 | 1 |

Cuma 6 baris - sengaja kecil supaya tiap angka bisa dilacak dan dipelajari. Pola yang kita harap ditemukan model: ada semacam "ambang" di sekitar 4–5 jam; di bawah itu gagal, di atas itu lulus.

---

## 3. Anatomi Satu Neuron

Satu neuron melakukan dua hal:

**(a) Kombinasi linear** - kalikan input dengan weight, tambahkan bias:

$$z = w\,x + b$$

- $w$ (weight) = seberapa **penting** input ini. Weight besar → input sangat berpengaruh.
- $b$ (bias) = pergeseran/ambang. Membuat neuron bisa "miring", tidak harus lewat titik nol.

**(b) Activation function** - tekan $z$ ke bentuk yang berguna. Kita pakai **sigmoid**, yang memetakan angka berapa pun ke rentang 0–1 (cocok untuk probabilitas):

$$\hat{y} = \sigma(z) = \frac{1}{1 + e^{-z}}$$

Bentuk sigmoid: huruf S. $\sigma(0)=0.5$, makin besar $z$ makin mendekati 1, makin kecil $z$ makin mendekati 0. Jadi output neuron bisa dibaca sebagai "peluang lulus".

---

## 4. STEP 1 - Forward Propagation (model menebak)

Awalnya neuron belum pintar. Weight kita isi random, bias nol:

$$w = 0.5, \qquad b = 0$$

Ambil **satu** data dulu untuk dilacak penuh: $x = 2$, $y = 0$ (belajar 2 jam, kenyataannya **tidak** lulus).

**Hitung $z$:**
$$z = (0.5)(2) + 0 = 1.0$$

**Lewatkan sigmoid:**
$$\hat{y} = \sigma(1.0) = \frac{1}{1 + e^{-1}} = 0.73106$$

Neuron berkata: *"Saya 73.1% yakin siswa ini lulus."* Padahal kenyataannya $y=0$ (gagal). Jadi neuron **salah** - tebakannya terlalu tinggi.

---

## 5. STEP 2 - Loss (ukur seberapa salah)

Kita pakai **Mean Squared Error** (selisih dikuadratkan):

$$L = (y - \hat{y})^2 = (0 - 0.73106)^2 = 0.53445$$

Loss = ukuran "kebodohan" model saat ini. Makin besar, makin salah. Tujuan seluruh training cuma satu: **buat $L$ sekecil mungkin.** Mengkuadratkan dipakai supaya error positif dan negatif tidak saling menghapus, dan error besar dihukum lebih berat.

---

## 6. STEP 3 - Backpropagation (cari penyebab error)

Pertanyaan inti: **"weight harus dinaikkan atau diturunkan, dan seberapa banyak?"** Jawabannya = **gradient** $\frac{\partial L}{\partial w}$, yang artinya: *"kalau $w$ diubah sedikit, $L$ naik atau turun seberapa?"*

**Intuisi dulu (tanpa rumus):** model bilang peluang lulus 73%, padahal harusnya 0. Tebakan terlalu tinggi. Dari $z = wx + b$, kalau $w$ **diperkecil**, maka $z$ mengecil, sigmoid turun, prediksi mendekati 0. Jadi tebakan kita: **weight harus turun.** Backprop tinggal membuktikan ini secara matematis dan memberi angka pastinya.

**Kenapa butuh chain rule?** Karena $L$ tidak bergantung langsung ke $w$. Rantainya:

$$w \;\rightarrow\; z \;\rightarrow\; \hat{y} \;\rightarrow\; L$$

Untuk tahu efek $w$ ke $L$, kita kalikan efek tiap mata rantai (inilah kenapa namanya **back**prop - kita jalan mundur dari $L$ ke $w$):

$$\frac{\partial L}{\partial w} = \underbrace{\frac{\partial L}{\partial \hat{y}}}_{\text{(1)}} \cdot \underbrace{\frac{\partial \hat{y}}{\partial z}}_{\text{(2)}} \cdot \underbrace{\frac{\partial z}{\partial w}}_{\text{(3)}}$$

Hitung tiap potongan dengan angka kita ($y=0$, $\hat{y}=0.73106$, $x=2$):

**(1)** Turunan MSE terhadap prediksi:
$$\frac{\partial L}{\partial \hat{y}} = -2(y - \hat{y}) = -2(0 - 0.73106) = 1.46212$$

**(2)** Turunan sigmoid (rumus rapi: $\sigma'(z) = \hat{y}(1-\hat{y})$):
$$\frac{\partial \hat{y}}{\partial z} = 0.73106 \times (1 - 0.73106) = 0.19661$$

**(3)** Turunan $z = wx+b$ terhadap $w$:
$$\frac{\partial z}{\partial w} = x = 2$$

**Kalikan semua:**
$$\frac{\partial L}{\partial w} = 1.46212 \times 0.19661 \times 2 = 0.57494$$

Hasilnya **positif**. Artinya: menaikkan $w$ akan **menaikkan** loss (makin buruk). Maka $w$ harus **diturunkan** - persis seperti tebakan intuisi tadi. ✅

Bias dihitung sama, bedanya $\frac{\partial z}{\partial b} = 1$:
$$\frac{\partial L}{\partial b} = 1.46212 \times 0.19661 \times 1 = 0.28747$$

> Catatan kecil: jangan keliru, $\frac{\partial z}{\partial w} = x$, jadi gradient **harus dikalikan $x$**. Kalau lupa, angkanya akan beda (mis. 0.287 vs 0.575 yang benar di sini).

---

## 7. STEP 4 - Gradient Descent (perbaiki weight)

Sekarang gunakan gradient untuk meng-update. Aturannya: **geser parameter berlawanan arah gradient**, sebanyak *learning rate* ($\eta$):

$$w_{\text{baru}} = w - \eta \frac{\partial L}{\partial w}, \qquad b_{\text{baru}} = b - \eta \frac{\partial L}{\partial b}$$

Pakai $\eta = 0.1$:

$$w_{\text{baru}} = 0.5 - 0.1 \times 0.57494 = 0.44251$$
$$b_{\text{baru}} = 0.0 - 0.1 \times 0.28747 = -0.02875$$

Weight **turun** (0.5 → 0.443) - sesuai harapan, karena kita ingin output untuk data ini lebih kecil. Lakukan ini berulang untuk semua data, dan neuron pelan-pelan menemukan $w$ dan $b$ terbaik.

> **Backprop ≠ gradient descent.** Backprop = *menghitung* gradient (langkah 6). Gradient descent = *memakai* gradient untuk update (langkah 7). Dua hal berbeda yang sering disamakan.

**Peran learning rate ($\eta$):** seberapa besar langkah tiap update.
- Terlalu besar → lompat-lompat, loss bisa naik turun liar, tidak konvergen.
- Terlalu kecil → belajar sangat lambat.

---

## 8. STEP 5 - Kode Python dari Nol (tanpa framework)

Sekarang seluruh konsep di atas dalam kode murni - tanpa TensorFlow/PyTorch - supaya mekanismenya kelihatan telanjang. Loop-nya: forward → loss → backprop → update, diulang tiap epoch untuk seluruh dataset.

```python
import math

# ========== DATASET ==========
X = [1, 2, 3, 6, 7, 8]   # jam belajar (input)
Y = [0, 0, 0, 1, 1, 1]   # lulus? (label)

# ========== PARAMETER AWAL ==========
w  = 0.5    # weight (random kecil)
b  = 0.0    # bias
lr = 0.1    # learning rate (eta)

def sigmoid(z):
    return 1 / (1 + math.exp(-z))

# ========== TRAINING ==========
for epoch in range(2001):
    total_loss = 0

    for x, y in zip(X, Y):
        # --- FORWARD ---
        z = (w * x) + b
        y_pred = sigmoid(z)

        # --- LOSS (MSE) ---
        total_loss += (y - y_pred) ** 2

        # --- BACKPROP (chain rule) ---
        dL_dypred = -2 * (y - y_pred)        # (1) dL/dŷ
        dypred_dz = y_pred * (1 - y_pred)    # (2) dŷ/dz  (turunan sigmoid)
        dz_dw     = x                        # (3) dz/dw
        dz_db     = 1                        #     dz/db

        dL_dw = dL_dypred * dypred_dz * dz_dw
        dL_db = dL_dypred * dypred_dz * dz_db

        # --- GRADIENT DESCENT (update) ---
        w = w - lr * dL_dw
        b = b - lr * dL_db

    if epoch in (0, 50, 100, 200, 500, 1000, 2000):
        print(f"Epoch {epoch:>4} | loss={total_loss:.4f} | w={w:.4f} | b={b:.4f}")
```

**Output asli saat dijalankan:**

```text
Epoch    0 | loss=1.5094 | w=0.3626 | b=-0.0809
Epoch   50 | loss=0.4053 | w=0.5861 | b=-2.0005
Epoch  100 | loss=0.2267 | w=0.7482 | b=-2.8815
Epoch  200 | loss=0.1208 | w=0.9356 | b=-3.8390
Epoch  500 | loss=0.0508 | w=1.2114 | b=-5.1764
Epoch 1000 | loss=0.0259 | w=1.4358 | b=-6.2289
Epoch 2000 | loss=0.0130 | w=1.6689 | b=-7.3046
```

Loss turun dari 1.51 → 0.013. **Neuron benar-benar belajar.**

### Cara membaca hasilnya

- **$w$ jadi besar (≈1.67):** "jam belajar sangat berpengaruh terhadap kelulusan."
- **$b$ jadi negatif (≈−7.3):** ada ambang. Sigmoid baru "menyala" ke arah lulus setelah $wx$ cukup besar untuk mengalahkan bias negatif ini.
- **Titik ambang (di mana peluang = 0.5)** ada saat $z=0$, yaitu $x = -b/w = 7.3046/1.6689 \approx 4.4$ jam. Artinya model menyimpulkan sendiri: belajar di bawah ~4.4 jam cenderung gagal, di atasnya cenderung lulus.

Yang luar biasa: **kita tidak pernah menuliskan aturan "4.4 jam" itu.** Neuron menemukannya sendiri lewat error → backprop → update, ribuan kali.

---

## 9. STEP 6 - Testing / Inference (coba ke data baru)

Training selesai, $w$ dan $b$ sudah bagus. Sekarang pakai untuk memprediksi data yang **belum pernah dilihat** - ini disebut inference. Tidak ada backprop di sini, cuma forward pass.

```python
print("=== TESTING ===")
for x in [1, 2, 4, 5, 6, 8, 10]:
    p = sigmoid((w * x) + b)
    print(f"Jam belajar: {x:>2} | peluang lulus: {p:.4f}")
```

**Output asli:**

```text
Jam belajar:  1 | peluang lulus: 0.0036
Jam belajar:  2 | peluang lulus: 0.0186
Jam belajar:  4 | peluang lulus: 0.3478
Jam belajar:  5 | peluang lulus: 0.7389
Jam belajar:  6 | peluang lulus: 0.9376
Jam belajar:  8 | peluang lulus: 0.9976
Jam belajar: 10 | peluang lulus: 0.9999
```

Persis seperti diharapkan - kurva S yang mulus: 4 jam masih ragu (0.35), 5 jam sudah condong lulus (0.74), 8 jam hampir pasti (0.998).

---

## 10. STEP 7 & 8 - Threshold, Confusion Matrix, dan Metrics

Output model berupa probabilitas (0.74, 0.35, ...). Untuk klasifikasi kita butuh keputusan tegas 0/1, jadi pasang **threshold** (umumnya 0.5):

$$\hat{y} \ge 0.5 \rightarrow 1 \text{ (lulus)}, \qquad \hat{y} < 0.5 \rightarrow 0 \text{ (gagal)}$$

Lalu bandingkan prediksi dengan jawaban asli. Empat kemungkinan tiap data:

| | Prediksi 0 | Prediksi 1 |
|---|---|---|
| **Asli 0** | **TN** (benar bilang gagal) | **FP** (false alarm: bilang lulus, padahal gagal) |
| **Asli 1** | **FN** (kelewatan: bilang gagal, padahal lulus) | **TP** (benar bilang lulus) |

Susunan ini disebut **confusion matrix**.

```python
print("=== EVALUATION ===")
X_test = [1, 4, 5, 9]      # data uji baru
Y_true = [0, 0, 1, 1]      # kunci jawabannya

TP = TN = FP = FN = 0
for x, y in zip(X_test, Y_true):
    y_pred = 1 if sigmoid((w * x) + b) >= 0.5 else 0
    if   y == 1 and y_pred == 1: TP += 1
    elif y == 0 and y_pred == 0: TN += 1
    elif y == 0 and y_pred == 1: FP += 1
    elif y == 1 and y_pred == 0: FN += 1

accuracy  = (TP + TN) / (TP + TN + FP + FN)
precision = TP / (TP + FP + 1e-8)
recall    = TP / (TP + FN + 1e-8)
f1        = 2 * precision * recall / (precision + recall + 1e-8)

print(f"TP={TP} TN={TN} FP={FP} FN={FN}")
print(f"Accuracy : {accuracy:.4f}")
print(f"Precision: {precision:.4f}")
print(f"Recall   : {recall:.4f}")
print(f"F1 Score : {f1:.4f}")
```

**Output asli:**

```text
TP=2 TN=2 FP=0 FN=0
Accuracy : 1.0000
Precision: 1.0000
Recall   : 1.0000
F1 Score : 1.0000
```

### Apa arti tiap metric

- **Accuracy** $= \dfrac{TP+TN}{\text{total}}$ - berapa persen prediksi yang benar secara keseluruhan.
- **Precision** $= \dfrac{TP}{TP+FP}$ - *"dari semua yang model bilang lulus, berapa yang benar lulus?"* (mengukur false alarm).
- **Recall** $= \dfrac{TP}{TP+FN}$ - *"dari semua yang benar-benar lulus, berapa yang berhasil ditangkap model?"* (mengukur yang kelewatan).
- **F1** = rata-rata harmonik precision & recall - satu angka penyeimbang keduanya.

**Kenapa tidak cukup accuracy saja?** Bayangkan 99 siswa gagal, 1 lulus. Model yang asal selalu menjawab "gagal" dapat accuracy 99% - padahal tidak berguna (recall untuk kelas "lulus" = 0). Pada data tidak seimbang, precision/recall/F1 jauh lebih jujur.

---

## 11. Versi Framework: `model.compile()` (Keras)

Semua yang kita tulis manual di atas, di dunia nyata diserahkan ke framework. Inilah neuron yang sama persis, ditulis dalam **Keras (TensorFlow)** - dan di sinilah kata **"compile"** muncul.

```python
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

# ========== 1. DATASET ==========
X = np.array([1, 2, 3, 6, 7, 8], dtype=float)
Y = np.array([0, 0, 0, 1, 1, 1], dtype=float)

# ========== 2. ARSITEKTUR MODEL ==========
# 1 neuron, 1 input, activation sigmoid  -> identik dengan neuron manual kita
model = keras.Sequential([
    layers.Dense(units=1, activation="sigmoid", input_shape=(1,))
])

# ========== 3. COMPILE ==========
# Di sinilah kita "merakit" mesin belajarnya:
model.compile(
    optimizer=keras.optimizers.SGD(learning_rate=0.1),  # gradient descent
    loss="mse",                                          # fungsi loss (= (y-ŷ)²)
    metrics=["accuracy"]                                 # apa yang dipantau
)

# ========== 4. TRAINING ==========
model.fit(X, Y, epochs=2000, verbose=0)   # otomatis: forward → loss → backprop → update

# ========== 5. INFERENCE & EVALUASI ==========
print(model.predict(np.array([[1], [4], [5], [8]])))   # probabilitas
loss, acc = model.evaluate(X, Y, verbose=0)
print(f"loss={loss:.4f}  accuracy={acc:.4f}")

w, b = model.layers[0].get_weights()
print("weight:", w.ravel(), "bias:", b)   # akan mirip w≈1.6, b≈-7
```

### `compile()` itu sebenarnya apa?

`model.compile()` **bukan** "compile" seperti mengkompilasi bahasa C. Di Keras, compile = **merakit konfigurasi training** sebelum model dilatih. Kita memberi tahu model tiga hal yang tadi kita tulis manual:

| Argumen `compile` | Padanannya di kode manual kita |
|---|---|
| `optimizer=SGD(lr=0.1)` | aturan update `w = w - lr * dL_dw` (Step 7) |
| `loss="mse"` | rumus `(y - y_pred) ** 2` (Step 5) |
| `metrics=["accuracy"]` | perhitungan accuracy kita (Step 8) |

Setelah `compile`, barulah `model.fit()` menjalankan loop training - dan di balik layar `fit` melakukan **persis** forward → loss → backprop → gradient descent yang kita tulis tangan, hanya saja:

- gradient dihitung otomatis (**autodiff** / `GradientTape`), tidak perlu turunkan chain rule sendiri,
- jauh lebih cepat (vektorisasi + GPU),
- skalabel ke jutaan neuron.

Konsep fundamentalnya **tidak berubah sama sekali** dari neuron tangan kita.

---

## 12. Jembatan ke Deep Learning

Yang barusan kita bangun, secara teknis, adalah **logistic regression / single-neuron classifier** - fondasi yang sama yang menyangga semua model besar. Naik level tinggal menyusun neuron:

- **Multi-layer (MLP):** banyak neuron bertumpuk; backprop berjalan mundur lewat tiap layer dengan chain rule yang lebih panjang.
- **CNN, RNN, Transformer, LLM:** arsitektur berbeda untuk gambar / urutan / bahasa - tapi tetap *forward → loss → backprop → optimize → evaluate*.

Beberapa hal yang biasanya "klik" setelah paham ini:
- **Kenapa butuh GPU?** Jutaan operasi gradient sekaligus → butuh paralelisme matriks.
- **Vanishing gradient:** turunan sigmoid maksimal cuma 0.25; dikalikan berlapis-lapis lewat banyak layer, gradient mengecil drastis → layer awal nyaris berhenti belajar.
- **Kenapa ReLU populer?** Turunannya 1 (untuk input positif), jadi gradient tidak cepat lenyap.
- **Kenapa learning rate krusial?** Sudah dibahas - terlalu besar lompat-lompat, terlalu kecil lambat.

---
Reinforcement Learning
│
├── Framework masalah → MDP (Markov decision process)
│
├── Algoritma value-based → Q-learning
│
├── Algoritma on-policy → SARSA
│
├── Policy-based → Policy Gradient
│
└── Actor-Critic → PPO, A2C, dll

Reinforcement Learning merupakan metode yang berbeda penggunaannya dibandingkandenganSupervised Learning  danUnsupervised Learning . Apabila kita mengenal bahwa supervisedlearning  danunsupervised learning  menggunakan data yang bersifat historikal, makareinforcementlearning  tidak demikian. Reinforcement Learning memiliki pendekatan untuk menggunakan rewardand punishment secara berulang kali untuk mempelajari sebuah pola terhadap data, tergantung dari parameter yang diinginkan. 


### Istilah dalam RL
Agent:
Sebuah agent merupakan representasi fisik dari AI yang berinteraksi dan bertindak untuk mengamati environment . Sebuah agent dapat melakukan berbagai macam tindakan dalam environment dan memberikan sebuah pengamatan terhadap environmentyang dialami

Environment:
Sebuahe nvironment merupakan tempat dimanaagentdapat bertindak dan melakukan sebuahaksi tertentu. Biasanya environment merupakan kumpulan data yang kita berikan kepadaagent . Environmentini namun dapat berubah sesuai dengan tindakan yang dilakukan olehagent , ataupun dapat berubah dengan sendirinya tergantung dengan aturan yang diberikan

Reward:
Reward merupakan sebuah ‘hadiah’ atau nilai yang diberikan kepada sebuah agent ketika melakukan sebuah aksi. Selain memberikan sebuahreward , kita juga bisa memberikan sebuah punishment atas aksi yang dilakukan oleh agent 

Policy:
sebuah aturan yang diterima oleh agent setelah melakukan sebuah aksi dan mendapatkanreward/punishment .Policy ini akan selalu diperbarui setelah agent melakukan sebuah tindakan apapun, baik sebagai pengamat maupun tindakan terhadap environment

State:
sebuah kondisi yang mempengaruhi baik agent maupun environment setelah agent melakukan sebuah tindakan atau pengamatan terhadap environment . Nilai state ini akan terus diperbarui tiap kali agent berinteraksi dengan environment , yang digunakan sebagai landasan untuk melakukan iterasi berikutnya


Yang kamu butuhkan sebenarnya bukan definisi satu-satu, tapi alur logika RL dari awal sampai algoritma modern.
Kalau flow-nya jelas, semua bab di buku itu langsung masuk akal.

Aku tulis flow sebenarnya dari Reinforcement Learning.

1. Masalah paling sederhana: Bandit

Situasi:

kita punya beberapa pilihan aksi
tidak ada state

Contoh:

memilih iklan

memilih slot machine

Agent hanya belajar:

action mana paling sering memberi reward

Algoritma:

epsilon-greedy

value estimation

Masalah yang diselesaikan:

exploration vs exploitation
2. Masalah mulai kompleks: ada STATE

Sekarang keputusan tidak sekali saja.

Keputusan sekarang mempengaruhi masa depan.

Contoh:

robot bergerak di maze

Robot harus memilih:

state → action → state → action → ...

Ini disebut:

MDP (Markov Decision Process)

Komponen MDP:

state
action
reward
transition
policy

Ini adalah framework RL.

3. Kita butuh cara menilai STATE

Pertanyaan penting:

state mana yang bagus?

Jawabannya:

value function

Artinya:

value state =
reward sekarang
+
reward masa depan

Ini disebut:

Bellman Equation

Semua algoritma RL berasal dari sini.

4. Cara menghitung Value

Sekarang kita punya persamaan Bellman.

Masalah:

bagaimana menghitung V(s)?

Ada beberapa metode.

5. Dynamic Programming

Dipakai kalau model environment diketahui.

Artinya kita tahu:

P(s'|s,a)

Algoritma:

Policy Iteration

flow:

1 evaluasi policy
2 perbaiki policy
3 ulangi
Value Iteration

langsung cari optimal value.

Masalah:

jarang tahu model environment
6. Monte Carlo

Solusi ketika:

environment tidak diketahui

Agent belajar dari episode pengalaman.

Flow:

main game
episode selesai
hitung reward total
update value

Contoh:

blackjack AI

Masalah:

harus tunggu episode selesai
7. Temporal Difference (TD)

Solusi Monte Carlo yang lebih cepat.

Update dilakukan setiap step.

Flow:

state
action
reward
update value
lanjut

Algoritma:

SARSA

belajar mengikuti policy yang digunakan.

Q-learning

belajar optimal policy langsung.

Update rule:

Q(s,a) ← r + γ max Q(s',a')

Ini algoritma RL klasik.

8. Masalah baru: State terlalu banyak

Contoh:

game Atari

State:

pixel gambar

Jumlah state = jutaan.

Q-table tidak bisa dipakai.

Solusi:

neural network
9. Deep Q Network (DQN)

Q-value diprediksi neural network.

Flow:

state → neural network → Q(s,a)

Dipakai untuk:

game Atari
robot
control problem

Teknik penting:

experience replay
target network
10. Policy Gradient

Pendekatan berbeda.

Tidak belajar Q-value.

Agent langsung belajar:

policy π(a|s)

Dipakai ketika:

action space continuous

Contoh:

robot arm
drone control
Flow Besar RL

Ini flow yang sebenarnya dari buku itu:

Bandit
↓
MDP (framework RL)
↓
Bellman equation (core math)
↓
Dynamic Programming (model known)
↓
Monte Carlo (model unknown)
↓
Temporal Difference
↓
Q-learning
↓
Deep Q Network
↓
Policy Gradient
↓
Modern RL (PPO, A2C, etc)
Cara Cepat Mengingat

Masalah menentukan algoritma.

Jika hanya memilih action
Bandit

contoh:

ads recommendation
Jika ada state kecil
Q-learning
SARSA

contoh:

maze
gridworld
navigation
Jika state sangat besar
DQN

contoh:

game AI
vision RL
Jika action continuous
Policy Gradient
PPO
DDPG

contoh:

robot arm
drone
self-driving
Jika dikaitkan dengan penelitian kamu

Misalnya:

RL untuk SQL injection bypass WAF

State:

payload sekarang

Action:

mutasi payload

Reward:

bypass = 1
blocked = 0

Flow RL:

payload
↓
mutation action
↓
request ke server
↓
reward
↓
update Q

Algoritma cocok:

Q-learning
atau DQN

Kalau kamu mau, aku bisa jelaskan juga peta konsep RL yang biasanya dipakai di kuliah master AI.

Biasanya setelah lihat peta itu, 90% kebingungan RL langsung hilang dalam 10 menit.

## References
https://learning.oreilly.com/library/view/reinforcement-learning/
https://vpslabs.net/reinforcement-learning/
https://github.com/JMLcommunity/Kurikulum-AI/blob/master/Reinforcement%20Learning/
https://id.scribd.com/presentation/750125009/Modul-5b-Reinforcement-Learning
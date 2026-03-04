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

## References
https://learning.oreilly.com/library/view/reinforcement-learning/
https://vpslabs.net/reinforcement-learning/
https://github.com/JMLcommunity/Kurikulum-AI/blob/master/Reinforcement%20Learning/
https://id.scribd.com/presentation/750125009/Modul-5b-Reinforcement-Learning
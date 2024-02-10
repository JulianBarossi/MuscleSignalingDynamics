import matplotlib.pyplot as plt

# Phase names and speeds
phases = ['Action Potentail', 'Depolarization', 'Propagation', 'Nuerotransmitter Release', 'Muscle Activation', 'Contraction']
speeds = [1, 2, 2.5, 3, .5, .6]

plt.figure(figsize = (10, 6))
plt.bar(phases, speeds, color = 'skyblue')
plt.xlabel('Phase')
plt.ylabel('Duration')
plt.title("Muscle Signaling Modeling")
plt.xticks(rotation=45)
plt.show()

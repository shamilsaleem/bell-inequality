import numpy as np
import matplotlib.pyplot as plt

trials = []
S_abs_values = []

N = int(input("No of particles: "))

def correlation(a, b):
    return np.mean(a * b)

print("E_xx\tE_xy\tE_yx\tE_yy\tS\t|S|")

for i in range(100):

    alice_X = np.random.choice([1, -1], N)
    alice_Y = np.random.choice([1, -1], N)

    bob_X   = np.random.choice([1, -1], N)
    bob_Y   = np.random.choice([1, -1], N)

    E_xx = correlation(alice_X, bob_X)
    E_xy = correlation(alice_X, bob_Y)
    E_yx = correlation(alice_Y, bob_X)
    E_yy = correlation(alice_Y, bob_Y)

    S = E_xx + E_xy + E_yx - E_yy

    trials.append(i)
    S_abs_values.append(abs(S))

    print(f"{E_xx:7.4f}\t{E_xy:7.4f}\t{E_yx:7.4f}\t{E_yy:7.4f}\t{S:7.4f}\t{abs(S):.4f}")

plt.plot(trials, S_abs_values, ".")

plt.xlabel("Trial number")
plt.ylabel("|S|")
plt.grid(axis="y")
plt.ylim(0, 2)

plt.title(f"Classical CHSH Simulation (N = {N})")

plt.savefig(f"Classical_CHSH_N_{N}.png", dpi=300, bbox_inches="tight")
plt.close()

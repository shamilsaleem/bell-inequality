import numpy as np

N = 100000

a  = 0
a_p = np.pi/2
b  = np.pi/4
b_p = -np.pi/4

def quantum_correlation(theta):
    p_same = (1 - np.cos(theta)) / 2
    results = []
    for _ in range(N):
        if np.random.rand() < p_same:
            A = np.random.choice([1, -1])
            B = A
        else:
            A = np.random.choice([1, -1])
            B = -A
        
        results.append(A * B)
    return np.mean(results)

E_ab   = quantum_correlation(a - b)
E_ab_p = quantum_correlation(a - b_p)
E_a_p_b = quantum_correlation(a_p - b)
E_a_p_b_p = quantum_correlation(a_p - b_p)

S = E_ab + E_ab_p + E_a_p_b - E_a_p_b_p

print("E(a,b)      =", E_ab)
print("E(a,b')     =", E_ab_p)
print("E(a',b)     =", E_a_p_b)
print("E(a',b')    =", E_a_p_b_p)
print("\nCHSH S =", S)
print("|S| =", abs(S))

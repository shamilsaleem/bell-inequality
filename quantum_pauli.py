import numpy as np

# ----- Pauli matrices -----
sigma_x = np.array([[0, 1],
                    [1, 0]])

sigma_y = np.array([[0, -1j],
                    [1j, 0]])

sigma_z = np.array([[1, 0],
                    [0, -1]])

I = np.eye(2)

# ----- Function to build a·σ operator -----
def a_dot_sigma(theta):
    """
    Measurement in x-z plane
    a = (cosθ, 0, sinθ)
    """
    return np.cos(theta)*sigma_x + np.sin(theta)*sigma_z

# ----- Singlet state -----
# |ψ⁻> = (|01> - |10>) / √2
psi = np.array([0, 1, -1, 0]) / np.sqrt(2)

# ----- CHSH angles -----
a   = 0
a_p = np.pi/2
b   = np.pi/4
b_p = -np.pi/4

# ----- Expectation value function -----
def correlation(theta1, theta2):
    A = a_dot_sigma(theta1)
    B = a_dot_sigma(theta2)
    operator = np.kron(A, B)
    return np.real(np.conjugate(psi) @ operator @ psi)

# ----- Compute correlations -----
E_ab     = correlation(a, b)
E_ab_p   = correlation(a, b_p)
E_a_p_b  = correlation(a_p, b)
E_a_p_b_p= correlation(a_p, b_p)

S = E_ab + E_ab_p + E_a_p_b - E_a_p_b_p

print("E(a,b)   =", E_ab)
print("E(a,b')  =", E_ab_p)
print("E(a',b)  =", E_a_p_b)
print("E(a',b') =", E_a_p_b_p)

print("\nCHSH S =", S)
print("|S| =", abs(S))

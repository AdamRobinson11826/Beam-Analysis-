import numpy as np
import matplotlib.pyplot as plt

print('Simply supported beam analysis'.title())

def input_var():

    # User inputs for length, load and position.

    while True:
        L = input('Length of beam (m)')
        try:

            L = float(L)
            if L <= 0:
                print('Length must be  > 0')
                continue
            break
        except ValueError:
            print('Enter a number e.g 2.0')

    while True:
        C = input('Enter number corresponding to option: Point load (1), UDL (2), Both (3)')
        if C in ('1', '2', '3'):
            break
        else:
            print('Invalid choice. Please enter 1, 2, or 3')

    # Default values
    F = None; a = None; w = None; x1 = None; x2 = None          

    if C == '1':
        F = float(input('Point load (kN)'))
        while True:
            a = float(input('Position from left side (m)'))
            if 0 <= a <= L:
                break
            else:
                print("Position must lie on the beam ")
    
    elif C == '2':
        w = float(input("UDL (kN/m)"))
        while True:
            x1 = float(input('Start of UDL from left (m)'))
            x2 = float(input('End of UDL from the left (m)'))

            valid = (0 <= x1 < x2 <= L)
            if valid:
                break
            else:
                print("UDL must lie on the beam and have nonzero length") 

    elif C == '3':
        F = float(input('Point load (kN)'))
        w = float(input("UDL (kN/m)"))
        while True:
            a = float(input('Point load\'s position from left side (m)'))
            x1 = float(input('Start of UDL from left (m)'))
            x2 = float(input('End of UDL from the left (m)'))

            valid = (0 <= a <= L) and (0 <= x1 < x2 <= L)
            if valid:
                break
            else:
                print("Position must lie on the beam ")

    return (L, F, a, w, x1, x2)
    
    
   
L, F, a, w, x1, x2 = input_var()

# Support reaction


F = 0 if F is None else F; a = 0 if a is None else a
if w is None:
    W = 0
    a2 = 0
else:
    W = w * (x2 - x1)
    a2 = (x1 + x2) / 2


Rb = (F * a + W * a2) / L
Ra = (W + F) - Rb
print(f'Support reactions: Ra = {Ra:.3f} kN, Rb = {Rb:.3f} kN')

x1 = 0 if x1 is None else x1
x2 = 0 if x2 is None else x2
w = 0 if w is None else w



# Plotting shear and bending moments
n = 1000
x = np.linspace(0, L, 100)

plt.figure()
plt.grid(True)
plt.axhline(0, linewidth=1, color="Black")
plt.axvline(0, linewidth=1, color="Black")
plt.xlabel("Location (m)")
plt.ylabel("Shear (kN)")
plt.title("Shear Force Diagram")


H = lambda x: np.heaviside(x, 0)
V = (Ra - w * H(x - x1 ) * (x - x1) + w * H(x - x2) * (x - x2) - F * H(x - a))


plt.plot(x, V, c="red", linewidth=2, linestyle="dashed")
plt.fill_between(x, V, 0, color="Blue", alpha=0.2)
plt.show()

plt.figure()
plt.grid(True)
plt.axhline(0, linewidth=1)
plt.axvline(0, linewidth=1)
plt.xlabel("Location (m)")
plt.ylabel("Moment (kNm)")
plt.title("Bending Moment Diagram")

M = (Ra * x -  0.5 * w *H(x - x1) * (x - x1)**2 + 0.5 * w * H(x - x2) * (x - x2)**2 - F * (x - a) * H(x - a))



plt.plot(x, M, c="red", linewidth=2, linestyle="dashed")
plt.fill_between(x, M, 0, color="Blue", alpha=0.2)
plt.show()



























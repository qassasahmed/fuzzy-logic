import matplotlib.pyplot as plt
import numpy as np
import skfuzzy as fuzz # Recommended a Python3.9 3.9 interpreter

a = np.linspace(0,10, 100)
mu_a = fuzz.trimf(a, [0, 5, 10])

b = np.linspace(5, 15, 100)
mu_b = fuzz.trimf(b, [5, 10, 15])


a_union_b = fuzz.fuzzy_or(a, mu_a, b, mu_b)
print(a_union_b)

plt.plot(a, mu_a, label='Set A')
plt.plot(b, mu_b, label='Set B')
plt.plot(a_union_b[0], a_union_b[1],
         color='black',
         linestyle='solid',
         label='Union'
         )
plt.legend()
plt.title("A union B")
plt.xlabel('Universe of Discourse')
plt.ylabel('Fuzzy Membership')
plt.show()



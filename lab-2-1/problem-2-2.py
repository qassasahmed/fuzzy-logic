import matplotlib.pyplot as plt
import numpy as np
import skfuzzy as fuzz

items = np.array([1, 2, 3, 4])

mu_a = np.array([0.4, 0.35, 0.5, 0.6])
plt.scatter(items, mu_a)
plt.plot(items, mu_a, label='A\u0330')

mu_b = np.array([0.7, 0.75, 0.65, 0.8])
plt.scatter(items, mu_b)
plt.plot(items, mu_b, label='B\u0330')


a_intersect_b = fuzz.fuzzy_and(items, mu_a, items, mu_b)
print(f"A\u3030 \u2229 B\u3030 = {set(zip(a_intersect_b[1], a_intersect_b[0]))}")

plt.plot(a_intersect_b[0], a_intersect_b[1],
         color='black',
         linewidth='3',
         label='A\u0330 \u2229 B\u0330')
plt.legend()
plt.xlabel("Universe of Discourse")
plt.ylabel("Membership Function")
plt.title("A\u0330 \u2229 B\u0330")
plt.show()


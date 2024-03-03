import skfuzzy as fuzz
import numpy as np
import matplotlib.pyplot as plt

a = np.linspace(0, 5, 100)
mu_a = fuzz.trapmf(a, [0, 1, 4, 5])
mu_a = mu_a / (10 / 3)
plt.plot(a, mu_a, label='A')

b = np.linspace(3, 7, 100)
mu_b = fuzz.trapmf(b, [3, 4, 6, 7])
mu_b = mu_b / 2
plt.plot(b, mu_b, label='B')

c = np.linspace(5, 8, 100)
mu_c = fuzz.trapmf(c, [5, 6, 7, 8])
plt.plot(c, mu_c, label='C')

a_union_b = fuzz.fuzzy_or(a, mu_a, b, mu_b)
a_union_b_union_c = fuzz.fuzzy_or(a_union_b[0], a_union_b[1], c, mu_c)
plt.plot(a_union_b_union_c[0],
         a_union_b_union_c[1],
         label='Union',
         linewidth='2')

# 1- using max-membership or height method
deff_lom = fuzz.defuzz(a_union_b_union_c[0], a_union_b_union_c[1], 'lom')
# plt.scatter(deff_lom, 0, label=f'Max-Membership: {deff_lom:.2f}')

deff_centroid = fuzz.defuzz(a_union_b_union_c[0], a_union_b_union_c[1], 'centroid')
plt.scatter(deff_centroid, 0, label=f'Centroid: {deff_centroid:.2f}')



deff_mean_max = fuzz.defuzz(a_union_b_union_c[0], a_union_b_union_c[1],'mom')
plt.scatter(deff_mean_max, 0, label=f'Mean-Maxima: {deff_mean_max:.2f}')


plt.legend()
plt.xticks(np.arange(0, 10, 1))
plt.yticks(np.arange(0, 1.1, 0.1))
plt.xlabel('Universe of Discourse')
plt.ylabel('Membership function')
plt.show()
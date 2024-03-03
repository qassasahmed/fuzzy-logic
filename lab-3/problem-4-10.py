import skfuzzy as fuzz # needs python3.9 or less
import numpy as np
import matplotlib.pyplot as plt

a = np.linspace(140, 160, 100)
mu_a = fuzz.trimf(a, [140, 150, 160])
plt.plot(a, mu_a, label='A')

b = np.linspace(150, 180, 100)
mu_b = fuzz.trapmf(b, [150, 160, 170, 180])
plt.plot(b, mu_b, label='B')

a_union_b = fuzz.fuzzy_or(a, mu_a, b, mu_b)
plt.plot(a_union_b[0],
         a_union_b[1],
         label='Union',
         linewidth='2',
         color='red')


# 1- using centroid method
deff_centroid = fuzz.defuzz(a_union_b[0],
                            a_union_b[1],
                            'centroid')
plt.scatter(deff_centroid, 0,
            label=f'Centroid: {deff_centroid:.2f}')

# 2- using max-mean method
deff_mean_max = fuzz.defuzz(a_union_b[0],
                            a_union_b[1],
                            'mom')
plt.scatter(deff_mean_max, 0,
            label=f'Mean-Maxima: {deff_mean_max:.2f}')

plt.legend()
plt.xticks(np.arange(130, 190, 10))
plt.yticks(np.arange(0, 1.1, 0.1))
plt.xlabel('Universe of Discourse')
plt.ylabel('Membership function')
plt.show()

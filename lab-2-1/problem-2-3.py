import matplotlib.pyplot as plt
import numpy as np
import skfuzzy as fuzz

a = np.linspace(5000, 50000, 100)
mean_a = np.mean(a)
sigma_a = np.std(a)/2
gauss_mu_a = fuzz.gaussmf(a, mean_a, sigma_a)
plt.plot(a, gauss_mu_a, label='A\u0330', color='green')

b = np.linspace(10000, 100000, 100)
mean_b = np.mean(b)
sigma_b = np.std(b)/2
gauss_mu_b = fuzz.gaussmf(b, mean_b, sigma_b)
plt.plot(b, gauss_mu_b, label='B\u0330', color='orange')

a_union_b = fuzz.fuzzy_or(a, gauss_mu_a, b, gauss_mu_b)
# plt.plot(a_union_b[0], a_union_b[1],
#          label='A\u0330 \u222A B\u0330',
#          linewidth=3,
#          color='#0072e4')

a_intersect_b = fuzz.fuzzy_and(a, gauss_mu_a, b, gauss_mu_b)
# plt.plot(a_intersect_b[0], a_intersect_b[1],
#          label='A\u0330 \u2229 B\u0330',
#          linewidth=3,
#          color='#0072e4')

b_complement = fuzz.fuzzy_not(gauss_mu_b)
plt.plot(b, b_complement,
         linestyle="--",
         color='red',
         label='B\u0305')

a_diff_b = fuzz.fuzzy_and(a, gauss_mu_a, b, fuzz.fuzzy_not(gauss_mu_b))
plt.plot(a_diff_b[0], a_diff_b[1],
         label="A\u0330 - B\u0330",
         linewidth=3,
         color='#0072e4')

de_morgan_a_union_b = fuzz.fuzzy_and(a, fuzz.fuzzy_not(gauss_mu_a), b, fuzz.fuzzy_not(gauss_mu_b))
# plt.plot(de_morgan_a_union_b[0],
#          de_morgan_a_union_b[1],
#          label='A\u0305 \u2229 B\u0305',
#          linewidth=3,
#          color='#0072e4')
plt.xlabel("Universe of Discourse")
plt.ylabel("Membership Value (\u03bc)")
plt.legend()
plt.show()

import numpy as np
import random
def Exponential_generator(m, lmda):
    ans = [0] * m
    for i in range(m):
        ans[i] = - np.log(1 - random.uniform(0, 1)) / lmda
    return ans
print(np.mean(Exponential_generator(10000, 0.5)))

# import numpy as np
# import random
# def Random_uniform(m):
#     ans = [0] * m
#     for i in range(m):
#         x0 = random.uniform(0, 1)
#         x1 = random.uniform(0, 1)
#         exp_len = 2
#         while x0 < x1:
#             x0 = x1
#             x1 = random.uniform(0, 1)
#             exp_len += 1
#         ans[i] = exp_len
#     return ans
# print(np.mean(Random_uniform(10000)))

# import numpy as np
# import random
# def Random_drawing(m, n):
#     ans = [0] * m
#     for i in range(m):
#         x = list(range(1, n + 1))
#         x0 = random.sample(x, 1)[0]
#         x.remove(x0)
#         x1 = random.sample(x, 1)[0]
#         ans[i] = 2
#         while x1 > x0:
#             x0 = x1
#             x.remove(x0)
#             x1 = random.sample(x, 1)[0]
#             ans[i] += 1
#     return ans
# print(np.mean(Random_drawing(10000, 1000)))

# import numpy as np
# def Binomial_generator1(m, n, p):
#     ans = [0] * m
#     for i in range(m):
#         k, ind, u = 0, 0, random.uniform(0, 1)
#         while k < n:
#             if u < p:
#                 ind += 1
#                 u /= p
#             else:
#                 u = (u - p) / (1 - p)
#             k += 1
#         ans[i] = ind
#     return ans
# print(np.mean(Binomial_generator1(10000, 10, 0.5)))

# import numpy as np
# from collections import Counter
# def NBA_generator(m, n, p):
#     ans = [0] * m
#     for i in range(m):
#         game, win, lose = 0, 0, 0
#         while win < n // 2 + 1 and lose < n // 2 + 1:
#             game += 1
#             if np.random.uniform(0, 1, 1) < p:
#                 win += 1
#             else:
#                 lose += 1
#         ans[i] = game
#     return ans
# print(Counter(NBA_generator(10000, 7, 0.5))[7] / 10000)

# import numpy as np
# def Binomial_generator(m, n, p):
#     ans = [0] * m
#     for i in range(m):
#         ans[i] = sum(np.random.uniform(0, 1, n) < p)
#     return ans
# print(np.mean(Binomial_generator(10000, 10, 0.5)))

# import numpy as np
# import random
# def Geometric_generator(n, p):
#     ans = [0] * n
#     for i in range(n):
#         k = 1
#         v = random.uniform(0, 1)
#         while v < (1 - p) ** k:
#             k += 1
#         ans[i] = k
#     return ans
# print(np.mean(Geometric_generator(2000, 0.5)))

# import numpy as np
# import random
# def Poisson_generator(n, lmda):
#     ans = [0] * n
#     for i in range(n):
#         x, pdf, cdf = 0, np.exp(-lmda), np.exp(-lmda)
#         u = random.uniform(0, 1)
#         while u > cdf:
#             x += 1
#             pdf *= lmda / x
#             cdf += pdf
#         ans[i] = x
#     return ans
# print(np.mean(Poisson_generator(20000, 20)))

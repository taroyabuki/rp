import numpy as np
x = np.random.randint(1, 7, 10000)
plt.hist(x, bins=6)

import numpy as np
x = np.random.uniform(0, 1, 1000)
# あるいは
x = np.random.random(1000)
plt.hist(x)

tmp = np.random.uniform(1, 7, 1000)
x = np.array(tmp, dtype=int)
plt.hist(x, bins=6) # 結果は割愛

import numpy as np
x = np.random.binomial(100, 0.5, 1000)
plt.hist(x)

import numpy as np
x = np.random.normal(165, 10, 1000)
plt.hist(x)


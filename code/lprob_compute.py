import numpy, data_read, training

W, T = data_read.read_model()

X, Y = data_read.read_train()

import time

t0 = time.time()

for i in range(len(X)):
	training.compute_log_p(X[i], Y[i], W, T)

t1 = time.time()

print(f"Time: {t1-t0}")

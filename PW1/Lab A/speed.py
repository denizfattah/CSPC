import time
import decay

atoms = 200000

# Time the NumPy simulation
start = time.perf_counter()
decay.simulate(atoms, 0.4)
end = time.perf_counter()
numpy_time = end - start

print(f"NumPy time: {numpy_time:.6f} s")

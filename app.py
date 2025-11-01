import math
import time
import os
import matplotlib.pyplot as plt

def cpu_stress(n):
    result = 0
    for i in range(n):
        result += math.sqrt(i**2)
    return result

def run_test(cpu_label, n_iterations, mem_mb):
    print(f"Testi me CPU={cpu_label}, Memory={mem_mb}MB, Iterations={n_iterations}")
    start = time.time()
    cpu_stress(n_iterations)
    data = ['x' * 1024 * 1024 for _ in range(mem_mb)]  # QETU E STIMULPN RAMIN
    end = time.time()
    exec_time = end - start
    print(f"Perfundon: {exec_time:.2f} sekonda\n")
    return exec_time


N = int(os.getenv("ITERATIONS", "10000000"))
MEM = int(os.getenv("MEMORY_MB", "100"))

# 3 kufizimet e CPU-s
cpu_limits = [0.5, 1.0, 2.0]
execution_times = []

for cpu in cpu_limits:
    exec_time = run_test(cpu, N, MEM)
    execution_times.append(exec_time)

#Rez
output_path = "/app/output"
os.makedirs(output_path, exist_ok=True)

#File
with open(f"{output_path}/results.txt", "w") as f:
    f.write("Performance Results (Simulated CPU Limits)\n")
    f.write("------------------------------------------\n")
    for cpu, t in zip(cpu_limits, execution_times):
        f.write(f"CPU Limit: {cpu} | Execution Time: {t:.2f} seconds\n")

# Grafi
plt.plot(cpu_limits, execution_times, marker='o')
plt.xlabel('CPU Limit (simulated)')
plt.ylabel('Execution Time (s)')
plt.title('Performance vs CPU Limit')
plt.grid(True)
plt.savefig(f"{output_path}/results.png")

print("Rezulatet jane ne /app/output/")
print(" - results.txt per rezultatet numerike")
print(" - results.png per grafikun e performances")

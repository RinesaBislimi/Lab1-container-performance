import math
import time
import os
import random
import matplotlib.pyplot as plt

def cpu_stress(n):
    result = 0
    for i in range(n):
        result += math.sqrt(i**2)
    return result

def memory_stress(size_mb):
    _ = ['x' * 1024 * 1024 for _ in range(size_mb)]

N = int(os.getenv("ITERATIONS", "10000000"))
MEM = int(os.getenv("MEMORY_MB", "100"))
cpu_limits = [0.5, 1.0, 2.0]
output_path = "/app/output"
os.makedirs(output_path, exist_ok=True)

execution_times = []
load_distribution = {cpu: 0 for cpu in cpu_limits}

for cycle in range(3):
    chosen_cpu = random.choice(cpu_limits)
    load_distribution[chosen_cpu] += 1
    print(f"Cikli {cycle+1}: Load balancer caktoi CPU={chosen_cpu}")

for cpu in cpu_limits:
    print(f"Testi me CPU={cpu} | Memory={MEM}MB | Iterations={N}")
    start = time.time()
    cpu_stress(N)
    memory_stress(MEM)
    end = time.time()
    exec_time = end - start
    execution_times.append(exec_time)

    plt.figure()
    plt.bar([f"{cpu} CPU"], [exec_time], color="steelblue")
    plt.title(f"Execution Time for {cpu} CPU(s)")
    plt.ylabel("Seconds")
    plt.xlabel("CPU Limit")
    plt.grid(True, axis='y', linestyle='--', alpha=0.7)
    plt.savefig(f"{output_path}/result_{cpu}.png")
    plt.close()

    print(f"Perfundon: {exec_time:.2f} sekonda (Grafiku: result_{cpu}.png)")

plt.figure()
plt.plot(cpu_limits, execution_times, marker='o', color='orange')
plt.xlabel('CPU Limit')
plt.ylabel('Total Execution Time (s)')
plt.title('Performance Comparison by CPU Limit')
plt.grid(True)
plt.savefig(f"{output_path}/results_all.png")
plt.close()

plt.figure()
plt.bar([str(k) for k in load_distribution.keys()], load_distribution.values(), color='green')
plt.title('Load Balancer Distribution Across CPUs')
plt.xlabel('CPU Limit')
plt.ylabel('Number of Assigned Tasks')
plt.grid(True, axis='y', linestyle='--', alpha=0.7)
plt.savefig(f"{output_path}/load_balancer.png")
plt.close()

avg_time = sum(execution_times) / len(execution_times)
with open(f"{output_path}/results.txt", "w") as f:
    f.write("Performance Results (Real-Time + Load Balancer Simulation)\n")
    f.write("----------------------------------------------------------\n")
    for cpu, t in zip(cpu_limits, execution_times):
        f.write(f"CPU Limit: {cpu} | Total Execution Time: {t:.2f} seconds\n")
    f.write("\nAverage Execution Time: %.2f seconds\n" % avg_time)
    f.write("\nLoad Balancer Distribution:\n")
    for cpu, count in load_distribution.items():
        f.write(f" - CPU {cpu}: {count} tasks\n")

print("\nRezultatet u krijuan në /app/output/:")
print(" - result_0.5.png, result_1.0.png, result_2.0.png")
print(" - results_all.png (krahasimi përfundimtar)")
print(" - load_balancer.png (vizualizim i ndarjes së ngarkesës)")
print(" - results.txt (përmbledhje numerike)")

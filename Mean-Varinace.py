# I have implemented Expected Value(Mean) and Variance manually using dice roll example 

import numpy as np

number_of_simmulation = 10000 # you can change this number to see how Mean and Variance differ from the actual Mean if we take low n number of dice rolls
dice1 = np.random.randint(1, 7, num_sim)
dice2 = np.random.randint(1,7, num_sim)
sums = dice1 + dice2

print(f"Raw Data Dice sums: {sums}")

def manual_mean(data):
    total = 0
    count = 0
    for value in data:
        total = total + value
        count = count + 1
    return total/count
    
emp_mean = manual_mean(sums)
theoretical_mean = 7
print(f'Empirical Mean: {emp_mean} and Theoretical Mean: {theoretical_mean}')

# CUMULATIVE SUM
def manual_cumsum(data):
    current_sum = 0
    results = []
    for value in data:
        current_sum = current_sum + value
        results.append(current_sum)
    return results

cumulative_sum = manual_cumsum(sums)
print("\nFirst 10 cumulative Sum:")
print(cumulative_sum[:10])

print("\nLast 10 cumulative Sum")
print(cumulative_sum[-10:])
# CUMULATIVE AVERAGES

def manual_cumavg(data):
    results = []
    current_sum = 0
    for i, value in enumerate(data, 1):
        current_sum = current_sum + value
        current_avg = current_sum / i
        results.append(current_avg)
    return results

cumulative_avg = manual_cumavg(sums)
print("\nFirst 10 cumulative averages (very volatile):")
print(cumulative_avg[:10])

print("\nLast 10 cumulative averages (stable, close to 7):")
print(cumulative_avg[-10:])

# VARIANCE

def manual_var(data):
    # calculate Mean (μ)
    total = 0
    count = 0
    for value in data:
        total = total + value
        count = count + 1
    mean = total/count
    
    # Calculate squared deviations from mean
    sum_squared_deviations = 0
    for value in data:
        deviations = value - mean # (x- μ)
        sqaured_deviations = deviations * deviations # (x- μ)**2
        sum_squared_deviations = sum_squared_deviations + sqaured_deviations
        
    variance = sum_squared_deviations/count
    return variance

variance = manual_var(sums)
print(f"Variance: {variance}")

# Manual Runnign Variance
print("\n5. Manual Running Variance (step by step):")
running_var = []
for i in range(1, num_sim + 1):
    current_slice = sums[:i]
    var = manual_var(current_slice)
    running_var.append(var)
    print(f"   After {i} rolls: data {list(current_slice)} → variance = {var:.2f}")

print(f"\nFinal running variance array: {[round(x, 2) for x in running_var]}")
print(f"Verification with previous np.var method: {[round(x, 2) for x in running_var]}")

# verify our manual variance calculation with the formula
print("\n6. Manual Variance Step-by-Step Verification:")
n = len(sums)
mean = manual_mean(sums)
print(f"   Data: {list(sums)}")
print(f"   Mean (μ): {mean:.2f}")
print("\n   Calculating Σ(x - μ)²:")
sum_sq_dev = 0
for i, value in enumerate(sums):
    deviation = value - mean
    sq_dev = deviation ** 2
    sum_sq_dev = sum_sq_dev + sq_dev
    print(f"   (x{i+1} - μ)² = ({value} - {mean:.2f})² = {deviation:.2f}² = {sq_dev:.2f}")
print(f"\n   Sum of squared deviations = {sum_sq_dev:.2f}")
print(f"   Variance = {sum_sq_dev:.2f} / {n} = {sum_sq_dev/n:.2f}")

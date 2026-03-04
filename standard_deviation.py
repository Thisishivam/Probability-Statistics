# Standard Deviation - It quantify the amount of Spread around the Mean
#Low Standard Deviation means data points clustered around mean and High Standard Deviation means they are spread over a wider range. 
# Again we use 2 dice problem

import numpy as np

# Generate our dice data
num_sim = 10 # Here we have taken only 10 rolls so the expected output would not be correct so for correct expected output we must use high number of rolls like around 10,000 Rolls
dice1 = np.random.randint(1, 7, num_sim)
dice2 = np.random.randint(1, 7, num_sim)
sums = dice1 + dice2

print(f"Raw data (dice sums): {sums}")

# Example: The sum of 2 dice are [ 6  9 12  9  6  4  4  4 11  7]

# First, our manual variance function
def manual_var(data):
    # Variance Formula: Σ(x - μ)²/n
    # calculate Mean (μ)
    total = 0
    count = 0
    for value in data:
        total = total + value
        count = count + 1
    mean = total / count
    
    # Calculate squared deviations
    sum_squared_deviations = 0
    for value in data:
        deviation = value - mean
        squared_deviation = deviation * deviation # ---> (x - μ)²
        sum_squared_deviations = sum_squared_deviations + squared_deviation #---> Σ(x - μ)²
    
    # Average the squared deviations
    variance = sum_squared_deviations / count
    return variance

# NEW: Manual Standard Deviation
def manual_std(data):
    # Step 1: Get variance
    variance = manual_var(data)
    
    # Step 2: Take square root
    standard_deviation = variance ** 0.5  # or math.sqrt(variance)
    
    return standard_deviation


# Calculate for our data
variance = manual_var(sums)
std_dev = manual_std(sums)


"""

EXAMPLE OUTPUT
==================================================
STEP-BY-STEP VARIANCE
==================================================
Mean (μ) = 72/10 = 7.2000 The Mean not what we expect because we have taken 10 rolls but if we take 10000 rolls Mean(Expected Value) will get around 7

Calculate squared deviations (x - μ)²:
   (x1 - μ)² = (6 - 7.2000)² = -1.2000² = 1.4400
   (x2 - μ)² = (9 - 7.2000)² = 1.8000² = 3.2400
   (x3 - μ)² = (12 - 7.2000)² = 4.8000² = 23.0400
   (x4 - μ)² = (9 - 7.2000)² = 1.8000² = 3.2400
   (x5 - μ)² = (6 - 7.2000)² = -1.2000² = 1.4400
   (x6 - μ)² = (4 - 7.2000)² = -3.2000² = 10.2400
   (x7 - μ)² = (4 - 7.2000)² = -3.2000² = 10.2400
   (x8 - μ)² = (4 - 7.2000)² = -3.2000² = 10.2400
   (x9 - μ)² = (11 - 7.2000)² = 3.8000² = 14.4400
   (x10 - μ)² = (7 - 7.2000)² = -0.2000² = 0.0400

Variance (σ²) = 77.6000 / 10 = 7.7600 ---> Σ(x - μ)²/n
Standard Deviation (σ) = √7.7600 = 2.7857 ---? √var
"""

print(f"\nVariance: {variance:.4f}")
print(f"Standard Deviation: {std_dev:.4f}")
print(f"Verification with numpy: np.var={np.var(sums):.4f}, np.std={np.std(sums):.4f}")

# Let's see step-by-step calculation
print("\n" + "="*50)
print("STEP-BY-STEP STANDARD DEVIATION CALCULATION")
print("="*50)

n = len(sums)
total = 0
for value in sums:
    total = total + value
mean = total / n
print(f"Step 1: Mean (μ) = {total}/{n} = {mean:.4f}")

print(f"\nStep 2: Calculate squared deviations (x - μ)²:")
sum_sq_dev = 0
for i, value in enumerate(sums):
    deviation = value - mean
    sq_dev = deviation ** 2
    sum_sq_dev = sum_sq_dev + sq_dev
    print(f"   (x{i+1} - μ)² = ({value} - {mean:.4f})² = {deviation:.4f}² = {sq_dev:.4f}")

variance = sum_sq_dev / n
print(f"\nStep 3: Variance (σ²) = {sum_sq_dev:.4f} / {n} = {variance:.4f}")

std_dev = variance ** 0.5
print(f"Step 4: Standard Deviation (σ) = √{variance:.4f} = {std_dev:.4f}")

# NEW: Running Standard Deviation
print("\n" + "="*50)
print("RUNNING STANDARD DEVIATION")
print("="*50)

running_std = []
for i in range(1, num_sim + 1):
    current_slice = sums[:i]
    std = manual_std(current_slice)
    running_std.append(std)
    print(f"After {i} rolls: data {list(current_slice)}")
    print(f"   Variance = {manual_var(current_slice):.4f}, Std Dev = {std:.4f}\n")

print(f"Final running standard deviation array: {[round(x, 4) for x in running_std]}")

# Compare with running variance from before
print("\n" + "="*50)
print("VARIANCE vs STANDARD DEVIATION")
print("="*50)

for i in range(num_sim):
    print(f"After {i+1} rolls: Variance={manual_var(sums[:i+1]):.4f}, Std Dev={running_std[i]:.4f}")


"""
STEP BY STEP Rolls OUTPUT

==================================================
VARIANCE vs STANDARD DEVIATION
==================================================
After 1 rolls: Variance=0.0000, Std Dev=0.0000
After 2 rolls: Variance=2.2500, Std Dev=1.5000
After 3 rolls: Variance=6.0000, Std Dev=2.4495
After 4 rolls: Variance=4.5000, Std Dev=2.1213
After 5 rolls: Variance=5.0400, Std Dev=2.2450
After 6 rolls: Variance=6.8889, Std Dev=2.6247
After 7 rolls: Variance=7.5510, Std Dev=2.7479
After 8 rolls: Variance=7.6875, Std Dev=2.7726
After 9 rolls: Variance=8.6173, Std Dev=2.9355
After 10 rolls: Variance=7.7600, Std Dev=2.7857
"""

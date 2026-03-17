import numpy as np

# Real-world data: 20 customer purchases (in dollars)
# Ranges from small to large purchases
purchases = np.array([
    15, 25, 15, 50, 35,    # Customer 1-5
    25, 45, 15, 60, 25,    # Customer 6-10
    35, 25, 15, 55, 35,    # Customer 11-15
    45, 15, 25, 35, 50     # Customer 16-20
])

print("CUSTOMER PURCHASE ANALYSIS: ")
print(f"Purchase amounts: {purchases}")
print(f"Number of customers: {len(purchases)}")
print()


# Manual PMF implementation
def manual_pmf(data):
    """
    Calculate Probability Mass Function:
    For each unique value, P(x) = count(x) / total_count
    """
    # Count frequencies of each unique value
    frequencies = {}
    for amount in data:
        if amount in frequencies:
            frequencies[amount] = frequencies[amount] + 1
        else:
            frequencies[amount] = 1
    
    print("FREQUENCY COUNT: ")
    for amount in sorted(frequencies.keys()):
        print(f"Purchase ${amount}: {frequencies[amount]} customers")
    print(f"Total customers: {len(data)}")
    print()
    
    
    # Convert to probabilities
    total = len(data)
    probabilities = {}
    for amount, count in frequencies.items():
        probabilities[amount] = count / total
    
    print("PROBABILITY MASS FUNCTION: ")
    for amount in sorted(probabilities.keys()):
        print(f"P(${amount}) = {frequencies[amount]}/{total} = {probabilities[amount]:.3f}")
    print()
    
    # Verify total probability = 1
    total_prob = 0
    for prob in probabilities.values():
        total_prob = total_prob + prob
    
    print("VERIFICATION")
    print(f"Sum of all probabilities = {total_prob:.6f}")
    print(f"Is sum ≈ 1? {'✓' if abs(total_prob - 1.0) < 0.0001 else '✗'}")
    print()
    
    return probabilities, frequencies

# Calculate PMF
probabilities, frequencies = manual_pmf(purchases)

# Most common purchase amount
most_common_amount = None
highest_prob = 0
for amount, prob in probabilities.items():
    if prob > highest_prob:
        highest_prob = prob
        most_common_amount = amount

print(f"1. Most common purchase: ${most_common_amount}")
print(f"   Probability: {highest_prob:.1%} of customers")
print(f"   That's {frequencies[most_common_amount]} out of {len(purchases)} customers")
print()

# Probability of high-value purchase (≥ $50)
high_value_prob = 0
for amount, prob in probabilities.items():
    if amount >= 50:
        high_value_prob = high_value_prob + prob

print(f"2. High-value purchase probability (≥ $50):")
print(f"   P(amount ≥ $50) = {high_value_prob:.1%}")
print(f"   Expected: {high_value_prob * len(purchases):.1f} customers")
print()

# Probability of low-value purchase (≤ $20)
low_value_prob = 0
for amount, prob in probabilities.items():
    if amount <= 20:
        low_value_prob = low_value_prob + prob

print(f"3. Low-value purchase probability (≤ $20):")
print(f"   P(amount ≤ $20) = {low_value_prob:.1%}")
print()

# Expected value from PMF
expected_value = 0
for amount, prob in probabilities.items():
    expected_value = expected_value + (amount * prob)

print(f"4. Expected purchase amount:")
print(f"   E[X] = Σ [x × P(x)] = {expected_value:.2f}")
print(f"   Verification with manual_mean: {sum(purchases)/len(purchases):.2f}")
print()

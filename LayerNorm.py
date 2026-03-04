# In this we'll understand how Mean, Variance and Standard Deviation is the core of LayerNorm

import numpy as np

# Generate some sample data - imagine this is a batch of activations from a neural network
# Shape: (batch_size, features) - 3 samples, each with 4 features
activations = np.array([
    [1.0, 2.0, 3.0, 4.0],    # Sample 1
    [0.5, 1.5, 2.5, 3.5],    # Sample 2
    [2.0, 3.0, 4.0, 5.0]     # Sample 3
])

print("Original Activations:")
print(activations)
print(f"Shape: {activations.shape}\n")

# Mean function (works on 1D arrays)
def manual_mean_1d(data):
    total = 0
    count = 0
    for value in data:
        total = total + value
        count = count + 1
    return total / count

# Standard Deviation function (works on 1D arrays)
def manual_std_1d(data):
    # Calculate mean first
    total = 0
    count = 0
    for value in data:
        total = total + value
        count = count + 1
    mean = total / count
    
    # Calculate variance
    sum_sq_dev = 0
    for value in data:
        deviation = value - mean
        sq_dev = deviation * deviation
        sum_sq_dev = sum_sq_dev + sq_dev
    variance = sum_sq_dev / count
    
    # Return standard deviation
    return variance ** 0.5

# Layer Normalization from scratch
def manual_layer_norm(x, gamma=None, beta=None, eps=1e-5):
    """
    x: input array of shape (features,) - a single sample
    gamma: scale parameter (learnable)
    beta: shift parameter (learnable)
    eps: small constant to avoid division by zero
    """
    # Calculate mean across features (for this single sample)
    mean = manual_mean_1d(x)
    
    # Calculate standard deviation across features
    std = manual_std_1d(x)
    
    print(f"   Mean = {mean:.4f}, Std = {std:.4f}")
    
    # Normalize: (x - mean) / std
    normalized = []
    for value in x:
        norm_value = (value - mean) / (std + eps) 
        normalized.append(norm_value)
    normalized = np.array(normalized)
    
    print(f"   Normalized: {[round(n, 4) for n in normalized]}")
    
    # Apply scale (gamma) and shift (beta) if provided
    if gamma is not None and beta is not None:
        output = []
        for i, norm_val in enumerate(normalized):
            output.append(gamma[i] * norm_val + beta[i])
        return np.array(output)
    else:
        return normalized

# Apply LayerNorm to each sample
print("LAYER NORMALIZATION STEP BY STEP:")
print("=" * 50)

normalized_activations = []
for i, sample in enumerate(activations):
    print(f"\nSample {i+1}: {sample}")
    norm_sample = manual_layer_norm(sample)
    normalized_activations.append(norm_sample)

print("\n" + "=" * 50)
print("RESULTS:")
print("=" * 50)
print("\nOriginal Activations:")
print(activations)
print("\nLayer Normalized Activations (mean=0, std=1):")
print(np.array(normalized_activations))

# Verify that each normalized sample has mean≈0 and std≈1
print("\n" + "=" * 50)
print("VERIFICATION:")
print("=" * 50)
for i, sample in enumerate(normalized_activations):
    mean = manual_mean_1d(sample)
    std = manual_std_1d(sample)
    print(f"Sample {i+1} - Mean: {mean:.6f}, Std: {std:.6f}")

# Now with learnable parameters (gamma and beta)
print("\n" + "=" * 50)
print("WITH LEARNABLE PARAMETERS:")
print("=" * 50)

# Initialize learnable parameters
feature_dim = activations.shape[1]
gamma = np.array([1.0, 1.0, 1.0, 1.0])  # Scale - starts as 1 (identity)
beta = np.array([0.0, 0.0, 0.0, 0.0])    # Shift - starts as 0 (identity)

print(f"Gamma (scale): {gamma}")
print(f"Beta (shift): {beta}\n")

normalized_with_params = []
for i, sample in enumerate(activations):
    print(f"Sample {i+1}: {sample}")
    output = manual_layer_norm(sample, gamma, beta)
    normalized_with_params.append(output)
    print(f"   Output: {[round(o, 4) for o in output]}\n")

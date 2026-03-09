# Covariance/Correlation

import numpy as np

hours = np.array([2, 3, 4, 5, 6])      # X variable
scores = np.array([65, 70, 80, 85, 95]) # Y variable

def mean(data):
    total = 0
    count = 0
    for value in data:
        total = total + value
        count = count + 1
    return total / count

def Standard_dev(data):
    "first we calculate mean"
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

def Covariance(x, y):
    """
    Covariance measures how x and y move together
    Formula: Cov(x,y) = Σ(x - μx)(y - μy) / n
    """
    
    "Calculate Mean of Both X and Y"
    mean_x = mean(x)
    mean_y = mean(y)
    print(f"Mean of hours (μx) = {mean_x:.2f}")
    print(f"Mean of scores (μy) = {mean_y:.2f}")
    print()

    """
    Mean of hours (μx) = 4.00
    Mean of scores (μy) = 79.00
    """
    
    # first Calculate products of deviations
    
    sum_of_product = 0
    n = len(x)
    print("Step 2: Calculate (x - μx)(y - μy) for each student:")
    print("-----------------------------------------------")
    print(f"{'Student':<8} {'Hours(x)':<10} {'Score(y)':<10} {'x-μx':<10} {'y-μy':<10} {'Product':<10}")
    print("-----------------------------------------------")
    
    for i in range(n):
        dev_x = x[i] - mean_x
        dev_y = y[i] - mean_y
        product = dev_x * dev_y
        sum_of_product = sum_of_product + product
        
        print(f"{i+1:<8} {x[i]:<10} {y[i]:<10} {dev_x:<10.2f} {dev_y:<10.2f} {product:<10.2f}")
    
    print("-" * 60)
    print(f"{'':<38} Sum of products = {sum_of_product:.2f}")
    print()
    
    # Then Divide by n
    covariance = sum_of_product / n
    print(f"Step 3: Covariance = Sum of products / n")
    print(f"        Covariance = {sum_of_product:.2f} / {n} = {covariance:.2f}")

   """
   Calculate (x - μx)(y - μy) for each student:
----------------------------------------------------------
Student  Hours(x)   Score(y)   x-μx       y-μy       Product
----------------------------------------------------------
1        2          65         -2.00      -14.00     28.00
2        3          70         -1.00      -9.00      9.00
3        4          80         0.00       1.00       0.00
4        5          85         1.00       6.00       6.00
5        6          95         2.00       16.00      32.00
------------------------------------------------------------
                                       Sum of products = 75.00

Step 3: Covariance = Sum of products / n
        Covariance = 75.00 / 5 = 15.00

Calculate standard deviations
σx (hours std) = 1.4142
σy (scores std) = 10.6771
σx × σy = 1.4142 × 10.6771 = 15.0997

Correlation = Cov / (σx × σy)
Correlation = 15.0000 / 15.0997 = 0.9934
Covariance = 15.0000
Correlation = 0.9934

Interpretation:
- Covariance is positive (15.00) → as hours increase, scores increase
- Correlation = 0.9934 → very strong positive relationship
  (close to +1 means almost perfect linear relationship)
   """
    
    return covariance

def Correlation(x, y):
    """
    Correlation standardizes covariance to -1 to +1
    Formula: Corr(x,y) = Cov(x,y) / (σx * σy)
    """
    
    # so first get Covariance
    cov = Covariance(x, y)
    
    # then Get standard deviations
    std_x = Standard_dev(x)
    std_y = Standard_dev(y)
    
    print(f"\nCalculate standard deviations")
    print(f"σx (hours std) = {std_x:.4f}")
    print(f"σy (scores std) = {std_y:.4f}")
    print(f"σx × σy = {std_x:.4f} × {std_y:.4f} = {std_x * std_y:.4f}")
    
    # now calculate Correlation
    
    correlate = cov / (std_x * std_y)
    print(f"\nCorrelation = Cov / (σx × σy)")
    print(f"Correlation = {cov:.4f} / {std_x * std_y:.4f} = {correlate:.4f}")
    
    return correlate

print("COVARIANCE CALCULATION")
covariance = Covariance(hours, scores)

print("CORRELATION CALCULATION")
correlation = Correlation(hours, scores)

print(f"Covariance = {covariance:.4f}")
print(f"Correlation = {correlation:.4f}")
print("\nInterpretation:")
print(f"- Covariance is positive ({covariance:.2f}) → as hours increase, scores increase")
print(f"- Correlation = {correlation:.4f} → very strong positive relationship")
print(f"  (close to +1 means almost perfect linear relationship)")

# Verify with numpy built-in Methods
print(f"NumPy Covariance: {np.cov(hours, scores, ddof=0)[0][1]:.4f}")
print(f"NumPy Correlation: {np.corrcoef(hours, scores)[0][1]:.4f}")

"""
This is the Value from Numoy Built-in Covariance/Correlation Methods
NumPy Covariance: 15.0000
NumPy Correlation: 0.9934
"""

# Different correlations
print("------------------------------------------------------------")
print("UNDERSTANDING CORRELATION POSITIVE, NEGATIVE, NO CORRELATION")
print("------------------------------------------------------------")

# Positive correlation
x1 = np.array([1, 2, 3, 4, 5])
y1 = np.array([2, 4, 6, 8, 10])  # y = 2x
corr1 = Correlation(x1, y1)
print(f"\nPerfect Positive (y=2x): Correlation = {corr1:.4f}")

# No correlation (random)
x2 = np.array([1, 2, 3, 4, 5])
y2 = np.array([5, 3, 8, 2, 7])  # Random
corr2 = Correlation(x2, y2)
print(f"No Correlation (random): Correlation = {corr2:.4f}")

# Negative correlation
x3 = np.array([1, 2, 3, 4, 5])
y3 = np.array([10, 8, 6, 4, 2])  # y = -2x + 12
corr3 = Correlation(x3, y3)
print(f"Perfect Negative (y=-2x+12): Correlation = {corr3:.4f}")

import numpy as np
import pandas as pd
np.random.seed(42) 
data = pd.DataFrame({
    'value': np.random.randint(1, 100, 1000)
})
print(data.head())
mean_estimate = np.mean(data['value'])
print(f'Mean Estimate: {mean_estimate}')
variance_estimate = np.var(data['value'], ddof=1) 
print(f'Variance Estimate: {variance_estimate}')
sample_size = 100  
random_sample = data['value'].sample(n=sample_size, random_state=42)
sample_mean = np.mean(random_sample)
sample_variance = np.var(random_sample, ddof=1)

print(f'\nSample Mean: {sample_mean}')
print(f'Sample Variance: {sample_variance}')

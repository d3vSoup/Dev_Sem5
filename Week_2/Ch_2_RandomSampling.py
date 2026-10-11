# Random sampling 

'''

Random sampling is a core statistical technique used to draw an unbiased subset from a 
population so that statistical inferences can generalize to the whole dataset.   

Slide Excerpt:

"Random sampling is a method used in statistics and data analysis to select a subset of 
individuals or data points from a larger population."   

"The key characteristic of random sampling is that each member of the population has an 
equal chance of being chosen and that the selection process is entirely by chance." 

"It aims to ensure that the sample reflects the characteristics of the larger population."   


'''

import numpy as np
import pandas as pd

# Create a 10x8 DataFrame
dat = np.arange(80).reshape(10, 8)
df = pd.DataFrame(dat)

# Generate a randomly permuted array of row indices 0 through 9
sampler = np.random.permutation(10)
# Example output: array([1, 5, 3, 6, 2, 4, 9, 0, 7, 8])

# Rearrange rows in the order of the permuted indices
df.take(sampler)





#Random sampling without sampling

'''
Slide 
Excerpt:"To compute random sampling without replacement, follow these steps:

1. To perform random sampling without replacement, we first create a 
permutation array.

2. Next, we slice off the first n elements of the array where n is the 
desired size of the subset you want to sample.

3. Then we use the df.take() method to obtain actual samples:"   


'''
import numpy as np
import pandas as pd

data = np.arange(80).reshape(10, 8)
df = pd.DataFrame(data)
sampler = np.random.permutation(10)[:5]       # Select 5 random indices
sample_without_replacement = df.take(sampler) # Use .take() to select rows by index

print(sample_without_replacement)  

# Select 3 distinct random rows without replacement:
df.take(np.random.permutation(len(df))[:3])


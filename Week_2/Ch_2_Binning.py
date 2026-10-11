'''

Discretization (or binning) is the process of converting continuous numerical features into 
discrete categorical buckets or intervals.   

Slide Excerpt:"Continuous datasets need to be converted into discrete or interval forms."   
"Each interval is referred to as a bin"

'''

#The pd.cut() function maps continuous values into specified numerical intervals:
import numpy as np
import pandas as pd

height = [120, 122, 125, 127, 121, 123, 137, 131, 161, 145, 141, 132]  #
bins = [118, 125, 135, 160, 200]  #

category = pd.cut(height, bins)  

# intervals created are right-closed and left-open:
# (118, 125] → includes 125 but not 118
# (125, 135] → includes 135 but not 125

# right=False does the opposite now... [ )

'''

Assigning Categorical Labels & Frequency Counting (Slide 107)
Raw intervals like (118, 125] can be replaced with human-readable labels using the labels parameter. 
To inspect the distribution of items across bins, use pd.value_counts():

for the code below : 
Output distribution:   
Short Height: 5 
Average height: 3   
Good Height: 3

Taller: 1

'''
bin_names = ['Short Height', 'Average height', 'Good Height', 'Taller']  #
category = pd.cut(height, bins, labels=bin_names)  #
pd.value_counts(category)  #






#example : 

import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [25, 42, 31, 19, 50]
}
df = pd.DataFrame(data) 

# Define bin edges and category labels
bins = [0, 18, 30, 40, 60]                  # Intervals: (0, 18], (18, 30], (30, 40], (40, 60]
labels = ['0-18', '19-30', '31-40', '41-60'] 

# Create new discretized column
df['Age_Group'] = pd.cut(df['Age'], bins=bins, labels=labels)  



#Equal-Length Automatic Binning (Slide 110)

# Instead of passing explicit boundary lists, passing an integer N 
# partitions the range between the minimum and maximum observed values into $N$ 
# equal-width ranges:


# Generates 5 equal-width intervals with 2 decimal points of precision
pd.cut(np.random.rand(40), 5, precision=2)  #




# While pd.cut() divides data based on numerical value widths, pd.qcut() divides 
#data based on sample quantiles so that every bin contains approximately the 
#same number of data points.

'''

Slide Excerpt:"qcut method that forms the bins based on sample quantiles"   

"Quantiles are points taken at regular intervals from the cumulative distribution function 
of a random variable. They are used to partition a dataset into intervals with an equal 
number of data points or to represent divisions of the probability distribution of a 
dataset."   

"Median (2-Quantile): Divides the data into two equal halves. 
It's the value below which 50% of the data falls."   

"Quartiles (4-Quantiles): Divide the data into four equal parts."  

'''

randomNumbers = np.random.rand(2000) 

# Divides 2000 data points into 4 equal-frequency quartiles (approx. 500 points each)
category3 = pd.qcut(randomNumbers, 4) 


'''

During Exploratory Data Analysis (EDA), extreme anomalous values must be detected and 
filtered out prior to downstream modeling.   

Slide Excerpt:

"Outliers are data points that diverge from other observations for several reasons."   
"An outlier is an observation that lies an abnormal distance from other values in a random 
sample from a population"   

"During the EDA phase, one of our common tasks is to detect and filter these outliers."      

"The main reason for this detection and filtering of outliers is that the presence of such 
outliers can cause serious issues in statistical analysis"   


'''


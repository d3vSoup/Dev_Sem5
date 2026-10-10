#what is data 

# Data encompasses a collection of numbers, words, events, facts, measurements, observations or even description of things

#Dataset - collection of Data 

#Columns - Attributes / Variables / Features 
#Rows = Samples



# Types of Data
# Structured Data - standardized format of rows and columns that typicallyd efine data attributes. Eg. CSV , DB tables
# Semi strcutured data - Semi-structured data is a form of structured data that does not obey the tabular structure of data models associated with relational databases or other forms of data tables, but nonetheless contains tags or other markers to separate semantic elements and enforce hierarchies of records and fields within the data. Eg. JSON , XML , PDF 
# Unstructured Data - Unstructured data is information that either does not have a predefined data model or is not organized in a predefined manner. Eg. Text files, Emails, Social Media posts
# Streaming Data - Data that is generated continuously by many sources ( in real time ). Such data should be processed incrementally using stream processing techniques without knowing all of the data. This data can be structured, unstructured, semi structured and volume can be huge. Eg. Stock Market Data, Sensor Data, Social Media Feeds



# Exploratory Data Analysis - EDA 

# Take Raw Data --> Extract main characteristiocs and insights. ( qialitattive and quantitative analysis of raw data ) 
# EDA is a statistical approach to analyze and summarize the main characteristics of a raw dataset, often with visual methods. 
# It helps understand data patterns, spot anomalies, test assumptions, and check hypotheses before formal modeling.
# used to determine relationship between variables and handle missing values asw.

'''
EDA - classified into 2 =methods 

Graphical and Non graphical 


Data insight - > Extracted from raw Data in a meaningful and useful format.
                Data insights refer to the process of collecting, analyzing, and acting on data
                related to your company and its clients. The goal is simple: make better
                decisions. A good data management and analysis strategy help companies
                monitor the health of critical systems, streamline processes, and improve
                profitability.
   
                data - > Analytics -> Insights

Customer shopping se we get - > maket strategies, products , overall customer experinece , age, gender, history of purchase, preferred payment , 
                               frew pf purchases , and can enhance product offerings and enghance customer satisfaction



AIM of EDA : 

1. Maximise insight into dataset 
2. Uncover underlying Str
3. Extract imp variables
4. Test assumptions and edge cases and detetct outliers
5. Develeop valid models and dtermine Xs ( Variables that impact output )


Steps in EDA : 

•Problem definition
        •Before trying to extract useful insight from the data, it is essential to define the business problem to be solved... so....
        •Defining main objective of the analysis
        •Defining the main deliverables
        •Outlining the main roles and responsibilities
        •Obtaining the current state of the data
        •Performing Cost/benefit analysis
        •Defining the time table



•Data Preparation
        •Define the source of data and data schemes and tables and understandun the chaarcteristcs of data 
        •Data Pre-processing and Delete non relevant datasets, Delete rows with missing data (or use interpolation methods) 
        •Data preparation involves, handling missing values and preparing the dataset for further analysis
        •This stage includes data cleaning, feature engineering, and transformation of raw data into a usable format


•Data analysis -- one of the most crucuial steps with desc stats and analytical data visualization
        •Summarizing the data { tables, graphs, descriptive statistics, inferential statistics, correlation statistics, grouping and models}
        •Finding the hidden correlation and relationships among the data
        •Developing predictive models
        •Evaluating the models


•Development and representation of the results
        •This step involves presenting the dataset to the target audience in the form of
            •Graphs
            •Summary tables
            •Maps and
            •Diagrams
        •This is also an essential step as the result analyzed from the dataset should be interpretable by the business stakeholders



'''


#Data Analytics 
    # use of tools and process to combine and examine data and identify patterns and relationships and treds
    # The goal of analytics is to answer specific questions, discover new insights, and help organizations make better, data-driven decisions.

# insight - > realising a pattern in data or a relationship between variables that no one knew it existed b4
# eg. 



# Business Qs
'''

•Simple (descriptive) Stats
• “Who are the most profitable customers?”

•Hypothesis Testing
• “Is there a difference in value to the company of these
customers?”

•Segmentation/Classification
• What are the common characteristics of these customers?

•Prediction
• Will this new customer become a profitable customer? If so, how
profitable?




1. Descriptive: e.g., Mean; describes data you have but can't be generalized beyond that
•We’ll talk about in Exploratory Data Analysis


2. Inferential: e.g., t-test, that enable inferences about the population beyond our data
•These are the techniques we’ll leverage for Machine Learning and Prediction

'''








#DATA : 

#Qualitative Data  : Thats abt info of qualoiities that cant be measured ... descriptive / textual mostly 
#                       Such data can be observed and recorded. Like eye colour or car colour, Gender, Religion , etc. 
'''
Methods for gathering qualitative data
• Surveys
• Opinion polls
• Observations
• Focus groups
• Interviews
• Case studies
• Previous documents
• Video and audio recordings
'''


#Quantitative Data : numerical , used to define info that can be counted .. eg . distance , speed, height , L or W, age, income, Group size, etc. 
# Quant Data analysis :  SWOT , text, MaxDiff, TURF 




#Structured data : 

'''
Most of the structured dataset falls into 2 categories 

Numerical data : 

This data has a sense of measurement. So called Quantitative Data. 
Can be ... Discrete or Continuous
                                        Discrete : Data is countable. Values can be listed. Eg. Rank of studemnts, No of coin toss, No of countries.
                                        a variable that represents discrete datset == discrete variable 

                                        Continuous : Infinite no. Of Numerical values within a specific range. Like temp , weight , duration of call ( time ) 
                                        a variable desc continuous data == continupus variable


Categorical data :

Data represnets the characteriscs of an object. Hence called QUALITITATIVE dataset. Eg. gender, narital status , Movie Genres , educational level, Sex
        A variable describing categorical data is referred to as a categorical variable

• A binary categorical variable can take exactly two values and is also referred to as a dichotomous variable
                Example : Completed (Yes/No) , result (Pass/Fail), Attendance (Present/Absent)

• Polytomous variables are categorical variables that can take more than two possible values
                Example : Marital status, Movie genres

'''




#Scale of measurement : Describes the relationship b/w the values that are allocated to variables 

'''
Types of measuring scales : 

1. Nominal Scale  - data in the form of categories or groups.  Eg. Eye Color, Gender, Religion, Movie Genres etc. 
      = , =/=         Also called categorical variable scale. 
                    It is defined as a scale that labels variables into distinct classifications and doesnt involve a quantitative value or order.
                    In nominal data, the values are merely labels and do not have any inherent order or ranking cz they have no value.

                    ex :
                    • The languages that are spoken in a particular country
                    • Biological species
                    • Parts of speech in grammar (noun, pronoun, adjective, and so on)
                    • Taxonomic ranks in biology (Archea, Bacteria, and Eukarya)
                    • Gender (Male, Female,Others)
                    
                    Numbers associated here -- only labels... used for classification / categorization / divisioon : 
                    Where do you live?
                        •1- Suburbs
                        •2- City
                        •3- Town

                    How to collect Nominal data ? 

                    By asking an open ended Qn. Ans can be coded to respective no. of labe;s decided by the researcher. 
                    Or,
                    collect it via MCQ in which answers are labelled

                    In both cases, the analysis of gathered data will happen using percentages or mode
                        •The most common answer received for the question.
                        • is it possible for a single question to have more than one mode? Ans : Yes... it can have any no. of modes
                        • is it possible for two common favorites to exist in a target population? Ans : Yes... it can have any no. of modes... but statistically only one can be considered





2. Ordinal Scale - This is used to classify data into categories but with an order or ranking
   =, =/= , </>            Eg. Class 1, Class 2, Class 3, etc.
                    In this scale, the values can be ranked or ordered, but the differences between the values are not necessarily equal.

                    1. Ordinal Scale is defined as a variable measurement scale used to simply depict the order of variables and not the difference between each variable
                    2. These scales generally depict non-mathematical ideas such as frequency, satisfaction, happiness, a degree of pain
                    3. Ordinal Scale maintains intrinsic order but is void of an origin of scale, and thus, the distance between variables cant be calculated.
                    4. Descriptional qualities indicate tagging properties similar to the nominal scale, in addition to which the ordinal scale also has a relative position of variables

                        Thus this generally used in market research surveys and questionnaires  bcz we only care abt the order , not the diff b/w variables 
                    Ex : 
                    • How satisfied are you with the customer service?  
                        •Very Dissatisfied - 1
                        •Dissatisfied - 2
                        •Neutral - 3
                        •Satisfied - 4
                        •Very Satisfied - 5


                Ordinal scale data can be presented in tabular or graphical formats for a researcher to conduct a convenient analysis of collected data
                



3. Interval Scale - Quantitative scale .. diff b/w 2 variables is useful & meaningful & can be measured
    =,=/=,</>,+/-           Ex : IQ Test Data, Temperature in F/C 

                    1. In this type of scale, the mean is calculable, along with which, other arithmetic operations like addition and subtraction can also be performed on the collected data
                    2. It is defined as a numerical scale where the variables order is known and the difference between these variables.
                    3. Interval indicates distance between two entities, which is what theInterval scale helps achieve.
                    4. These scales are effective as they open doors for the statisticalanalysis of provided data. Mean, median, or mode can be used to calculate the central tendency in this scale.
                    
                    5. DRAWBACK : The only drawback of this scale is that there is no pre-decided starting point or a true zero value.
                                        
                        Detailed Ex of celcius fahrenheit Scale : 
                          • Eighty degrees is always higher than 50 degrees, and the difference between these two temperatures is the same as the difference between 70 degrees and 40 degrees.
                          • Also, the value of 0 is arbitrary because negative temperature values exist.. which makes the Celsius/Fahrenheit temperature scale a classic example of an interval scale.

                    
                    Analysis of Interval data : 
                                All the techniques applicable to nominal and ordinal data analysis are applicable to Interval Data as well.
                                Apart from those techniques, there are a few analysis methods, such as 
                                                        descriptive statistics correlation regression analysis, 
                                                                                                    which is extensively used for analyzing interval data.
                                Descriptive analysis statistics is the term given to the analysis of numerical data.
                                It helps to describe, depict, or summarize data in a meaningful manner, and it helps in the calculation of mean, median, and mode.




4. Ratio Scale :  Quantitative scale with absolute zero point...  all arithmetic operations can be performed.  Eg. Height, Weight, Age, Income, Number of children
    =,=/=,</>,+/-, *,/              1. Has an absolute zero that is meaningful .. thus its an INTERVAL SCALE with addn property that its 0 position indicates the absence of the quantity being measured.
                                    2. In ratio scale, the difference between any two values is meaningful and calculable. 
                                    3. Also, any arithmetical operation performed on the scale is valid.. this means that not only can we compute how much higher one value is than another (addition/subtraction),  but we can also determine how many times greater it is (multiplication/division).
                                    Ex : Height, weight, age, income, shoe size, distance, height, etc.
    

'''



# compare classical DA vs EDA vs bayesian analysis 
'''
classical DA vs EDA vs Bayesian

Classical : problem define --> Data collect --> model development --> Data analysis --> results 
thus, its hypothesis driven .. eg . A medical researcher believes a new puill lowers blood prresssure. So they set up stat model firsr, test patinets , analyse results to see if hypothesis is right.. publish findings 

EDA : problem define --> Data collect --> Data analysis --> Model development / Data visualisation --> results 
thus, its data driven .. eg . A data analyst picks up a dataset and starts exploring it using graphs and summaries to see what patterns emerge... thus discover trend and algos


Bayesian : problem define -> Data collect --> Model Dev --> prior distribution --> Data analysis --> posterior distribution -> Update prior distribution --> final results / inference 

How it works: You set up a model and combine existing beliefs (Prior Distribution) with new data to update your conclusions.
eg.  A meteorologist predicts tomorrow's rain chance. They start with historical weather records (prior belief ) combine with current weather data (likelihood) and calculate updated probability (posterior).. and communicate the forecast 



'''



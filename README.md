# Student_performance_prediction
Student performance prediction using machine learning ensemble techniques

Introduction
	 The objective of the project was to write a program which would be able to predict student performance based on various qualitative and quantitative characters exhibited by the student over a period.  Machine learning algorithms were used to predict the student performance over a time period. Models were successful in predicting the performance with an accuracy of 92%. The same models with minor adjustments can be used for various use cases.

Purpose
 	Although educational systems are changing rapidly from classrooms to internet based teaching, there hasn’t been any change in how students are guided to be successful either in achieving good grades or finding a job after graduation. At an institutional level, the idea of student performance analyzing software would help any individual schools to work on a specific parameter to make their school more successful than its competitors. At an individual level, students can be given personal feedback to work on a specific goal to get good grades in school based on their previous performance. This level of personalized feedback would earn the school a good reputation among society for the personal care taken by the school for its students.
	At a higher educational level like graduate level college finding a good job is as important as getting good grades during the semester. With the help of this software previous data of students who were successfully placed can be analyzed. This analysis can help other students by providing information about qualities or parameters which made them more successful. 
	The other use cases of this software would be predicting how successful an employee would be in the company. Companies invest time and money to train an employee to make the individual ready for the company. All the resources would go in vain if the employee isn’t able to adapt to the company’s environment. So a software like this would help a company to utilize its resources on the right candidate.
Proposal
	To build comprehensive software to predict student performance in educational institutions, probability of a student’s placement after graduation, and provide assistance with personalized coaching.
Dataset :-
Source:- https://archive.ics.uci.edu/ml/datasets/student+performance
Attribute Information:
● 1 school - student's school 
● 2 sex - student's sex 
● 3 age - student's age 
● 4 address - student's home address type 
● 5 famsize - family size 
● 6 Pstatus - parent's cohabitation status 
● 7 Medu - mother's education 
● 8 Fedu - father's education 
● 9 Mjob - mother's job 
● 10 Fjob - father's job 
● 11 reason - reason to choose this school  
● 12 guardian - student's guardian 
● 13 traveltime - home to school travel time  
● 14 studytime - weekly study time  
● 15 failures - number of past class failures 
● 16 schoolsup - extra educational support 
● 17 famsup - family educational support 
● 18 paid - extra paid classes within the course subject 
● 19 activities - extra-curricular activities 
● 20 nursery - attended nursery school 
● 21 higher - wants to take higher education  
● 22 internet - Internet access at home  
● 23 romantic - with a romantic relationship  
● 24 famrel - quality of family relationships  
● 25 freetime - free time after school  
● 26 goout - going out with friends  
● 27 Dalc - workday alcohol consumption  
● 28 Walc - weekend alcohol consumption  
● 29 health - current health status  
● 30 absences - number of school absences 
● 31 G1 - first period grade  
● 31 G2 - second period grade
● 32 G3 - final grade  

Data Preprocessing:
 	The dataset was processed to check for  Null Values and there are no such irregularities in the dataset,implying that data is already clean and processed.

Modification of Dataset:
A new column called ‘FinalGrade’ is asserted which reflects ‘Grade3’ and a broader level view of ‘Grade3’.
The column is inferred broadly as five categories under given conditions
as follows:
● 'Excellent'[(data.G3 >= 18) & (data.G3 <= 20)]
● 'Good' [(data.G3 >= 15) & (data.G3 <= 17)]
● 'Satisfactory' [(data.G3 >= 11) & (data.G3 <= 14)]
● 'Poor' [(data.G3 >= 6) & (data.G3 <= 10)]
● 'Failure' [(data.G3 >= 0) & (data.G3 <= 5)]
Encoding :
There are several attributes which are non-numeric and categorical ,so they must be encoded,because models cannot deal with non-numeric attributes. But as observed,the dataset has only a few categories(max of 5) for every column,so the best assumption would be one-hot-encoding.

Exploratory Data Analysis(EDA):
To study and observe the behaviour of data,attributes ,relationship between attributes and target variable are graphically visualized ,so that pattern of data is keenly studied and to explore the dependency and weightage of attribute so as to extract reliable features to develop a reliant model with robust features. Attributes against target variable(‘FinalGrade’)[to study the dependency and weightage]

Feature Extraction:
Exploring and observing the data through visualizations helps in understanding features and makes a primary contribution to extract and structure important features.
So major conclusions from visualizations are-:
● ‘G1’ and ‘G2’ play a vital role in prediction of ‘FinalGrade’,so structuring these columns would help.
● ‘absences’(number of absent days) has good weightage among features to decide the prediction.
● Information about Students whose father is working at home has least importance as per data analysis.
● Parental status information has negligible influence or effect on ‘FinalGrade’ prediction.

Decision Tree Algorithm
A decision tree is a flowchart-like tree structure where an internal node represents feature(or attribute), the branch represents a decision rule, and each leaf node represents the outcome. The topmost node in a decision tree is known as the root node. It learns to partition on the basis of the attribute value. It partitions the tree in a recursive manner called recursive partitioning. This flowchart-like structure helps you in decision making. It's visualization like a flowchart diagram which easily mimics the human level thinking. That is why decision trees are easy to understand and interpret.
Decision Tree Model Score : 0.8561643835616438 , Cross Validation Score : 0.7929936305732485
Random Forest
The random forest is a model made up of many decision trees. Rather than just simply averaging the prediction of trees (which we could call a “forest”), this model uses two key concepts that gives it the name random:
1.	Random sampling of training data points when building trees
2.	Random subsets of features considered when splitting nodes
Random Forest Model Score : 0.936986301369863 , Cross Validation Score : 0.7484076433121019

SVC Algorithm
The objective of a Linear SVC (Support Vector Classifier) is to fit to the data provided, returning a "best fit" hyperplane that divides, or categorizes, data. From there, after getting the hyperplane,  some features can be added to the classifier to see what the "predicted" class is. This makes this specific algorithm rather suitable for our uses, though it can be used for many situations. 
SVC Model Score : 0.9054794520547945 , Cross Validation Score : 0.7707006369426752

XGBoost
XGBoost is well known to provide better solutions than other machine learning algorithms. In fact, since its inception, it has become the "state-of-the-art” machine learning algorithm to deal with structured data.

XGBoost Train data Score : 1.0 , Validation data Score : 0.7929936305732485

Conclusion
	All the four models have given the same result which suggests that any model can be used but using XGBoost classifier would deliver a better accuracy in prediction. the same model can be implemented for various data and the accuracy can be increased if the sample size to be evaluated is much larger than the current dataset.


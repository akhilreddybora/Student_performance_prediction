import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
import seaborn as sns

data = pd.read_csv('students.csv')
data.head()

from pandas.plotting import scatter_matrix
grades = data[['G1','G2','G3']]
scatter_matrix(grades)

#corelation
corr = data.corr()
fig, ax = plt.subplots(figsize=(20, 15))
colormap = sns.diverging_palette(150,50, as_cmap=True)
sns.heatmap(corr, cmap=colormap, annot=True, fmt=".2f")
plt.xticks(range(len(corr.columns)), corr.columns);
plt.yticks(range(len(corr.columns)), corr.columns)
plt.savefig('Correlation.png', bbox_inches='tight')
plt.show()

#going out ditribution
f, ax = plt.subplots()
figure = sns.countplot(x = 'goout', data=data, order=[1,2,3,4,5])
ax = ax.set(ylabel="Count", xlabel="Going Out")
figure.grid(False)
plt.title('Going Out Distribution')
plt.savefig('Going_out_plot.png', bbox_inches='tight')


data['FinalGrade'] = 'na'
data.loc[(data.G3 >= 18) & (data.G3 <= 20), 'FinalGrade'] = 'Excellent'
data.loc[(data.G3 >= 15) & (data.G3 <= 17), 'FinalGrade'] = 'Good' 
data.loc[(data.G3 >= 11) & (data.G3 <= 14), 'FinalGrade'] = 'Satisfactory' 
data.loc[(data.G3 >= 6) & (data.G3 <= 10), 'FinalGrade'] = 'Poor' 
data.loc[(data.G3 >= 0) & (data.G3 <= 5), 'FinalGrade'] = 'Failure' 
data.head(5)


#Grade based on relationship status
perc = (lambda col: col/col.sum())
index = ['Failure','Poor','Satisfactory','Good','Excellent']
relationship_index = pd.crosstab(index=data.FinalGrade, columns=data.romantic)
romantic_index = relationship_index.apply(perc).reindex(index)
romantic_index.plot.bar(fontsize=16, figsize=(14,8))
plt.title('Grade By Relationship Status', fontsize=20)
plt.ylabel('Percentage of Students', fontsize=16)
plt.xlabel('Final Grade', fontsize=16)
plt.savefig('Grade_Relationshipstatus.png', bbox_inches='tight')
plt.show()


#Grade based on the free time avaiable
index = ['Failure','Poor','Satisfactory','Good','Excellent']
status_index = pd.crosstab(index=data.FinalGrade, columns=data.freetime)
status_index = status_index.apply(perc).reindex(index)
status_index.plot.bar(fontsize=16, figsize=(14,8))
plt.title('Grade By freetime', fontsize=20)
plt.ylabel('Percentage of Students', fontsize=16)
plt.xlabel('Final Grade', fontsize=16)
plt.savefig('Grade_freetime_status.png', bbox_inches='tight')

# health - current health status
health_index = pd.crosstab(index=data.FinalGrade, columns=data.health)
Overall_health_index = health_index.apply(perc).reindex(index)

Overall_health_index.plot.bar(colormap='summer',fontsize=16, figsize=(14,8))
plt.title('Grade By Overall health', fontsize=20)
plt.ylabel('Percentage of Students ', fontsize=16)
plt.xlabel('Final Grade', fontsize=16)
plt.savefig('Grade_overall_health.png', bbox_inches='tight')
plt.show()



X = data.drop(labels=['FinalGrade','G3'],axis=1)
y = data.FinalGrade

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3)

#x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0,stratify=y)

X_train = pd.get_dummies(X_train)
X_test = pd.get_dummies(X_test)

#X_train=np.expand_dims(X_train.values[:,:-1], axis=2)
#X_train.shape

len(list(X_train))


# final model
tree = DecisionTreeClassifier(min_samples_leaf=17)
t= tree.fit(X_train, y_train)
print("Decisioin Tree Model Score" , ":" , t.score(X_train, y_train) , "," , 
      "Cross Validation Score" ,":" , t.score(X_test, y_test))



# final model
forest = RandomForestClassifier(n_estimators=36, min_samples_leaf=2)
f = forest.fit(X_train, y_train)
print("Raondom Forest Model Score" , ":" , f.score(X_train, y_train) , "," ,
      "Cross Validation Score" ,":" , f.score(X_test, y_test))




svc = SVC(C=0.2, kernel='poly', degree=1, gamma='auto')
s= svc.fit(X_train, y_train)
print("SVC Model Score" , ":" , s.score(X_train, y_train) , "," ,
  "Cross Validation Score" ,":" , s.score(X_test, y_test))




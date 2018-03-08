
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_digits
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
import matplotlib.pyplot as plot

# Loading the digits data into variable
db=load_digits()
ctn=db.data
ar1=db.target
sl, sw, pl, pw = train_test_split(ctn, ar1, test_size=0.2, random_state=30)
# Now let us perform LDA
ldperform = LinearDiscriminantAnalysis()
# Here we are performing regression with logistic orientation #logistic=LogisticRegression()
a = ldperform.fit(sl,pl)
yprediction = ldperform.predict(sw) #Predicting the outcomes
#logistic.fit(sl, pl)
# Now here we perform outcome predicting process.
yprediction=ldperform.predict(sw)

# let us Calculate accuracy score with applyication of LinearDiscriminantAnalysis model
print("Accuracy of Linear discriminant analysis:", accuracy_score(yprediction, pw))

plot.figure()
col = ['green', 'red', 'blue']
for x, y, z in zip(col, [0, 1, 2], db):
    plot.scatter(a[ar1 == y, 0], a[ar1 == y, 1], alpha=.8, color=x,label=z)
plot.legend(loc='best', shadow=False, scatterpoints=1)
plot.title('Linear Discriminant Analysis results performed on Iris data set:')
plot.show()

from sklearn import svm
from sklearn import datasets
from sklearn import metrics
from sklearn.model_selection import train_test_split

# Default data set from the available, digits is being loaded
iris = datasets.load_digits()

# loading data into the variable
xload = iris.data

# loading target into the variable
yload = iris.target

# We are going to divide the test data and training data in
xtrainer, xtesting, ytrainer, ytesting = train_test_split(xload, yload, test_size=0.2)

print("Support Vector Machine classification with Linear Model :")

# We are Creating model for Support vector machine  with linear_kernel
linearkernel = svm.SVC(kernel="linear")
linearkernel.fit(xtrainer, ytrainer)
yprediction = linearkernel.predict(xtesting)

print("The accuracy that is obtained for support vector machine classification with Linear kernel: %.3f" % metrics.accuracy_score(ytesting, yprediction))

print("\n Support vector machine classification with rbf kernel Model :")

# Creating  model for Support Vecctor Machinde using RBF_kernel
rbfmodel = svm.SVC(kernel="rbf")

# Fitting the data
rbfmodel.fit(xtrainer, ytrainer)

yprediction = rbfmodel.predict(xtesting)


# Checking the accuracy score on comparing ytesting data  and ypredicting data
print("The accuracy score that is obtained for Support Vector Machine Classification using RBF_kernel is : %.3f" % metrics.accuracy_score(ytesting, yprediction))
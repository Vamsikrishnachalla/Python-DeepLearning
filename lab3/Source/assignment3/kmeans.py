from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn import neighbors,datasets

# loading the default dataset IRIS.
k1 = datasets.load_iris()

# loading data into the variable
k2 = k1.data

# Loading target into the variable
labd1=k1.target

# Here we define and divide test data to 20% and training data at 80%
xtrainer, xtester, ytraining, ytesting = train_test_split(k2, labd1, test_size=0.2, random_state=42)

# Here we are seen setting the n-neighbours to the perform KNN
knn = neighbors.KNeighborsClassifier(n_neighbors=50)
knn.fit(xtrainer, ytraining)

# Now let us perform prediction
yprediction=knn.predict(xtester)


# now we perform accuracy calculation over knn algorithm
print(" Accuracy for (k = 50) ", accuracy_score(yprediction, ytesting))
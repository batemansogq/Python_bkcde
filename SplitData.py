from sklearn.model_selection import train_test_split
data   = [0,1,2,3,4, 5,6,7,8,9]  # input dataframe samples
labels = [0,0,0,0,0, 1,1,1,1,1]  # the function we're training is " >4 "

data_train, data_test, label_train, label_test = train_test_split(data, labels, test_size=0.5, random_state=7)

data_train
#[9, 7, 3, 6, 4]

label_train
#[1, 1, 0, 1, 0]

data_test
#[8, 5, 0, 2, 1]

label_test
#[1, 1, 0, 0, 0]

from sklearn.metrics import accuracy_score

# Returns an array of predictions:
predictions = my_model.predict(data_test)
predictions
#[0, 0, 0, 1, 0]

# The actual answers:
label_test
#[1, 1, 0, 0, 0]

accuracy_score(label_test, predictions)
#0.4000000000000000

accuracy_score(label_test, predictions, normalize=False)
#2

#====================================================
# Process:
# Load a dataset into a dataframe
X = pd.read_csv('data.set', index_col=0)

# Do basic wrangling, but no transformations
# ...

# Immediately copy out the classification / label / class / answer column
y = X['classification'].copy()
X.drop(labels=['classification'], inplace=True, axis=1)

# Feature scaling as necessary
# ...

# Machine Learning
# ...

# Evaluation
# ...

# From now on, you only train on a "portion" of your dset:
X_train = pd.DataFrame([ [0], [1], [2], [3] ])
y_train = [0, 0, 1, 1]

from sklearn.neighbors import KNeighborsClassifier
model = KNeighborsClassifier(n_neighbors=3)
 model.fit(X_train, y_train) 
#KNeighborsClassifier(...)

# You can pass in a dframe or an ndarray
model.predict([[1.1]])

model.predict_proba([[0.9]])
#[[ 0.66666667  0.33333333]]

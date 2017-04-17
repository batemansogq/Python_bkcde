from sklearn import linear_model
model = linear_model.LinearRegression()
model.fit(X_train, y_train)

LinearRegression(copy_X=True, fit_intercept=True, n_jobs=1, normalize=False)


# R2 Score
model.score(X_test, y_test)
#153.244939109

# Sum of Squared Distances
np.sum(model.predict(X_test) - y_test) ** 2)
#5465.15


#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Support vector clustering
#

from sklearn.svm import SVC
model = SVC(kernel='linear')
model.fit(X, y) 

#SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0,
#  decision_function_shape=None, degree=3, gamma='auto', kernel='linear',
#  max_iter=-1, probability=False, random_state=None, shrinking=True,
#  tol=0.001, verbose=False)

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
 # Decision Trees Classifier
#

# You know the drill...
from sklearn import tree
model = tree.DecisionTreeClassifier(max_depth=9, criterion="entropy")
model.fit(X,y)
#DecisionTreeClassifier(class_weight=None, criterion='entropy', max_depth=9,
#            max_features=None, max_leaf_nodes=None, min_samples_leaf=1,
#            min_samples_split=2, min_weight_fraction_leaf=0.0,
#            presort=False, random_state=None, splitter='best')

# .DOT files can be rendered to .PNGs, if you've already `brew install graphviz`.
tree.export_graphviz(model.tree_, out_file='tree.dot', feature_names=X.columns)

from subprocess import call
call(['dot', '-T', 'png', 'tree.dot', '-o', 'tree.png'])


###################################################################
# random forest

from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier(n_estimators=10, oob_score=True)
model.fit(X, y)
#RandomForestClassifier(bootstrap=True, class_weight=None, criterion='gini',
#            max_depth=None, max_features='auto', max_leaf_nodes=None,
#            min_samples_leaf=1, min_samples_split=2,
##            min_weight_fraction_leaf=0.0, n_estimators=10, n_jobs=1,
#            oob_score=True, random_state=None, verbose=0, warm_start=False)
            
#print model.oob_score_
0.789925345

# PCA and Isomap work by intelligently simplify your data by either variability or intrinsic geometry. 
# K-Means clusters your data based on feature similarity. 
# K-Neighbors classifies your data by feature similarity. 
# Linear regression models a continuous, linear correlation in your data. 
# decision trees classify your data probabilistically based off of entropy, which can be thought of as 'purity' or information gain.

#load libraries
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib


#read in a csv
wheat = pd.read_csv("C:/Users/mckinns/Documents/GitHub/DAT210x/Module3/Datasets/wheat.data", 
                              index_col=0, header=0)

# Also get rid of the 'area' and 'perimeter' features
df_lim = wheat.drop([ 'area','perimeter'], axis=1)

#force into a pandas DF
df_wh = pd.DataFrame(wheat)

#check if df has nan's
x.isnull().sum()

#subset a DF, remains a DF
s1 = df_wh[['perimeter', 'area']]


#object type
print type(y_train), type(X_train) # y_train and X_train are Series, as described below; need to convert X_train to DataFrame

#object length
print len(X_train), len(y_train) # X_train and y_train are the same length

#convert to DF
X_train = pd.DataFrame(X_train)

#replace a char in a string
df['range'] = df['range'].str.replace(',','-')

#find a value in a DF
X.loc[X['z4'] == '-14420-11-2011 04:50:23.713']

df.query('(a < b) & (b < c)')

#find unique values
df_cn['education'].unique()
# values spread
df_cn.age.value_counts()
print csv_dataframe.head(5)
print csv_dataframe.columns
print csv_dataframe.describe()
print csv_dataframe.index
print csv_dataframe.dtypes

#define a colum as an ordered category
df_cn['classification'] = df_cn['classification'].astype("category",
  ordered=True,
  categories=['<=50K', '>50K']
).cat.codes

#explode features out into binary cols
df_cn = pd.get_dummies(df_cn,columns=['sex'])

#rename columns
df_ht1.columns = ['RK', 'PLAYER' , 'TEAM' , 'GP' , 'G' , 'A' , 'PTS' , '+/-' , 'PIM' , 'PTS/G', 	
              'SOG' , 'PCT' , 'GWG' , 'PP G' , 'PP A' , 'SH G' , 'SH A']
#drop rows over a threshold
df_ht1 = df_ht1.dropna(axis=0, thresh=4)

#remove a columns
df_ht1 = df_ht1.drop(labels=['RK'], axis=1)

#update a data types
df_ht1.GP = pd.to_numeric(df_ht1.GP, errors='coerce')

#count rows
len(df_ht1)

#filter a subset
df_sr[(df_sr.motor=='E') & (df_sr.screw=='E')]

#fill all NaN's will a scalar
print df.fillna(0)

#fill foward with previous value
print df.fillna(method='ffill', limit=1)

#find all rows with NaNs
print X[pd.isnull(X).any(axis=1)]

#drop all rows with NaN's
df.dropna(axis=0)
#drop all columns with NaN
df.dropna(axis=1)
# drop some columes
df = df.drop(labels=['Features', 'To', 'Delete'], axis=1)

# Drop any row that has at least 4 NON-NaNs within it:
df = df.dropna(axis=0, thresh=4)


# drop duplicates, where teh unq key is a subset of features
print df.drop_duplicates(subset=['Major category', 'Total']).reset_index()	  
   
# reset an index
x.reset_index()   
   
### limit a df by a bol array
# create booline array value
lt_bol = model.labels_  == 2
# make a series for DF
Bo = pd.Series(lt_bol, name='bools')
#filter the df to just that results
user1[Bo.values]


#make a table display
ps = pd.Series(model.labels_)
counts = ps.value_counts()
print counts

# make a confusion matrix
import sklearn.metrics as metrics
y_true = [1, 1, 2, 2, 3, 3]  # Actual, observed testing dataset values
y_pred = [1, 1, 1, 3, 2, 3]  # Predicted values from your model
metrics.confusion_matrix(y_true, y_pred)
#array([[2, 0, 0],
#       [1, 0, 1],
 #      [0, 1, 1]])

 #make a heat map plot of it
import matplotlib.pyplot as plt

columns = ['Cat', 'Dog', 'Monkey']
confusion = metrics.confusion_matrix(y_true, y_pred)

plt.imshow(confusion, cmap=plt.cm.Blues, interpolation='nearest')
plt.xticks([0,1,2], columns, rotation='vertical')
plt.yticks([0,1,2], columns)
plt.colorbar()

plt.show()
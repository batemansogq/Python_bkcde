# 4. Transforming Data > Lecture: Isomap

from sklearn import manifold

iso = manifold.Isomap(n_neighbors=4, n_components=2)
iso.fit(df)

Isomap(eigen_solver='auto', max_iter=None, n_components=2, n_neighbors=4,
    neighbors_algorithm='auto', path_method='auto', tol=0)

manifold = iso.transform(df)
df.shape
#(430, 6)

manifold.shape
#(430, 2)

from GaussianNB.prep_terrain_data import makeTerrainData
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier

features_train, labels_train, features_test, labels_test = makeTerrainData()

clf = KNeighborsClassifier(n_neighbors=5)
clf.fit(features_train, labels_train)
pred = clf.predict(features_test)
acc = accuracy_score(pred, labels_test)
print(acc)
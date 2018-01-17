from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
from GaussianNB.prep_terrain_data import makeTerrainData

features_train, labels_train, features_test, labels_test = makeTerrainData()

clf = RandomForestClassifier(max_depth=2, random_state=0)
clf.fit(features_train, labels_train)
pred = clf.predict(features_test)
acc = accuracy_score(pred, labels_test)
print(acc)
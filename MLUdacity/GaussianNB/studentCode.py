from GaussianNB.prep_terrain_data import makeTerrainData
from GaussianNB.ClassifyNB import NBAccuracy

features_train, labels_train, features_test, labels_test = makeTerrainData()

def submitAccuracy():
    accuracy = NBAccuracy(features_train, labels_train, features_test, labels_test)
    return accuracy

# if __name__ == '__main__':
#     print(submitAccuracy())
from sklearn.decomposition import PCA

def doPCA(data):
    pca = PCA(n_components=2)
    pca.fit(data)
    return pca

x = [[1., 2.], [2., 3.], [3., 4.], [4., 5.], [5., 6.] ,[6., 7.] , [7., 8.]]

pca = doPCA(x)
print(pca.explained_variance_ratio_)
first_pca = pca.components_[0]
second_pca = pca.components_[1]

transform_data = pca.transform(x)
for ii, jj in zip(transform_data, x):
    print()
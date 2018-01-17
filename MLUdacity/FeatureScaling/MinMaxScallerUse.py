from sklearn.preprocessing import MinMaxScaler
import numpy

arr = numpy.array([[115.], [140.], [175.]])
scaler = MinMaxScaler()
rescale_arr = scaler.fit_transform(arr)
print(rescale_arr)
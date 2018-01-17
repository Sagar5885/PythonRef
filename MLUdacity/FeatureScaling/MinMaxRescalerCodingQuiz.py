def featureScaling(arr):
    tmp1 = arr[1] - arr[0]
    tmp2 = arr[2] - arr[0]
    res = tmp1 / tmp2

    return res


# tests of your feature scaler--line below is input data
data = [115, 140, 175]
print(featureScaling(data))
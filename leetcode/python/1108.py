def defanging(str):
    return '[.]'.join(str.split('.'))


print(defanging("1.1.1.1"))

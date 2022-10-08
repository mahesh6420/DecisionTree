from sklearn.datasets import load_iris
classificationNames = ['setosa','versicolor','virginica']

def loadDataSet():
    return load_iris()

def convertToClasses(indexes):
    class_seq = []
    for i in range(len(indexes)):
        class_seq.append(classificationNames[indexes[i]])
    return class_seq

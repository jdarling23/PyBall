from sklearn import tree
import csv

allData = []
features = []
with open('MachineBasketball.csv', 'r') as f:
    reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
    reader = list(reader)
    allData = reader
    features = allData[1:]

training_labels = []
test_labels = []
test_features = []
training_features = []

counter = 0
for item in features:
    if counter < 30:
        training_labels.append(allData[counter][0])
        training_features.append(item)
    if counter >= 30 and counter < 74:
        test_labels.append(allData[counter][0])
        test_features.append(item)
    if counter >= 74 and counter < 103:
        training_labels.append(allData[counter][0])
        training_features.append(item)
    if counter >= 103:
        test_labels.append(allData[counter][0])
        test_features.append(item)
    counter = counter + 1

clf = tree.DecisionTreeClassifier()
clf = clf.fit(training_features, training_labels)

counter = 0
rights = 0.
total = 0.
for item in test_features:
    actual = test_labels[counter]
    
    #clf.predict needs to have an array containing in a single arry, so we need to put item (an array) into another array (itemContainer)
    itemContainer = []
    itemContainer.append(item)

    prediction = clf.predict(itemContainer)
    if actual == prediction:
        rights = rights + 1
    counter = counter + 1
    total = total + 1

perc = (rights/total)*100
print("Percentage Correct: " + str(perc))
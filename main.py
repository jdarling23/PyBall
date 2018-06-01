from sklearn import tree
import csv
import argparse

#Command line arguments that determine which rows of data corrspond to which player's test and train categories
# EXAMPLE: [Last Row # for Player 1 Train] [Last Row # for Player 1 Test] [Last Row # for Player 2 Train] [Last Row # for Player 2 Test]
parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer for the accumulator')
args = parser.parse_args()
rows = args.integers

#Reads in data from csv
allData = []
features = []
with open('MachineBasketball.csv', 'r') as f:
    reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
    reader = list(reader)
    allData = reader
    features = allData[1:]

#These are the arrays for our training and test data that we will fill with our data from the csv
training_labels = []
test_labels = []
test_features = []
training_features = []

counter = 0
for item in features:
    #Player 1 Training Data
    if counter < rows[0]:
        training_labels.append(allData[counter][0])
        training_features.append(item)
    #Player 1 Test Data
    if counter >= rows[0] and counter < rows[1]:
        test_labels.append(allData[counter][0])
        test_features.append(item)
    #Player 2 Training Data
    if counter >= rows[1] and counter < rows[2]:
        training_labels.append(allData[counter][0])
        training_features.append(item)
    #Player 2 Test Data
    if counter >= rows[2] and counter < rows[3]:
        test_labels.append(allData[counter][0])
        test_features.append(item)
    counter = counter + 1

clf = tree.DecisionTreeClassifier()
clf = clf.fit(training_features, training_labels)

#These are some counter variables that will be used during testing
counter = 0
rights = 0.
total = 0.
f = open('learningoutput.csv', 'wb')

for item in test_features:
    result = "Incorrect"
    actual = test_labels[counter]
    
    #clf.predict needs to have an array containing in a single arry, so we need to put item (an array) into another array (itemContainer)
    itemContainer = []
    itemContainer.append(item)

    #Program makes prediciton and checks to see if it's correct
    prediction = clf.predict(itemContainer)
    if actual == prediction:
        rights = rights + 1
        result = "Correct"
    counter = counter + 1
    total = total + 1

    #Write individual results to csv
    writer = csv.writer(f, lineterminator="\n")
    writer.writerow(["Game " + str(counter),"Predicted Player: " + str(prediction[0]),"Actual Player: " + str(actual),result])

f.close()
perc = (rights/total)*100
print("Percentage Correct: " + str(perc))
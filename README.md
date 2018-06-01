# PyBall
A machine learning program written in Python that can tell the difference between two different basketball players based on stats

To run the program, you will need to install numPy, sciPy, and scikit-learn (enter pip [package name] into the command line).

#Training Data and Test Data
The program will use a set of data for each player known as training data. Tranining data prepares the model to make a prediciton for the test data. 

#Command Line
The command line follows this format:
python main.py [Last Row # for Player 1 Train] [Last Row # for Player 1 Test] [Last Row # for Player 2 Train] [Last Row # for Player 2 Test]

So for the example provided (which uses the first 30 games as training data), you'd juse the following command:
python main.py 30 74 104 152

#CSV Format
The first column should contain a 0 or 1 to donote if the data belongs to the first or second data. After that, you can use as many different columns of statistics as you want (so long as they are contiguous).

import numpy as np

from mnist import MNIST
from sklearn import svm

DATA_DIR = 'data'

# Print image to console
def print_to_console(im):
	'''
		Print the image from numpy format onto the console
	'''
	counter = 0
	range = 28 ** 2
	while counter < range:
		string = ""
		for j in range(28):
			if images[number][counter + j] > 0:
				string += "x"
			else:
				string += " "
		print(string)
		counter += 28          # This is a more efficient loop

# Calculate the accuracy of our model
def accuracy(X, y, model):
	'''
		Calculat accuracy of model
		X : input images
		y : labels for images
		model : the model we are testing
	'''
	# Check if X and y have same number of rows
    m = np.shape(X)[0]
    assert m == np.shape(y)[0]
    
    right = 0
    for i in range(m):
        predicted = model.predict([X[i]])
        if predicted[0] == y[i]:
            right += 1
    acc = right / m * 100
    return acc

# Main program
if __name__ == "__main__":

	# Load data
	mndata = MNIST(DATA_DIR)
	X_train, y_train = mndata.load_training()
	X_test, y_test = mndata.load_testing()

	# Fitting the model
	# svm.LinearSVC is a linear model
	lin_clf = svm.LinearSVC()
	lin_clf.fit(X_train, y_train)

	# Accuracy
	train_acc = accuracy(X_train, y_train, lin_clf)
	test_acc = accuracy(X_test, y_test, lin_clf)
	print("Training accuracy = {:2.2f}\nTesting accuracy = {:2.2f}".format(
		train_acc, test_acc))
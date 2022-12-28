The following tasks served as an introduction to test driven development.

Task 0: Integer Addition
	> Prototype: def add_integers(a, b=98):
	> a and b must be integers or floats , otherwise rasie a TypeErrror exception with the message "a must be an integer" or "b must be an integer"
	> a abd b must be the first casted to integers if they are float
	> Returns an integer: the addition of a and b
	> You are allowed to import any module.

Task 1: Divide matrix
	> Prototype: def matrix_divided(matrix, div):
	> matrix mst be a list of lists of integers or floats, otherwise raise a TypeError exception with the message  "matrix must be a matrix (list of lists) of integers/floats
	> Each row of the matrix must be of the same size, otherwise raise a TypeError exception with the message "Each row of the matrix must have the same size"
	> div must be a number (integer or float), otherwise raise a TypeError exception with the message "div must be a number"
	> div can't be equla to 0, otherwise raise a ZeroDivisionErrror exception with the message "division by zero"
	> All elements of the matrix should be divided by div, rounded to 2 decimal places
	> Returns a new matrix
	> You are not allowed to import any module

Task 2: Say my name
	> Prototype: def say_my_name(first_name, last_name=""):
	> first_name and last_name must be strings otherwise, raise a TypeError exception with the message "first_name must be a string" or "last_name must be a string"
	> You are not allowed to import any module.

Task 3: Print Square - Prints square with #
	> Prototype: def print_square(size):
	> size is the size length of the square
	> size must be an integer, otherwise raise a TypeError exception with the message "size must be an integer"
	> if size is less than 0, raise a ValueError exception with the message "size must be >= 0"
	> if size is s afloat and is less than 0, raise a TypeError exception with the message "size must be an integer"
	> You are not allowed to import any module.

Task 4: Text indentation - A function that prints with 2 new lines after each of these characters: . , ? and :
	> Prototype: def text_indentation(text):
	> text must be a string, otherwise raise a TypeError exception with the message "text mus be a string"
	> There should be no space at the beginning or at the end of each printed line.
	> You are not allowed to import any module.

Task 5: Max integer - Unittest
	> Your test file should be inside a folder tests.
	> You have to use the unittest module
	> Your test file should be python files (extension: .py)
	> Yourtest file should be executed by using this command: python3 -m unittest tests.6-max_integer_test
	> All tests you make must be passable by the function below.
	> We strongly encourage you to work together omn test cases, so that you don't miss any edge case.


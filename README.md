# Iris-Type-Prediction
The code provided is an example of a basic machine learning project. Specifically, it is an implementation of the k-nearest neighbors algorithm to predict the type of iris flower based on user input of the sepal length, sepal width, petal length, and petal width.

This code uses simple Python program that uses the [pandas](https://pandas.pydata.org/) library to read in data from a CSV file, then prompts the user to input values for the sepal length, sepal width, petal length, and petal width of an iris flower. The program then calculates the Euclidean distance between the user input and each row in the dataset, finds the row with the closest distance, and returns the type of iris for that row.

## Installation

To run this program, you will need to have Python 3 installed on your machine, as well as the following libraries:

- pandas
- numpy

You can install these libraries using pip, the Python package manager. Open a terminal or command prompt and run the following command:

```
pip install pandas numpy
```

## Usage

1. Download the `iris.csv` file and the `main.py` script and save them to the same directory on your machine.

2. Open a terminal or command prompt and navigate to the directory where you saved the files.

3. Run the script by typing the following command:

   ```
   python main.py
   ```

4. Follow the prompts to enter values for the sepal length, sepal width, petal length, and petal width of an iris flower.

5. The program will then calculate the closest match to the input values and display the predicted type of iris.

Note: The script contains a `while True` loop that will keep running until you manually stop it. To exit the loop, press `Ctrl + C` on your keyboard.

## License

This program is licensed under the MIT License. Feel free to use and modify the code as you see fit!

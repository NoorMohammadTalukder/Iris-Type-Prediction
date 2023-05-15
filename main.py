import pandas as pd

data = pd.read_csv("iris.csv")

def get_iris_type():
    # Ask the user for input
    sepal_length = float(input("Enter the sepal length: "))
    sepal_width = float(input("Enter the sepal width: "))
    petal_length = float(input("Enter the petal length: "))
    petal_width = float(input("Enter the petal width: "))
    
    # Convert user input to a pandas DataFrame
    input_df = pd.DataFrame([[sepal_length, sepal_width, petal_length, petal_width]], columns=["sepal_length", "sepal_width", "petal_length", "petal_width"])
    # Calculate the Euclidean distance between the user input and each row in the dataset
    distances = ((data.iloc[:, :-1] - input_df) ** 2).sum(axis=1) ** 0.5
    # Find the index of the closest row
    closest_index = distances.idxmin()
    # Return the type of the closest row
    return data.iloc[closest_index, -1]

# Call the function and print the result
while True:
    print("The predicted type of iris is:", get_iris_type())

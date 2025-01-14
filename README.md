# linear_regression_penguins
Prediction of penguins body mass based on its bill lenght, gender and species

This repository contains two Python scripts that use the seaborn, pandas, matplotlib, and statsmodels libraries to perform linear regression analyses on the penguins dataset. The scripts load the dataset, remove missing values, fit linear regression models, and visualize the results. Additionally, they include functions to predict body mass based on user input.

The first script performs a multiple linear regression analysis to understand the relationship between penguin body mass and various predictors such as bill length, gender, and species. The script splits the data into training and testing sets, fits a linear regression model, evaluates the model's performance, and visualizes the results using scatter plots and bar plots. It also allows the user to input specific values for bill length, gender, and species to get a predicted body mass.

The second script performs a simple linear regression analysis to understand the relationship between penguin body mass and bill length. The script fits a simple linear regression model, evaluates the model's performance, and visualizes the results using scatter plots. It also allows the user to input a specific value for bill length to get a predicted body mass.

In summary, these scripts provide statistical approaches to understanding the factors that influence penguin body mass and allow for predictions based on user input.

Getting Started
To run these scripts, you need to have Python 3 and the following libraries installed:

pip install pandas seaborn matplotlib statsmodels scikit-learn

Usage
Clone this repository to your local machine:

git clone https://github.com/<your-username>/penguin-regression.git

Navigate to the cloned repository:

cd penguin-regression

Run the scripts:

python penguin_regression.py

python penguin_simple_regression.py

Follow the prompts and enter the required values.

The scripts will output the predicted body mass based on the input values.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
This project was inspired by the need to analyze the relationship between penguin body mass and various predictors. The statsmodels library made it easy to fit linear regression models and obtain detailed results.

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf

# Load the penguins dataset from the seaborn library
penguins = sns.load_dataset("penguins")

# Remove rows with missing values
penguins = penguins.dropna()

# Define the simple formula
simple_formula = "body_mass_g ~ bill_length_mm"

# Fit the simple linear regression model
simple_model = smf.ols(formula=simple_formula, data=penguins).fit()

# Summary of the simple model
print(simple_model.summary())

# Predictions from the simple model
penguins['simple_predicted_body_mass_g'] = simple_model.predict(penguins)

# Scatter plot with simple regression line for bill_length_mm
plt.figure(figsize=(10, 6))
sns.scatterplot(x='bill_length_mm', y='body_mass_g', hue='species', style='sex', data=penguins, s=100)
sns.lineplot(x='bill_length_mm', y='simple_predicted_body_mass_g', data=penguins, color='red')
plt.xlabel('Bill Length (mm)')
plt.ylabel('Body Mass (g)')
plt.title('Simple Linear Regression: Bill Length vs Body Mass')
plt.legend(title='Species and Sex')
plt.show()

# Function to predict body mass based on operator input
def predict_body_mass():
    bill_length_mm = float(input("Enter bill length (mm): "))

    # Create a DataFrame with the input value
    input_data = pd.DataFrame({
        'bill_length_mm': [bill_length_mm]
    })

    # Make the prediction
    predicted_mass = simple_model.predict(input_data)
    print(f"The predicted body mass is: {predicted_mass.iloc[0]:.2f} g")

# Call the function to predict body mass
predict_body_mass()

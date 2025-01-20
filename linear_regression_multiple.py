import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf
from sklearn.model_selection import train_test_split

# Load the penguins dataset from seaborn library
penguins = sns.load_dataset("penguins")

# Remove rows with missing values
penguins = penguins.dropna()

# Split the data into training and testing sets
train_data, test_data = train_test_split(penguins, test_size=0.3, random_state=42)

# Define the formula
ols_formula = "body_mass_g ~ bill_length_mm + C(sex) + C(species)"

# Fit the linear regression model using the formula on the training set
model = smf.ols(formula=ols_formula, data=train_data).fit()

# Print the model summary
print(model.summary())

# Predictions on the test set
test_data['predicted_body_mass_g'] = model.predict(test_data)

# Scatter plot with regression line for bill_length_mm on the test set
plt.figure(figsize=(10, 6))
sns.scatterplot(x='bill_length_mm', y='body_mass_g', hue='species', style='sex', data=test_data, s=100)
sns.lineplot(x='bill_length_mm', y='predicted_body_mass_g', data=test_data, color='red')
plt.xlabel('Bill Length (mm)')
plt.ylabel('Body Mass (g)')
plt.title('Linear Regression: Bill Length vs Body Mass (Test Set)')
plt.legend(title='Species and Sex')
plt.show()

# Bar plot to visualize the effect of categorical variables on the test set
plt.figure(figsize=(10, 6))
sns.barplot(x='species', y='body_mass_g', hue='sex', data=test_data, ci=None)
plt.xlabel('Species')
plt.ylabel('Body Mass (g)')
plt.title('Body Mass by Species and Sex (Test Set)')
plt.show()

# Function to predict body mass based on operator input
def predict_body_mass():
    bill_length_mm = float(input("Enter bill length (mm): "))
    sex = input("Enter sex (Male/Female): ")
    species = input("Enter species (Adelie/Chinstrap/Gentoo): ")

    # Create a DataFrame with the input values
    input_data = pd.DataFrame({
        'bill_length_mm': [bill_length_mm],
        'sex': [sex],
        'species': [species]
    })

    # Make the prediction
    predicted_mass = model.predict(input_data)
    print(f"The predicted body mass is: {predicted_mass.iloc[0]:.2f} g")

# Call the function to predict body mass
predict_body_mass()

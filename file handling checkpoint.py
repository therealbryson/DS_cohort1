import numpy as np

# Open the CSV file
filename = 'Loan_prediction_dataset.csv'
file = open(filename, 'r')

# Load data using NumPy's genfromtxt function
data = np.genfromtxt(file, delimiter=',')

# Close the file
file.close()

# Calculate mean, median, and standard deviation of loan amounts
loan_amounts = data[:, 4]  # Assuming loan amounts are in the 5th column (index 4)
mean_loan_amount = np.mean(loan_amounts)
median_loan_amount = np.median(loan_amounts)
std_loan_amount = np.std(loan_amounts)

# Print results
print(f"Mean loan amount: {mean_loan_amount}")
print(f"Median loan amount: {median_loan_amount}")
print(f"Standard deviation of loan amounts: {std_loan_amount}")

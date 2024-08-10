import matplotlib.pyplot as plt
import seaborn as sns

# Define your columns
numeric_columns = ['Price', 'Distance', 'Landsize', 'BuildingArea', 'YearBuilt', 'Lattitude', 'Longtitude', 'Propertycount']
categorical_columns = ['Postcode', 'Bedroom2', 'Bathroom', 'Car', 'CouncilArea', 'Regionname']



def plot_numerical_imputation(original_df, imputed_df, column):
    plt.figure(figsize=(12, 6))
    
    # Plot the original data distribution
    sns.histplot(original_df[column], kde=True, color='blue', label='Original')
    
    # Overlay the imputed data distribution
    sns.histplot(imputed_df[column], kde=True, color='red', alpha=0.5, label='Imputed')
    
    plt.title(f'Distribution of {column} with Imputed Values Highlighted')
    plt.legend()
    plt.show()




def plot_categorical_imputation(original_df, imputed_df, column):
    plt.figure(figsize=(10, 6))
    
    # Get the count of original and imputed values
    original_counts = original_df[column].value_counts(dropna=False)
    imputed_counts = imputed_df[column].value_counts(dropna=False) - original_counts
    
    # Create a bar plot for the original counts
    sns.barplot(x=original_counts.index, y=original_counts.values, color='blue', label='Original')
    
    # Overlay the bar plot with the imputed counts
    sns.barplot(x=imputed_counts.index, y=imputed_counts.values, bottom=original_counts.values, color='red', label='Imputed')
    
    plt.title(f'Counts of {column} with Imputed Values Highlighted')
    plt.xticks(rotation=90)
    plt.legend()
    plt.show()






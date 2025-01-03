import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Import data
    data = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(data['Year'], data['CSIRO Adjusted Sea Level'], label='Original Data', alpha=0.6)

    # Create first line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(data['Year'], data['CSIRO Adjusted Sea Level'])
    years_extended = pd.Series(range(1880, 2051))
    best_fit = slope * years_extended + intercept
    plt.plot(years_extended, best_fit, 'r', label='Best Fit: 1880-2050')

    # Create second line of best fit using data from 2000 onwards
    data_2000 = data[data['Year'] >= 2000]
    slope_2000, intercept_2000, r_value_2000, p_value_2000, std_err_2000 = linregress(
        data_2000['Year'], data_2000['CSIRO Adjusted Sea Level']
    )
    years_recent = pd.Series(range(2000, 2051))
    best_fit_recent = slope_2000 * years_recent + intercept_2000
    plt.plot(years_recent, best_fit_recent, 'green', label='Best Fit: 2000-2050')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()

    # Save plot
    plt.savefig('sea_level_plot.png')
    plt.show()

# Run the function to generate the plot
if __name__ == "__main__":
    draw_plot()

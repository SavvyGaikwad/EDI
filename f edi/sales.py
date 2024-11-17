import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# Read the Excel file
df = pd.read_excel('project_data_large.xlsx')

# Convert Project_Date to datetime
df['Project_Date'] = pd.to_datetime(df['Project_Date'], format='%d-%m-%Y')

# Sort by date
df = df.sort_values('Project_Date')

# Create separate dataframes for each type
architecture_df = df[df['Type'] == 'Architecture']
interior_df = df[df['Type'] == 'Interior']

# Create the plot
plt.figure(figsize=(12, 6))

# Plot lines
plt.plot(architecture_df['Project_Date'], architecture_df['Revenue_Generated'].cumsum(), 
         color='blue', label='Architecture', linewidth=2)
plt.plot(interior_df['Project_Date'], interior_df['Revenue_Generated'].cumsum(), 
         color='orange', label='Interior', linewidth=2)

# Customize the plot
plt.title('Cumulative Revenue by Project Type Over Time', pad=20, size=14)
plt.xlabel('Date', size=12)
plt.ylabel('Cumulative Revenue (\u20b9)', size=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(fontsize=10)

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)

# Format y-axis labels to show millions
current_values = plt.gca().get_yticks()
plt.gca().set_yticklabels(['{:.1f}M'.format(x/1e6) for x in current_values])

# Adjust layout to prevent label cutoff
plt.tight_layout()

# Save the plot as an image file
plt.savefig('sales.png')

# Show the plot
plt.show()

# Print summary statistics
print("\
Total Revenue by Project Type:")
print(df.groupby('Type')['Revenue_Generated'].sum().apply(lambda x: f"\u20b9{x:,.2f}"))

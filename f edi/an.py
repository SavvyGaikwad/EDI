import pandas as pd
import matplotlib.pyplot as plt
import os

# Load the data from Excel
file_path = r'C:\Users\hp\OneDrive\Desktop\f edi\project_data_large.xlsx'  # Replace with your actual file path

df = pd.read_excel(file_path)

# Clean column names by stripping any leading/trailing spaces
df.columns = df.columns.str.strip()

# Print the column names to check
print(df.columns)

# Perform the groupby operation
revenue_by_type = df.groupby('Type')['Revenue_Generated'].sum()

# Total revenue by city
revenue_by_city = df.groupby('Site_City')['Revenue_Generated'].sum()

# Total revenue by manager
revenue_by_manager = df.groupby('Manager_Name')['Revenue_Generated'].sum()

# Plotting Pie Charts side by side
plt.figure(figsize=(18, 6))  # Adjust the figure size for side-by-side layout

# Pie chart for revenue by project type
plt.subplot(1, 3, 1)  # 1 row, 3 columns, first subplot
plt.pie(revenue_by_type, labels=revenue_by_type.index, autopct='%1.1f%%', startangle=140)
plt.title('Revenue Distribution by Project Type')

# Pie chart for revenue by city
plt.subplot(1, 3, 2)  # 1 row, 3 columns, second subplot
plt.pie(revenue_by_city, labels=revenue_by_city.index, autopct='%1.1f%%', startangle=140)
plt.title('Revenue Distribution by City')

# Pie chart for revenue by manager
plt.subplot(1, 3, 3)  # 1 row, 3 columns, third subplot
plt.pie(revenue_by_manager, labels=revenue_by_manager.index, autopct='%1.1f%%', startangle=140)
plt.title('Revenue Distribution by Manager')

# Ensure the file path is correct and set the save path
save_path = os.path.join(os.path.dirname(file_path), 'analysis_side_by_side.png')

# Delete the existing file if it exists
if os.path.exists(save_path):
    os.remove(save_path)

# Save the plot as an image
plt.tight_layout()
plt.savefig(save_path)

# Show the plots
plt.show()

print(f"Image saved as: {save_path}")

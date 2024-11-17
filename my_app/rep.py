import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the Excel file
df = pd.read_excel('Mediation Hall.xlsx')

# Get the last row details
last_row = df.iloc[-1]
project_info = f"Project Name: {last_row['Project Name']}\n\
Site Name: {last_row['Project Site']}\n\
Client Name: {last_row['Client Name']}"

# Convert timestamp to date only
df['Date'] = pd.to_datetime(df['Timestamp']).dt.date

# Create timeline visualization
fig, ax = plt.subplots(figsize=(12, 6))
sns.set_style('whitegrid')

# Add project info at the top with better positioning
plt.figtext(0.5, 0.95, project_info, ha='center', va='top', fontsize=12, 
            bbox=dict(facecolor='white', edgecolor='black', alpha=0.8, pad=10))

# Create the timeline
plt.plot(df['Date'], [1]*len(df), marker='o', linestyle='-', linewidth=2, markersize=10, color='blue')
plt.yticks([])

# Add annotations with improved spacing
for idx, row in df.iterrows():
    plt.annotate(f"Status: {row['Status']}\n\
Timeline: {row['Expected Timeline']}", 
                (row['Date'], 1),
                xytext=(0, -25), 
                textcoords='offset points',
                ha='center',
                va='top',
                bbox=dict(boxstyle='round,pad=0.5', fc='white', ec='gray', alpha=0.8))

plt.title('Project Timeline', pad=50)
plt.xlabel('Date')
plt.xticks(rotation=45)
plt.subplots_adjust(top=0.8)
plt.show()

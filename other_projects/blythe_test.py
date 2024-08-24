import pandas as pd

# Load the Excel file and read the first column
excel_file_path = '/Users/guystamant/launch_school/other_projects/中文筆記Index.xlsx'  # Replace with your Excel file path
df = pd.read_excel(excel_file_path)

# Extract titles from the first column
titles = df.iloc[:, 0].astype(str).tolist()

# Load the plain text document
text_file_path = '/Users/guystamant/launch_school/other_projects/Guanzhui bian minus addenda'  # Replace with your text file path
with open(text_file_path, 'r', encoding='utf-8') as file:
    text_content = file.read()

# Count occurrences of each title in the text document
title_counts = {title: text_content.count(title) for title in titles}

# Create a new DataFrame for the output
output_df = pd.DataFrame(list(title_counts.items()), columns=['Title', 'Count'])

# Save the output to a new Excel file
output_excel_path = 'title_counts.xlsx'  # Replace with your desired output file path
output_df.to_excel(output_excel_path, index=False)

print(f"Title counts have been successfully saved to {output_excel_path}.")
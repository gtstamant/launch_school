import pandas as pd
import re

# Load the Excel file and read the first column
excel_file_path = '/Users/guystamant/launch_school/other_projects/中文筆記Index.xlsx'  # Replace with your Excel file path
df = pd.read_excel(excel_file_path)

# Extract titles from the first column and ensure all are treated as strings
titles = df.iloc[:, 0].astype(str).tolist()

# Read the content of the plain text document
file_path = '/Users/guystamant/launch_school/other_projects/Guanzhui bian minus addenda'
with open(file_path, 'r', encoding='utf-8') as file:
    text_content = file.read()

# Initialize a dictionary to hold the total count and sections for each title
title_data = {title: {'count': 0, 'sections': []} for title in titles}

# Split text content into sections based on the pattern #section_identifier#
sections = re.split(r'(#[^#]+#)', text_content)

# Iterate over the split content to pair section names with their respective content
current_section = None

for segment in sections:
    if re.match(r'#[^#]+#', segment):
        # This is a section header
        current_section = segment.strip('#').strip()
    elif current_section:
        # This is the content of a section
        for title in titles:
            count = segment.count(title)
            # Add to the total count for the title
            title_data[title]['count'] += count
            # If the title is found in this section and section is valid, add the section
            if count > 0 and current_section not in title_data[title]['sections']:
                title_data[title]['sections'].append(current_section)

# Prepare data for output
output_data = []
for title, data in title_data.items():
    num_sections = len(data['sections'])  # Count of unique sections where the title appears
    sections_str = ', '.join(data['sections'])  # Join sections into a single string
    output_data.append([title, data['count'], num_sections, sections_str])

# Create a new DataFrame for the output
output_df = pd.DataFrame(output_data, columns=['Title', 'Count', 'Number of Sections', 'Sections'])

# Save the output to a new Excel file
output_excel_path = 'title_counts_with_sections.xlsx'  # Replace with your desired output file path
output_df.to_excel(output_excel_path, index=False)

print(f"Title counts and sections have been successfully saved to {output_excel_path}.")
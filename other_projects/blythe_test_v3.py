import pandas as pd
import re

# Step 1: Build the Data Structure from the Cleaned Text File
def build_data_structure(cleaned_file_path):
    # Read the cleaned content of the plain text document
    with open(cleaned_file_path, 'r', encoding='utf-8') as file:
        cleaned_text_content = file.read()

    # Initialize a dictionary to store sections
    sections_dict = {}

    # Split text content into sections based on the pattern #section_identifier#
    sections = re.split(r'(#[^#]+#)', cleaned_text_content)

    # Iterate through sections to populate the dictionary
    for i in range(1, len(sections), 2):  # Use step 2 to handle header-content pairs
        section_header = sections[i].strip('#').strip()  # Clean the section header
        section_content = sections[i + 1].strip() if i + 1 < len(sections) else ''  # Corresponding content

        # Store the section in the dictionary
        sections_dict[section_header] = section_content

    return sections_dict

# Step 2: Remove Duplicate Titles from the Excel File
def get_unique_titles(excel_file_path):
    # Load the Excel file and read the first column for the list of titles
    df = pd.read_excel(excel_file_path)

    # Extract titles from the first column and ensure all are treated as strings
    titles = df.iloc[:, 0].astype(str).tolist()

    # Remove duplicates from the list of titles
    unique_titles = list(set(titles))

    return unique_titles

# Step 3: Count Occurrences and Produce the Final Excel
def count_occurrences_and_produce_excel(sections_dict, unique_titles, output_excel_path):
    # Initialize a dictionary to hold the total count and sections for each title
    title_data = {title: {'count': 0, 'sections': []} for title in unique_titles}

    # Iterate through sections in the sections_dict to count title occurrences
    for section_header, section_content in sections_dict.items():
        for title in unique_titles:
            # Use simple string count to find occurrences of the title
            count = section_content.count(title)
            
            # Add to the total count for the title
            title_data[title]['count'] += count

            # If the title is found in this section and the section is not already recorded, add the section
            if count > 0 and section_header not in title_data[title]['sections']:
                title_data[title]['sections'].append(section_header)

    # Prepare data for output
    output_data = []
    for title, data in title_data.items():
        num_sections = len(data['sections'])  # Count of unique sections where the title appears
        sections_str = ', '.join(data['sections'])  # Join sections into a single string
        output_data.append([title, data['count'], num_sections, sections_str])

    # Create a new DataFrame for the output
    output_df = pd.DataFrame(output_data, columns=['Title', 'Count', 'Number of Sections', 'Sections'])

    # Save the output to a new Excel file
    output_df.to_excel(output_excel_path, index=False)
    print(f"Title counts and sections have been successfully saved to {output_excel_path}.")

# Paths to the necessary files
cleaned_file_path = '/Users/guystamant/launch_school/other_projects/guanzhui_bian_no_notes.txt'  # Path to the cleaned text document
excel_file_path = '/Users/guystamant/launch_school/other_projects/中文筆記Index.xlsx'  # Path to the Excel file with titles
output_excel_path = 'title_counts_with_sections_final_v4.xlsx'  # Path for the final output Excel file

# Execute the steps
sections_dict = build_data_structure(cleaned_file_path)
unique_titles = get_unique_titles(excel_file_path)
count_occurrences_and_produce_excel(sections_dict, unique_titles, output_excel_path)

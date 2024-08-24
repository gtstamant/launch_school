import re
from collections import defaultdict

# Read the cleaned content of the plain text document after manual notes removal
cleaned_file_path = '/Users/guystamant/launch_school/other_projects/guanzhui_bian_no_notes.txt'  # Replace with your cleaned document path
with open(cleaned_file_path, 'r', encoding='utf-8') as file:
    cleaned_text_content = file.read()

# Split text content into sections based on the pattern #section_identifier#
sections = re.split(r'(#[^#]+#)', cleaned_text_content)

# Initialize a dictionary to track section headers and their occurrences
section_counts = defaultdict(int)
section_contents = defaultdict(str)

# Iterate through sections to track occurrences
for i in range(1, len(sections), 2):  # Use step 2 to handle header-content pairs
    section_header = sections[i].strip('#').strip()  # Clean the section header
    section_content = sections[i + 1].strip() if i + 1 < len(sections) else ''  # Corresponding content

    # Increment the count for this section header
    section_counts[section_header] += 1
    section_contents[section_header] = section_content

# Find all duplicate sections
duplicates = {header: count for header, count in section_counts.items() if count > 1}

# Output the list of duplicates for manual review
print(duplicates)
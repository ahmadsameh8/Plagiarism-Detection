import os
import xml.etree.ElementTree as ET
import pandas as pd

# Define the exact directories for suspicious and source documents
suspicious_folder = r"C:\Users\medhat6969\Downloads\ExAraCorpusPAN2015\ExAraCorpusPAN2015\ExAraCorpusPAN2015\ExAraPlagDet-10-08-2015-Training\suspicious-documents"
source_folder = r"C:\Users\medhat6969\Downloads\ExAraCorpusPAN2015\ExAraCorpusPAN2015\ExAraCorpusPAN2015\ExAraPlagDet-10-08-2015-Training\source-documents"
xml_base_folder = r"C:\Users\medhat6969\Downloads\ExAraCorpusPAN2015\ExAraCorpusPAN2015\ExAraCorpusPAN2015\ExAraPlagDet-10-08-2015-Training\plagiarism-annotation"

# Prepare a list to store the CSV rows
csv_data = []

# Function to extract text content from a file and check for Arabic encoding issues
def get_file_content(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read().strip()
            if content:
                print(f"Successfully read content from {file_path}")
                return content
            else:
                print(f"File {file_path} is empty.")
                return None
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None
    except UnicodeDecodeError as e:
        print(f"Encoding issue with file: {file_path} - {e}")
        return None

# Recursively process the XML files from subfolders in the plagiarism-annotation directory
for subfolder in os.listdir(xml_base_folder):
    subfolder_path = os.path.join(xml_base_folder, subfolder)
    
    # Only process subfolders
    if os.path.isdir(subfolder_path):
        print(f"Processing subfolder: {subfolder}")
        
        # Loop over each XML file in the current subfolder
        for xml_file in os.listdir(subfolder_path):
            if xml_file.endswith('.xml'):
                xml_path = os.path.join(subfolder_path, xml_file)
                try:
                    tree = ET.parse(xml_path)
                    root = tree.getroot()
                    print(f"Processing XML file: {xml_file}")
                except ET.ParseError:
                    print(f"Failed to parse XML file: {xml_file}")
                    continue

                # The corresponding suspicious document
                suspicious_file_name = xml_file.replace('.xml', '.txt')
                suspicious_file_path = os.path.join(suspicious_folder, suspicious_file_name)
                suspicious_content = get_file_content(suspicious_file_path)

                if suspicious_content is None:
                    print(f"Skipping suspicious document {suspicious_file_name} because it's missing or empty.")
                    continue

                # Process each plagiarism feature and extract all attributes
                for plagiarism in root.findall('feature'):
                    # Extract feature attributes
                    this_offset = plagiarism.get('this_offset')
                    this_length = plagiarism.get('this_length')
                    source_reference = plagiarism.get('source_reference')
                    source_offset = plagiarism.get('source_offset')
                    source_length = plagiarism.get('source_length')
                    obfuscation = plagiarism.get('obfuscation')
                    plagiarism_type = plagiarism.get('type')

                    # Get the source document content if available
                    source_content = ""
                    if source_reference:
                        source_file_path = os.path.join(source_folder, source_reference)
                        source_doc_content = get_file_content(source_file_path)
                        if source_doc_content:
                            source_content = source_doc_content
                        else:
                            print(f"Skipping source document {source_reference} because it's missing or empty.")

                    # Append all the extracted information to the CSV data
                    csv_data.append({
                        'suspicious_file': suspicious_file_name,
                        'suspicious_content': suspicious_content,
                        'plagiarism_type': subfolder,  # Record the subfolder type (e.g., 01-no-plagiarism)
                        'source_file': source_reference,
                        'source_content': source_content,
                        'this_offset': this_offset,
                        'this_length': this_length,
                        'source_offset': source_offset,
                        'source_length': source_length,
                        'obfuscation': obfuscation,
                        'type': plagiarism_type
                    })

# Create a DataFrame from the CSV data
if csv_data:
    df = pd.DataFrame(csv_data)

    # Save the DataFrame to a CSV file
    csv_output_path = 'plagiarism_detection_output_with_features.csv'
    df.to_csv(csv_output_path, index=False, encoding='utf-8-sig')  # Using utf-8-sig to ensure proper Arabic handling in Excel

    print(f"CSV file saved to {csv_output_path}")
else:
    print("No data to save to CSV. The CSV file will not be created.")

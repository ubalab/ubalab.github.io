import os

def find_html_files(directory):
    """Finds all HTML files in the given directory and its subdirectories."""
    html_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".html"):
                html_files.append(os.path.join(root, file))
    return html_files

def process_html_file(filepath, message):
    """
    Reads an HTML file, inserts the message after </header> if not already present, 
    and writes it back.
    Returns a status string: "modified", "skipped_exists", "skipped_no_header", 
                             "error_read", "error_write".
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"Warning: Could not read file {filepath}: {e}")
        return "error_read"

    if message in content:
        print(f"Info: Message already present in {filepath}. Skipping file.")
        return "skipped_exists"

    header_end_tag = '</header>'
    header_end_index = content.find(header_end_tag)

    if header_end_index == -1:
        print(f"Warning: '</header>' tag not found in {filepath}. Skipping file.")
        return "skipped_no_header"

    insert_position = header_end_index + len(header_end_tag)
    modified_content = content[:insert_position] + message + content[insert_position:]

    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(modified_content)
        return "modified"
    except Exception as e:
        print(f"Warning: Could not write to file {filepath}: {e}")
        return "error_write"

def main():
    """Main function to process HTML files."""
    archive_message = '<div class="container" style="background-color: #fcf8e3; padding: 15px; margin-bottom: 20px; border: 1px solid #faebcc; color: #8a6d3b;">Este website foi arquivado em 2019 e não será mais atualizado. Se tiver interesse em saber mais sobre as atividades do UbaLab (2009-2019), entre em contato com <a href="https://efeefe.me">Felipe Schmidt Fonseca</a>.</div>'
    
    current_directory = '.'
    html_files = find_html_files(current_directory)

    modified_files_count = 0
    skipped_exists_count = 0
    skipped_no_header_count = 0
    error_read_count = 0
    error_write_count = 0
    
    if not html_files:
        print("No HTML files found in the current directory and its subdirectories.")
        return

    total_files = len(html_files)
    print(f"Found {total_files} HTML file(s) to process.")

    for i, filepath in enumerate(html_files):
        print(f"Processing file {i+1}/{total_files}: {filepath}...")
        status = process_html_file(filepath, archive_message)
        
        if status == "modified":
            modified_files_count += 1
            print(f"Successfully modified {filepath}")
        elif status == "skipped_exists":
            skipped_exists_count += 1
        elif status == "skipped_no_header":
            # Warning already printed by process_html_file
            skipped_no_header_count += 1
        elif status == "error_read":
            error_read_count += 1
        elif status == "error_write":
            error_write_count += 1
            
    print("\n--- Summary ---")
    print(f"Total HTML files found: {total_files}")
    print(f"Files successfully modified: {modified_files_count}")
    print(f"Files skipped (message already existed): {skipped_exists_count}")
    print(f"Files skipped (no '</header>' tag): {skipped_no_header_count}")
    print(f"Errors reading files: {error_read_count}")
    print(f"Errors writing files: {error_write_count}")

if __name__ == "__main__":
    main()

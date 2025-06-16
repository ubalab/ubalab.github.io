import os
import sys

def update_html_files(directory_path):
    replacements = {
        "http://cdn.jsdelivr.net/bootswatch/3.3.7/yeti/bootstrap.css": "https://cdn.jsdelivr.net/bootswatch/3.3.7/yeti/bootstrap.css",
        "http://code.jquery.com/jquery-1.9.1.js": "https://code.jquery.com/jquery-1.9.1.js",
        "http://cdn.jsdelivr.net/bootstrap/3.3.7/js/bootstrap.js": "https://cdn.jsdelivr.net/bootstrap/3.3.7/js/bootstrap.js"
    }
    updated_files_count = 0
    processed_files_count = 0
    for root, _, files in os.walk(directory_path):
        for filename in files:
            if filename.endswith(".html"):
                filepath = os.path.join(root, filename)
                processed_files_count += 1
                try:
                    with open(filepath, 'r', encoding='utf-8', errors='replace') as file:
                        content = file.read()
                    original_content = content
                    modified_content = content
                    for old_url, new_url in replacements.items():
                        modified_content = modified_content.replace(old_url, new_url)
                    if modified_content != original_content:
                        with open(filepath, 'w', encoding='utf-8') as file:
                            file.write(modified_content)
                        print(f"UPDATED: {filepath}")
                        updated_files_count += 1
                except Exception as e:
                    print(f"ERROR processing {filepath}: {e}")
    print(f"--- Summary ---")
    print(f"Processed {processed_files_count} HTML files.")
    print(f"Updated {updated_files_count} HTML files for mixed content.")

if __name__ == "__main__":
    target_directory = "."
    if len(sys.argv) > 1:
        target_directory = sys.argv[1]
    print(f"Starting update in directory: {os.path.abspath(target_directory)}")
    update_html_files(target_directory)
    print("Script finished. Review changes before committing.")

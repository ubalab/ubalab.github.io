#!/usr/bin/python3
import os

replacements = {
    "http://cdn.jsdelivr.net/bootswatch/3.3.7/yeti/bootstrap.css": "https://cdn.jsdelivr.net/bootswatch/3.3.7/yeti/bootstrap.css",
    "http://code.jquery.com/jquery-1.9.1.js": "https://code.jquery.com/jquery-1.9.1.js",
    "http://cdn.jsdelivr.net/bootstrap/3.3.7/js/bootstrap.js": "https://cdn.jsdelivr.net/bootstrap/3.3.7/js/bootstrap.js"
}

processed_files_count = 0
updated_files_count = 0

for root, _, files in os.walk("."):
    for filename in files:
        if filename.endswith(".html"):
            filepath = os.path.join(root, filename)
            processed_files_count += 1

            try:
                with open(filepath, 'r', encoding='utf-8', errors='ignore') as file: # Added errors='ignore' for robustness
                    content = file.read()
            except Exception as e:
                print(f"Error reading {filepath}: {e}")
                continue

            original_content = content
            modified_content = content
            made_change = False

            for old_url, new_url in replacements.items():
                if old_url in modified_content:
                    modified_content = modified_content.replace(old_url, new_url)
                    made_change = True

            if made_change:
                try:
                    with open(filepath, 'w', encoding='utf-8') as file:
                        file.write(modified_content)
                    print(f"UPDATED (mixed content): {filepath}")
                    updated_files_count += 1
                except Exception as e:
                    print(f"Error writing {filepath}: {e}")
            # else: # Optional: reduce verbosity by not printing "no changes needed" for every file
            #    print(f"No changes needed for (mixed content): {filepath}")

print("\n--- Mixed content update process complete ---")
print(f"Processed {processed_files_count} HTML files.")
print(f"Updated {updated_files_count} HTML files for mixed content.")

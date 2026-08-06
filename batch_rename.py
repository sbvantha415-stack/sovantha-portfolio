import os
import re

PROJECT_DIR = "."

def make_url_friendly(filename):
    name, ext = os.path.splitext(filename)
    if filename.startswith(".") or filename.endswith(".py"):
        return filename

    clean_name = name.lower().strip()
    clean_name = re.sub(r'[\s_]+', '-', clean_name)
    clean_name = re.sub(r'[^a-z0-9\-]', '', clean_name)
    clean_name = re.sub(r'-+', '-', clean_name)
    
    return f"{clean_name}{ext.lower()}"

def update_html_references(renames):
    for root, _, files in os.walk(PROJECT_DIR):
        for file in files:
            if file.endswith(".html"):
                html_path = os.path.join(root, file)
                with open(html_path, "r", encoding="utf-8", errors="ignore") as f:
                    content = f.read()

                updated_content = content
                for old_name, new_name in renames.items():
                    if old_name in updated_content:
                        updated_content = updated_content.replace(old_name, new_name)

                if updated_content != content:
                    with open(html_path, "w", encoding="utf-8") as f:
                        f.write(updated_content)
                    print(f"📄 Updated links in: {file}")

def batch_rename():
    renames = {}
    for root, _, files in os.walk(PROJECT_DIR):
        if "venv" in root or ".git" in root:
            continue

        for file in files:
            new_file = make_url_friendly(file)
            if file != new_file:
                old_path = os.path.join(root, file)
                new_path = os.path.join(root, new_file)
                
                os.rename(old_path, new_path)
                renames[file] = new_file
                print(f"✅ Renamed: '{file}' ➔ '{new_file}'")

    if renames:
        print("\nUpdating internal references in HTML files...")
        update_html_references(renames)
        print("\n🎉 Done! All files are now URL-friendly and links are updated.")
    else:
        print("✨ All files are already URL-friendly!")

if __name__ == "__main__":
    batch_rename()
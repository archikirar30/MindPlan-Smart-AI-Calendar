import subprocess
import re
from pathlib import Path

README_PATH = Path("README.md")

# Step 1: Get current pip dependencies
def get_dependencies():
    result = subprocess.run(["pip", "freeze"], capture_output=True, text=True)
    packages = result.stdout.strip().split("\n")
    # Optional: remove versions for simplicity
    packages_simple = [pkg.split("==")[0] for pkg in packages if "==" in pkg]
    return packages_simple

# Step 2: Read README
def read_readme():
    if README_PATH.exists():
        return README_PATH.read_text(encoding="utf-8")
    return ""

# Step 3: Replace Dependencies section
def update_dependencies(readme_text, deps):
    deps_text = "\n".join(f"- `{dep}`" for dep in deps)
    new_section = f"## 📦 Dependencies\n\n{deps_text}\n\n> Keep this updated with `pip freeze > requirements.txt` after adding new packages."

    # Use regex to replace old Dependencies section
    pattern = r"(## 📦 Dependencies\n\n)(.*?)(\n\n> Keep this updated.*?)"
    if re.search(pattern, readme_text, flags=re.DOTALL):
        readme_text = re.sub(pattern, new_section, readme_text, flags=re.DOTALL)
    else:
        # If Dependencies section does not exist, append at the end
        readme_text += "\n\n" + new_section
    return readme_text

# Step 4: Write back README
def write_readme(text):
    README_PATH.write_text(text, encoding="utf-8")   # <- add encoding
    print("✅ README.md dependencies updated!")

# Main
if __name__ == "__main__":
    deps = get_dependencies()
    readme = read_readme()
    updated_readme = update_dependencies(readme, deps)
    write_readme(updated_readme)

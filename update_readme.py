import subprocess
from pathlib import Path
import re

# Paths
README_PATH = Path("README.md")
FEATURES_FILE = Path("features.txt")
BUGS_FILE = Path("bugs.txt")

# -------------------------------
# 1️⃣ Get current pip dependencies
# -------------------------------
def get_dependencies():
    result = subprocess.run(["pip", "freeze"], capture_output=True, text=True)
    packages = result.stdout.strip().split("\n")
    # Simplify: remove versions
    packages_simple = [pkg.split("==")[0] for pkg in packages if "==" in pkg]
    return packages_simple

# -------------------------------
# 2️⃣ Read README, Features, Bugs
# -------------------------------
def read_file(path):
    return path.read_text(encoding="utf-8") if path.exists() else ""

def read_list_file(path):
    text = read_file(path)
    return [line.strip() for line in text.splitlines() if line.strip()]

# -------------------------------
# 3️⃣ Update sections
# -------------------------------
def update_section(header, items, readme_text):
    """Replace or append section"""
    section_text = f"## {header}\n\n" + "\n".join(f"- {item}" for item in items) + "\n"
    pattern = rf"(## {re.escape(header)}\n\n.*?)(?=\n## |\Z)"
    if re.search(pattern, readme_text, flags=re.DOTALL):
        readme_text = re.sub(pattern, section_text, readme_text, flags=re.DOTALL)
    else:
        readme_text += "\n" + section_text
    return readme_text

# -------------------------------
# 4️⃣ Write README
# -------------------------------
def write_readme(text):
    README_PATH.write_text(text, encoding="utf-8")
    print("✅ README.md updated successfully!")

# -------------------------------
# 5️⃣ Main
# -------------------------------
if __name__ == "__main__":
    # Get data
    deps = get_dependencies()
    features = read_list_file(FEATURES_FILE)
    bugs = read_list_file(BUGS_FILE)
    readme_text = read_file(README_PATH)

    # Update sections
    readme_text = update_section("📦 Dependencies", deps, readme_text)
    readme_text = update_section("⚡ Features", features, readme_text)
    readme_text = update_section("📝 Updating the README", bugs, readme_text)

    # Write README
    write_readme(readme_text)

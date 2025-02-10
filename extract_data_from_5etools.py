import os

import requests

# GitHub API URL for the 'data' folder
GITHUB_API_URL = (
    "https://api.github.com/repos/5etools-mirror-3/5etools-src/contents/data"
)

# Headers for the API request
HEADERS = {
    "Accept": "application/vnd.github+json",
    "X-GitHub-Api-Version": "2022-11-28",
}

# Local directory where files will be saved
OUTPUT_DIR = "data"
os.makedirs(OUTPUT_DIR, exist_ok=True)


def download_file(file_url, local_path):
    """Download a single file from GitHub and save it locally."""
    print(f"⬇️ Downloading: {local_path}...")
    response = requests.get(file_url)

    if response.status_code == 200:
        with open(local_path, "wb") as f:
            f.write(response.content)
        print(f"✅ Saved: {local_path}")
    else:
        print(f"❌ Failed to download: {file_url}")


def process_folder(folder_url, local_folder):
    """Recursively process files and subfolders in a GitHub repository folder."""
    print(f"\n📂 Fetching folder: {folder_url}")

    # Create the corresponding local folder
    os.makedirs(local_folder, exist_ok=True)

    # Fetch folder contents from GitHub API
    response = requests.get(folder_url, headers=HEADERS)

    if response.status_code == 200:
        items = response.json()

        for item in items:
            item_name = item["name"]
            item_path = os.path.join(local_folder, item_name)

            if item["type"] == "file":  # Download files
                download_file(item["download_url"], item_path)

            elif item["type"] == "dir":  # Process subdirectories recursively
                new_folder_url = f"https://api.github.com/repos/5etools-mirror-3/5etools-src/contents/{item['path']}"
                process_folder(new_folder_url, item_path)

    else:
        print(
            f"❌ Failed to fetch folder contents: {folder_url} ({response.status_code})"
        )


# Start processing from the main 'data' folder
process_folder(GITHUB_API_URL, OUTPUT_DIR)

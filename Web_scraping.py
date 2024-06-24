import os
import requests

def download_pdf(url, folder):
    # Get the file name from the URL
    file_name = url.split('/')[-1]
    file_path = os.path.join(folder, file_name)

    try:
        # Send HTTP request to the URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)

        # Write the content of the response to a file
        with open(file_path, 'wb') as f:
            f.write(response.content)
        print(f'Successfully downloaded: {file_name}')
    except requests.exceptions.RequestException as e:
        print(f'Failed to download: {file_name}. Error: {e}')

# Define the URL of the PDF and the folder to save it
url = 'https://main.sci.gov.in/judgment/judis/'
folder = 'dataset'

# Create the folder if it doesn't exist
if not os.path.exists(folder):
    os.makedirs(folder)

# Download the PDF
for i in range(1,12855):
    ur=url+str(i)+".pdf"
    download_pdf(ur, folder)


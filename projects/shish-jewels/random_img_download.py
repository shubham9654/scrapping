import requests, os

image_url = "http://shishjewels.com/wp-content/uploads/2022/02/NECKLACE.jpg"

# Send an HTTP GET request to the URL
response = requests.get(image_url)
if response.status_code == 200:
  image_data = response.content
  directory_path = "/home/shubhamsarkar/Desktop/bruce/python-project/scrapping/"
  os.makedirs(directory_path, exist_ok=True)
  local_image_path = os.path.join(directory_path, 'image.jpg')

  with open(local_image_path, "wb") as image_file:
    image_file.write(image_data)

    print(f"Image downloaded and saved to {local_image_path}")
else:
    print(f"Failed to download image. Status code: {response.status_code}")

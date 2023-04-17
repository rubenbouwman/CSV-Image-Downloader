from pandas import * # pip install pandas
import requests # pip install requests

# -------------------- Setup --------------------
# Reading CSV file
data = read_csv("CSV Files/Bol-product-reviews.csv") # Path to your CSV File

# converting column data to list
images = data['img'].tolist() # change the string within [] to the collumn name containing the image URL'S

# -------------------- Methods --------------------
# Method to download an image from a given URL
def downloadImage(imageURL):
    response = requests.get(imageURL).content
    filename = imageURL.split('/')[-1]
    with open('Images/' + filename, 'wb') as handler:
        print('Downloading: ' + filename)
        handler.write(response)

# Method to download all images from the links in the list
def downloadAllImages():
    print('Starting download...')
    for imageURL in images:
        downloadImage(imageURL)
    print('Finished downloading!')

# -------------------- Run --------------------
downloadAllImages()

from pandas import * # pip install pandas
import requests # pip install requests

# -------------------- Setup --------------------
# Reading CSV file
data = read_csv("CSV Files/Decathlon-product-reviews.csv") # Path to your CSV File

# converting column data to list
images = data['Img'].tolist() # change the string within [] to the collumn name containing the image URL'S

# -------------------- Methods --------------------
# Method to download all images from the links in the list
def imageDownloader():
    for imageURL in images:
        response = requests.get(imageURL).content
        filename = imageURL.split('/')[-1]
        with open('Images/' + filename, 'wb') as handler:
            handler.write(response)

# -------------------- Run --------------------
imageDownloader()

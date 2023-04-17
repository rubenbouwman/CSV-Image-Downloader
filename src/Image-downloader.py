from pandas import * # pip install pandas
import requests # pip install requests

# -------------------- Setup --------------------
# Reading CSV file
data = read_csv("CSV Files/Decathlon-product-reviews.csv")

# converting column data to list
Images = data['Img'].tolist()

# -------------------- Methods --------------------
# Method to download all images from the links in the list
def imageDownloader():
    for imageURL in Images:
        response = requests.get(imageURL).content
        filename = imageURL.split('/')[-1]
        with open('Images/' + filename, 'wb') as handler:
            handler.write(response)

# -------------------- Run --------------------
imageDownloader()

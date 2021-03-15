from bs4 import BeautifulSoup
import requests
import os
import PySimpleGUI as sg



def folder_create(images):
    global folder_name
    try:
        folder_name = input("Folder: ")
        os.mkdir(folder_name)
    except:
        pass

    download_images(images, folder_name)
    
def download_images(images, folder_name):
    global image_link
    count = 0
    print(f"Total {len(images)} images found")
    if len(images) != 0:
        for i, image in enumerate(images):
            try:
                image_link = image["src"]
            except:
                pass
            try:
                r = requests.get(image_link).content
                with open(f"{folder_name}/images{i + 1}.jpg", "wb+") as f:
                    f.write(r)
                    count += 1
            except:
                pass
        if count == len(images):
            print("All images downloaded")

def main(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    images = soup.findAll('img')
    folder_create(images)


url = input("URL: ")

main(url)

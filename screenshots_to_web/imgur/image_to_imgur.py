from screenshots_to_web.imgur.auth import get_imgur_client
import pyperclip

client = get_imgur_client(skip_auth=True)

config = {
    'album': None,
    'name': 'Second Upload via CLI',
    'title': 'Second Upload via CLI',
    'description': 'A Screenshot of my linked in profile'
}

print("Uploading image... ")
image = client.upload_from_path('ImageToUpload.png', config=config, anon=False)
print("Done")
print()

print("Image was posted! Go check your images you sexy beast!")
print()
print()
print('Image = ')
print(image)
print()
print()
link = image['link']
print("You can find it here: {0}".format(link))
pyperclip.copy(link)


import os
import pyperclip

from screenshots_to_web.imgur.auth import get_imgur_client
from utils.hash_utils import generate_random_string_of_length

def screenshot_to_imgur():
    client = get_imgur_client(skip_auth=True)
    image_name = generate_random_string_of_length()

    config = {
        'album': None,
        'name': image_name,
        'title': image_name,
        'description': ''
    }

    print(f'Taking a screenshot and storing it into {image_name}.png ...')
    os.system(f'screencapture -i {image_name}.png')

    print(f'Uploading image {image_name}.png to imgur ')
    image = client.upload_from_path(f'{image_name}.png', config=config, anon=False)

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

    osascript = f'''
        osascript <<EOF
        display notification "Copied URL to clipboard" with title "{link}"
        EOF
    '''
    os.system(osascript)

    print(f'Removing {image_name}.png file')
    os.system(f'rm {image_name}.png')






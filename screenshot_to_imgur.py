#!/usr/local/bin/python3
from image_to_imgur import upload_img_to_imgur, access_keys_exist
from imgur.auth import get_imgur_client
from utils.hash_utils import generate_random_string_of_length
from utils.system_utils import take_screenshot, remove_file, display_notification, copy_to_clipboard


def main():
    img_name = generate_random_string_of_length(10)
    img_path = f'{img_name}.png'
    take_screenshot(img_path)

    if access_keys_exist():
        url = upload_img_to_imgur(img_name, img_path, with_auth=False)
    else:
        url = upload_img_to_imgur(img_name, img_path, with_auth=True)

    copy_to_clipboard(url)
    remove_file(img_path)


if __name__ == '__main__':
    main()



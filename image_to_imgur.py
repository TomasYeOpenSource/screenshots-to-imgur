from imgurpython.helpers.error import ImgurClientRateLimitError

from imgur.auth import get_imgur_client


def access_keys_exist():
    return True


def upload_img_to_imgur(img_name, img_path, img_description=None, album=None, with_auth=False):
    client = get_imgur_client(with_auth=with_auth)
    try:
        config = {
            'album': album,
            'name': img_name,
            'title': img_name,
            'description': img_description
        }

        print(f'Uploading image {img_path} to imgur ')
        image = client.upload_from_path(img_path, config=config, anon=False)
        return image['link']
    except ImgurClientRateLimitError as e:
        print(e)
        print('Your temporary credentials are no longer valid')
        print('Please reauthenticate...')
        return upload_img_to_imgur(img_name=img_name,
                                   img_path=img_path,
                                   img_description=img_description,
                                   album=album,
                                   with_auth=True)

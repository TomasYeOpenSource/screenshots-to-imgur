from imgurpython import ImgurClient
from screenshots_to_web.imgur.api_keys import CLIENT_ID, CLIENT_SECRET


def get_imgur_client(skip_auth: bool = True) -> ImgurClient:
    client = ImgurClient(CLIENT_ID, CLIENT_SECRET)

    if skip_auth:
        access_token = 'access_token'
        refresh_token = 'refresh_token'
    else:
        authorization_url = client.get_auth_url('pin')
        print("Go to the following URL: {0}".format(authorization_url))
        pin = input('Enter pin code:')

        credentials = client.authorize(pin, 'pin')
        access_token = credentials['access_token']
        refresh_token = credentials['refresh_token']

    print("Authentication successful! Here are the details:")
    print("   Access token:  {0}".format(access_token))
    print("   Refresh token: {0}".format(refresh_token))
    client.set_user_auth(access_token, refresh_token)
    return client





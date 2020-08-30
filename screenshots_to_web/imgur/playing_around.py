from imgurpython import ImgurClient
from screenshots_to_web.imgur.api_keys import CLIENT_ID, CLIENT_SECRET

# Authorization flow, pin example (see docs for other auth types)
# Read in the pin, handle Python 2 or 3 here.
client = ImgurClient(CLIENT_ID, CLIENT_SECRET)
authorization_url = client.get_auth_url('pin')

print("Go to the following URL: {0}".format(authorization_url))
pin = input('Enter pin code:')

# ... redirect user to `authorization_url`, obtain pin (or code or token) ...
credentials = client.authorize(pin, 'pin')
client.set_user_auth(credentials['access_token'], credentials['refresh_token'])

print("Authentication successful! Here are the details:")
print("   Access token:  {0}".format(credentials['access_token']))
print("   Refresh token: {0}".format(credentials['refresh_token']))

config = {
    'album': None,
    'name': 'First Upload via CLI',
    'title': 'First Upload via CLI',
    'description': 'A Screenshot of my linked in profile'
}

print("Uploading image... ")
image = client.upload_from_path('ImgurUploadFromCLI.png', config=config, anon=False)
print("Done")
print()

print("Image was posted! Go check your images you sexy beast!")
print()
print()
print('Image = ')
print(image)
print()
print()
print("You can find it here: {0}".format(image['link']))

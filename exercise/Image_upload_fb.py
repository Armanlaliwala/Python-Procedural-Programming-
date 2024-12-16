import facebook
import requests
import random

# Facebook access token (get it from https://developers.facebook.com/tools/access_token/)
ACCESS_TOKEN = 'EAA0R1qq9Mo0BO1jdoWAGtj8adZAHvab4DkUyKrS55EJIKSmuEa7N1kZBLo5RY0SLlQzicKxfjPN3dRrZACWv7sP5JgXTLBFrwGzMYZCIHHyR4ErBS97DjqH3S78YI4Lo76Yc78NLUNqC9rcpb3kGzvEp6w8cMe0KSWd7yapZBPv20PaeZAmwy6Naq7jMWkDXcnB7Ud5C27rIZBKKW2AedqIK8IE4NQFU0aM1XcRMvUZD'

# Dictionary with 100 photo paths
photos = {
    1: 'photo1.jpg',
    2: 'photo2.jpg',
    3: 'photo3.jpg',
    4: 'photo4.jpg',
    5: 'photo5.jpg',
    6: 'photo6.jpg',
    7: 'photo7.jpg',
    8: 'photo8.jpg',
    9: 'photo9.jpg',
    10: 'photo10.jpg',
    11: 'photo11.jpg',
    12: 'photo12.jpg',
    13: 'photo13.jpg',
    14: 'photo14.jpg',
    15: 'photo15.jpg',
    16: 'photo16.jpg',
    17: 'photo17.jpg',
    18: 'photo18.jpg',
    19: 'photo19.jpg',
    20: 'photo20.jpg',
    21: 'photo21.jpg',
    22: 'photo22.jpg',
    23: 'photo23.jpg',
    24: 'photo24.png'
    
}

# Initialize the Graph API with your access token
graph = facebook.GraphAPI(access_token=ACCESS_TOKEN, version='3.0')

# Get a list of groups you're a member of
groups = graph.get_object('me/groups')

# Iterate over the groups and upload a random photo
for group in groups['data']:
    try:
        group_id = group['631688414219516']
        group_name = group['AHMEDABAD BUSINESS & JOBS GROUP']
        print(f"Uploading photo to group: {group_name}")

        # Select a random photo
        photo_number = random.randint(1, 100)
        photo_path = photos[photo_number]

        # Upload the photo to the group
        photo = open(photo_path, 'rb')
        graph.put_photo(image=photo, album_path=f'{group_id}/photos')
        photo.close()

        print(f"Photo uploaded successfully to group: {group_name}")
    except Exception as e:
        print(f"Error uploading photo to group {group_name}: {e}")

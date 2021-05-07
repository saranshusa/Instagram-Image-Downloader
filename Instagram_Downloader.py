"""
This program downloads the Instagram profile picture and all posts of the provided username

install python
install instaloader
"""

import instaloader

def main():

    print('INSTAGRAM POSTS AND PROFILE DOWNLOADER\n')
    username = input('Enter the username : ')

    L = instaloader.Instaloader()

    option = int(input('\nWhat do you want to download ? \n1. Only Profile Picture\n2. All Post\'s Images and Videos\nEnter 1 or 2: '))
    if option == 1:
        L.download_profile(username, profile_pic_only=True)
    else:
        posts = instaloader.Profile.from_username(L.context, username).get_posts()
        for post in posts:
            L.download_post(post, username)

    print('A folder containing the downloaded resources will be created in the current directory if no errors were occured.')

if __name__ == '__main__':
    main()
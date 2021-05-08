"""
This program downloads the Instagram profile picture and all other media files from the posts of the provided username.

install python
install instaloader
"""

import instaloader

def main():

    print('INSTAGRAM POSTS AND PROFILE PICTURE DOWNLOADER\n')
    username = input('Enter the username of profile : ')

    L = instaloader.Instaloader()

    option = input('\nREMEMBER: For downloading posts of a PRIVATE profile, you will need to Login with your own account.\nDo you wish to Login or skip to download only the profile picture.\n\n\tEnter Y/N : ')
    
    if option.lower() == 'y':
        USER = input("Enter your USERNAME: ")
        PASS = input('Enter your PASSWORD: ')
        L.login(USER, PASS)
    

    option = int(input('\nWhat do you want to download ? \n\n1. Only Profile Picture\n2. All Images and Videos\n\n\tEnter 1 or 2: '))
    if option == 1:
        L.download_profile(username, profile_pic_only=True)
    else:
        posts = instaloader.Profile.from_username(L.context, username).get_posts()
        for post in posts:
            L.download_post(post, username)

    print('\nA folder containing all the downloaded resources will be created in the current directory, if no errors were occured.\t Thank You for using.\n\n Developed by SARANSH')

if __name__ == '__main__':
    main()
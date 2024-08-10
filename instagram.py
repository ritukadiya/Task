import instaloader
#creating an instaloader() object
ig=instaloader.Instaloader()

#taking the instagram user as input from user
username=input("enter username: ")

#fetching the details of provided username using instaloader object
profile=instaloader.Profile.from_username(ig.context,username)

#print the fetched details and storing the profile pic of that account
print("username: ",profile.username)
print("number of post uploaded: ",profile.mediacount)
print(profile.username+"is having "+ str(profile.followers)+'followers.')
print(profile.username+"is following "+ str(profile.followers)+'people.')
print("bio: ",profile.biography )
instaloader.Instaloader().download_profile(username,profile_pic_only=True)
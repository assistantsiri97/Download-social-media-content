import instaloader
from pytube import YouTube
def audio_from_youtube(url):
    yt=YouTube(url)
    so=yt.streams.filter(resolution="720p",file_extension="mp4").first()
    so.download()
def instagram():
    insta = instaloader.Instaloader()
    user = input("Enter your instagram username: ")
    insta.download_profile(user, profile_pic_only=True)

    profile = instaloader.Profile.from_username(insta.context, user)
    posts = list(profile.get_posts())
    latestPost = posts[0]
    insta.download_post(latestPost, target=profile.username)


choice = input("Enter 1 for instagram operation and 2 for youtube: ")

if choice == '1':
    instagram()
else:

    video_url = input("Enter youtube url")
    audio_from_youtube(video_url)





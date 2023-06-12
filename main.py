from pytube import YouTube, Playlist

Email = input(" your email")
p = Playlist(Email)

print(f'Downloading: {p.title}')
# HD Quality
for video in p.videos:
    video.streams.filter(file_extension='mp4', res="1080p").first().download()


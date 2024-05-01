from pytube import Search

def get_youtube_link(video_title):
    search = Search(video_title)
    for video in search.results:
        return video.watch_url
print(get_youtube_link("Taylor Swift  -  Fortnight (feat. Post Malone)"))
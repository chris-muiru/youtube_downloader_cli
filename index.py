#!/usr/bin/python3

# project: shell Youtube-downloader
# author:  kris muiru

from pytube import YouTube,Playlist,Channel
import os,shutil

if __name__=='__main__':
    if os.path.exists('Songs'):
        pass
    else:
        os.mkdir('Songs')
    PATH=os.path.abspath('Songs')
    user=input('enter url here: ') 
    link_type=input('''
        Link type?
        a.Playlist
        b.Channel
        c.Youtube link
    ''')
    AUD_VID=input('Audio or video?(y-video,n-audio):  ')
    if AUD_VID=='y':
        AUD_VID=False
    else:
        AUD_VID=True
    while True:
        if link_type=='a':
            NUM_VIDEOS=input('How many audio/videos do you want to download in this playlist?')
            NUM_VIDEOS=int(NUM_VIDEOS)
            playlist=Playlist(str(user))
            for audio in playlist.video_urls[:NUM_VIDEOS]:
                link=YouTube(audio)
                print('Downloading {}'.format(link.title))
                stream=link.streams.filter(only_audio=AUD_VID)
                stream.first().download()
        elif link_type=='b':
            NUM_VIDEOS=input('How many channel videos or audio do you want to download in this playlist?')
            NUM_VIDEOS=int(NUM_VIDEOS)
            channel=Channel(user)
            for video in playlist.video_urls[:NUM_VIDEOS]:
                link=YouTube(audio)
                print('Downloading {}'.format(link.title))
                stream=link.streams.filter(file_extension='mp4',only_audio=AUD_VID)
                stream.first().download()
        
        elif link_type=='c':
            yt_link=YouTube(user)
            print('Downloading {}'.format(yt_link.title))
            stream=yt_link.streams.filter(only_audio=AUD_VID)
            stream.first().download() 
        
        CWD=os.getcwd()
        THIS_DIR=os.listdir(CWD)
        for i in THIS_DIR:
            if i.endswith('.mp3'):
                shutil.move(os.path.abspath(i),PATH)
        break
#!/usr/bin/python3

# project: shell Youtube-downloader

# author:  kris muiru

from pytube import YouTube,Playlist,Channel
from search_feature import single_video_search_feature,playlist_search_feature,channel_search_feature
import os,shutil,send2trash
from youtubesearchpython import VideosSearch,PlaylistsSearch,ChannelsSearch

if __name__=='__main__':

    if os.path.exists('Songs'):
        pass
    else:
        os.mkdir('Songs')

    PATH=os.path.abspath('Songs')
    preference=input("search or url feature (y-search n-url): ")
    link_type=input('''Video/audio type?
        a.Playlist
        b.Channel
        c.Single video/audio\n: ''')
    AUD_VID=input('Audio or video?(y-video,n-audio): ')
    
    if preference=='y':
            user=input('Enter video or audio name:  ')
            if link_type=='a':
                user=playlist_search_feature(user)
            elif  link_type=='b':
                user=channel_search_feature(user)
            else:
                user=single_video_search_feature(user)
    else:
        user=input('enter url here: ')
    if AUD_VID=='y':
        AUD_VID=False
    else:
        AUD_VID=True
    while True:
        if link_type=='a':
            NUM_VIDEOS=input('How many audio/videos do you want to download in this playlist? ')
            NUM_VIDEOS=int(NUM_VIDEOS)
            playlist=Playlist(str(user))
            for video in playlist.video_urls[:NUM_VIDEOS]:
                link=YouTube(video)
                print('Downloading {}'.format(link.title)+'\n') 
                if AUD_VID==False:
                     stream=link.streams.filter(res="720p")
                     stream.first().download() 
                if AUD_VID==True:
                    stream=link.streams.filter(only_audio=AUD_VID)
                    stream.first().download()

        elif link_type=='b':
            NUM_VIDEOS=input('How many channel videos or audio do you want to download in this playlist?')
            NUM_VIDEOS=int(NUM_VIDEOS)
            channel=Channel(user)
            for video in channel.video_urls[:NUM_VIDEOS]:
                link=YouTube(video)
                print('Downloading {}'.format(link.title)) 
                if AUD_VID==False:
                     stream=link.streams.filter(res="720p",type="video")
                     stream.first().download() 
                if AUD_VID==True:
                    stream=link.streams.filter(only_audio=AUD_VID)
                    stream.first().download()
        
        elif link_type=='c':
            yt_link=YouTube(user)
            print('Downloading {}'.format(yt_link.title))
            if AUD_VID==False:
                 stream=yt_link.streams.filter(res="720p")
                 stream.first().download()
            if AUD_VID==True:
                 stream=yt_link.streams.filter(only_audio=AUD_VID)
                 stream.first().download() 
        
        CWD=os.getcwd()
        THIS_DIR=os.listdir(CWD)
        for i in THIS_DIR:
            if i.endswith('.mp4'):
                if i not in os.listdir(PATH):
                    shutil.move(os.path.abspath(i),PATH)
                else:
                    send2trash.send2trash(i)
        break
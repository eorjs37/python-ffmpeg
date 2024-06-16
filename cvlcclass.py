import vlc
import time
class VLCPlayer:
    def __init__(self):
        self.media_player =vlc.MediaPlayer()
        self.media = None
        
    def set_mediafile(self,path):
        self.media = vlc.Media(path)
        self.media_player.set_media(self.media)
    
    def music_play(self):
        if(self.media):
            self.media_player.play()
            time.sleep(1)
    
    def music_volume(self,volumeval):
        self.media_player.audio_set_volume(volumeval)
    
    def music_stop(self):
       self.media_player.pause()             
    
    def get_musictime(self):
        return self.media_player.get_time()
    
    def set_sleeptime(self,timeval):
        time.sleep(timeval)
        
    def get_duration(self):
        return self.media_player.get_length()
    
           
music_path = "https://daegeon-everybody.s3.ap-northeast-2.amazonaws.com/m3u8/lauv/music.m3u8"
player1 = VLCPlayer()

player1.set_mediafile(music_path)
player1.music_play()
duration = player1.get_duration()/1000
player1.set_sleeptime(duration)

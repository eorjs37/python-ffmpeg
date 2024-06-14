import vlc

class VlcPlayer:
    '''
     args:VLC인스턴스 생성옵션
    '''
    
    def __init__(self,*args):
        if(args):
            instance = vlc.Instance(*args)
            self.media = instance.media_player_new()
            
        

    
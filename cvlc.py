import vlc
import time

media_file = "./video/lauv/1.mp4"

# VLC 인스턴스 생성
media_player = vlc.MediaPlayer()

# 재생할 뮤직비디오 파일을 vlc 모듈의 미디어로 변환.
media = vlc.Media(media_file)

# 읽어드린 미디어를 재생할 수 있도록 
# 미디어 플레이어 객체에 세팅 (재생 준비 상태)
media_player.set_media(media)

# start playing video
media_player.play()

# 플레이할 영상의 길이와 상관 없이
# 0.5초 동안만 영상을 플레이합니다.
time.sleep(20)

# 재생한 미디어플레이어의 플레이타임(초)를 반환.
duration = media_player.get_length()
print("Duration : " + str(duration))

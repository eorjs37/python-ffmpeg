import vlc
import time
# vlc media player 객체 생성
media_player = vlc.MediaPlayer()

# 뮤직비디오 파일
media_file = "./video/video1.mp4"

# 미디어 파일을 vlc 객체로 읽어들이기
media = vlc.Media(media_file)

# 읽어드린 미디어파일을 media_player 객체에 세팅하기(재생목록)
media_player.set_media(media)

time.sleep(5)
print("(1) 영상 재생 시작")
media_player.play()

duration = media_player.get_length()
print("Duration : " + str(duration))
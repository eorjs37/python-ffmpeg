import vlc
import time

media_player = vlc.MediaPlayer()

media_file = "./video/lauv/1.mp4"

# 미디어 파일을 vlc 객체로 읽어들이기
media = vlc.Media(media_file)

# 읽어드린 미디어파일을 media_player 객체에 세팅하기(재생목록)
media_player.set_media(media)
 
 
media_player.audio_set_volume(100)
time.sleep(1)
print(f"(0) 오디오 볼륨을 {media_player.audio_get_volume()}으로 초기 조정")

media_player.play()
time.sleep(3)
print(f" - 재생중 상태 체크값(is_playing): {media_player.is_playing()}")
print("\n")

print("(2) 영상을 1초 일시 중지")
media_player.pause()
time.sleep(3)
print(f"- 현재 play 상태(get_state): {media_player.get_state()}")
print("\n")

print("(3) 영상을 1초 동안 재생")
media_player.play()
time.sleep(3)
print(f"  - 현재 play 상태(get_state): {media_player.get_state()}")
print("\n")
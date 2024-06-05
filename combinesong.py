import ffmpeg
import os

entries = os.listdir('video/lauv')

# 폴더 읽기


# 파일 만들기
f = open('songlist.txt','w')
pwd = os.getcwd()

for entry in sorted(entries):
    data = 'file'+" '"+pwd+'/video/lauv_codec/'+entry+"'\n"
    f.write(data)

f.close();

ffmpeg.input('video/lauv/1.mp4').output('video/lauv/1_.mp4',**{'c:v': 'libx265'}).run()

# ffmpeg으로 convert

# ffmpeg으로 concat
# ffmpeg.input('songlist.txt',
#              format='concat', safe=0).output('video/lauv.mp4', c='copy').run()
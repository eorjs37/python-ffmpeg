import ffmpeg
import os

entries = os.listdir('video/lauv')

# 폴더 읽기


# 파일 만들기
f = open('songlist.txt','w')
pwd = os.getcwd()

for entry in sorted(entries):
    data = 'file'+" '"+pwd+'/video/lauv/'+entry+"'\n"
    f.write(data)

f.close()

# ffmpeg으로 convert

# ffmpeg으로 concat
# ffmpeg.input('songlist.txt',
#              format='concat', safe=0).output('video/lauv.mp4', c='copy').run()
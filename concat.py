import ffmpeg
import os


# 인코딩 폴더(ENCODING_FOLDER) 생성
def mkdir():
    if(os.path.isdir(os.getcwd()+'/video'+'/ENCODING_FOLDER') == False):
        os.mkdir(os.getcwd()+'/video'+'/ENCODING_FOLDER')
     
# 코덱 변환
def changeCodec():
    # 리스트 불러오기
    root = os.getcwd()+'/video'
    ffmpeg.input(root+'/lauv'+'/1_.mp4').output(root+'/ENCODING_FOLDER'+'/1__.mp4',vcodec='libx264').run()

# video concat
def concatVideo():
    cmd = "ffmpeg -safe 0 -f concat -i list.txt -c copy video/lauv2.mp4"
    os.system(cmd)
        
mkdir()
# changeCodec()
concatVideo()
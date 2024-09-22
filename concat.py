import ffmpeg
import os


# 인코딩 폴더(ENCODING_FOLDER) 생성
def mkdir():
    if(os.path.isdir('ENCODING_FOLDER') == False):
        os.mkdir("ENCODING_FOLDER")
     
# 코덱 확인
def checkCodec():
    # file_list = os.listdir('video/lauv')
    # for i in file_list:
    #     print(i)
    #     video = ffmpeg.input('video/lauv/6.mp4')
    #     print(video)
    print(os.getcwd())
    video = ffmpeg.input('/Users/choedaegeon/project/python-project/video/lauv/1_.mp4')
    print(video)
    #    video = ffmpeg.input('video/lauv/6.mp4')
    #    print(video)
    
mkdir()
checkCodec()
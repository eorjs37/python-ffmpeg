# python

## codec 맞추기
```
ffmpeg -i video/lauv/3.mp4 -c:v libx264 -c:a aac video/lauv/3_.mp4
```

## concat 
```
ffmpeg -safe 0 -f concat -correct_ts_overflow 0 -i list.txt -map 0:v -c copy  video/lauv.mp4
```

```
ffmpeg -safe 0 -f concat -i list.txt -c copy video/output.mp4
```

## m3u8 생성
```
ffmpeg -i video/output.mp4 -profile:v baseline -strict -2 -level 3.0 -start_number 0 -hls_time 3 -hls_list_size 0 -f hls output/lauv/music.m3u8
```

## 명령어 정리
```
ffmpeg  -i video/lauv/1.mp4 -vf mpdecimate,setpts=N/FRAME_RATE/TB video/lauv_codec/1_.mp4
ffmpeg  -i video/lauv/2.mp4 -vf mpdecimate,setpts=N/FRAME_RATE/TB video/lauv_codec/2_.mp4
ffmpeg  -i video/lauv/3.mp4 -vf mpdecimate,setpts=N/FRAME_RATE/TB video/lauv_codec/3_.mp4
ffmpeg  -i video/lauv/4.mp4 -vf mpdecimate,setpts=N/FRAME_RATE/TB video/lauv_codec/4_.mp4
ffmpeg  -i video/lauv/5.mp4 -vf mpdecimate,setpts=N/FRAME_RATE/TB video/lauv_codec/5_.mp4
ffmpeg  -i video/lauv/6.mp4 -vf mpdecimate,setpts=N/FRAME_RATE/TB video/lauv_codec/6_.mp4


ffmpeg  -i video/lauv/1.mp4 -fflags +genpts -c copy video/lauv_codec/1_.mp4
ffmpeg  -i video/lauv/2.mp4 -fflags +genpts -c copy video/lauv_codec/2_.mp4
ffmpeg  -i video/lauv/3.mp4 -fflags +genpts -c copy video/lauv_codec/3_.mp4
ffmpeg  -i video/lauv/4.mp4 -fflags +genpts -c copy video/lauv_codec/4_.mp4

ffmpeg  -i video/lauv/1.mp4 -c:v libx264 -c:a aac -strict experimental -f mp4 video/lauv_codec/1_.mp4
ffmpeg  -i video/lauv/2.mp4 -c:v libx264 -c:a aac -strict experimental -f mp4 video/lauv_codec/2_.mp4
ffmpeg  -i video/lauv/3.mp4 -c:v libx264 -c:a aac -strict experimental -f mp4 video/lauv_codec/3_.mp4
ffmpeg  -i video/lauv/4.mp4 -c:v libx264 -c:a aac -strict experimental -f mp4 video/lauv_codec/4_.mp4

ffmpeg  -i video/lauv/1.mp4 -avoid_negative_ts make_zero -c copy video/lauv_codec/1_.mp4
ffmpeg  -i video/lauv/2.mp4 -avoid_negative_ts make_zero -c copy video	/lauv_codec/2_.mp4
ffmpeg  -i video/lauv/3.mp4 -avoid_negative_ts make_zero -c copy video/lauv_codec/3_.mp4
ffmpeg  -i video/lauv/4.mp4 -avoid_negative_ts make_zero -c copy video/lauv_codec/4_.mp4


ffmpeg  -i video/lauv/1.mp4 -vcodec mpeg4 -vf fps=30 video/lauv_codec/1_.mp4
ffmpeg  -i video/lauv/2.mp4 -vcodec mpeg4 -vf fps=30 video/lauv_codec/2_.mp4
ffmpeg  -i video/lauv/3.mp4 -vcodec mpeg4 -vf fps=30 video/lauv_codec/3_.mp4
ffmpeg  -i video/lauv/4.mp4 -vcodec mpeg4 -vf fps=30 video/lauv_codec/4_.mp4
ffmpeg  -i video/lauv/5.mp4 -vcodec mpeg4 -vf fps=30 video/lauv_codec/5_.mp4
ffmpeg  -i video/lauv/6.mp4 -vcodec mpeg4 -vf fps=30 video/lauv_codec/6_.mp4



ffmpeg -i video/lauv2.mp4 -profile:v baseline -strict -2 -level 3.0 -start_number 0 -hls_time 3 -hls_list_size 0 -f hls output/lauv/lauv.m3u8
ffmpeg -i video/animation_song_codec/1_.mp4 -profile:v baseline -strict -2 -level 3.0 -start_number 0 -hls_time 3 -hls_list_size 0 -f hls output/lauv/attack_on_titan.m3u8

ffmpeg  -i video/animation_song/attack_on_titan.mp4 -vcodec mpeg4 -vf fps=30 video/animation_song_codec/1_.mp4
ffmpeg  -i video/animation_song/FULLMETAL_ALCHEMIST.mp4 -vcodec mpeg4 -vf fps=30 video/animation_song_codec/2_.mp4
```

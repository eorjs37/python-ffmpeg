# python

## codec 맞추기
```
ffmpeg -i video/lauv/3.mp4 -c:v libx264 video/lauv/3_.mp4
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
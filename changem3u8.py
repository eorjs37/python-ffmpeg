import ffmpeg

input_video = ffmpeg.input('./video/lauv.mp4')
out_video = ffmpeg.output(input_video,'./output/lauv/music1.m3u8', format='hls', start_number=0, hls_time=3, hls_list_size=0)

out_video.run()
ffserver -f /etc/ffserver1.conf & ffmpeg -f video4linux2 -s 1280x720 -r 30 -re -i /dev/video0 -an -vcodec libx264  http://localhost:8099/feed1.ffm

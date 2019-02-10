from subprocess import call

if __name__=="__main__":
    call("fswebcam -S 10 -r 1280x720 --save /home/pi/Desktop/photos/bonchi/pic_%Y%m%d-%H:%M.jpg", shell=True)

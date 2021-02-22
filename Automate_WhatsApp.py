import pywhatkit

try:
    pywhatkit.sendwhatmsg('+91 xxxxx xxxxx', 'Happy Birthday', 9, 38)
    print('Sending message...')

except:
    print('Unexpected Error.')

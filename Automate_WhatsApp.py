import pywhatkit

try:
    pywhatkit.sendwhatmsg('+919163198148', 'Happy Birthday', 9, 38)
    print('Sending message...')

except:
    print('Unexpected Error.')

import time
import winsound

节奏=500
#
一闪一闪亮晶晶='1155665-4433221-5544332-5544332-1155665-4433221-'
# 警报='3213213131'
#
#
n1=523
n2=587
n3=659
n4=698
n5=784
n6=880
n7=988
#
h1=1046
h2=1175
h3=1318
h4=1397
h5=1568
h6=1760
h7=1976
#
def play(音符,t=节奏):
    winsound.Beep(音符,t)

for 音符 in 一闪一闪亮晶晶:
    if 音符=='1':
        play(h1)
    if 音符=='2':
        play(h2)
    if 音符== '3':
        play(h3)
    if 音符== '4':
        play(h4)
    if 音符== '5':
        play(h5)
    if 音符== '6':
        play(h6)
    if 音符== '7':
        play(h7)
    if 音符=='-':
        time.sleep(节奏/1000)



Message=input("Mettez votre message ici:")
Décalage=input("Choisissez votre décalage:")
def Caesar(msg, dcl):
    alpha="abcdefghijklmnopqrstuvwxyz"
    buffer=0
    if dcl>26:
        dcl=dcl-26
    i=0
    while(i<=len(msg)):
        if msg[i] == alpha[0]:
            buffer=1
        elif msg[i] == alpha[1]:
            buffer=2
        elif msg[i] == alpha[2]:
            buffer=3
        elif msg[i] == alpha[3]:
            buffer=4
        elif msg[i] == alpha[4]:
            buffer=5
        elif msg[i] == alpha[5]:
            buffer=6
        elif msg[i] == alpha[6]:
            buffer=7
        elif msg[i] == alpha[7]:
            buffer=8
        elif msg[i] == alpha[8]:
            buffer=9
        elif msg[i] == alpha[9]:
            buffer=10
        elif msg[i] == alpha[10]:
            buffer=11
        elif msg[i] == alpha[11]:
            buffer=12
        elif msg[i] == alpha[12]:
            buffer=13
        elif msg[i] == alpha[13]:
            buffer=14
        elif msg[i] == alpha[14]:
            buffer=15
        elif msg[i] == alpha[15]:
            buffer=16
        elif msg[i] == alpha[16]:
            buffer=17
        elif msg[i] == alpha[17]:
            buffer=18
        elif msg[i] == alpha[18]:
            buffer=19
        elif msg[i] == alpha[19]:
            buffer=20
        elif msg[i] == alpha[20]:
            buffer=21
        elif msg[i] == alpha[21]:
            buffer=22
        elif msg[i] == alpha[22]:
            buffer=23
        elif msg[i] == alpha[23]:
            buffer=24
        elif msg[i] == alpha[24]:
            buffer=25
        elif msg[i] == alpha[25]:
            buffer=26
        else:
            buffer=30
        if buffer!=30:
            buffer=buffer+dcl
            if buffer>26:
                buffer= buffer-26
                print(alpha[buffer],end="")
            else:
                print(msg[i],end="")
        i+=1
Caesar(Message,int(Décalage))
import pyttsx3
tts = pyttsx3.init()
rate = tts.getProperty('rate')#скорость произношения
tts.setProperty('rate', rate-40)

volume = tts.getProperty('volume')#volume
tts.setProperty('volume', volume+0.9)

voices = tts.getProperty('voices')

tts.setProperty('voice', "ru")

#favorite voice
for voice in voices:
    if voice.name == "Irina":
        tts.setProperty('voice', voice.id)
        

while True:
    a = input("Введите пример: ")
    try:
        b = ""
        d_str = ""
        s_list = []
        for i in a:
            if i != " ":
                b += i
        #print(b)
        for i in range(len(b)):
            if not b[i].isdigit():
                s_list.append(b[i])
                d_str += " "
            else:
                d_str += b[i]
        #print(d_str)
        d_list = d_str.split(" ")
        #print(d_list, s_list)
        res = int(d_list[0])
        for i in range(len(s_list)):
            if s_list[i] == "+":
                res += int(d_list[i+1])
            elif s_list[i] == "-":
                res -= int(d_list[i+1])
            elif s_list[i] == "*":
                res *= int(d_list[i+1])
            elif s_list[i] == "/":
                res /= int(d_list[i+1])
            else:
                print(s_list[i], " - Invalid symbol!")
                raise Exception("Invalid symbol!")
        print("Результат равен ", res)
        if res < 0:
            tts.say("Результат равен минус" + str(res))
            tts.runAndWait()
        else:
            tts.say("Результат равен" + str(res))
            tts.runAndWait()
    except:
        print("Пример введен не правильно, попробуйте еще раз")
        tts.say("Пример введен не правильно, попробуйте еще раз")
        tts.runAndWait()
        
    x = input()
    if x == "exit":
        break
    print('\n')
    
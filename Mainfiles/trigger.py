import RobotSlave
import datetime

#for transparency, variables saved to files since program might restart often
def igiveup():
    with open('dayandhasconfig.txt', 'r') as file:
        data = file.read()
    if data < str(datetime.datetime.now().day) and datetime.datetime.now().hour >= 15:
        answer = RobotSlave.solve()
        with open('robitsanswers.txt', 'w') as file:
            file.write(answer)
        with open('dayandhasconfig.txt', 'w') as file:
            file.write(str(datetime.datetime.now().day))
    else:
        with open('robitsanswers.txt', 'r') as myfile:
            answer = myfile.read()
    return answer

def help():
    return "help stuff"

def reminder():
    return "reminder.txt for specific people maybe set timers? and it will @them reminding them like an alarmclock"

#create text trigger here with function
triggers = {
            "!igiveup": igiveup(),
            "!help": help(),
            "!reminder": reminder()
}
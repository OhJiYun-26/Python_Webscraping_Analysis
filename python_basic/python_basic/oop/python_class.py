class SoccerPlayer(object):
    def __init__(self, name, position, back_number):
        self.name = name
        self.position = position
        self.back_number = back_number

    def change_back_number(self, new_number):
        print("선수의 등번호를 변경합니다 : From %d to %d" % (self.back_number, new_number))
        self.back_number = new_number

    def __str__(self):
        return "Hello, My name is %s. I play in %s in center " % (self.name, self.position)


def say_hello(msg):
    # pass
    '''
    이주석은 docstring comment 입니다.

    '''
    sum = int('350') + 350
    # print('합계는'+sum)
    print('합계는 :' + str(sum))
    return "hello  " + msg


jinhyun = SoccerPlayer("Jinhyun", "MF", 10)
print(jinhyun)

print("현재 선수의 등번호는 :", jinhyun.back_number)
jinhyun.change_back_number(5)
print("현재 선수의 등번호는 :", jinhyun.back_number)

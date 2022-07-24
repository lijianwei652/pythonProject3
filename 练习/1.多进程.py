import multiprocessing
import time

#
# def dance():
#     for i in range(3):
#         print('跳舞...')
#         time.sleep(0.5)
#
# def sing():
#     for i in range(3):
#         print('唱歌')
#         time.sleep(0.5)
#
#
# mul_dance = multiprocessing.Process(target=dance)
# mul_sing = multiprocessing.Process(target=sing)

# 启动带参数的多线程


def dance(who):
    for i in range(3):
        print('跳舞...',who)
        time.sleep(0.5)

def sing(num ):
    for i in range(3):
        print('唱歌',num)
        time.sleep(0.5)

# 多进程演示
mul_dance = multiprocessing.Process(target=dance,args=("zhaoli",))
mul_sing = multiprocessing.Process(target=sing,kwargs={'num':'5'})

if __name__ == '__main__':
    mul_sing.start()
    mul_dance.start()
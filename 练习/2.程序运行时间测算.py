import time
def log_func_time(func):
    def wrapper():
        start_time = time.perf_counter()
        my_func = func()
        end_time= time.perf_counter()
        print('方法{} 消耗了{}ms'.format(func.__name__,(end_time-start_time)*1000))
        return my_func
    return wrapper

@log_func_time

def calculate_func_1():
    list_1=[i for i in range(66666666)]
    print(list_1)

@log_func_time
def calculate_func_2():
    list_2=(i for i in range(66666666))
    print(next(list_2))
    print(next(list_2))

# calculate_func_1()
# calculate_func_2()

# def foo():
#     for i in range(10):
#         yield i*2

# def foo():
#     print('1111')
#     yield
#     print('2222')
#     yield
#     print('3333')
#     yield
#     print('4444')
#
#
# f = foo()
# for i in f:
#     print(i)

# def foo():
#     yield 1
#     yield ('222')
#     yield 3
#     yield ('4444')
#
# def fooo2():
#     yield {
#         'text':text,
#         'class_attrib':format_html('class="column-{}"',field_name),
#         'sortable':False,
#     }
# for i in foo():
#     print(i)

def a():
    for i in range(20):
        yield i*1

for i in a():
    print(i)
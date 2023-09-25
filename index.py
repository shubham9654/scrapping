# import time, threading

# def calc_square(numbers):
#     for n in numbers:
#         print(f"\n{n} ^ 2 = {n*n}")
#         time.sleep(0.1)

# def calc_cube(numbers):
#     for n in numbers:
#         print(f"\n{n} ^ 3 = {n*n*n}")
#         time.sleep(0.1)

# numbers1 = [2, 3, 5, 8]
# numbers2 = [2, 3, 5, 8, 5, 6, 778, 9]
# start = time.time()

# square_thread = threading.Thread(target=calc_square, args=(numbers1,))
# cube_thread = threading.Thread(target=calc_cube, args=(numbers2,))

# square_thread.start()
# cube_thread.start()
# square_thread.join()
# cube_thread.join()

# end = time.time()

# print("Execution Time: {}".format(end - start))

my_list = [1, 2, 3, 4, 5]
for item in my_list:
    print(item)
    break

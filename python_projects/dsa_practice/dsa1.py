# # # fh1 = int(input())
# # # fh2 = int(input())
# # # step = int(input())
# # # cth = fh1
# # # while cth <= fh2:
# # #     c = int((cth - 32) * 5 / 9)
# # #     print(str(cth) + "\t" + str(c))
# # #     cth = cth + step
# # # print(cth)

# # n = int(input())
# # rev = 0
# # while n > 0:
# #     l = n % 10
# #     n = n // 10
# #     rev = rev * 10 + l
# # print(rev)

# n = int(input())
# nclone = n
# rev = 0
# while n > 0:
#     l = n % 10
#     n = n//10
#     rev = rev * 10 + l
# if nclone == rev:
#     print("true")
# else :
#     print("false")

n = int(input())
i = 1
while i <= n :
    j = 1
    while j <= i:
        if (j == 1) or (j == i):
            if (i-1==0):
                print("1" , end = "")
            else:
                print(i-1 , end = "")
        else:
            print(" " , end = "")
        j = j + 1
    print()
    i = i +1
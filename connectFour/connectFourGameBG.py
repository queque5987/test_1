# def win_check():
#     for l in reversed(tilestatus):
#         ren = 0 # 승리 조건 확인용 변수
#         for i in l:
#             if i == 1:
#                 ren += 1
#                 ren = ren % 10
#             elif i == 2:
#                 ren += 10
#                 ren = ren - ren % 10
#             elif ren == 4:
#                 print("player 1 win")
#             elif ren == 40:
#                 print("player 2 win")
#             elif i == 0:
#                 ren = 0
#                 break
# def taketurn():
#     if turn1:
#         turn1 = False
#         return True
#     else:
#         turn1 = True
#         return False
# def tile_flip(xpos, isturn1):
#     if tilestatus[xpos][-1] ==0:
#         taketurn()
#         return False
#     index_to_input = tilestatus[xpos].index(0)
#     if isturn1:
#         tilestatus[xpos][index_to_input] = 1
#         return True
#     else:
#         tilestatus[xpos][index_to_input] = 2
#         return True

# turn1 = True
# """main"""
# tilestatus = [
#    	[0,0,0,0,0,0],
#     [0,0,0,0,0,0],
#     [0,0,0,0,0,0],
#     [0,0,0,0,0,0],
#     [0,0,0,0,0,0],
#     [0,0,0,0,0,0],
#     [0,0,0,0,0,0]
# ]

# for i in tilestatus:
#     for j in i:
#         print (j,end = "")
#     print ("")

x = True

print(x)
x = not x
print(x)
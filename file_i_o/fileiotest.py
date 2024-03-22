# my_file = open("plik.txt")
# print(my_file)
#
# file_handler = open('mbox.txt')
# count = 0
# for line in file_handler:
#     count = count + 1
#     print('Line Count:', count)
#
# # file_handler = open('mbox.txt')
# # inp = file_handler.read()
# # print(len(inp))
# # print(inp[:20])
# # inp = file_handler.read()
# # print(len(inp))
#
# # fhand = open('mbox.txt')
# # for line in fhand:
# #     line = line.rstrip()
# #     if line.startswith('From:'):
# #         print(line)
#
# # fhand = open('mbox.txt')
# # for line in fhand:
# #     line = line.rstrip()
# #     # Skip 'uninteresting lines'
# #     if not line.startswith('From:'):
# #         continue
# #     # Process our 'interesting' line
# #     print(line)
#
# # fhand = open('mbox.txt')
# # for line in fhand:
# #     line = line.rstrip()
# #     if line.find('@uct.ac.za') == -1: continue
# #     print(line)
#
# # fname = input('Enter the file name: ')
# # try:
# #     fhand = open(fname)
# # except:
# #     print('File cannot be opened:', fname)
# #     exit()
# #
# # count = 0
# # for line in fhand:
# #     if line.startswith('Subject:'):
# #         count = count + 1
# # print('There were', count, 'subject lines in', fname)
#
#
# # fout = open('output.txt', 'w')
# # line = "add this line to the file\n"
# # print(fout.write(line))
#
# t = ['a', 'b', 'c', 'd', 'e']
# s = t[:]
# print(id(t))
# print(id(s))
# s.append('h')
# print(t)
# print(s)
# print(id(t))
# print(id(s))
#
# fhand = open('mbox.txt')
# for line in fhand:
#     line = line.rstrip()
#     if not line.startswith('From '): continue
#     words = line.split()
#     print(words[2])
#
#



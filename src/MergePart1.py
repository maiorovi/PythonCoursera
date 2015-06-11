"""
Merge function for 2048 game.
"""
l = [2, 0, 2, 4]
print l.__len__()

def merge(line):
    result_line = []

    for i in range(0, line.__len__()):
       if (line[i] == 0):
           continue
       result_line.append(line[i])

    for i in range(result_line.__len__(), line.__len__()):
        result_line.append(0)

    print result_line

    final_result = []
    i = 0

    while i < result_line.__len__() :
        if (i + 1 == result_line.__len__()):
            final_result.append(result_line[i])
            i = i + 1
            continue
        if (result_line[i] == result_line[i+1]):
            final_result.append(result_line[i] + result_line[i+1])
            i = i + 2
        elif (result_line[i] != result_line[i+1]):
            final_result.append(result_line[i])
            i = i + 1

    for i in range(final_result.__len__(), result_line.__len__()):
        final_result.append(0)

    print final_result

    return final_result

merge(l)
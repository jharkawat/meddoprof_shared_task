file = open("train.txt", "r")
lines = file.readlines()
count = 0
i = 0
# smallfile = open("train.txt","w")
for line in lines:
    if line == "\n":
        count += 1
    i += 1
    # if i == 697157:
    #     smallfile.close()
    #     smallfile = open("dev.txt","w")
    # if i == 935652:
    #     smallfile.close()
    #     smallfile = open("test.txt", "w")
    # smallfile.write(line)
print(i)
print(count)
file.close()


# 33405 697157
# 11135 935652
# 11136 1165844

    # for lineno, line in enumerate(bigfile):
    #     if lineno % lines_per_file == 0:
    #         if smallfile:
    #             smallfile.close()
    #         small_filename = 'small_file_{}.txt'.format(lineno + lines_per_file)
    #         smallfile = open(small_filename, "w")
    #     smallfile.write(line)
    # if smallfile:
    #     smallfile.close()
## Use to create train test and dev in conll

file = open("test.txt", "r")
lines = file.readlines()
count = 0
i = 0
smallfile = None
# smallfile = open("train.txt","w")
for line in lines:
    if line == "\n":
        count += 1
        if smallfile:
            smallfile.close()
        small_filename = 'test/small_file_test_{}.txt'.format(count)
        smallfile = open(small_filename, "w")
    smallfile.write(line)
if smallfile:
    smallfile.close()
file.close()

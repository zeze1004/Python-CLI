fin = open("redis.tf", "rt") ### redis랑 new_redis랑 바꾸기
#output file to write the result to
fout = open("new_redis.tf", "wt")
#for each line in the input file
for line in fin:
    #read replace the string and write to output file
    fout.write(line.replace('NODE_TYPE', 'cache.t2.small'))
#close input and output files
fin.close()
fout.close()
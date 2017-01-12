binned = bin(input())[2:]
bin_list = binned.split('0')
max = len(bin_list[0])
for i in range(1, len(bin_list)):
    if len(bin_list[i]) > max:
        max = len(bin_list[i])
print max



#n = int(raw_input().strip())
#core = 1
#binned = bin(n)[2:]
#for i in range(len(binned) - 1):
#    if binned[i] == '1' and binned[i + 1] == '1':
#        score += 1
#print score

cro_list = ['c=','c-','dz=','d-','lj','nj','s=','z=']
cro_count = 0
input_list = input()
for i in range(len(input_list)):
    if input_list[i:i+2] in cro_list or input_list[i:i+3] in cro_list:
        cro_count += 1
print(len(input_list) - cro_count)
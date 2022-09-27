raw_num = input().strip().split()
#raw_num = ['15', '20', '0', '5']
int_num = [int(i) for i in raw_num]
avg_num = sum(int_num) / len(int_num)

print('{:.0f} {}'.format(avg_num, max(int_num)))

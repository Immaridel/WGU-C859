phone_number = int(input())

'''
#breakup = list(str(phone_number))

area_code = breakup[0] + breakup[1] + breakup[2]
prefix = breakup[3] + breakup[4] + breakup[5]
suffix = breakup[6] + breakup[7] + breakup[8] + breakup[9]
'''

area_code = phone_number // 10000000
prefix = (phone_number // 10000) % 1000
suffix = phone_number % 10000

print('({}) {}-{}'.format(area_code, prefix, suffix))

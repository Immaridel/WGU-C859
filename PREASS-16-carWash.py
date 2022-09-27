services = { 'Air freshener' : 1 , 'Rain repellent': 2, 'Tire shine' : 2, 'Wax' : 3, 'Vacuum' : 5 }
base_wash = 10
total = base_wash

service_choice1 = input()
service_choice2 = input()

print('ZyCar Wash')
print(f'Base car wash -- ${base_wash}')

for i in service_choice1, service_choice2:
    if i != "-":
        print(f'{i} -- ${services[i]}')
        total += services[i]

print('----')
print(f'Total price: ${total}')

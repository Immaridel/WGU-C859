gas_constant = 8.3144621  # Joules / (mol*Kelvin)

'''
Use to test:
    Enter pressure (in Pascals): 2500
    Enter volume (in cubic meters): 35.5
    Enter number of moles: 18
    Temperature = 593.01 K
'''

def convert_to_temp(pressure, volume, mols):
    """Convert pressure, volume, and moles to a temperature"""
    return (pressure * volume) / (mols * gas_constant)

press = float(input('Enter pressure (in Pascals): '))
vol = float(input('Enter volume (in cubic meters): '))
mols = float(input('Enter number of moles: '))

print('Temperature = {:.2f} K'.format(convert_to_temp(press, vol, mols)))
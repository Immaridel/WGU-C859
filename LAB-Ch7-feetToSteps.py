def feet_to_steps(feet_walked):
    steps = feet_walked // 2.5
    return (steps)

if __name__ == '__main__':
    feet = float(input())

    print('{:.0f}'.format(feet_to_steps(feet)))
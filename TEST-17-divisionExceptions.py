try:
    user_num = int(input())
    div_num = int(input())
    skeet = user_num / div_num
    print(int(skeet))
except ValueError as e1:
    print(f'Input Exception: {e1}')
except ZeroDivisionError:
    print("Zero Division Exception: integer division or modulo by zero")
    
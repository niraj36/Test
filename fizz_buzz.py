def fizz_buzz (start_value, end_value, fizz_value, buzz_value):
    count = start_value
    message = count
    while count <= end_value:
        if count % fizz_value == 0:
            message = 'FIZZ'
            if count % buzz_value == 0:
                message += 'BUZZ'
        elif count % buzz_value == 0:
            message = 'BUZZ'
        print(message)
        count += 1
        message = count


fizz_buzz(1,100,3,5)
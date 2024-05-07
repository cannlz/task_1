
def answer_word(input_number):
    #Проверка введенной строки на число
    try:
        input_number = int(input_number)
    except:
        return 'Введенный текст не является числом или это не целое число'
    
    if input_number % 10 == 1:
        return(f'{input_number} Компьютер')
    elif input_number % 10 in [2, 3, 4] and input_number < 1000:
        return(f'{input_number} Компьютера')
    elif input_number % 10 in [5, 6, 7, 8, 9, 0]:
        return(f'{input_number} Компьютеров')
    elif input_number > 1000 and input_number % 10 == 2:
        return(f'{input_number} Компьютеров')
    
        
print(answer_word(input("Введите число: "))) #Указываем число
def str2float(val: str):
    '''
    приводим к типу float
    '''
    try:
        res = float(str(val).replace(",", "."))
        if res < 0:
            print("Вы ввели не верное значение! Число должно быть положительным!")
            res = None
    except:
        print("Вы ввели не верное значение")
        res = None
    return res

def add_cash(full_cash):
    inp_v = input('Введите сумму пополнения счета: ')
    cash_val = str2float(inp_v)
    if cash_val is None:
        dlt = 0
    else:
        dlt = cash_val
        print(f"Сумма добавлена. Баланс = {full_cash + dlt}")
    return full_cash + dlt

def buy_obj(hist: list, full_cash: float):
    inp_v = input('Введите сумму покупки: ')
    buy_val = str2float(inp_v)

    if buy_val is None:
        return hist, full_cash

    if buy_val > full_cash:
        print("К сожалению, денег не хватает")
        return hist, full_cash

    inp_v = input('Введите название покупки: ')
    hist.append({"name": inp_v, "summa": buy_val})
    full_cash -= buy_val
    return hist, full_cash

def print_buylist(hist_list):
    for v in reversed(hist_list):
        print(v)


def start_bank():
    full_cash = 0
    hist_list = []
    while True:
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')

        choice = input('Выберите пункт меню: ')
        if choice == '1':
            full_cash = add_cash(full_cash)
        elif choice == '2':
            hist_list, full_cash = buy_obj(hist_list, full_cash)
        elif choice == '3':
            print_buylist(hist_list)
        elif choice == '4':
            break
        else:
            print('Неверный пункт меню')

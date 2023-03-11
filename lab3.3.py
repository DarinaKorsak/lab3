if __name__ == '__main__':
    def month_name(num, lang):
        en = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September',
              'October', 'November', 'December']
        ru = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь',
              'Октябрь', 'Ноябрь', 'Декабрь']
        if lang == 'en':
            return en[num - 1]
        else:
            return ru[num - 1]


    string = input("Enter number and language: ").split()
    num = int(string[0])
    lang = string[1]

    print(month_name(num, lang))


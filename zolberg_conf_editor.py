import re
import click

def prYellow(skk): print("\033[93m{}\033[00m" .format(skk))
def prGreen(skk): print("\033[92m{}\033[00m" .format(skk))
def prRed(skk): print("\033[91m{}\033[00m" .format(skk))

clean_list_conf = []
# f = input("Введите путь до файла конфигурации или ACL:")
def DeleteString(f):
    try:
        with open(f, 'r', encoding="utf-8") as f_input:
            for l in f_input:
                if not l.startswith('  '):
                    l = re.sub(r'\Whitcnt.*', '', l)
                    clean_list_conf.append(l)
        with open(f, 'w', encoding="utf-8") as f_out:
            f_out.write(''.join(clean_list_conf))
            prGreen('Файл успешно очищен!')
    except IOError:
        prRed(
                 '#######################################' +
          '\n' + '############### ОШИБКА ###############' +
          '\n' + '######################################' +
          '\n' + '### ' + 'Не указан путь до файла' + ' ###' +
          '\n' + '#####################################')

@click.command()
@click.option('-f', help='Путь для файла', )

def main(f):
    """
    Отчиска файла конфиграции и ACL от избыточных данных.
    \b
    Скрипт разработан:
    Кузнецовым Дмитрием Вадимовичем
    Центр кибербезопасности ООО "ИТСК"
    """
    getPath = DeleteString(f)

if __name__ == "__main__":
    main()
    #
    # prRed(
    #            '###############################' +
    #     '\n' + '############ ОШИБКА ###########' +
    #     '\n' + '###############################' +
    #     '\n' + '### ' + 'Не указан путь до файла' + ' ###' +
    #     '\n' + '###############################')
    #

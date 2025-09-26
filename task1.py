# Лабораторная №1: Первичная инициализация
# Курс: Основы теории систем
# Студент: [Давыдов Тимофей Олегович]

def get_system_info():
    """
    Эта функция должна вернуть словарь с информацией о вашей "системе".
    """
    # TODO: Заполните словарь вашими реальными данными
    system_info = {
        "student_name": "Давыдов Тимофей Олегович",
        "academic_group": "ИВТИИбд-11",
        "github_link": "https://github.com/PanabeeWQW"
    }
    return system_info

# Вывод информации для проверки
if __name__ == "__main__":
    info = get_system_info()
    print("Информация о системе:")
    for key, value in info.items():
        print(f"- {key}: {value}")
        
print("Hello world!")
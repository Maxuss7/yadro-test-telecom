import requests

def check_url(url):
    print(f"\nЗапрос к: {url}")
    try:
        response = requests.get(url)
        status = response.status_code
        if 100 <= status < 400:
            print(f"Успех ({status}):")
            print(f"Тело ответа: [{response.text.strip()}]")
        elif 400 <= status < 500:
            raise Exception(f"Ошибка ({status}): ошибка на стороне клиента.")
        elif 500 <= status < 600:
            raise Exception(f"Ошибка ({status}): ошибка на стороне сервера.")
        else:
            print(f"Неожиданный код ответа: {status}")
    except Exception as e:
        print(str(e))


def main():
    urls = [
        "https://httpstat.us/200",
        "https://httpstat.us/201",
        "https://httpstat.us/302",
        "https://httpstat.us/404",
        "https://httpstat.us/500",
    ]

    print("Выберите режим:\n1 - Проверить предопределённые URL-ы\n2 - Ввести свой URL вручную")
    choice = input("Ваш выбор: ")

    if choice == "1":
        for url in urls:
            check_url(url)
            print("---------------------------------------------")
    elif choice == "2":
        user_url = input("Введите URL: ")
        check_url(user_url)
    else:
        print("Неверный выбор. Завершение.")

if __name__ == "__main__":
    main()

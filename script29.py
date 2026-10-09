from bs4 import BeautifulSoup
import requests
class Converter:
    def __init__(self,rate):
        self.rate = rate
    def to_dollars(self,money):
        return money/ self.rate
try:
    response = requests.get(
        "https://bank.gov.ua/ua/markets/exchangerates",
        headers={"User-Agent":"Mozilla/5.0"},
        timeout=15
    )
    response.raise_for_status()
    soup = BeautifulSoup(response.content, "html.parser")
    rate = None
    for cell in soup.find_all("td"):
        if cell.text.strip() == "USD":
            row = cell.find_parent("tr")
            cells = row.find_all("td")
            rate = float(cells[-1].text.strip().replace(",", "."))
            break
    if rate is None or rate <= 0:
        raise ValueError("Курс долара не найден или указан неверно")
    converter = Converter(rate)
    print("Курс НБУ: 1 USD =", rate, "грн")
    money = float(input("Введи сумму в гривнах: ").replace(",", "."))
    if money < 0:
        raise ValueError("Сума не может быть отрицательной")
    result = converter.to_dollars(money)
    print("В доларах:", round(result, 2))
except requests.RequestException as e:
    print("Не удалось загрузить сайт НБУ:", e)
except ValueError as e:
    print("Ошибка:", e)
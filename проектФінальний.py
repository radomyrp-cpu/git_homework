import sqlite3
import requests
from bs4 import BeautifulSoup
class Database:
    def __init__(self):
        self.connection = sqlite3.connect("sites.db")
        self.connection.execute(
            "CREATE TABLE IF NOT EXISTS sites (url TEXT UNIQUE)"
        )
        self.connection.commit()
    def add(self, url):
        self.connection.execute(
            "INSERT OR IGNORE INTO sites VALUES (?)",
            (url,)
        )
        self.connection.commit()
    def get_sites(self):
        return self.connection.execute(
            "SELECT url FROM sites"
        ).fetchall()
    def clear(self):
        self.connection.execute("DELETE FROM sites")
        self.connection.commit()
class Parser:
    def search(self, sites, word):
        results = []
        for site in sites:
            url = site[0]
            try:
                response = requests.get(url, timeout=10)
                soup = BeautifulSoup(response.text, "html.parser")
                text = soup.get_text().lower()
                count = text.count(word.lower())
                results.append((count, url))
            except:
                print("Не вдалося відкрити:", url)
        results.sort(reverse=True)
        return results
class Interface:
    def __init__(self, database, parser):
        self.database = database
        self.parser = parser
    def menu(self):
        while True:
            print()
            print("1 - додати сайт")
            print("2 - Пошук")
            print("3 - Показати сайти")
            print("4 - очистити базу")
            print("0 - Вихід")
            choice = input("вибери дію: ")
            if choice == "1":
                url = input("Введи адресу сайту: ")
                if not url.startswith("http"):
                    url = "https://" + ur
                self.database.add(url)
                print("сайт додано")
            elif choice == "2":
                word = input("Що шукаємо: ")
                sites = self.database.get_sites()
                if len(sites) == 0:
                    print("Спочатку додай сайт")
                else:
                    results = self.parser.search(sites, word)
                    for count, url in results:
                        print(url, "- збігів:", count)
            elif choice == "3":
                sites = self.database.get_sites()
                for site in sites:
                    print(site[0])
            elif choice == "4":
                self.database.clear()
                print("базу очищено")
            elif choice == "0":
                break
            else:
                print("Невідома команда")
def run():
    database = Database()
    parser = Parser()
    interface = Interface(database, parser)
    interface.menu()
if __name__ == "__main__":
    run()
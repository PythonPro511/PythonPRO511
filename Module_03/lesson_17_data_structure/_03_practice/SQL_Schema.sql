--
--Ситуация:
--Вам предстоит подготовить данные к разработке ORM. Но сперва необходимо сформировать схему будущей базы данных.
--
--Задача:
--Создайте схему на SQL, которая будет использоваться для построения ORM.
--
--Шаги реализации:
--
--1) Создание таблицы валют (currencies).

CREATE TABLE IF NOT EXISTS currencies (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    code TEXT NOT NULL UNIQUE,
    name TEXT NOT NULL
)
--Создаём таблицу currencies, если она не существует. Добавляются поля:
--
--id – автоинкрементируемый первичный ключ,
--code – буквенный код валюты (например, USD, EUR) с ограничением UNIQUE,
--name – полное название валюты (например, «Доллар США»).


--2) Создание таблицы курсов (exchange_rates).

CREATE TABLE IF NOT EXISTS exchange_rates (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    currency_id INTEGER NOT NULL,
    date TEXT NOT NULL,
    value REAL NOT NULL,
    FOREIGN KEY (currency_id) REFERENCES currencies(id)
    UNIQUE (currency_id, date)
)

--Создаём таблицу exchange_rates. Добавляются поля:
--
--id – первичный ключ,
--currency_id – внешний ключ, ссылающийся на таблицу currencies,
--date – дата курса в формате TEXT (рекомендуется ISO 8601: YYYY-MM-DD).
--value – значение курса (тип REAL для дробных чисел).
--Устанавливается:
--
--связь FOREIGN KEY с таблицей валют,
--ограничение UNIQUE для пары (currency_id, date).
--Одна валюта может иметь только один курс на дату.
--Автоматическая проверка ссылочной целостности.

--3) Создание индексов (оптимизация).
CREATE INDEX IF NOT EXISTS idx_currency_code ON currencies(code);
CREATE INDEX IF NOT EXISTS idx_rate_date ON exchange_rates(date);
CREATE INDEX IF NOT EXISTS idx_rate_currency ON exchange_rates(currency_id);
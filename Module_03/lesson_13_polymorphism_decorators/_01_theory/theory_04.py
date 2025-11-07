def cache_queries(func):
    cache = {}

    def wrapper(self, query):
        if query in cache:
            print(f'Результат из кэша')
            return cache[query]
        result = func(self, query)
        cache[query] = result
        return result

    return wrapper


class Database:
    @cache_queries
    def execute(self, query):
        print(f'Выполнение тяжелого запроса...')
        return f"Результат запроса: '{query}'"


if __name__ == '__main__':
    db = Database()
    print(db.execute('SELECT * FROM users;'))
    print(db.execute('SELECT * FROM users;'))

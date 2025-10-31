from practice_00_SimpleORM import SimpleORM

if __name__ == '__main__':
    orm = SimpleORM(r'databases\example.db')
    # TASK1
    # orm.create_table('users', name="TEXT", age='INTEGER')
    # orm.insert('users', name='Alice', age=30)
    # orm.insert('users', name='Bob', age=25)
    print(orm.select('users'))

    # TASK2
    # print(orm.select('users', age=25, name='Bob'))
    # orm.update('users', {'age': 31}, name='Alice')
    # print(orm.select('users'))
    # print()
    # orm.delete('users', name='Bob')
    # print(orm.select('users'))




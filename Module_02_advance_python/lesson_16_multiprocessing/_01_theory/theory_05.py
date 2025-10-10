from multiprocessing import Process, Pipe
import time


def sender(conn):
    for i in range(5):
        print(f'Отправитель отправляет: {i}')
        conn.send(i)  # Отправляем данные через канал
        time.sleep(1)


def receiver(conn):
    while True:
        data = conn.recv()   # Получаем данные из канала
        if data == "DONE":
            break
        print(f'Получатель получил: {data}')


if __name__ == '__main__':
    # Создаём канал связи
    parent_conn, child_conn = Pipe()

    # Запускаем два процесса: отправитель и получатель
    sender_process = Process(target=sender, args=(parent_conn,))
    receiver_process = Process(target=receiver, args=(child_conn,))

    sender_process.start()
    receiver_process.start()

    sender_process.join()
    # Отправляем сигнал завершения для получателя
    parent_conn.send("DONE")
    receiver_process.join()

    print(f'Обмен данными завершен.')

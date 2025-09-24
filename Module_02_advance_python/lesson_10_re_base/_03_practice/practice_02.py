import re


def display_correct_ips(text):
    pattern = re.compile(r'\b(?:\d{1,3}\.){3}\d{1,3}\b')
    ip_addresses = re.findall(pattern, text)
    # print(ip_addresses)

    valid_ips = []
    for ip_address in ip_addresses:
        parts = ip_address.split('.')
        if all(0 <= int(part) <= 255 for part in parts):
            valid_ips.append(ip_address)

    print(f'Корректныe ip адреса: {valid_ips}')


if __name__ == '__main__':
    my_text = "Серверы доступны по адресам: 192.168.1.1, 256.256.256.256, 127.0.0.1, 0.0.0.0, 300.300.300.300."
    display_correct_ips(my_text)
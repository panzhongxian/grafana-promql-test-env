import math
import random
import sys
import time

from prometheus_client import Counter, start_http_server

if __name__ == '__main__':
    port = 8080
    start_http_server(port)

    item_dict = {
        "S": [1, 2, 3, 4],
        "A": [5, 6, 7],
        "B": [8, 9, 10],
        "C": [11, 12, 13, 14],
        "D": [1001, 1002, 1003, 1004],
    }
    c = Counter('item_total', 'demo item counter', ['id', 'type'])
    period = 600
    while True:
        type_ = random.choice(list(item_dict.keys()))
        id_ = random.choice(item_dict[type_])
        c.labels(id_, type_).inc()

        _, res = divmod(int(time.time()), period)

        cnt_per_second = 20 * math.sin(res / period * 2 * math.pi) + 30
        time.sleep(1 / cnt_per_second)

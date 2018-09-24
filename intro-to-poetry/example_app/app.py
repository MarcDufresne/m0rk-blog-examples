import time

import click


def demo():
    with click.progressbar(range(7)) as entries:
        for _ in entries:
            time.sleep(1)


if __name__ == '__main__':
    demo()

import datetime


def print_message(msg):
    time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print('[%s]:%s' % (time, msg))


def print_logo():
    print_message('+----------------------+')
    print_message('|          /\\          |')
    print_message('|         /  \\         |')
    print_message('|        /    \\        |')
    print_message('|       /      \\       |')
    print_message('|      /        \\      |')
    print_message('|     /          \\     |')
    print_message('|    /            \\    |')
    print_message('|   /              \\   |')
    print_message('|  /      SAKA      \\  |')
    print_message('|  \\      ____      /  |')
    print_message('|   \\              /   |')
    print_message('|    \\            /    |')
    print_message('|     \\          /     |')
    print_message('|      \\        /      |')
    print_message('|       \\      /       |')
    print_message('|        \\    /        |')
    print_message('|         \\  /         |')
    print_message('|          \\/          |')
    print_message('+----------------------+')

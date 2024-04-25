import time
import sys

# submodule test

def rate_limiter(maxPerSecond):
    minInterval = 1.0 / float(maxPerSecond)

    def decorate(func):
        lastTimeCalled = [0.0]

        def rateLimitedFunction(*args, **kargs):
            elapsed = time.time() - lastTimeCalled[0]
            leftToWait = minInterval - elapsed
            if leftToWait > 0:
                time.sleep(leftToWait)
            ret = func(*args, **kargs)
            lastTimeCalled[0] = time.time()
            return ret

        return rateLimitedFunction

    return decorate


def percentify(n, is_a_fraction=False):
    try:
        float_n = float(n)
        if not is_a_fraction:
            return f"{float_n:.2f}%"
        else:
            return f"{100 * float_n:.2f}%"
    except ValueError:
        return n


def dollarize(n):
    if n is None or n == 'None':
        return 'None'

    try:
        # Check if it's a number
        n = float(n)
    except ValueError:
        return n

    try:
        # small amounts
        if abs(n) < 1000:
            n = round(n, 2)
            return '$ ' + format(n, '.2f')

        # discard decimals for the rest of the function
        n = int(n)

        # up to 1e4
        if abs(n) > 1e3 and abs(n) < 1e4:
            return '$ ' + format(n / 1e3, '.1f') + 'k'

        # up to 1e6
        if abs(n) < 0.99 * 1e6:
            return '$ ' + format(n / 1e3, '.1f') + 'k'

        # up to 1e9
        if abs(n) < 1e9 - 1e4:
            return '$ ' + format(n / 1e6, '.1f') + 'm'

        # up to 1e12
        if abs(n) < 1e12 - 1e7:
            return '$ ' + format(n / 1e9, '.1f') + 'B'

        # up to 1e15
        if abs(n) < 1e15 - 1e10:
            return '$ ' + format(n / 1e12, '.1f') + 'T'
    except:
        return n


def numberize(n):
    try:
        dollarized = dollarize(n)
        return dollarized[1:]  # Slice from 2 to discard '$ '
    except:
        return n


def split_list(lst, n):
    k, m = divmod(len(lst), n)
    return [lst[i * k + min(i, m):(i + 1) * k + min(i + 1, m)] for i in range(n)]


def print_status(status):
    sys.stdout.write('\r' + str(status))
    sys.stdout.flush()


def dict_to_list_of_lists(input_dict):
    data_list_of_lists = []
    cols = []
    for k, v in input_dict.items():
        cols.append(k)
        data_list_of_lists.append(v)

    data_list_of_lists = [data_list_of_lists]
    return {
        'columns': cols,
        'list_of_lists': data_list_of_lists,
    }


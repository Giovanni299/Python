import queue

if __name__ == "__main__":
    policy = 'fifo'.upper()
    if policy not in ['FIFO', 'LIFO']:
        raise ValueError()

    if policy.upper == 'FIFO':
        
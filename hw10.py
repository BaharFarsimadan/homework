def transfer_data():
    queues = []
    stacks = []

    for i in range(1000):
        q = CircularQueue(10)
        s = Stack(20)

        for j in range(5):
            q.enqueue(j)

        queues.append(q)
        stacks.append(s)

    for i in range(1000):
        q = queues[i]
        s = stacks[i]

        temp = []
        while not q.is_empty():
            temp.append(q.dequeue())

        for value in reversed(temp):
            s.push(value)

    return stacks

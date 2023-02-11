def minNumberOfJumps(array):
    if len(array) == 1:
        return 0

    max_reach_index = array[0]
    steps = array[0]
    jumps = 0

    for i in range(1, len(array) - 1):
        steps -= 1
        max_reach_index = max(max_reach_index, i + array[i])

        if steps == 0:
            jumps += 1
            steps = max_reach_index - i

    jumps += 1

    return jumps
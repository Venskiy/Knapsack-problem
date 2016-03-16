def get_episodes():
    episodes = []
    amount_episodes = int(input("Enter the amount of episodes in podcast: "))

    for i in range(0, amount_episodes):
        episodes.append(float(input("Enter the memory of the episode #{}(in gigabyte): ".format(i + 1))))

    print()

    return episodes


def show_episodes(table, episodes, maximized_memory):
    subset = {}

    print("Maximized memory, that we can cover = {}".format(maximized_memory))

    while maximized_memory != 0:
        i = relocate(maximized_memory, table)
        subset[i + 1] = episodes[i]
        maximized_memory = round((maximized_memory - episodes[i]), 2)

    print("Set of episodes to copy to the storage:")
    for key, value in subset.items():
        print("Episode #{}, size = {}.".format(key, value))


def relocate(max_memory, table):
    counter = 0
    for item in table:
        if max_memory in item:
            return counter
        counter += 1

    return 1


def main():
    storage_memory = float(input("Enter the memory of SD card(in gigabyte): "))

    episodes = get_episodes()
    amout_episodes = len(episodes)

    # Main part of the algorithm.
    # Counting the maximized memory, that we can cover.
    knapsack = [[0, episodes[0]]]
    for i in range(1, amout_episodes):
        knapsack.append([])

        for j in range(0, len(knapsack[i - 1])):
            if knapsack[i - 1][j] not in knapsack[i]:
                knapsack[i].append(round(knapsack[i - 1][j], 2))

            if knapsack[i - 1][j] + episodes[i] == storage_memory:
                maximized_memory = knapsack[i - 1][j] + episodes[i]
                maximized_memory
                knapsack[i].append(round(maximized_memory, 2))
                show_episodes(knapsack, episodes, maximized_memory)

                return

            if knapsack[i - 1][j] + episodes[i] < storage_memory:
                if knapsack[i - 1][j] + episodes[i] not in knapsack[i]:
                    knapsack[i].append(round(knapsack[i - 1][j] + episodes[i], 2))

    knapsack[amout_episodes - 1].sort()
    knapsack[len(episodes) - 1].reverse()
    maximized_memory = knapsack[amout_episodes - 1][0]

    show_episodes(knapsack, episodes, maximized_memory)

    return 0


if __name__ == '__main__':
    main()

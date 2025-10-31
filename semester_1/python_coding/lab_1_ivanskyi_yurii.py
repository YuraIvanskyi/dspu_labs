import math
import random


def task_1_1():
    print("Task 1.1: Compute the value of the given expression")
    x, a, b = map(float, input("Enter x, a, b, separated by whitespace: ").split())
    print(f"{x=}, {a=}, {b=}")
    y = math.pow(math.e, -a * x * ((x + math.sqrt(x + a)) / (x - math.sqrt(x - b))))
    print(f"{y=}")


def task_1_2():
    print("Task 1.2: Compute the value of the given expression")
    x, a, b = map(float, input("Enter x, a, b, separated by whitespace: ").split())
    print(f"{x=}, {a=}, {b=}")
    y = math.pow(2, -x) * math.atan(x + a) - math.pow(3, -b * x) * math.cos(x + b)
    print(f"{y=}")


def task_2():
    print("Task 3: List operations")
    random_list = [random.randint(-10, 12) for _ in range(10)]
    print(f"Original list: {random_list}")
    all_increased_twice = [x * 2 for x in random_list]
    print(f"All elements increased by 2: {all_increased_twice}")

    original_positive_sum = sum(x for x in random_list if x > 0)
    original_negative_sum = sum(x for x in random_list if x < 0)
    original_negative_count = len([x for x in random_list if x < 0])
    original_positive_count = len([x for x in random_list if x > 0])
    original_positive_average = original_positive_sum / original_positive_count if original_positive_count > 0 else 0
    original_negative_average = original_negative_sum / original_negative_count if original_negative_count > 0 else 0

    increased_positive_sum = sum(x for x in all_increased_twice if x > 0)
    increased_negative_sum = sum(x for x in all_increased_twice if x < 0)
    increased_negative_count = len([x for x in all_increased_twice if x < 0])
    increased_positive_count = len([x for x in all_increased_twice if x > 0])
    increased_positive_average = (
        increased_positive_sum / increased_positive_count if increased_positive_count > 0 else 0
    )
    increased_negative_average = (
        increased_negative_sum / increased_negative_count if increased_negative_count > 0 else 0
    )

    print(
        f"Differences in sums: Original positive sum: {original_positive_sum}, "
        f"Increased positive sum: {increased_positive_sum}, "
        f"Difference: {original_positive_sum - increased_positive_sum}"
    )
    print(
        f"Differences in sums: Original negative sum: {original_negative_sum}, "
        f"Increased negative sum: {increased_negative_sum}, "
        f"Difference: {original_negative_sum - increased_negative_sum}"
    )
    print(
        f"Differences in counts: Original positive count: {original_positive_count}, "
        f"Increased positive count: {increased_positive_count}, "
        f"Difference: {original_positive_count - increased_positive_count}"
    )
    print(
        f"Differences in counts: Original negative count: {original_negative_count}, "
        f"Increased negative count: {increased_negative_count}, "
        f"Difference: {original_negative_count - increased_negative_count}"
    )
    print(
        f"Differences in averages: Original positive average: {original_positive_average}, "
        f"Increased positive average: {increased_positive_average}, "
        f"Difference: {original_positive_average - increased_positive_average}"
    )
    print(
        f"Differences in averages: Original negative average: {original_negative_average}, "
        f"Increased negative average: {increased_negative_average}, "
        f"Difference: {original_negative_average - increased_negative_average}"
    )


def task_3():
    print("Task 4: List index operations")
    random_list = [round(random.random() * random.randint(1, 9), 2) for _ in range(20)]
    print(f"Original list: \n{random_list}\n")
    print(f"Index of biggest element: {random_list.index(max(random_list))}")
    print(f"Min/Max difference: {max(random_list) - min(random_list)}")
    # We have random floats here, no chance to have an even number in this list, so I add one
    random_list.append(random.randint(1, 9) * 2)
    print(f"Max even element: {max([x for x in random_list if x % 2 == 0])}")
    print(f"Min positive element: {min([x for x in random_list if x > 0])}")
    min_index = random_list.index(min(random_list))
    max_index = random_list.index(max(random_list))
    random_list[min_index], random_list[max_index] = random_list[max_index], random_list[min_index]
    print(f"List after swapping min and max: \n{random_list}")


def task_4():
    print("Task 5: List sorting")
    best_songs = [
        "Samurai Diva",  # by Yuko Suzuhana
        "The Hole in the Wall",  #  by Jan Valta
        "Nija",  # by Orbit Culture
        "Through my veins",  # by Ancient Bards
        "Burden",  # by Opeth
        "The Apparition",  # by Sleep Token
        "Aqua Regia",  # by Sleep Token
        "千本桜",  # by Wagakki Band
        "Karl Denke",  # by Heldmachine
        "Kuttenberg Market",  # by Jan Valta
        "Voices in my head",  # by Falling in Reverse
        "BEG!",  # by Vana
    ]
    print(f"Original list: \n{best_songs}\n")
    print("Sorted by length (ascending): \n", sorted(best_songs, key=len))
    print("Sorted by length (descending): \n", sorted(best_songs, key=len, reverse=True))
    longest_song = max(best_songs, key=len)
    print(f"Longest song: {longest_song}")
    shortest_song = min(best_songs, key=len)
    print(f"Shortest song: {shortest_song}")
    del best_songs[best_songs.index(shortest_song)]
    del best_songs[best_songs.index(longest_song)]
    print("Updated list after removing the longest and shortest songs: \n", best_songs)


def task_5():
    print("Task 5: Set/list operations")
    random_list = [random.randint(-10, 12) for _ in range(10)]
    print(f"Original list: {random_list}")
    has_repetitions = len(random_list) != len(set(random_list))
    print("Has repetitions" if has_repetitions else "No repetitions")


def task_6():
    print("Task 6: Set operations")
    random_list_1 = [random.randint(1, 9) for _ in range(10)]
    random_list_2 = [random.randint(1, 9) for _ in range(10)]
    print(f"Original lists: \nList 1: {random_list_1}\nList 2: {random_list_2}")
    print(f"Joined sets: {set(random_list_1).union(set(random_list_2))}")
    print(f"Intersection: {set(random_list_1).intersection(set(random_list_2))}")


def task_7():
    print("Task 7: Dictionary operations")
    human = {
        "name": "Yuko",
        "surname": "Suzuhana",
        "fathers_name": "Japonivna",
        "age": 30,
        "email": "yukosuzu@gmail.com",
        "phone": "+81 123 456 7890",
    }
    print(f"Surname: {human['surname']}")
    print(f"Age: {human['age']}")
    print(f"Email: {human.get('email', 'No email provided')}")


if __name__ == "__main__":
    print("My tasks number is 4!")
    task_1_1()
    task_1_2()
    task_2()
    task_3()
    task_4()
    task_5()
    task_6()
    task_7()

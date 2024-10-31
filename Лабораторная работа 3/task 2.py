def find_common_participants(first_group, second_group, splitter=","):
    first_team = first_group.split(splitter)
    second_team = second_group.split(splitter)
    common_participants = list(set(first_team).intersection(second_team))
    common_participants.sort()

    return common_participants


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(find_common_participants(participants_first_group, participants_second_group, "|"))

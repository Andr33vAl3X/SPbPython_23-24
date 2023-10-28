#Вы организуете встречу для двух групп участников, и вам необходимо определить,
#кто является общими участниками для обеих групп.
#Для этого вам нужно написать функцию, которая будет принимать две строки с фамилиями участников,
#перечисленными без пробелов через разделитель.
#Чаще всего в качестве разделителя используется запятая.

def find_common_participants(participants_first_group, participants_second_group, separator=","):
    first_group = set(participants_first_group.split(separator))
    second_group = set(participants_second_group.split(separator))

    common_participants = list(first_group.intersection(second_group))
    return sorted(common_participants)

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
common_participants = find_common_participants(participants_first_group, participants_second_group, separator="|")

print(common_participants)

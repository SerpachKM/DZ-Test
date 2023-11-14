courses = ["Python-разработчик с нуля", "Java-разработчик с нуля", "Fullstack-разработчик на Python",
           "Frontend-разработчик с нуля"]

mentors = [
    ["Евгений Шмаргунов", "Олег Булыгин", "Дмитрий Демидов", "Кирилл Табельский", "Александр Ульянцев",
     "Александр Бардин", "Александр Иванов", "Антон Солонилин", "Максим Филипенко", "Елена Никитина", "Азамат Искаков",
     "Роман Гордиенко"],
    ["Филипп Воронов", "Анна Юшина", "Иван Бочаров", "Анатолий Корсаков", "Юрий Пеньков", "Илья Сухачев",
     "Иван Маркитан", "Ринат Бибиков", "Вадим Ерошевичев", "Тимур Сейсембаев", "Максим Батырев", "Никита Шумский",
     "Алексей Степанов", "Денис Коротков", "Антон Глушков", "Сергей Индюков", "Максим Воронцов", "Евгений Грязнов",
     "Константин Виролайнен", "Сергей Сердюк", "Павел Дерендяев"],
    ["Евгений Шмаргунов", "Олег Булыгин", "Александр Бардин", "Александр Иванов", "Кирилл Табельский",
     "Александр Ульянцев", "Роман Гордиенко", "Адилет Асканжоев", "Александр Шлейко", "Алена Батицкая", "Денис Ежков",
     "Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Максим Филипенко", "Елена Никитина"],
    ["Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Валерий Хаслер", "Татьяна Тен", "Александр Фитискин",
     "Александр Шлейко", "Алена Батицкая", "Александр Беспоясов", "Денис Ежков", "Николай Лопин", "Михаил Ларченко"]
]


def get_all_mentors():
    all_list = []
    [[all_list.append(m) for m in i] for i in mentors]
    return all_list


def get_unique_names():
    all_list = get_all_mentors()
    all_names_list = []
    for mentor in all_list:
        name = mentor.split(' ')
        all_names_list.append(name[0])
    unique_names = set(all_names_list)
    unique_list = list(unique_names)
    all_names_sorted = sorted(unique_list)
    return all_names_sorted


durations = [14, 20, 12, 20]

courses_list = []
for course, mentor, duration in zip(courses, mentors, durations):
    course_dict = {"title": course, "mentors": mentor, "duration": duration}
    courses_list.append(course_dict)


def find_name(course):
    all_name = []
    full_name = course.get('mentors')
    [all_name.append(name.split()[0]) for name in full_name]
    unique_names = sorted(set(all_name))

    name_list = []
    for i in unique_names:
        if all_name.count(i) > 1:
            for k in course['mentors']:
                if i in k and k not in name_list:
                    name_list.append(k)
    return name_list


duration_index = []
mcount_index = []

for index, course in enumerate(courses_list):
    duration_index.append([course["duration"], index])
    mcount_index.append([len(course["mentors"]), index])
duration_index.sort()
mcount_index.sort()
indexes_d = []
indexes_m = []

for id1 in duration_index:
    indexes_d.append(id1[1])
for id2 in mcount_index:
    indexes_m.append(id2[1])
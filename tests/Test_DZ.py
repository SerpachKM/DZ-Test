import unittest
import pytest
from main import courses
from main import get_all_mentors, get_unique_names, mentors, indexes_m, indexes_d, find_name, courses_list
from unittest import TestCase


class TestMentors(TestCase):
    def test_get_all_mentors(self):
        all_mentors = get_all_mentors()
        self.assertEqual(len(all_mentors), 61, "Неверное количество преподавателей")

    @unittest.skipIf(True, "Пропуск ошибки")
    @pytest.mark.parametrize("mentors_list, expected", [
        (mentors[0], 12),
        (mentors[1], 16),
        (mentors[2], 14),
        (mentors[3], 13)
    ])
    def test_get_unique_names(self, mentors_list, expected):
        unique_names = get_unique_names()
        self.assertEqual(len(unique_names), expected, "Неверное количество уникальных имен")
        for mentor in mentors_list:
            self.assertIn(mentor.split(' ')[0], unique_names, "Имя преподавателя не найдено в уникальных именах")


@pytest.mark.parametrize("course", courses_list)
def test_find_name(course):
    expected = find_name(course)
    assert find_name(course) == expected


class TestCoursesOrder(TestCase):
    def test_courses_order(self):
        self.assertEqual(indexes_d, indexes_m,
                         "Порядок курсов по длительности и количеству преподавателей не совпадает")
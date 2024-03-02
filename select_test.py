#!/usr/bin/env python3
import sqlite3
import unittest

from lib.sql_queries import (
    select_all_female_bears_return_name_and_age,
    select_all_bears_names_and_orders_in_alphabetical_order,
    select_all_bears_names_and_ages_that_are_alive_and_order_youngest_to_oldest,
    select_oldest_bear_and_returns_name_and_age,
    select_youngest_bear_and_returns_name_and_age,
)

class TestSelect(unittest.TestCase):
    def setUp(self):
        self.connection = sqlite3.connect(":memory:")
        self.cursor = self.connection.cursor()

        create_file = open("lib/create.sql")
        create_as_string = create_file.read()
        self.cursor.executescript(create_as_string)

        insert_file = open("lib/insert.sql")
        insert_as_string = insert_file.read()
        self.cursor.executescript(insert_as_string)

    def tearDown(self):
        self.cursor.close()
        self.connection.close()

    def test_select_all_female_bears_return_name_and_age(self):
        result = self.cursor.execute(select_all_female_bears_return_name_and_age)
        expected_result = [
            ("Tabitha", 6),
            ("Melissa", 13),
            ("Wendy", 6)
        ]
        self.assertEqual(result.fetchall(), expected_result)

    def test_select_all_bears_names_and_orders_in_alphabetical_order(self):
        result = self.cursor.execute(select_all_bears_names_and_orders_in_alphabetical_order)
        expected_result = [
            (None,),
            ("Grinch",),
            ("Melissa",),
            ("Mr. Chocolate",),
            ("Rowdy",),
            ("Sergeant Brown",),
            ("Tabitha",),
            ("Wendy",)
        ]
        self.assertEqual(result.fetchall(), expected_result)

    def test_select_all_bears_names_and_ages_that_are_alive_and_order_youngest_to_oldest(self):
        result = self.cursor.execute(select_all_bears_names_and_ages_that_are_alive_and_order_youngest_to_oldest)
        expected_result = [
            ("Grinch", 2),
            ("Tabitha", 6),
            ("Wendy", 6),
            ("Rowdy", 10),
            ("Melissa", 13),
        ]
        self.assertEqual(result.fetchall(), expected_result)

    def test_select_oldest_bear_and_returns_name_and_age(self):
        result = self.cursor.execute(select_oldest_bear_and_returns_name_and_age)
        expected_result = [
            ("Mr. Chocolate", 20),
        ]
        self.assertEqual(result.fetchall(), expected_result)

    def test_select_youngest_bear_and_returns_name_and_age(self):
        result = self.cursor.execute(select_youngest_bear_and_returns_name_and_age)
        expected_result = [
            ("Grinch", 2),
        ]
        self.assertEqual(result.fetchall(), expected_result)


if __name__ == "__main__":
    unittest.main()
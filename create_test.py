#!/usr/bin/env python3

import sqlite3
import unittest

class TestCreate(unittest.TestCase):
    def setUp(self):
        self.connection = sqlite3.connect(":memory:")
        self.cursor = self.connection.cursor()

        sql_file = open("lib/create.sql")
        sql_as_string = sql_file.read()
        self.cursor.executescript(sql_as_string)

    def tearDown(self):
        self.cursor.close()
        self.connection.close()

    def test_creates_bears_with_name_column(self):
        result = self.cursor.execute("SELECT name FROM bears;")
        self.assertIsNotNone(result.fetchall())

    def test_creates_bears_with_age_column(self):
        result = self.cursor.execute("SELECT age FROM bears;")
        self.assertIsNotNone(result.fetchall())

    def test_creates_bears_with_sex_column(self):
        result = self.cursor.execute("SELECT sex FROM bears;")
        self.assertIsNotNone(result.fetchall())

    def test_creates_bears_with_color_column(self):
        result = self.cursor.execute("SELECT color FROM bears;")
        self.assertIsNotNone(result.fetchall())

    def test_creates_bears_with_temperament_column(self):
        result = self.cursor.execute("SELECT temperament FROM bears;")
        self.assertIsNotNone(result.fetchall())

    def test_creates_bears_with_alive_column(self):
        result = self.cursor.execute("SELECT alive FROM bears;")
        self.assertIsNotNone(result.fetchall())

    def test_creates_bears_with_id_pk(self):
        result = self.cursor.execute("PRAGMA table_info(bears);")
        columns = [column[1] for column in result.fetchall()]
        self.assertIn("id", columns)
        self.assertIn("INTEGER PRIMARY KEY", columns)


if __name__ == "__main__":
    unittest.main()
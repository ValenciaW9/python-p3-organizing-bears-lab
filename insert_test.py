#!/usr/bin/env python3
import sqlite3
import unittest

class TestInsert(unittest.TestCase):
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

    def test_inserts_eight_bears_into_table(self):
        result = self.cursor.execute("SELECT COUNT(*) FROM bears;")
        assert result.fetchone()[0] == 8

    def test_has_unnamed_bear(self):
        result = self.cursor.execute("SELECT COUNT(*) FROM bears WHERE name IS NULL;")
        assert result.fetchone()[0] == 1

if __name__ == "__main__":
    unittest.main()
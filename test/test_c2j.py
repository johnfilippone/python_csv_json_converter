import unittest
import sys, os
sys.path.append(os.getcwd() + "/../src")
from c2j import get_json_from_csv

class C2VTest(unittest.TestCase):
    def test_valid_format(self):
        csv_data = "name,id\r\njohn,0\r\nfred,1\r\n"
        json_data = [{"name":"john", "id":"0"}, {"name":"fred", "id":"1"}]
        self.assertEqual(get_json_from_csv(csv_data), json_data)

    def test_pipe_dialect(self):
        csv_data = "name|id\r\njohn|0\r\nfred|1\r\n"
        json_data = [{"name":"john", "id":"0"}, {"name":"fred", "id":"1"}]
        self.assertEqual(get_json_from_csv(csv_data, delimiter='|'), json_data)

    def test_tab_dialect(self):
        csv_data = "name\tid\r\njohn\t0\r\nfred\t1\r\n"
        json_data = [{"name":"john", "id":"0"}, {"name":"fred", "id":"1"}]
        self.assertEqual(get_json_from_csv(csv_data, delimiter='\t'), json_data)

    def test_missing_data(self):
        csv_data = "name,id\r\njohn,\r\n,1\r\n"
        json_data = [{"name":"john", "id":""}, {"name":"", "id":"1"}]
        self.assertEqual(get_json_from_csv(csv_data), json_data)

if __name__ == "__main__":
    unittest.main()


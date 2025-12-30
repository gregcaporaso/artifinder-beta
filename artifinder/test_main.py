import unittest

from typer.testing import CliRunner

from .main import app

runner = CliRunner()


class ArtifinderCliTests(unittest.TestCase):
    def test_app_missing_result(self):
        result = runner.invoke(app, [".", "not-a-real-result"])
        print(result)
        self.assertEqual(result.exit_code, 1)
        #self.assertRaises(FileNotFoundError, )
        assert "Target Result file path does not exist: not-a" in str(result.output)

    def test_app_missing_search_dir(self):
        result = runner.invoke(app, ["not-a-real-directory", "not-a-real-result"])

        self.assertEqual(result.exit_code, 1)
        assert "Search directory does not exist: not-a" in str(result.output)

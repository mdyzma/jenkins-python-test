import pytest
from click.testing import CliRunner

from irisvmpy import iris

class TestCLI(object):

    @pytest.fixture()
    def runner(self):
        return CliRunner()

    def test_print_help_succeeds(self, runner):
        result = runner.invoke(iris.cli, ['--help'])
        assert result.exit_code == 0
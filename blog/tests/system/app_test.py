from unittest import TestCase
import app
from unittest.mock import patch
from blog import Blog

class AppTest(TestCase):

    # def test_menu_prints_prompt(self):
    #     with patch('builtins.print') as moked_print:
    #         app.menu()
    #         moked_print.assert_called_with(app.MENU_PROMPT)
    #
    # def test_menu_calls_print_blogs(self):
    #     with patch('app.print_blogs') as moked_print_blogs:
    #         with patch('builtins.print'):
    #             app.menu()
    #             moked_print_blogs.assert_called_with()

    def test_print_blog(self):
        blog = Blog('Test', 'Test Author')
        app.blogs = {'Test': blog}
        with patch('builtins.print') as moked_print:
            app.print_blogs()
            moked_print.assert_called_with('- Test by Test Author (0 posts)')
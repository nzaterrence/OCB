import openerp.tests

class WebSuite(openerp.tests.HttpCase):
    def test_01_js(self):
        self.phantom_js('/web/tests?module=web',"","", login='admin')

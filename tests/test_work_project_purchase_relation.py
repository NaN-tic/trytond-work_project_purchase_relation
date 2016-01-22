# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
import unittest
# import doctest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import test_view, test_depends
# TODO: Remove if no sceneario needed.
# from trytond.tests.test_tryton import doctest_setup, doctest_teardown


class TestCase(unittest.TestCase):
    'Test module'

    def setUp(self):
        trytond.tests.test_tryton.install_module('work_project_purchase_relation')

    def test0005views(self):
        'Test views'
        test_view('work_project_purchase_relation')

    def test0006depends(self):
        'Test depends'
        test_depends()


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestCase))
    # TODO: remove if no scenario needed.
    #suite.addTests(doctest.DocFileSuite('scenario_work_project_purchase_relation.rst',
    #        setUp=doctest_setup, tearDown=doctest_teardown, encoding='utf-8',
    #        optionflags=doctest.REPORT_ONLY_FIRST_FAILURE))
    return suite

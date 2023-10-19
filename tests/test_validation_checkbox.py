import allure

from elements.checkboxes import Checkboxes

Ch = Checkboxes()

def test_checking_checkboxes_section_about_project(standard_preparation):

    Ch.checking_status_change_checkboxes()

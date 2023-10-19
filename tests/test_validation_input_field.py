import os

import allure

from elements.input_fields import InputFields

IF = InputFields()

def test_validation_field_name(standard_preparation):

    IF.validation_field_name()

def test_validation_field_email(standard_preparation):

    IF.validation_field_email()

def test_validation_field_telephone(standard_preparation):

    IF.validation_field_telephone()

def test_validation_field_company(standard_preparation):

    IF.validation_field_company()

def test_validation_field_tell_about_your_project(standard_preparation):

    IF.validation_field_tell_about_your_project()


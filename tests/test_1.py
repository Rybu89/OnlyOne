from base.base_class import Base
from elements.input_fields import InputFields
from elements.titles_and_names import TitlesAndNames

TaN = TitlesAndNames()
IF = InputFields()
base = Base()

def test():

    # print(TaN.sections_names)
    # print(TaN.radio_button_names)
    # print(TaN.titles_messages)
    print(IF.valid_data_for_field_email)

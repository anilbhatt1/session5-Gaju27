import inspect
import os
import re

import pytest

import session5

README_CONTENT_CHECK_FOR = [
    'time_it',
    'squared_power_list',
    'polygon_area',
    'temp_converter',
    'speed_converter'
]


def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"


def test_readme_contents():
    readme = open("README.md", "r")
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 1, "Make your README.md file interesting! Add atleast 500 words"


def test_readme_proper_description():
    READMELOOKSGOOD = True
    f = open("README.md", "r")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"


def test_readme_file_for_formatting():
    f = open("README.md", "r")
    content = f.read()
    f.close()
    assert content.count("#") >= 5


def test_indentations():
    ''' Returns pass if used four spaces for each level of syntactically \
    significant indenting.'''
    lines = inspect.getsource(session5)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines"


def test_function_name_had_cap_letter():
    functions = inspect.getmembers(session5, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"


def test_print_repetitons_zero_and_negative():
    with pytest.raises(ValueError) as e_info:
        session5.time_it(print, 1, 2, 3, sep='-', end=' ***\n', repetitons=-1)
    with pytest.raises(ValueError) as e_info:
        session5.time_it(print, 1, 2, 3, sep='-', end=' ***\n', repetitons=0)


def test_invalid_repetion_valueerror_provides_relevant_message():
    with pytest.raises(ValueError, match=r".* greater than 0 .*"):
        session5.time_it(print, 1, 2, 3, sep='-', end=' ***\n', repetitons=-1)


def test_squared_power_list_assertion():
    assert session5.squared_power_list(2, start=0, end=5) == [1, 2, 4, 8, 16, 32]


def test_squared_power_list_assertion_for_only_negetive_start():
    assert session5.squared_power_list(2, start=-5, end=3) == [0.03125, 0.0625, 0.125, 0.25, 0.5, 1, 2, 4, 8]


def test_squared_power_list_assertion_for_only_negetive_end():
    assert session5.squared_power_list(2, start=0, end=-3) == []


def test_squared_power_list_assertion_for_negetive_start_end():
    assert session5.squared_power_list(2, start=-6, end=-3) == [0.015625, 0.03125, 0.0625, 0.125]


def test_proper_number_square_power_list():
    with pytest.raises(ValueError):
        session5.squared_power_list(-1, start=0, end=5)


def test_invalid_number_square_power_list_relevant_message():
    with pytest.raises(ValueError, match=r".* Power value .*"):
        session5.time_it('squared_power_list', -1, start=0, end=5, repetitons=5)
    with pytest.raises(ValueError, match=r".* Power value .*"):
        session5.time_it('squared_power_list', 0, start=0, end=5, repetitons=5)


def test_invalid_range_valueerror_provides_relevant_message():
    with pytest.raises(ValueError, match=r".* range of 3 to 6.*"):
        session5.time_it("polygon_area", 15, sides=2, repetitons=10)


def test_invalid_side_for_polygon():
    with pytest.raises(ValueError):
        session5.time_it("polygon_area", 15, sides=7, repetitons=10)
    with pytest.raises(ValueError):
        session5.time_it("polygon_area", 15, sides=0, repetitons=10)


def test_polygon_area_assertion_for_triangle():
    assert session5.polygon_area(15, sides=3) == 97.42785792574935


def test_polygon_area_assertion_for_square():
    assert session5.polygon_area(15, sides=4) == 225


def test_polygon_area_assertion_for_pentagon():
    assert session5.polygon_area(15, sides=5) == 36.28811764110858


def test_polygon_area_assertion_for_hexagon():
    assert session5.polygon_area(15, sides=6) == 584.5671475544962


def test_invalid_temp_input_provides_relevant_message():
    with pytest.raises(Exception, match=r".* standard temperature .*"):
        session5.time_it("temp_converter", 100, temp_given_in='g', convert_temp='k', repetitons=100)


def test_invalid_temp_output_provides_relevant_message():
    with pytest.raises(Exception, match=r".* value must in 'c' or 'k' .*"):
        session5.time_it("temp_converter", 100, temp_given_in='f', convert_temp='g', repetitons=100)
    with pytest.raises(Exception, match=r".* value must in 'f' or 'k' .*"):
        session5.time_it("temp_converter", 100, temp_given_in='c', convert_temp='g', repetitons=100)
    with pytest.raises(Exception, match=r".* value must in 'f' or 'c' .*"):
        session5.time_it("temp_converter", 100, temp_given_in='k', convert_temp='g', repetitons=100)


def test_wrong_format_speed_converter_relevant_message():
    with pytest.raises(Exception, match=r".* speed converter .*"):
        session5.time_it("speed_converter", 100, dist='watt', time='joule', repetitons=200)


def test_kmph_to_yard_day_speed_convertion():
    assert session5.speed_converter(100, dist='yard', time='min') == 1822.7


def test_kmph_to_feet_hour_speed_convertion():
    assert session5.speed_converter(100, dist='ft', time='hr') == 328100


def test_kmph_to_feet_milli_second_speed_convertion():
    assert session5.speed_converter(100, dist='ft', time='hr') == 328100


def test_kmph_to_yard_minute_speed_convertion():
    assert session5.speed_converter(100, dist='yard', time='min') == 1822.7


def test_kmph_to_mtr_minute_speed_convertion():
    assert session5.speed_converter(100, dist='m', time='min') == 1.6666666666666667

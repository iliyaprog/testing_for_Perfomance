import json
import sys


def for_values(i_list, values_data):
    for i in i_list:
        for value in values_data['values']:
            if value['id'] == i['id']:
                desired_value = value['value']
                i['value'] = desired_value
                break
        if 'values' in i.keys():
            for_values(i['values'], values_data)


def new_file(tests_json, values_json):
    with open(values_json, 'r', encoding='utf-8') as v_file:
        values_data = json.load(v_file)
        with open(tests_json, 'r', encoding='utf-8') as t_file:
            tests_data = json.load(t_file)
            for i_dict_tests in tests_data['tests']:
                for value in values_data['values']:
                    if value['id'] == i_dict_tests['id']:
                        desired_value = value['value']
                        break
                i_dict_tests['value'] = desired_value
                if 'values' in i_dict_tests.keys():
                    for_values(i_dict_tests['values'], values_data)
            with open('report.json', "w", encoding="utf-8") as end_test_file:
                json.dump(tests_data, end_test_file, sort_keys=True, indent=1, ensure_ascii=False)


if __name__ == "__main__":
    new_file(sys.argv[1], sys.argv[2])

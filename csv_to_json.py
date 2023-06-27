import csv
import json

def read_csv():
    countries = []
    with open('country_codes.csv', 'r') as country_code_csv:
        csv_reader = csv.reader(country_code_csv)
        for line in csv_reader:
            countries.append(line)
    return countries


def csv_to_dict(countries):
    country_dict_list = []
    for country in countries:
        country_dict = {
            'country': country[0],
            'code': country[1]
        }
        country_dict_list.append(country_dict)
    return country_dict_list


def write_json_file(dict_list):
    i = 0
    country_json_list = []
    json_file = open('countries.json', 'w')
    json_file.write('[')
    for dict in dict_list:
        i += 1
        country_json = json.dumps(dict)
        country_json_list.append(country_json)
        if i == len(dict_list):
            json_file.writelines(f'{country_json}\n')
        else:
            json_file.writelines(f'{country_json},\n')
    json_file.write(']')
    json_file.close()


def csv_to_json():
    countries = read_csv()
    country_dict_list = csv_to_dict(countries)
    write_json_file(country_dict_list)


csv_to_json()
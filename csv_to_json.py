import csv
import json

def read_csv(file):
    data_set = []
    with open(file, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for each_line in csv_reader:
            data_set.append(each_line)
    return data_set


def csv_to_dict(data_set):
    dict_list = []
    for data in data_set:
        dict = {
            data_set[0][0]: data[0],
            data_set[0][1]: data[1]
        }
        dict_list.append(dict)
    return dict_list


def write_json_file(dict_list, file_name):
    i = 0
    json_file = open(file_name, 'w')
    json_file.write('[')
    for dict in dict_list:
        print(dict)
        i += 1
        json_ = json.dumps(dict)
        if i == len(dict_list):
            json_file.writelines(f'{json_}\n')
        else:
            json_file.writelines(f'{json_},\n')
    json_file.write(']')
    json_file.close()


def csv_to_json(csv_file):
    data_set = read_csv(csv_file)
    dict_list = csv_to_dict(data_set)
    write_json_file(dict_list[1:], 'countries.json')


csv_to_json('country_codes.csv')
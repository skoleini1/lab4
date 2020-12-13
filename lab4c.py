#!/usr/bin/env python3

# Author : Sama Koleini
# Author ID: skoleini1


# Dictionaries
dict_york = {'Address': '29 Castlebury Cres', 'City': 'Toronto', 'Country': 'Canada', 'Postal Code': 'M2H1W7', 'Province': 'ON'}
dict_newnham = {'Address': '1750 Finch Ave E', 'City': 'Toronto', 'Country': 'Canada', 'Postal Code': 'M2J2X5', 'Province': 'ON'}
# Lists
list_keys = ['Address', 'City', 'Country', 'Postal Code', 'Province']
list_values = ['29 Castlebury cres', 'Toronto', 'Canada', 'M2H1W7', 'ON']

def create_dictionary(keys, values):
    # Place code here - refer to function specifics in section below
	newDict = dict()	
	for i in range(len(keys)):
		newDict[keys[i]]=values[i]
	return newDict
		


def shared_values(dict1, dict2):
    # Place code here - refer to function specifics in section below

	l1 = dict1.values()
	l2 = dict2.values()

	s1 = set(l1)
	s2 = set(l2)
	newSet = s2.intersection(s1)
	return newSet





if __name__ == '__main__':
    york = create_dictionary(list_keys, list_values)
    print('York: ', york)
    common = shared_values(dict_york, dict_newnham)
    print('Shared Values', common)


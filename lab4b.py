#!/usr/bin/env python3

# Author : Sama Koleini
# Author ID: skoleini1

def join_lists(l1, l2):
    # join_lists will return a list that contains every value from both l1 and l2
	
	s_1 = set(l1)
	s_2 = set(l2)
	new_Set = s_1 | s_2
	return list(new_Set)


def match_lists(l1, l2):
    # match_lists will return a list that contains all values found in both l1 and l2

	s_1 = set(l1)
	s_2 = set(l2)
	new_Set = s_2.intersection(s_1)
	return list(new_Set)




def diff_lists(l1, l2):
    # diff_lists will return a list that contains all different values, which are not shared between the lists
	s_1 = set(l1)
	s_2 = set(l2)

	new_Set = s_2.symmetric_difference(s_1)
	return list(new_Set)



if __name__ == '__main__':
    list1 = list(range(1,10))
    list2 = list(range(5,15))
    print('list1: ', list1)
    print('list2: ', list2)
    print('join: ', join_lists(list1, list2))
    print('match: ', match_lists(list1, list2))
    print('diff: ', diff_lists(list1, list2))


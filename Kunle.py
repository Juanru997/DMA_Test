import pandas as pd

print('wogoukunle')
print('wogoukunle2')
print('wogoukunle3')

print(pd.__version__)

# list
# dictionaries
# object-oriented

list_names = ['Yan','Ellie','Bognani']
dict_bday = {'Yan':21, 'Ellie':21, 'Bognani':20}

print(list_names)
print(dict_bday)

test_list = list()
test_series = pd.Series(dict_bday)
print(test_series)

test_dataframe = pd.DataFrame (dict_bday, index=columns(dict_bday.keys()))
print(test_dataframe)



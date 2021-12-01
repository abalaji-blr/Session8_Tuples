import session8_tuples 
from faker import Faker
from collections import namedtuple
from functools import wraps
import datetime, time
import random

def run_test(fn) -> 'bool':
  result = fn()
  if result:
    print(f'{fn.__doc__[0:-3]}:  PASSED')
  else:
    print(f'{fn.__doc__[0:-3]}:   FAILED')

def run_test_with_arg(fn, *arg) -> 'bool':
  result = fn(*arg)
  if result:
    print(f'{fn.__doc__[0:-3]}:  PASSED')
  else:
    print(f'{fn.__doc__[0:-3]}:   FAILED') 




# profile using namedtuple

def test_profile_uses_namedtuple(profile_ds) -> 'bool':
  '''
  Check whether the profile uses namedtuples.
  '''
  return(isinstance(profile_ds[0], tuple))

def test_examine_result_for_namedtuple(result) -> 'bool':
  '''
  Check the result is in terms of namedtuple
  '''
  return(isinstance(result, tuple))

def test_examine_result_for_fields(result) -> 'bool':
  '''
  Examine all the expected fields are in result.
  '''
  expected_fields = ['largest_blood_type', 'mean_current_location', 'oldest_person_age', 'average_age']
  for field in result._fields:
    if field not in expected_fields:
      return False
  return True


def test_examine_oldest_person_age(result) -> 'bool':
  '''
  Examine oldest person age is greater than average age
  '''
  return(result.oldest_person_age > result.average_age)

def test_examine_mean_current_location(result) -> 'bool':
  '''
  Examine mean current location has both lat and lng.
  '''
  return(len(result.mean_current_location) == 2)


# Run profile tests
profile_ds = session8_tuples.gen_profile_dataset(2)
run_test_with_arg(test_profile_uses_namedtuple, profile_ds)

result_profile_namedtuple = session8_tuples.gen_profile_report_using_namedtuple()

run_test_with_arg(test_examine_result_for_namedtuple, result_profile_namedtuple)
run_test_with_arg(test_examine_result_for_fields, result_profile_namedtuple)
run_test_with_arg(test_examine_oldest_person_age, result_profile_namedtuple)
run_test_with_arg(test_examine_mean_current_location, result_profile_namedtuple)

################ profiles using dictionary #####################
def test_profile_uses_dict(ds) -> 'bool':
  '''
  Examine whether profile uses dictionary.
  '''
  return(type(ds[0]) == dict)

def test_examine_result_for_dict(result) -> 'bool':
  '''
  Check the result is dictionary.
  '''
  return(type(result) == dict)

def test_examine_result_dict_has_all_info(result) -> 'bool':
  '''
  Examine the result dictionary has all info.
  '''
  expected_keys = ['largest_blood_type', 'mean_current_location', 'oldest_person_age', 'average_age']
  for k in result.keys():
    if k not in expected_keys:
      return False
  return True

def test_examine_oldest_person_age_dict(result) -> 'bool':
  '''
  Examine oldest person age is greater than average age
  '''
  return(result['oldest_person_age'] > result['average_age'])

def test_examine_mean_current_location_dict(result) -> 'bool':
  '''
  Examine mean current location has both lat and lng.
  '''
  return(len(result['mean_current_location']) == 2)


## tests using dictonary
ds = session8_tuples.gen_profile_dataset_using_dict(2)
run_test_with_arg(test_profile_uses_dict, ds)

result_profile_dict = session8_tuples.gen_profile_report_using_dictionary()

run_test_with_arg(test_examine_result_for_dict, result_profile_dict)
run_test_with_arg(test_examine_result_dict_has_all_info, result_profile_dict)
run_test_with_arg(test_examine_oldest_person_age_dict, result_profile_dict)
run_test_with_arg(test_examine_mean_current_location_dict, result_profile_dict)

######################## stock exchange #####################
all_companies = session8_tuples.stock_exchange(100)

def test_does_doc_string_exist(func) -> 'bool':
  '''
  Check whether doc string exists or not.
  '''
  if len(func.__doc__) == 0:
    return False
  return True

def test_uses_namedtuples(all_companies) -> 'bool':
  '''
  Check whether Stock uses namedtuple.
  '''
  return(isinstance(all_companies[0], tuple))

def test_check_num_companies(all_companies) -> 'bool':
  '''
  Check whether atleast 100 companies are listed in the exchange.
  '''
  return(len(all_companies) >= 100)

def test_check_namedtuple_complete(all_companies) -> 'bool':
  '''
  Check the stock namedtuple for all fields.
  '''
  #test_name = 'Check the stock namedtuple for all fields'
  fields = ['Name', 'Symbol', 'Open', 'High', 'Close']
  tup_fields = all_companies[0]._fields

  for f in fields:
    if f not in tup_fields:
      return False
  return True

def test_is_company_name_unique(all_companies) -> 'bool':
  '''
  Check whether company name is unique.
  '''
  companies = [stock.Name for stock in all_companies]
  return(len(companies) == len(set(companies)))

def test_is_ticker_symbol_unique(all_companies) -> 'bool':
  '''
  Check whether the ticker is unique.
  '''
  ticker_list = [stock.Symbol for stock in all_companies]
  #print(ticker_list)
  if len(ticker_list) != len(set(ticker_list)):
    return False
  else:
    return True

def test_is_high_ge_open(all_companies) -> 'bool':
  '''
  Check whether the high price is greater than or equal to the open price.
  '''
  for stock in all_companies:
    if stock.High < stock.Open:
      return False
  return True

def test_is_high_ge_close(all_companies) -> 'bool':
  '''
  Check whether high price is greater than or equal to close price.
  '''
  for stock in all_companies:
    if stock.High < stock.Close:
      return False
  return True

def test_is_weight_positive(all_companies) -> 'bool':
  '''
  Check company's weight for positive value.
  '''
  for stock in all_companies:
    if stock.CompanyWeight < 0:
      return False
  return True

def test_high_index_gt_open_index(all_companies) -> 'bool':
  '''
  Check weighted high stock index is >= to open stock index.
  '''
  open_index = sum([stock.Open * stock.CompanyWeight for stock in all_companies])
  high_index = sum([stock.High * stock.CompanyWeight for stock in all_companies])
  if int(high_index) < int(open_index):
    return False
  return True

def test_high_index_gt_close_index(all_companies) -> 'bool':
  '''
  Check weighted high stock index is >= close stock index
  '''
  close_index = sum([stock.Close * stock.CompanyWeight for stock in all_companies])
  high_index = sum([stock.High * stock.CompanyWeight for stock in all_companies])

  if int(high_index) < int(close_index):
    return False
  return True

### stock tests
stock_tests = [test_uses_namedtuples,
               test_check_num_companies,
               test_check_namedtuple_complete,
               test_is_company_name_unique,
               test_is_ticker_symbol_unique,
               test_is_high_ge_open,
               test_is_high_ge_close,
               test_is_weight_positive,
               test_high_index_gt_open_index,
               test_high_index_gt_close_index
               ]

def run_stock_test(test_name_func):
  func = test_name_func
  if func(all_companies):
    print(f'{func.__doc__[0:-3]}  :  PASSED')
  else:
    print(f'{func.__doc__[0:-3]}   : FAILED')

# Run the tests...
for test_name in stock_tests:
  run_stock_test(test_name)

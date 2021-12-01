from faker import Faker
from collections import namedtuple
from functools import wraps
import datetime, time
import random

fake = Faker()

def gen_profile_dataset(num_entries : int) -> 'dataset in namedtuple':
  '''
  Generate the profile dataset. The size of the dataset depends on the
  num_entries.

  Input: num_entries
  Output: dataset ( list of namedtuple of profile)
  '''
  result = []
  Profile = namedtuple('Profile', fake.profile().keys())
  for cnt in range(num_entries):
    # build namedtuple from the dictionary
    result.append(Profile(**fake.profile()))
  return result

# build a custom decorator to measure the time consumed.
# define timed decorator
def timed(fn):
  '''
  Decorator to measure the time consumed.
  '''
  @wraps(fn)
  def inner(*args, **kwargs):
    '''
    Closure function for the timed decorator.
    '''
    start = time.perf_counter()
    result = fn(*args, **kwargs)
    end = time.perf_counter()
    elapsed = end-start
    print(f'Run time: {elapsed}s')
    return result
  return inner


def get_age(birthdate):
  date_today = datetime.date.today()
  age = (date_today - birthdate).days
  return(int(age/365))

@timed
def gen_profile_report_using_namedtuple() -> 'namedtuple':
  '''
  Generate the profile report which calcualtes the following:
  1. largest blood type
  2. mean current location
  3. oldest person age
  4. average age
  '''
  num_entries = 10000
  profile_list = gen_profile_dataset(num_entries)
  #
  bg_dict = dict()
  loc_total = [0,0]
  old_age = 0
  total_age = 0

  # calculate
  for profile in profile_list:
     # blood group
    if profile.blood_group not in bg_dict.keys():
      bg_dict[profile.blood_group] = 1
    else:
      # found the blood group, inc count
      bg_dict[profile.blood_group] = bg_dict[profile.blood_group] +1
      
    # location
    loc_total[0] += profile.current_location[0]
    loc_total[1] += profile.current_location[1]

    # age
    age = get_age(profile.birthdate)
    if age > old_age:
      old_age = age
    total_age += age

  #print(bg_dict)
  # get the max based on count value
  bg_l = max(bg_dict, key=bg_dict.get)
  mean_location = (loc_total[0]/num_entries, loc_total[1]/num_entries)
  #print(bg_l)
  #print(f'Boold group {bg_l} is found {bg_dict[bg_l]} times.')
  #print(f'mean location {mean_location}')
  #print(f'old age is {old_age} years')
  #print(f'aveage age is {total_age/num_entries}')
  RESULT_DATA = namedtuple('RESULT_DATA', 'largest_blood_type mean_current_location oldest_person_age average_age')

  return(RESULT_DATA(bg_l, mean_location, old_age, total_age/num_entries))


### Uisng Dictionary
def gen_profile_dataset_using_dict(num_entries : int) -> 'dataset in dictionary':
  '''
  Generate the profile dataset. The size of the dataset depends on the
  num_entries.

  Input: num_entries
  Output: dataset (list of profile in dictionary format)
  '''
  result = []
  for cnt in range(num_entries):
    result.append(fake.profile())
  return result


@timed
def gen_profile_report_using_dictionary() -> 'dictionary':
  '''
  Generate the profile report which calcualtes the following:
  1. largest blood type
  2. mean current location
  3. oldest person age
  4. average age
  '''
  num_entries = 10000
  profile_list = gen_profile_dataset_using_dict(num_entries)
  #
  bg_dict = dict()
  loc_total = [0,0]
  old_age = 0
  total_age = 0

  # calculate
  for profile in profile_list:
     # blood group
    if profile['blood_group'] not in bg_dict.keys():
      bg_dict[profile['blood_group']] = 1
    else:
      # found the blood group, inc count
      bg_dict[profile['blood_group']] = bg_dict[profile['blood_group']] +1
      
    # location
    loc_total[0] += profile['current_location'][0]
    loc_total[1] += profile['current_location'][1]

    # age
    age = get_age(profile['birthdate'])
    if age > old_age:
      old_age = age
    total_age += age

  #print(bg_dict)
  # get the max based on count value
  bg_l = max(bg_dict, key=bg_dict.get)
  mean_location = (loc_total[0]/num_entries, loc_total[1]/num_entries)
  #print(bg_l)
  #print(f'Boold group {bg_l} is found {bg_dict[bg_l]} times.')
  #print(f'mean location {mean_location}')
  #print(f'old age is {old_age} years')
  #print(f'aveage age is {total_age/num_entries}')

  result = dict()
  result['largest_blood_type'] = bg_l
  result['mean_current_location'] = mean_location
  result['oldest_person_age'] = old_age
  result['average_age'] = total_age/num_entries
  return(result)

################################## stock exchange #################
all_stock_ticker = []
def get_stock_ticker(name):
  '''
  get the stock ticker based on company name
  '''
  ticker = ''.join(x for x in name if x.isupper())
  if ticker not in all_stock_ticker:
    all_stock_ticker.append(ticker)
    return(ticker)

  # if ticker exists, create new one by appending extra alphabet/number
  for idx in range(2,10):
    new_ticker = ticker + str(idx)
    if new_ticker not in all_stock_ticker:
      all_stock_ticker.append(new_ticker)
      return(new_ticker)



def stock_exchange(num_companies: int) -> 'list of company\'s stock details':
  '''
  Create stock exchange with 100 companies.
  '''
  Stock = namedtuple('Stock', 'Name Symbol Open High Close CompanyWeight')
  #num_companies = 100

  all_companies = []
  for _ in range(num_companies):
    name = fake.company()
    symbol = get_stock_ticker(name)
    open = round(random.uniform(10, 1000), 2)

    # make sure high is higher than open price
    factor = round(random.uniform(0.6, 1.6), 2)
    high = round(open * factor, 2) if factor > 1 else open

    # determine the close price
    # basically swing from open to high, also make sure high is always high.
    close = random.uniform(open - random.randint(-10, 10), high - random.randint(-10, 10))
    close = round(close, 2)
    if close > high:
      high = close

    # usually weights are like 2.3 times ...
    company_weight = round(random.uniform(0.1, 3.0), 1)

    all_companies.append(Stock(Name=name, Symbol=symbol, Open=open, 
                               High=high, Close=close, CompanyWeight=company_weight))
  
  [print(x) for x in all_companies]

  index_open = sum(x.Open * x.CompanyWeight for x in all_companies)
  index_open = round(index_open, 2)

  index_high = sum(x.High * x.CompanyWeight for x in all_companies)
  index_high = round(index_high, 2)

  index_close = sum(x.Close * x.CompanyWeight for x in all_companies)
  index_close = round(index_close, 2)
  print('-------------------------------------')
  print(f'index open: {index_open}')
  print(f'index high of day: {index_high}')
  print(f'index at close: { index_close}')
  return(all_companies)

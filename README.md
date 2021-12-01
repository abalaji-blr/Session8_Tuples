# EPAi4 Session8 - Tuples, NamedTuples
### About Namedtuple

In the case of sequence types - **lists and tuples**, the code access the elements by position and at times the code is **dependent on the position of the element**. Also, it affects the readability of the code as well.

To rescue from the above problems, **collections.namedtuple**() provides a mechanism to **structure** the **elements by name**.

The **collections.namedtuple()** is a factory method that returns a subclass of **tuple** type.

A major **use case** of a **namedtuple** is **decoupling** the code from the position of the element it manipulates. 

One possible use of **namedtuple** is as a **replacement** to **dictionary**, which requires more space to store. However be aware that unlike **dictionary**, **namedtuple is immutable**.



### About Faker Library

**Faker** is a python package to generate fake data.This library provides many kinds of fake data to be generated. Follow the below steps to get started on **Faker library**. Refer [this pydoc link](https://pypi.org/project/Faker/) for more info.

```
!pip install faker

from faker import Faker

fake = Faker()

# get fake name
fake.name()
```



 ### About Assignment

1. Using Faker library create a dataset of 10000 profiles and calculate the following using **nametuples**:
   * Largest_blood_type
   * Mean current-location
   * oldest person age
   * average age
2. Do the above with **dictionary** instead of namedtuple.
3. Create a imaginary stock exchange with 100 companies using fake data. Make sure the following info are populated:
   * name
   * symbol
   * open price
   * high price
   * close price



## Test Results

```
  Check whether the profile uses namedtuples.:  PASSED
  Check the result is in terms of namedtuple:  PASSED
  Examine all the expected fields are in result.:  PASSED
  Examine oldest person age is greater than average age:  PASSED
  Examine mean current location has both lat and lng.:  PASSED
  Examine whether profile uses dictionary.:  PASSED
  Check the result is dictionary.:  PASSED
  Examine the result dictionary has all info.:  PASSED
  Examine oldest person age is greater than average age:  PASSED
  Examine mean current location has both lat and lng.:  PASSED
  Check whether Stock uses namedtuple.  :  PASSED
  Check whether atleast 100 companies are listed in the exchange.  :  PASSED
  Check the stock namedtuple for all fields.  :  PASSED
  Check whether company name is unique.   : PASSED
  Check whether the ticker is unique.  :  PASSED
  Check whether the high price is greater than or equal to the open price.  :  PASSED
  Check whether high price is greater than or equal to close price.  :  PASSED
  Check company's weight for positive value.  :  PASSED
  Check weighted high stock index is >= to open stock index.  :  PASSED
  Check weighted high stock index is >= close stock index  :  PASSED
```


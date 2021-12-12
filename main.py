# Case-study #2
# Developers:   Abrarova V. (55%),
#               Grishaev G. (50%)
import local as lc

# Asking a taxpayer to choose a family status.
name = int(input(lc.SURVEY))
name_month = [lc.JAN, lc.FAB, lc.MAR, lc.APR, lc.MAY, lc.JUN, lc.JUL, lc.AUG, lc.SEP, lc.OCT, lc.NOV, lc.DEC]

# Input of information about revenue for each month.
annual_income = 0
for month in range(12):
  print('{} {}:'.format(lc.QUESTION,name_month[month], end =''))
  income = float(input())
  annual_income += income
print(lc.INCOME, annual_income, '.', sep='')

# Counting tax for a first-seventh level of revenue for one person.
if name == 1:
  if annual_income <= 9075:
    tax = 0.1 * annual_income
  elif annual_income <= 36900:
    tax = 907.6 + 0.15 * (annual_income - 9076)
  elif annual_income <= 89350:
    tax = 5081.35 + 0.25 * (annual_income - 36901)
  elif annual_income <= 186350:
    tax = 18193.85 + 0.28 * (annual_income - 89351)
  elif annual_income <= 405100:
    tax = 45353.85 + 0.33 * (annual_income - 186351)
  elif annual_income <= 406750:
    tax = 117541.35 + 0.35 * (annual_income - 405101)
  else:
    tax = 118118.85 + 0.396 * (annual_income - 406751)

# Counting tax for a first-seventh level of revenue for a married couple.
if name == 2:
  if annual_income <= 18150:
    tax = 0.1 * annual_income
  elif annual_income <= 73800:
    tax = 1815.1 + 0.15 * (annual_income - 18151)
  elif annual_income <= 148850:
    tax = 10162.6 + 0.25 * (annual_income - 73801)
  elif annual_income <= 226850:
    tax = 28925.1 + 0.28 * (annual_income - 148851)
  elif annual_income <= 405100 :
    tax = 50765.1 + 0.33 * (annual_income - 226851)
  elif annual_income <= 457600:
    tax = 109587.6 + 0.35 * (annual_income - 405101)
  else:
    tax = 127962.6 + 0.396 * (annual_income - 457601)

# Counting tax for a first-seventh level of revenue for a single parent.
if name == 3:
  if annual_income <= 12950:
    tax = 0.1* (annual_income)
  elif annual_income <= 49400:
    tax = 1295.1 + 0.15 * (annual_income - 12951)
  elif annual_income <= 127550:
    tax = 6762.6 + 0.25 * (annual_income - 12951)
  elif annual_income <= 206600:
    tax = 26300.1 + 0.28 * (annual_income - 127551)
  elif annual_income <= 405100:
    tax = 48434.1 + 0.33 * (annual_income - 206601)
  elif annual_income <= 432200:
    tax = 113939.1 + 0.35 * (annual_income - 405101)
  else:
    tax = 123424.1 + 0.396 * (annual_income - 432201)

# Output of full amount of taxes taxpayer has to pay.
print(lc.RESULT,'%.2f' % tax, '.',sep='')


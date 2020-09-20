import itertools

card_value = [1350,1500,1000,1000,800,400,250,800,550,300,250]

card_value_2 = [0,0,0,0,0,0,0,0,0,600,400]

setcard_one = 4000
setcard_two = 2600
setcard_three = 2400

fixed_card = [850]

one_box = 3950

three_values = list()
four_values = list()
three_four_values = list()

for s in itertools.combinations(card_value,3):
    three_value = sum(s)
    three_values.append(three_value)

for t in itertools.combinations(card_value_2,4):
    four_value = sum(t)
    four_values.append(four_value)

for d in itertools.product(three_values, four_values,fixed_card):
    four_three_value = sum(d)
    three_four_values.append(four_three_value)

three_profitable = len([0 for x in three_four_values if x>one_box])



setcard_one_values = list()
setcard_one_lastvalues = list()
for s in itertools.combinations(card_value,2):
    setcard_one_value = sum(s) + setcard_one
    setcard_one_values.append(setcard_one_value)
for d in itertools.product(setcard_one_values, four_values,fixed_card):
    setcard_one_last = sum(d)
    setcard_one_lastvalues.append(setcard_one_last)
setcard_one_profitable = len([0 for x in setcard_one_lastvalues if x>one_box])

setcard_two_values = list()
setcard_two_lastvalues = list()
for s in itertools.combinations(card_value,2):
    setcard_two_value = sum(s) + setcard_two
    setcard_two_values.append(setcard_two_value)
for d in itertools.product(setcard_two_values, four_values,fixed_card):
    setcard_two_last = sum(d)
    setcard_two_lastvalues.append(setcard_two_last)
setcard_two_profitable = len([0 for x in setcard_two_lastvalues if x>one_box])

setcard_three_values = list()
setcard_three_lastvalues = list()
for s in itertools.combinations(card_value,2):
    setcard_three_value = sum(s) + setcard_three
    setcard_three_values.append(setcard_three_value)
for d in itertools.product(setcard_three_values, four_values,fixed_card):
    setcard_three_last = sum(d)
    setcard_three_lastvalues.append(setcard_three_last)
setcard_three_profitable = len([0 for x in setcard_three_lastvalues if x>one_box])

print(((three_profitable)*9 + setcard_one_profitable + setcard_two_profitable + setcard_three_profitable)/(len(three_four_values)*9+len(setcard_one_lastvalues)+len(setcard_two_lastvalues)+len(setcard_three_lastvalues))*100,"%")

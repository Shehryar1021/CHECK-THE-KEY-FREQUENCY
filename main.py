test_dict = {'Codingal' : 2, 'is' : 2,'best' : 2,'for' : 2,'CODING' : 1}
print("THE ORIGINAL DICTIONARY :" + str(test_dict))
K = 2
res=0
for key in test_dict:
    if test_dict[key] ==K:
        res = res + 1
        print("FREQUENCY OF KEY IS :" + str(res))
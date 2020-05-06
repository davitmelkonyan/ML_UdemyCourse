my_dict = {'key1':'value1','key2':'value2'}
print (my_dict['key2'])
my_dict = {'key1':12,'key2':[12,123,23],'key3':['it1','it2']}
print (my_dict['key3'])
print (my_dict['key3'][0])
print (my_dict['key3'][0].upper())
my_dict['key1'] = my_dict['key1']-12
print (my_dict['key1'])

d = {}
d['animal']= 'dog'
d['number']= 1
print (d)
d = {'key1':{'nestkey':{'subnestkey':'value'}}}
print (d['key1']['nestkey']['subnestkey'])
print (d.keys())
print (d['key1'].keys())
print (d.values())
print (d['key1'].values())
print (d.items())
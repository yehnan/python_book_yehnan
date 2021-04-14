

friends = [
    {'first':'Amy', 'last':'Wallace', 'email':'plunk@service.com.ru'},
    {'first':'John', 'last':'Dickson', 'email':'john@edu.com.tw'}, 
    {'first':'Amy', 'last':'Obama', 'email':'amy@whitehouse.gov'}, 
    {'first':'Bob', 'last':'Banks', 'email':'bob@service.com.ru'},
    {'first':'Amy', 'last':'Southward', 'email':'amys@service.com.ru'},
    {'first':'Bob', 'last':'Wilkson', 'email':'bobwilkson@service.com.ru'}]

def key_func(x):
    return x['first'] + ' ' + x['last']
friends_sorted = sorted(friends, key=key_func)

print(friends_sorted)


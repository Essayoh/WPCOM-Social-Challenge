from urllib2 import urlopen
from json import load
import json

url = "http://databits.io/static_content/challenges/wordpress-dot-com-social-reciprocity-challenge/wordpress_com_userdata.json"
json_obj = urlopen(url)
data = load(json_obj)

user_list = []

for i in data:
	i = json.dumps(i['user_id'], indent = 2, separators=(',',': '))
	user_list.append(i)

# input_user = input('What User ID? ')
# input_user = str(input_user)

# if input_user in user_list:
# 	print "Yes"
# else: 
# 	print "No"

for i in data:
	i = json.dumps(i['user_blogs'], indent = 2, separators=(',',': '))
	print i 

# what about a dictionary of blog_id : user_id ? since users have many blogs but blogs
# have only one user - could then query dictionary for blogs / user, etc
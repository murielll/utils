import re
'''
Parse haproxy.cfg and print in format "ip port listen-title"
'''

f = open('haproxy.cfg')
for line in f:
	if 'listen ' in line:
		title = re.findall("listen (.+)", line)[0]
	if 'bind ' in line:
		if re.search("bind :", line):
	  		continue
		ip = re.findall("\d+.\d+.\d+.\d+", line)[0]
	  	if ip.startswith("10.50"):
	    		continue
	  	port = re.findall(":(\d+)", line)[0]
	  	print(ip, port, title, sep="\t")
f.close()

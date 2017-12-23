'''
Authon: MrYanc
Version: 3.5
Date: 11/20/2017
'''
import time
import random
import urllib
import sys
from bs4 import BeautifulSoup
from queue import Queue
from threading import Thread
from threading import Lock

'''
download proxy list from proxy website: 
input: none
output: proxy server address list
exception: connection abortion
'''
def proxyList():
	# proxy website url
	proxy_url = "https://www.us-proxy.org/";

	try:
		request = urllib.request.Request(proxy_url, headers=header);
	except Exception as e:
		raise e;
	else:
		page = urllib.request.urlopen(request).read();
		soup = BeautifulSoup(page, "lxml");
		table = soup.find("tbody");
		proxy = table.find_all("tr");
		# list all the proxy
		ips = [];
		for idx in range(1,len(proxy)):
			ip = proxy[idx];
			tds = ip.findAll("td");
			temp = "http://"+tds[0].contents[0]+":"+tds[1].contents[0];
			ips.append(temp);
		return ips;	

'''
vist the ebay item url with proxy
input: url: string, proxy: string
output: none
exception: connection abortion
'''
def view(url, queue):
	# random select sleep time
	sleep_time = random.randint(5, 10);
	# time sleep between each request
	request = urllib.request.Request(url, headers=header);
	proxy = queue.get();
	try:
		request.set_proxy(proxy, 'http');
		page = urllib.request.urlopen(url).read();
		print("Success view item with proxy {}".format(proxy));
	except Exception as e:
		print("Failed view item with proxy {}".format(proxy));
		print(e);
	else:
		pass

'''
get item list
input: file source
output: list
exception: file not found exception
'''
def getItemList(filename):
	# ebay item url
	item_urls = [];
	with open(filename) as f:
		lines = f.readlines();
		for line in lines:
			item_urls.append(line);
	return item_urls;

def main(item):
	print("Start adding views to item: {}.".format(item));

	# get proxy list
	ips = proxyList();
	print("Get proxy list, length is {}.".format(len(ips)));

	# initiate working thread pool
	queue = Queue();
	
	for i in range(1, len(ips)):
		t = Thread(target=view, args=(item, queue));
		t.start();

	# vist the ebay item with different proxy
	for proxy in ips:
		queue.put(proxy);

if __name__ == "__main__":
	# browser header
	USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36";
	header = {};
	header['User-Agent'] = USER_AGENT;

	directory = sys.argv[1];
	# ebay item url
	item_urls = getItemList(directory);

	# vist the ebay items
	for item in item_urls:
		main(item);
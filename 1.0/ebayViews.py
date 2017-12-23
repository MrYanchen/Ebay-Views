'''
Authon: MrYanc
Version: 3.5
Date: 10/20/2017
'''
import urllib
from bs4 import BeautifulSoup
import time
import os
import sys

'''
scrape proxy from proxy website
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
get item list
input: file source
output: list
exception: file not found exception
'''
def getItemList(file):
	# read txt file

	# ebay item url
	item_urls = [];

	return item_urls;

def main():
	ips = proxyList();
	print(len(ips));

	item_urls = getItemList();

	# vist the ebay item with different proxy
	for item_url in item_urls:
		print("View item: " + item_url);
		request = urllib.request.Request(item_url, headers=header);
		for proxy in ips:
			try:
				request.set_proxy(proxy, 'http');
				page = urllib.request.urlopen(item_url).read();
				print("Success: "+proxy);
			except Exception as e:
				print("Unsuccess: "+proxy);
				print(e);
	pass

if __name__ == "__main__":
	# browser header
	USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36";
	header = {};
	header['User-Agent'] = USER_AGENT;
	
	main();
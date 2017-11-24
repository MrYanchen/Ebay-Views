'''
Authon: MrYanc
Version: 3.5
Date: 11/20/2017
'''
import urllib
from bs4 import BeautifulSoup
import time
import threading

class View(threading.Thread):
	"""docstring for View"""
	def __init__(self, arg):
		super(View, self).__init__()
		self.arg = arg

	def run(self, url, proxy):
		view(url, proxy);
		pass

	'''
	vist the ebay item url with proxy
	input: url: string, proxy: string
	output: none
	exception: connection abortion
	'''
	def view(self, url, proxy):
		# random select sleep time
		sleep_time = random.randint(5, 10);
		# time sleep between each request
		request = urllib.request.Request(url, headers=header);

		try:
			request.set_proxy(proxy, 'http');
			page = urllib.request.urlopen(item_url).read();
			print("Success view item with proxy {}".format(proxy));
		except Exception as e:
			print("Failed view item with proxy {}".format(proxy));
			print(e);
		else:
			pass


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

def main():
	ips = proxyList();
	print("Get proxy list, length is {}.".format(len(ips)));

	# ebay item url
	item_urls = ["https://www.ebay.com/i/132346024745"]; #"https://www.ebay.com/i/132353217389"

	# vist the ebay item with different proxy
	for item_url in item_urls:
		print("Add views to item: {}.".format(item_url));
		
		for proxy in ips:
			try:
				
			except Exception as e:
				print("Error: unable to start thread");
				print(e)
			
	pass

if __name__ == "__main__":
	# browser header
	USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36";
	header = {};
	header['User-Agent'] = USER_AGENT;

	# thread control
	sema = threading.Semaphore(5);
	
	main();
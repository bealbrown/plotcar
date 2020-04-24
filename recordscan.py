# Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] on win32
# Type "help", "copyright", "credits" or "license()" for more information.


import py2700 as DMM
import time
from datetime import datetime
import sqlite3
import itertools
import pandas as pd


import database as rdb


def main():

	# my_multimeter = DMM.Multimeter('TCPIP::101.1.160.21::1394::SOCKET')
	# my_multimeter.set_temperature_units('C')
	# my_multimeter.set_timeout(100000)
	# my_multimeter.define_channels([101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140],
	# 			      DMM.MeasurementType.resistance())
	# my_multimeter.setup_scan()
	# 

	x = 0

	while (True):

		record = ['+9.9E37', '+0.000000SECS', '+00000RDNG#', '+9.9E37', '+0.350996SECS', '+00001RDNG#', '+9.9E37', '+0.701999SECS', '+00002RDNG#', '+9.9E37', '+1.052993SECS', '+00003RDNG#', '+9.9E37', '+1.403995SECS', '+00004RDNG#', '+9.9E37', '+1.794681SECS', '+00005RDNG#', '+9.9E37', '+2.145997SECS', '+00006RDNG#', '+9.9E37', '+2.496997SECS', '+00007RDNG#', '+9.9E37', '+2.887711SECS', '+00008RDNG#', '+9.9E37', '+3.238994SECS', '+00009RDNG#', '+9.9E37', '+3.589994SECS', '+00010RDNG#', '+9.9E37', '+3.980724SECS', '+00011RDNG#', '+9.9E37', '+4.331998SECS', '+00012RDNG#', '+9.9E37', '+4.682999SECS', '+00013RDNG#', '+9.9E37', '+5.073714SECS', '+00014RDNG#', '+9.9E37', '+5.424998SECS', '+00015RDNG#', '+9.9E37', '+5.775997SECS', '+00016RDNG#', '+9.9E37', '+6.166696SECS', '+00017RDNG#', '+9.9E37', '+6.518001SECS', '+00018RDNG#', '+9.9E37', '+6.868998SECS', '+00019RDNG#', '+9.9E37', '+7.259724SECS', '+00020RDNG#', '+9.9E37', '+7.610998SECS', '+00021RDNG#', '+9.9E37', '+7.961995SECS', '+00022RDNG#', '+9.9E37', '+8.352679SECS', '+00023RDNG#', '+9.9E37', '+8.703996SECS', '+00024RDNG#', '+9.9E37', '+9.054997SECS', '+00025RDNG#', '+9.9E37', '+9.445712SECS', '+00026RDNG#', '+9.9E37', '+9.797001SECS', '+00027RDNG#', '+9.9E37', '+10.147997SECS', '+00028RDNG#', '+9.9E37', '+10.538707SECS', '+00029RDNG#', '+9.9E37', '+10.889997SECS', '+00030RDNG#', '+9.9E37', '+11.240998SECS', '+00031RDNG#', '+9.9E37', '+11.631683SECS', '+00032RDNG#', '+9.9E37', '+11.982995SECS', '+00033RDNG#', '+9.9E37', '+12.333996SECS', '+00034RDNG#', '+9.9E37', '+12.724706SECS', '+00035RDNG#', '+9.9E37', '+13.075994SECS', '+00036RDNG#', '+9.9E37', '+13.427001SECS', '+00037RDNG#', '+9.9E37', '+13.817714SECS', '+00038RDNG#', '+9.9E37', '+14.168994SECS', '+00039RDNG#'];
		time.sleep(.5)

		# result = my_multimeter.scan(time.time_ns()/(10**9))

		x += 1

		print("saving scan")
		send_to_db(record)

def send_to_db(record):

	def fil(el):
		if ("SECS" not in el and "RDNG" not in el):
			# el = el.translate(None, '+')
			return True
		else:
			return False
	def format(el):
		return float(el.replace("+",""))

	formatted_record = (list(map(format, filter(fil, record))))
	rdb.store_record(formatted_record)


if __name__ == '__main__':
	main();

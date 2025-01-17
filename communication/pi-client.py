import os
import time
import socket
from datetime import datetime

if __name__ == "__main__":	
	exit_client = False
	it_counter = 0
	limit = 60
	skip = 0
	while exit_client == False:	
		file_name = "testsound.wav"
		latency_name = "non_lat_1b.txt"
		ip_address = "10.11.182.104"
	
		sound_file = open(file_name, "rb")
		latency_file = open(latency_name, "a+")
		sound_data = sound_file.read()
		
		done = False
		while done == False:
			try:
				skip = 0
				time.sleep(1) # Simulate 10 seconds of data collection
				client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				print("Connecting to server")
				start = datetime.now().timestamp()
				# Fog
				#client.connect(("10.16.9.113", 32500))
				# Server
				client.connect(("10.11.232.95", 32500))
				
				while sound_data:
					data = sound_data[:2048]
					if not data:
						break
					try:
						sent = client.send(data)
						sound_data = sound_data[sent:]
					except Exception as e:
						print(e)
						skip = 1
						time.sleep(2)
						break
				if skip == 0:
					end = datetime.now().timestamp()
					latency_file.write("Start {} {}\n".format(ip_address, start))
					latency_file.write("End {} {}\n".format(ip_address, end))
					done = True
				time.sleep(2)
			except Exception as e:
				print(e)
				time.sleep(2)
				client.close()
				done = False
		
		it_counter+=1
		print(it_counter)
		if it_counter >= limit:
			exit_client = True
				


	

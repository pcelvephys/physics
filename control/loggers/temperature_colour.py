#!/usr/bin/python
from sense_hat import SenseHat
from time import sleep, strftime, time
import irc


sleep(20)

sense = SenseHat()
sense.clear()

temp_logfile_name = "templog.txt"
temp_logfile_directory = "/home/pi/"

insta_logfile = "insta_temp.txt"
insta_log_directory = "/home/pi/"
#html_pre = "<html><body><h2>Current conditions: "
#html_post = "</h2></body></html>"


irclog = irc.irc('environment', 'environment', 'Lab environmental conditions')
irclog.login()
irclog.join('#logging')


def clamp(n, minn, maxn):
	if n < minn:
		return minn
	elif n > maxn:
		return maxn
	else:
		return n

def get_mag():
	magmin = 0.0
	magrange = 400.0
	magmax = magmin + magrange
	
	magdict = sense.get_compass_raw()
	mag = abs(magdict['x'])
	#print("mag: %f" % mag)

	mag_scale = clamp(    int((mag - magmin) * (8.0/magrange)), 1, 8)
	#print("mag_scale: %i" % mag_scale)

	mag_colour = clamp(int((mag - magmin)*(255.0/magrange)), 0, 254)
	#print("mag_colour: %i" % mag_colour)

	return (mag, mag_scale, mag_colour)
	

def get_humid():
	hmax = 45.0
	hrange = 20.0
	hmin = hmax - hrange
	
	humid = sense.get_humidity()
	#print("humid: %f" % humid)
	
	humid_scale = clamp(    int((humid - hmin) * (8.0/hrange)), 1, 8)
	#print("humid_scale: %i" % humid_scale)
	
	humid_colour = clamp(int((humid - hmin)*(255.0/hrange)), 0, 254) 
	#print("humid_colour: %i" % humid_colour)
	
	return (humid, humid_scale, humid_colour)

def get_pres():
	presmax = 1025.0
	presrange = 25.0
	presmin = presmax - presrange
	
	pres = sense.get_pressure()
	#print("pres: %f" % pres)

	pres_scale = clamp(  int( (pres - presmin)*(8.0/presrange)  ), 1, 8)
	#print("pres_scale: %i" % pres_scale)

	pres_colour = clamp(int((pres - presmin)*(255.0/presrange)), 0, 254)
	#print("pres_colour: %i" % pres_colour)

	return (pres, pres_scale, pres_colour)

def get_temp():
	tmax = 34.0
	trange = 9.0
	tmin = tmax - trange

	temp = sense.get_temperature()
	#print("temp: %f" % temp)

	temp_scale = clamp(   int(  (temp - tmin) * (8.0/trange) ) , 1, 8)
	#print("temp_scale: %i" % temp_scale)

	temp_colour = clamp(   int(   (temp - tmin) * (255.0/trange)), 0, 254)
	#print("temp_colour: %f" % temp_colour)

	return (temp, temp_scale, temp_colour)

def mag_bar(mag, mag_scale, mag_colour):
	sense.set_rotation(180)

	for x in range(6,8):
		for y in range(0,mag_scale):
			sense.set_pixel(x, y, mag_colour, mag_colour, mag_colour)

		for y in range(mag_scale,8):
			sense.set_pixel(x,y,0,0,0)

def temperature_bar(temp, temp_scale, temp_colour):
	sense.set_rotation(180)
	
	for x in range(0,2):
		for y in range(0,temp_scale):
			sense.set_pixel(x, y, temp_colour, 0, 0)

		for y in range(temp_scale,8):
			sense.set_pixel(x,y,0,0,0)

def pres_bar(pres, pres_scale, pres_colour):
	sense.set_rotation(180)
	for x in range(2,4):
		for y in range(0,pres_scale):
			sense.set_pixel(x, y, 0, pres_colour, 0)
		for y in range(pres_scale,8):
			sense.set_pixel(x,y,0,0,0)

def humid_bar(humid, humid_scale, humid_colour):
	sense.set_rotation(180)
	for x in range(4,6):
		for y in range(0,humid_scale):
			sense.set_pixel(x, y, 0, 0, humid_colour) 
		for y in range(humid_scale,8):
			sense.set_pixel(x,y,0,0,0)

def flash(lumin, delay):
	for x in range(0,8):
		for y in range(0,8):
			sense.set_pixel(x,y,lumin,lumin,lumin)
	sleep(delay)

def log(string_to_log, logfile_name, logfile_directory):
	with open(logfile_directory+logfile_name, 'a') as myfile:
		myfile.write(string_to_log)	

def insta_write(temp, pres, humid, insta_logfile, insta_log_directory):
	with open(insta_log_directory+insta_logfile, 'w') as instafile:
		write_line = "%.01f %.01f %.01f" % (temp, pres, humid)
		instafile.write(write_line)

def scroll_time():
	sense.set_rotation(0)
	sense.show_message(strftime("%H:%M"), scroll_speed = 0.05, text_colour = [255,255,255])

def scroll_temp(temp, temp_colour):
	sense.set_rotation(0)
	sense.show_message("%.01f" % temp, scroll_speed = 0.05, text_colour = [temp_colour, 0, 0])	

def scroll_humid(humid, humid_colour):
	sense.set_rotation(0)
	sense.show_message("%.01f" % humid, scroll_speed = 0.05, text_colour = [0, 0, humid_colour])

def scroll_pres(pres, pres_colour):
	sense.set_rotation(0)
	sense.show_message("%.01f" % pres, scroll_speed = 0.05, text_colour = [0, pres_colour, 0])

def scroll(humids, preses, temps):
	scroll_time()
	scroll_humid(humids[0], humids[2])
	scroll_pres(preses[0], preses[2])
	scroll_temp(temps[0], temps[2])

def main():
	while True:
		start_time = time()
		current_minutes = strftime("%M")
		current_seconds = strftime("%S")
		temps = get_temp()
		humids = get_humid()
		preses = get_pres()
		mags = get_mag()
		scrolled = False
		logged = False
		if mags[1] > 4:
			for i in range(20):
				flash(255,0.01)
				flash(0,0.01)
			scroll(humids, preses, temps)
		if current_minutes == "00":
			scroll(humids, preses, temps)
			sleep(60)
		if current_seconds == "00":
			log(str(temps[0])+"\t"+str(temps[1])+"\t"+strftime("%y-%m-%d_%H:%M")+"\t"+str(humids[0])+"\t"+str(preses[0])+"\n", temp_logfile_name, temp_logfile_directory)
			insta_write(temps[0], preses[0], humids[0], insta_logfile, insta_log_directory)
			message = 'Temperature: %.01f deg C\tHumidity: %.01f percent\tAir pressure: %.01f mBar\n' % (temps[0], humids[0], preses[0])
			irclog.privmsg('#logging', message)
			sleep(1)
		temperature_bar(temps[0], temps[1], temps[2])
		humid_bar(humids[0], humids[1], humids[2])
		pres_bar(preses[0], preses[1], preses[2])
		mag_bar(mags[0], mags[1], mags[2])
main()

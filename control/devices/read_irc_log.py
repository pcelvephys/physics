import time
import Tkinter as tkinter
from datetime import datetime

def follow(logfile):
	timeout_count = 0
	logfile.seek(0,2)
	while timeout_count < 3000:
		line = logfile.readline()
		if not line:
			time.sleep(0.1)
			timeout_count += 1
			#print timeout_count
			continue
		if line:
			timeout_count = 0
		yield line
	print("break")
	yield None
	return


window = tkinter.Tk()
window.title("Optomech status")
window.attributes("-fullscreen", True)
#window.geometry("500x300")
#window.overrideredirect(True)
#window.geometry("{0}x{1}+0+0".format(window.winfo_screenwidth(), window.winfo_screenheight()))


var_env_T = tkinter.StringVar()
var_env_H = tkinter.StringVar()
var_env_P = tkinter.StringVar()
var_env_time = tkinter.StringVar()
vars_env = [var_env_T, var_env_H, var_env_P, var_env_time]

var_edw_T = tkinter.StringVar()
var_edw_V = tkinter.StringVar()
var_edw_I = tkinter.StringVar()
var_edw_P = tkinter.StringVar()
var_edw_time = tkinter.StringVar()
vars_edw = [var_edw_T, var_edw_V, var_edw_I, var_edw_P, var_edw_time]

var_vc_P = tkinter.StringVar()
var_vc_time = tkinter.StringVar()
vars_vc = [var_vc_P, var_vc_time]

var_thorlabs_P = tkinter.StringVar()
var_thorlabs_time = tkinter.StringVar()
vars_thorlabs = [var_thorlabs_P, var_thorlabs_time]

var_edfa_alarm = tkinter.StringVar()
var_edfa_mode = tkinter.StringVar()
var_edfa_P_in = tkinter.StringVar()
var_edfa_P_out = tkinter.StringVar()
var_edfa_P_aim = tkinter.StringVar()
var_edfa_T_int = tkinter.StringVar()
var_edfa_V_in = tkinter.StringVar()
var_edfa_I_pre = tkinter.StringVar()
var_edfa_I_amp = tkinter.StringVar()
var_edfa_I_aim_pre = tkinter.StringVar()
var_edfa_I_aim_amp = tkinter.StringVar()
var_edfa_time = tkinter.StringVar()
vars_edfa = [var_edfa_alarm, var_edfa_mode, var_edfa_P_in, var_edfa_P_out, var_edfa_P_aim, var_edfa_T_int, var_edfa_V_in, var_edfa_I_pre, var_edfa_I_amp, var_edfa_I_aim_pre, var_edfa_I_aim_amp, var_edfa_time]

var_current_date = tkinter.StringVar()
var_current_time = tkinter.StringVar()

################# ENVIRONMENT #####################################################

label_env_title = tkinter.LabelFrame(window, text="Environment", font=("Helvetica", 26))# wraplength = 250)
label_env_title.grid(column = 0, row = 0, padx = 10, pady = 10, sticky="news")

label_env_title_T = tkinter.Label(label_env_title, text="Temperature [C]", wraplength = 250, font=("Helvetica", 22))
label_env_title_H = tkinter.Label(label_env_title, text="Humidity [%]", wraplength = 250, font=("Helvetica", 22))
label_env_title_P = tkinter.Label(label_env_title, text="Air pressure [mBar]", wraplength = 250, font=("Helvetica", 22))
label_env_title_time = tkinter.Label(label_env_title, text="Time", wraplength = 250, font=("Helvetica", 22))
label_env_title_T.grid(column = 0, row = 1, padx = 10, pady = 10)
label_env_title_H.grid(column = 0, row = 2, padx = 10, pady = 10)
label_env_title_P.grid(column = 0, row = 3, padx = 10, pady = 10)
label_env_title_time.grid(column = 0, row = 5, padx = 10, pady = 10)

label_env_T = tkinter.Label(label_env_title, textvariable = var_env_T, font=("Helvetica", 22), wraplength = 210)
label_env_H = tkinter.Label(label_env_title, textvariable = var_env_H, font=("Helvetica", 22), wraplength = 210)
label_env_P = tkinter.Label(label_env_title, textvariable = var_env_P, font=("Helvetica", 22), wraplength = 210)
label_env_time = tkinter.Label(label_env_title, textvariable = var_env_time, font=("Helvetica", 22), wraplength = 210)
labels_env = [label_env_T, label_env_H, label_env_P]
for n in range(len(labels_env)):
	labels_env[n].grid(column = 1, row = n+1, padx = 10, pady = 10)
label_env_time.grid(column = 1, row = 5, padx = 10, pady = 10)


############### EDWARDS ############################################################
label_edw_title = tkinter.LabelFrame(window, text="Scroll pump", font=("Helvetica", 26))#, wraplength = 250
label_edw_title.grid(column = 1, row = 0, padx = 10, pady = 10, sticky="news")

label_edw_title_T = tkinter.Label(label_edw_title, text="Temperature [C]", wraplength = 250, font=("Helvetica", 22))
label_edw_title_V = tkinter.Label(label_edw_title, text="Voltage [V]", wraplength = 250,  font=("Helvetica", 22))
label_edw_title_I = tkinter.Label(label_edw_title, text="Current [A]", wraplength = 250, font=("Helvetica", 22))
label_edw_title_P = tkinter.Label(label_edw_title, text="Power [W]", wraplength = 250, font=("Helvetica", 22))
label_edw_title_time = tkinter.Label(label_edw_title, text="Time", wraplength = 250, font=("Helvetica", 22))

label_edw_title_T.grid(column = 2, row = 1, padx = 10, pady = 10)
label_edw_title_V.grid(column = 2, row = 2, padx = 10, pady = 10)
label_edw_title_I.grid(column = 2, row = 3, padx = 10, pady = 10)
label_edw_title_P.grid(column = 2, row = 4, padx = 10, pady = 10)
label_edw_title_time.grid(column = 2, row = 5, padx = 10, pady = 10)

label_edw_T = tkinter.Label(label_edw_title, textvariable = var_edw_T, font=("Helvetica", 22), wraplength = 210)
label_edw_V = tkinter.Label(label_edw_title, textvariable = var_edw_V, font=("Helvetica", 22), wraplength = 210)
label_edw_I = tkinter.Label(label_edw_title, textvariable = var_edw_I, font=("Helvetica", 22), wraplength = 210)
label_edw_P = tkinter.Label(label_edw_title, textvariable = var_edw_P, font=("Helvetica", 22), wraplength = 210)
label_edw_time = tkinter.Label(label_edw_title, textvariable = var_edw_time, font=("Helvetica", 22), wraplength = 210)
labels_edw = [label_edw_T, label_edw_V, label_edw_I, label_edw_P, label_edw_time]
for n in range(len(labels_edw)):
	labels_edw[n].grid(column = 3, row = n+1, padx = 10, pady = 10)

################# VACUUM PRESSURE ###################################################

label_vc_title = tkinter.LabelFrame(window, text="Vacuum", font=("Helvetica", 26))#, wraplength = 250
label_vc_title.grid(column = 1, row = 1, padx = 10, pady = 10, sticky="news")

label_vc_title_P = tkinter.Label(label_vc_title, text="Chamber pressure [mBar]", wraplength = 250, font=("Helvetica", 22))
label_vc_title_time = tkinter.Label(label_vc_title, text="Time", wraplength = 250, font=("Helvetica", 22))

label_vc_title_P.grid(column = 2, row = 7, padx = 10, pady = 10)
label_vc_title_time.grid(column = 2, row = 8, padx = 10, pady = 10)

label_vc_P = tkinter.Label(label_vc_title, textvariable = var_vc_P, font=("Helvetica", 22), wraplength = 210)
label_vc_time = tkinter.Label(label_vc_title, textvariable = var_vc_time, font=("Helvetica", 22), wraplength = 210)
labels_vc = [label_vc_P, label_vc_time]
for n in range(len(labels_vc)):
	labels_vc[n].grid(column = 3, row = n+7, padx = 10, pady = 10)


################# THORLABS #########################################################

label_thorlabs_title = tkinter.LabelFrame(window, text="Thorlabs", font=("Helvetica", 26))#wraplength = 250,
label_thorlabs_title.grid(column = 0, row = 1, padx = 10, pady = 10, sticky="news")

label_thorlabs_title_P = tkinter.Label(label_thorlabs_title, text="Power", wraplength = 250, font=("Helvetica", 22))
label_thorlabs_title_time = tkinter.Label(label_thorlabs_title, text="Time", wraplength = 250, font=("Helvetica", 22))

label_thorlabs_title_P.grid(column = 0, row = 7, padx = 10, pady = 10)
label_thorlabs_title_time.grid(column = 0, row = 8, padx = 10, pady = 10)

label_thorlabs_P = tkinter.Label(label_thorlabs_title, textvariable = var_thorlabs_P, font=("Helvetica", 22), wraplength = 210)
label_thorlabs_time = tkinter.Label(label_thorlabs_title, textvariable = var_thorlabs_time, font=("Helvetica", 22), wraplength = 210)
labels_thorlabs = [label_thorlabs_P, label_thorlabs_time]
for n in range(len(labels_thorlabs)):
	labels_thorlabs[n].grid(column = 1, row = n+7, padx = 10, pady = 10)


################## EDFA ############################################################

label_edfa_title = tkinter.LabelFrame(window, text="EDFA", font=("Helvetica", 26))#wraplength = 250
label_edfa_title.grid(column = 2, row = 0, padx = 10, pady = 10, sticky="news")

label_edfa_title_alarm = tkinter.Label(label_edfa_title, text="Alarms", wraplength = 250, font=("Helvetica", 22))
label_edfa_title_mode = tkinter.Label(label_edfa_title, text="Mode", wraplength = 250, font=("Helvetica", 22))
label_edfa_title_P_in = tkinter.Label(label_edfa_title, text="P in [mW]", wraplength = 250, font=("Helvetica", 22))
label_edfa_title_P_out = tkinter.Label(label_edfa_title, text="P out [mW]", wraplength = 250, font=("Helvetica", 22))
label_edfa_title_P_aim = tkinter.Label(label_edfa_title, text="P set [mW]", wraplength = 250, font=("Helvetica", 22))
label_edfa_title_T_int = tkinter.Label(label_edfa_title, text="Internal temperature [C]", wraplength = 250, font=("Helvetica", 22))
label_edfa_title_V_in = tkinter.Label(label_edfa_title, text="Supply voltage [V]", wraplength = 250, font=("Helvetica", 22))
label_edfa_title_I_pre = tkinter.Label(label_edfa_title, text="Current p/amp [mA]", wraplength = 250, font=("Helvetica", 22))
label_edfa_title_I_amp = tkinter.Label(label_edfa_title, text="Current amp [mA]", wraplength = 250, font=("Helvetica", 22))
label_edfa_title_I_aim_pre = tkinter.Label(label_edfa_title, text="Current setpoint p/amp [mA]", wraplength = 250, font=("Helvetica", 22))
label_edfa_title_I_aim_amp = tkinter.Label(label_edfa_title, text="Current setpoint amp [mA]", wraplength = 250, font=("Helvetica", 22))
label_edfa_title_time = tkinter.Label(label_edfa_title, text="Time", wraplength = 250, font=("Helvetica", 22))
label_edfa_titles = [label_edfa_title_alarm, label_edfa_title_mode, label_edfa_title_P_in, label_edfa_title_P_out, label_edfa_title_P_aim, label_edfa_title_T_int, label_edfa_title_V_in, label_edfa_title_I_pre, label_edfa_title_I_amp, label_edfa_title_I_aim_pre, label_edfa_title_I_aim_amp, label_edfa_title_time]

for n in range(6):
	label_edfa_titles[n].grid(column = 4, row = n, padx = 10, pady = 10)
for n in range(6,len(label_edfa_titles)):
	label_edfa_titles[n].grid(column = 6, row = n-6, padx = 10, pady = 10)


label_edfa_alarm = tkinter.Label(label_edfa_title, textvariable = var_edfa_alarm, font=("Helvetica", 22), wraplength = 210)
label_edfa_mode = tkinter.Label(label_edfa_title, textvariable = var_edfa_mode, font=("Helvetica", 22), wraplength = 210)
label_edfa_P_in = tkinter.Label(label_edfa_title, textvariable = var_edfa_P_in, font=("Helvetica", 22), wraplength = 210)
label_edfa_P_out = tkinter.Label(label_edfa_title, textvariable = var_edfa_P_out, font=("Helvetica", 22), wraplength = 210)
label_edfa_P_aim = tkinter.Label(label_edfa_title, textvariable = var_edfa_P_aim, font=("Helvetica", 22), wraplength = 210)
label_edfa_T_int = tkinter.Label(label_edfa_title, textvariable = var_edfa_T_int, font=("Helvetica", 22), wraplength = 210)
label_edfa_V_in = tkinter.Label(label_edfa_title, textvariable = var_edfa_V_in, font=("Helvetica", 22), wraplength = 210)
label_edfa_I_pre = tkinter.Label(label_edfa_title, textvariable = var_edfa_I_pre, font=("Helvetica", 22), wraplength = 210)
label_edfa_I_amp = tkinter.Label(label_edfa_title, textvariable = var_edfa_I_amp, font=("Helvetica", 22), wraplength = 210)
label_edfa_I_aim_pre = tkinter.Label(label_edfa_title, textvariable = var_edfa_I_aim_pre, font=("Helvetica", 22), wraplength = 210)
label_edfa_I_aim_amp = tkinter.Label(label_edfa_title, textvariable = var_edfa_I_aim_amp, font=("Helvetica", 22), wraplength = 210)
label_edfa_time = tkinter.Label(label_edfa_title, textvariable = var_edfa_time, font=("Helvetica", 22), wraplength = 210)
labels_edfa = [label_edfa_alarm, label_edfa_mode, label_edfa_P_in, label_edfa_P_out, label_edfa_P_aim, label_edfa_T_int, label_edfa_V_in, label_edfa_I_pre, label_edfa_I_amp, label_edfa_I_aim_pre, label_edfa_I_aim_amp, label_edfa_time]

for n in range(6):
	labels_edfa[n].grid(column = 5, row = n, padx = 10, pady = 10)
for n in range(6, len(labels_edfa)):
	labels_edfa[n].grid(column = 7, row = n-6, padx = 10, pady = 10)

#################### CURRENT TIME ##################################################

label_current_time_title = tkinter.LabelFrame(window, text="Current time", font=("Helvetica", 26))
label_current_time_title.grid(column = 0, row = 2, padx = 10, pady = 10, sticky="news")

label_current_date = tkinter.Label(label_current_time_title, textvariable = var_current_date, font=("Helvetica", 22), wraplength = 210)
label_current_time = tkinter.Label(label_current_time_title, textvariable = var_current_time, font=("Helvetica", 22), wraplength = 210)
label_current_time.grid(column = 1, row = 0, padx = 10, pady = 10)
label_current_date.grid(column = 0, row = 0, padx = 10, pady = 10)

####################################################################################


server_loc = raw_input("where is server ZFS root directory?\t") 
current_date = time.strftime("%Y-%m-%d")


while True:
	filename = server_loc + "/logs/Optomech/#logging.%s.log" % current_date
	logfile = open(filename)
	loglines = follow(logfile)
	if time.strftime("%Y-%m-%d") == current_date:
		var_edfa_mode.get()
		try:
			for line in loglines:
				#print(line.strip())
				if "< edwards>" in line:
					entry = line.split()
					#print entry
					scroll_pump = [float(thing) for thing in [entry[8], entry[12], entry[16], entry[20]]]
					scroll_pump.append(entry[3][1:]+" "+entry[4][:8]+entry[5][:-1])
					for i in range(len(scroll_pump)):
						vars_edw[i].set(scroll_pump[i])
					if float(var_edw_P.get()) > 50:
						label_edw_P.config(fg="green")
					else:
						label_edw_P.config(fg="red")
					window.update_idletasks()
					
				elif "< environment>" in line:
					entry = line.split()
					#print entry
					environment = [float(thing) for thing in [entry[7], entry[11], entry[15]]]
					environment.append(entry[3][1:]+" "+entry[4][:8]+entry[5][:-1])
					for i in range(len(environment)):
						vars_env[i].set(environment[i])
					window.update_idletasks()
					
				elif "< Pressure>" in line:
					entry = line.split()
					#print entry
					environment = [float(thing) for thing in [entry[8]]]
					environment.append(entry[3][1:]+" "+entry[4][:8]+entry[5][:-1])
					for i in range(len(environment)):
						vars_vc[i].set(environment[i])
					if float(var_vc_P.get()) > 100:
						label_vc_P.config(fg="green")
					elif float(var_vc_P.get()) <= 1e-3:
						label_vc_P.config(fg="red")
					else:
						label_vc_P.config(fg="orange")
					label_vc_title_P.config(fg="black")
					label_vc_title_time.config(fg="black")
					window.update_idletasks()
					
				elif "< Thorlabs>" in line:
					entry = line.split()
					#print entry
					environment = [entry[8] + " " + entry[9]]
					environment.append(entry[3][1:]+" "+entry[4][:8]+entry[5][:-1])
					for i in range(len(environment)):
						vars_thorlabs[i].set(environment[i])
					window.update_idletasks()
					
				elif "< EDFA>" in line:
					entry = line.split(",")
					#print entry
					edfa = [entry[0].split()[8:-1], entry[1].split()[-1], entry[2].split()[1], entry[3].split()[1], entry[4].split()[1], entry[5].split()[1], entry[6].split()[1], entry[7].split()[1], entry[8].split()[1], entry[9].split()[1], entry[10].split()[1], entry[0].split()[3][1:]+" "+entry[0].split()[4][:8]+entry[0].split()[5][:-1]]
					
					for i in range(len(edfa)):
						vars_edfa[i].set(edfa[i])
					
					if "OFF" in str(var_edfa_mode.get()):
						label_edfa_mode.config(fg = "red")
					else:
						label_edfa_mode.config(fg = "green")
					
					if float(var_edfa_P_in.get()) > 1e-3:
						label_edfa_P_in.config(fg="green")
					else:
						label_edfa_P_in.config(fg="red")
					
					if float(var_edfa_P_out.get()) > 1:
						label_edfa_P_out.config(fg="green")
					else:
						label_edfa_P_out.config(fg="red")
					
					window.update_idletasks()
					
				var_current_date.set(datetime.utcnow().strftime("%Y-%m-%d"))
				var_current_time.set(datetime.utcnow().strftime("%H:%M:%S UTC"))
				window.update_idletasks()
		except:
			continue
	else:
		current_date = time.strftime("%Y-%m-%d")



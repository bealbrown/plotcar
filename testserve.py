from bokeh.plotting import figure, curdoc
from bokeh.driving import linear
from bokeh.models import Legend
from bokeh.models import ColumnDataSource, HoverTool, DatetimeTickFormatter, DatetimeTicker, Legend
import random
import pandas as pd
from datetime import datetime
import time

import database as rdb

p = figure(plot_width=1500, plot_height=1000, x_axis_type="auto")

# p.xaxis.formatter=DatetimeTickFormatter(minutes = [':%M', '%Mm'])
# p.xaxis.ticker = DatetimeTicker(desired_num_ticks=30)
p.xaxis.ticker.desired_num_ticks = 30

linelist = []
for x in range(0,40):
	linelist.append(p.line([], [], line_width=2, alpha=0.9, muted_alpha=0.2, color='grey', legend_label=str(x+1)))

dslist = []
for x in range(0,40):
	dslist.append(linelist[x].data_source)

p.legend.location = "top_left"
p.legend.click_policy="hide"


def load_data():


	dbdata = rdb.get_records()
	df = pd.DataFrame(dbdata)




	print(df)

	datetimes = []

	for timestamp in df.iloc[:,1].values:
		dateobj = datetime.fromtimestamp(int(timestamp))
		datetimes.append(dateobj)                
	
	for i in range(0,40):

		yvals = df.iloc[:,i+2].values

		newyvals = []
		for el in yvals:
			if (el > 100000000000):
				newyvals.append(1000000000)
			else:
				newyvals

		dslist[i].data.update({'x':datetimes, 'y': newyvals})
		dslist[i].trigger('data', dslist[i].data, dslist[i].data)


@linear()
def update(step):
	load_data()


curdoc().add_root(p)

# Add a periodic callback to be run every n milliseconds
curdoc().add_periodic_callback(update, 5000)

load_data()

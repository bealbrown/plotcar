# myplot.py
from bokeh.plotting import figure, curdoc
from bokeh.driving import linear
from bokeh.models import Legend
import random
import pandas as pd


from bokeh.models import ColumnDataSource, HoverTool, DatetimeTickFormatter, DatetimeTicker

import database as rdb



# TODO
# Format datetimes more pleasingly
# perhaps do multiline hover
# clean up repo
# set up time to meet

# multi line hover answers:
# https://stackoverflow.com/questions/49282078/multiple-hovertools-for-different-lines-bokeh


p = figure(plot_width=2000, plot_height=1000, x_axis_type="datetime")

p.xaxis.formatter=DatetimeTickFormatter(minutes = [':%M', '%Mm'])
# p.xaxis.ticker = DatetimeTicker(desired_num_ticks=30)
p.xaxis.ticker.desired_num_ticks = 30

linelist = []
for x in range(0,40):
	linelist.append(p.line([], [], line_width=2, alpha=0.9, muted_alpha=0.2, color='grey', legend_label=str(x)))

dslist = []
for x in range(0,40):
	dslist.append(linelist[x].data_source)

p.legend.location = "top_left"
p.legend.click_policy="hide"


def load_data():


	dbdata = rdb.get_records()

	df = pd.DataFrame(dbdata)
	datetimes = pd.to_datetime(df[1]).values

	for i in range(0,40):
		dslist[i].data['x'] = datetimes
		dslist[i].data['y'] = df.iloc[:,i+2].values

		dslist[i].trigger('data', dslist[i].data, dslist[i].data)

@linear()
def update(step):
	load_data()


curdoc().add_root(p)

# Add a periodic callback to be run every 1000 milliseconds
curdoc().add_periodic_callback(update, 5000)

load_data()
import pandas as pd
from pyecharts.charts import Pie
from pyecharts.charts import Bar
from pyecharts.charts import Grid
from pyecharts.charts import Map
from pyecharts.charts import Geo
from pyecharts.charts import WordCloud
from pyecharts.charts import PictorialBar
from pyecharts.charts import Liquid
from pyecharts.charts import Polar
from pyecharts import options as opts
from pyecharts.commons.utils import JsCode
df = pd.read_excel('2022年世界五百强排行榜.xlsx')
df.head(10)
df.info()
bar = (
    Bar(init_opts=opts.InitOpts(width='1000px', height='1000px',bg_color='#0d0735'))
    .add_xaxis(x_data)
    .add_yaxis("",y_data)
    .set_series_opts(label_opts=opts.LabelOpts(position="right",
                                              font_size=12,
                                              font_weight='bold',
                                              formatter='{c} 家'),
                    )
    .set_global_opts(
                    xaxis_opts=opts.AxisOpts(is_show=False,),
                    yaxis_opts=opts.AxisOpts(
                        axislabel_opts=opts.LabelOpts(font_size=13,color='#fff200'),
                        axistick_opts=opts.AxisTickOpts(is_show=False),
                        axisline_opts=opts.AxisLineOpts(is_show=False)
                    ),
                    title_opts=opts.TitleOpts(title="各国世界500强企业数量排名",pos_left='center',pos_top='1%',
                              title_textstyle_opts=opts.TextStyleOpts(font_size=22,color="#38d9a9")),
                    visualmap_opts=opts.VisualMapOpts(is_show=False,
                                      min_=20,
                                      max_=150,
                                      is_piecewise=False,
                                      dimension=0,
                                      range_color=['#203fb6', '#008afb', '#ffec4a', '#ff6611', '#f62336']
                                                     ),
                    )
    .reversal_axis()
)

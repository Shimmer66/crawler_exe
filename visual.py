from pyecharts import options as opts
from pyecharts.charts import Scatter
from pyecharts.faker import Faker
import pandas as pd

# 将数据读取为 DataFrame 格式
data = pd.read_csv('data.csv')

# 将数据转化为 pyecharts 所需的格式
scatter_data = []
for _, row in data.iterrows():
    scatter_data.append([row['Month'], row['Consumption2020'], row['Consumption2021'], row['Consumption2022']])

# 使用 Scatter 绘制散点图
scatter = (
    Scatter()
    .add_xaxis([d[0] for d in scatter_data])
    .add_yaxis('2020', [d[1] for d in scatter_data], symbol_size=10)
    .add_yaxis('2021', [d[2] for d in scatter_data], symbol_size=10)
    .add_yaxis('2022', [d[3] for d in scatter_data], symbol_size=10)
    .set_series_opts(label_opts=opts.LabelOpts(formatter='{b}'))
    .set_global_opts(title_opts=opts.TitleOpts(title='每月的居民消费价格指数'),
                     xaxis_opts=opts.AxisOpts(name='月份'),
                     yaxis_opts=opts.AxisOpts(name='居民消费价格指数', min_=99,  # 设置纵坐标最小值
                                              max_=105) ) # 设置纵坐标最大值)

                     .render("散点图.html")
                     )

# 显示图表
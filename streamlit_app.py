import pandas as pd
import streamlit as st
from DataProcessing import calculate
import time
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["font.sans-serif"] = ["SimHei"]  # 设置字体
plt.rcParams["axes.unicode_minus"] = False  # 该语句解决图像中的“-”负号的乱码问题

st.title('个人碳足迹计算器')

# --------------------------------------------------------------------------------------------------------
with st.container():
    st.header('能源消费')
    item_r11 = '用电量'
    value_r11 = st.number_input(item_r11 + '(kWh)', value=300.0, step=0.1)
    item_r12 = '用水量'
    value_r12 = st.number_input(item_r12 + '(吨)', value=3.0, step=0.1)
    item_r13 = '天然气用量'
    value_r13 = st.number_input(item_r13 + '(立方米)', value=15.0, step=0.1)
    item_r14 = '煤气用量'
    value_r14 = st.number_input(item_r14 + '(罐)', value=1.0, step=0.1, format='%.1f')
# --------------------------------------------------------------------------------------------------------
with st.container():
    st.header('交通出行')
    st.write('采用以下方式出行的距离')
    item_r21 = '飞机'
    value_r21 = st.number_input(item_r21 + '(km)', value=0.0, step=0.1)
    item_r22 = '火车'
    value_r22 = st.number_input(item_r22 + '(km)', value=0.0, step=0.1)
    item_r23 = '公交车'
    value_r23 = st.number_input(item_r23 + '(km)', value=0.0, step=0.1)
    item_r24 = '地铁'
    value_r24 = st.number_input(item_r24 + '(km)', value=0.0, step=0.1)
    item_r25 = '电梯'
    value_r25 = st.number_input(item_r25 + '(层)', value=0, step=1)

# --------------------------------------------------------------------------------------------------------
with st.container():
    st.header('饮食习惯')
    item3 = [['主食', '(g)', 0], ['牛肉', '(g)', 0], ['羊肉', '(g)', 0], ['猪肉', '(g)', 0], ['鸡肉', '(g)', 0],
             ['牛奶', '(瓶)', 0], ['鸡蛋', '(个)', 0]]
    for i in range(len(item3)):
        item3[i][2] = st.number_input(item3[i][0] + item3[i][1], value=0, step=1)

# --------------------------------------------------------------------------------------------------------
with st.container():
    st.header('购物行为')
    st.write('请选择您购买以下物品的数量')
    item4 = [['牛仔服饰', '(件)', 0], ['棉质服装', '(件)', 0], ['T恤衫', '(件)', 0], ['羽绒服饰', '(件)', 0], ['鞋子', '(双)', 0],
             ['空调', '(台)', 0], ['洗衣机', '(台)', 0], ['电冰箱', '(台)', 0], ['微波炉', '(台)', 0], ['热水器', '(台)', 0],
             ['吸尘器', '(台)', 0], ['电视机', '(台)', 0], ['手机', '(台)', 0], ['笔记本电脑', '(台)', 0], ['平板电脑', '(台)', 0],
             ['台式电脑', '(台)', 0]]
    for i in range(len(item4)):
        item4[i][2] = st.number_input(item4[i][0] + item4[i][1], value=0, step=1)

if st.button('计算碳足迹'):
    carbon_part1, carbon_part2, carbon_part3, carbon_part4 = 0, 0, 0, 0
    carbon_part1 = calculate(item_r11, value_r11) + calculate(item_r12, value_r12) + calculate(item_r13,
                                                                                               value_r13) + calculate(
        item_r14, value_r14)
    carbon_part2 = calculate(item_r21, value_r21) + calculate(item_r22, value_r22) + calculate(item_r23,
                                                                                               value_r23) + calculate(
        item_r24, value_r24) + calculate(item_r25, value_r25)
    for i in range(len(item3)):
        carbon_part3 += calculate(item3[i][0], item3[i][2])
    for i in range(len(item4)):
        carbon_part4 += calculate(item4[i][0], item4[i][2])
    carbon = carbon_part1 + carbon_part2 + carbon_part3 + carbon_part4
    st.write('您一年的碳足迹排放约为 ' + str(carbon) + ' kg 二氧化碳')
    # st.write(carbon_part1, carbon_part2, carbon_part3, carbon_part4)

    # chart_data = pd.DataFrame(np.array([carbon_part1, carbon_part2, carbon_part3, carbon_part4]),
    #                           columns=['能源消费', '交通出行', '饮食习惯', '购物行为'])
    # st.bar_chart(chart_data)
    arr = np.array([carbon_part1, carbon_part2, carbon_part3, carbon_part4])
    # st.write(arr)
    fig, ax1 = plt.subplots()
    labels = ['能源消费', '交通出行', '饮食习惯', '购物行为']
    ax1.pie(arr, labels=labels, autopct='%1.1f%%')
    ax1.axis('equal')
    st.pyplot(fig)

    fig, ax2 = plt.subplots()
    # x = np.arange(len(labels))
    width = 0.35
    p = ax2.bar(labels, arr, width)
    # ax2.set_xticks(x, labels)
    # ax2.bar_label(p, label_type='center')
    st.pyplot(fig)

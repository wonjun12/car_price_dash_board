import streamlit as st

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from app_module.app_home import run_app_home
from app_module.app_eda import run_app_eda
from app_module.app_ml import run_app_ml

def main():
    st.title('자동차 가격 예측 앱')
    st.text('자동 배포 처리된 앱입니다.')

    menu = ['Home', 'EDA', 'ML']
    choice = st. sidebar.selectbox('메뉴', menu)

    if choice == menu[0]:
        # 설명 글
        run_app_home()
    elif choice == menu[1]:
        run_app_eda()
    else : 
        run_app_ml()

    

if __name__ == '__main__':
    main()

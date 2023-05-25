import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def run_app_eda():
    st.subheader('데이터 분석')

    df = pd.read_csv('data/Car_Purchasing_Data.csv', encoding='ISO-8859-1')

    if st.checkbox('데이터 프레임 보기'):
        st.dataframe(df)

    st.subheader('기본 통계 데이터')
    st.dataframe(df.describe())

    st.subheader('최대 / 최소 데이터 확인하기')
    column = st.selectbox('컬럼을 선택하세요.', df.columns[3 : ]) # 계산할 수 있는 컬럼이 Gender 부터다.
    st.dataframe(df.loc[df[column] == df[column].max(), ])

    st.subheader('컬럼 별 히스토그램')
    column = st.selectbox('히스토그램을 확인할 컬럼을 선택하세요.', df.columns, 4)
    bins = st.number_input('빈의 갯수를 입력하세요.', 10, 30, 20)
        # 빈 최솟값10, 최댓값30, 기본값20
    fig = plt.figure() # 영역 잡기
    df[column].hist(bins=bins)
    plt.title(f"{column} | Histogram")
    plt.ylabel('Count')
    st.pyplot(fig)

    st.subheader('상관 관계 분석')
    column_list = st.multiselect('상관 분석 하고 싶은 컬럼 선택해!', df.columns[3:])
    if len(column_list) > 1:
        fig_corr = plt.figure()
        sns.heatmap(
            data = df[column_list].corr(numeric_only=True),
            annot = True,
            vmin = -1, #범위 설정
            vmax = 1,
            fmt = '.2f', # format 표시 소수점
            linewidth = 0.5, # 간격 설정
            cmap = 'coolwarm'
        )
        st.pyplot(fig_corr)
    




import streamlit as st

# 설명 작성
def run_app_home():
    st.subheader('오랴오랴')
    st.text('이 앱은 고객 데이터와 자동차 구매 데이터에 대한 내용임!')

    st.text('데이터 분석이 가능하고, 고객 정보를 넣으면 구매 차량 가격도 예측 해줌!')

    img_url = 'https://img.lovepik.com/free-png/20220108/lovepik-car-png-image_401292353_wh860.png'
    st.image(img_url)
    
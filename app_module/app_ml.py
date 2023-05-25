import streamlit as st
import numpy as np
import joblib # 인공지능 파일화 저장한것을 불러오기

def run_app_ml():
    st.subheader('자동차 금액 예측')

    # 성별, 나이, 연봉, 카드빚, 자산
    # 유저에게 정보를 입력 받는다.
    gender = st.radio('성별', ['남자', '여자']) # 성별 선택
    gender = 0 if gender == '남자' else 1
    
    age = st.number_input('나이 입력', 18, 100)

    salary = st.number_input('연봉 입력', 5000, 1000000) 

    debt = st.number_input('카드 빚', 0, 1000000)

    worth = st.number_input('자산 입력', 1000, 1000000)

    

    
    # 버튼을 누르면 예측한 금액을 표시한다.
    if st.button('금액 예측'):
        new_data = np.array([gender, age, salary, debt, worth])
        new_data = new_data.reshape(-1, 5)

        regressor = joblib.load('model/regressor.pkl') # 파일 불러오기
        # 코렙에서 작업한것과 여기서 작업하는게 버전이 맞지 않아서 실행이 되지 않는다.
        # 코렙의 버전이 더 높기때문에 conda 버전을 높인다.
            # 코렙의 최신버전 1.2.0 > conda 버전 1.1.0
        y_pred = regressor.predict(new_data) # 예측 데이터
        #print(y_pred)
        
        st.success(f'{int(y_pred)}$ 차량 구매 가능!')

    
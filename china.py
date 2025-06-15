from matplotlib import pyplot as plt
import streamlit as st
import pandas as pd
import plotly.express as px

st.markdown(
    """
    <style>
    /* 제목 */
    h1 {
        font-family: 'Black Han Sans', sans-serif !important;
        font-weight: 400 !important;
        font-size: 50px !important;
        margin-bottom: 0 !important;
        color: #0F3DF5 !important;
    }

     /* 소제목 */
    h3 {
        font-family: 'Black Han Sans', sans-serif !important;
        font-weight: 400 !important;
        font-size: 30px !important;
        margin-bottom: 0 !important;
        color: #000000 !important;
    }
    </style>

    <!-- Black Han Sans 폰트 불러오기 -->
    <link href="https://fonts.googleapis.com/css2?family=Black+Han+Sans&display=swap" rel="stylesheet">
    """,
    unsafe_allow_html=True,
)

st.markdown('<h1>미국 비자 정책의 역설</h1>', unsafe_allow_html=True)
st.write("2020년, 트럼프 정부는 Proclamation 10043을 통해 중국 인민해방군과 연계된 연구자 및 대학원생 약 1000명의 비자를 취소했습니다. 이는 미-중 간 기술 경쟁의 일환이자, 미국 내 첨단기술 유출을 막기 위한 조치였습니다.")
st.markdown('<h3>정책의 결과: 중국으로 돌아가는 학자 급증</h3>', unsafe_allow_html=True)


data = {
    "연도": [2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021],
    "공학 및 컴퓨터 과학": [3,1,3,9,13,15,17,23,31,52,65,77,84,89,125,103,154,147,168,192,240,297],
    "수학 및 물리 과학": [20,27,18,18,34,50,63,66,103,120,168,227,195,235,272,316,361,414,496,563,589,662],
    "생명 과학": [4,12,8,23,36,31,50,77,90,122,146,170,224,294,348,370,442,441,494,532,518,610],
    "사회 과학": [0,0,1,1,3,2,2,6,9,12,9,17,24,23,30,28,40,48,54,67,46,71]
}
df = pd.DataFrame(data)
df.set_index("연도", inplace=True)
st.line_chart(df)

df_recent = df.loc[[2019, 2020, 2021]]
subjects = ["공학 및 컴퓨터 과학", "수학 및 물리 과학", "생명 과학", "사회 과학"]
selected_subject = st.selectbox("학문 별로 중국 귀국 학자 수 확인:", subjects)
st.bar_chart(df_recent[[selected_subject]])

st.write("비자 정지 정책으로 인해 중국인 학자가 중국으로 귀국하는 것은 '우수한 인재들'의 유출로 볼 수도 있습니다.실제로 미국에서 중국으로 돌아간 학자가 중국 과학 기술의 발전에 기여한 사례도 있어요.")

st.markdown('<h3>미국이 놓친 인재 : 송춘주 교수</h3>', unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)

with col1:
    st.image("ucla.gif")
    st.markdown("<h2 style='text-align: center;'>UCLA</h2>", unsafe_allow_html=True)
    st.markdown("""
        <div style="background-color: #E5DDDA; padding: 10px; border-radius: 5px; text-align: center;">
            AI&CI 연구
        </div>
    """, unsafe_allow_html=True)
with col2:
    st.image("china.gif")
    st.markdown("<h2 style='text-align: center;'>China</h2>", unsafe_allow_html=True)
    st.markdown("""
        <div style="background-color: #E5DDDA; padding: 10px; border-radius: 5px; text-align: center;">
            비자 정지 정책으로 인해 귀국
        </div>
    """, unsafe_allow_html=True)
with col3:
    st.image("bigai.gif")
    st.markdown("<h2 style='text-align: center;'>BIGAI</h2>", unsafe_allow_html=True)
    st.markdown("""
        <div style="background-color: #E5DDDA; padding: 10px; border-radius: 5px; text-align: center;">
            배이징 일반인공지능 연구소 설립
        </div>
    """, unsafe_allow_html=True)

st.markdown("""
    <div style="display: flex; justify-content: center; margin-top: 30px; margin-bottom: 30px">
        <div style="position: relative; background-color: #2196F3; padding: 15px; border-radius: 10px; width: fit-content;">
            <b style="color: white;">
                미국에서 쫓겨난 송춘주 교수님은 중국 배이징에 일반 인공지능 연구소를 설립!<br>
                이 연구소는 최근에 세계 최초 기술을 개발하는 등 중국의 기술력에 크게 기여하고 있어요.
            </b>
            <div style="content: ''; position: absolute; top: -10px; left: 50%; transform: translateX(-50%); border-width: 0 10px 10px 10px; border-style: solid; border-color: transparent transparent #2196F3 transparent;"></div>
        </div>
    </div>
""", unsafe_allow_html=True)


st.markdown('<h3>중국의 과학기술력은 2000년대에 계속 성장중</h3>', unsafe_allow_html=True)

# 원본 데이터
data = {
    "Index": [
        "중국 혁신 지수",
        "GDP 대비 R&D 투자 비율 지수",
        "연구자 1인당 기초 연구 투자금 지수",
        "기업 매출 대비 R&D 투자 비율 지수",
        "인구 1만 명당 과학기술 논문 수 지수",
        "R&D 인력 1만 명당 고가치 특허 보유 수 지수",
        "신산업·신기술·신형 서비스(3신경제)의 GDP 대비 부가가치 비율 지수"
    ],
    "2015": [100, 100, 100, 100, 100, 100, 100],
    "2020": [138.9, 117.0, 121.5, 156.2, 116.6, 190.2, 115.6],
    "2021": [146.9, 118.3, 136.1, 147.7, 121.5, 200.9, 116.8],
    "2022": [155.9, 124.2, 140.5, 161.0, 128.3, 227.7, 118.1],
    "2023": [165.3, 128.6, 138.9, 170.9, 129.8, 263.3, 120.1]
}

df = pd.DataFrame(data)

selected_indices = [
    "인구 1만 명당 과학기술 논문 수 지수",
    "R&D 인력 1만 명당 고가치 특허 보유 수 지수",
    "GDP 대비 R&D 투자 비율 지수"
]

df_selected = df[df["Index"].isin(selected_indices)].set_index("Index").T
df_selected.index.name = "연도"

cols = st.columns(3)

for col, idx in zip(cols, selected_indices):
    fig = px.line(
        x=df_selected.index,
        y=df_selected[idx],
        labels={"x": "연도", "y": idx},
        title=idx,
        range_y=[0, df_selected[idx].max() * 1.2]
    )
    col.plotly_chart(fig, use_container_width=True)





st.markdown('<h3>이번 미국의 비자 제한 조치, 오히려 중국에 기회를 안겨줄지도...?</h3>', unsafe_allow_html=True)
st.write("미국이 우수한 중국인 유학생들을 대상으로 비자 제한 조치를 내리면서, 이들이 중국으로 돌아가 자국의 발전에 기여하는 결과를 초래할 가능성이 커지고 있습니다.")

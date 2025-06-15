st.markdown("<h1>미국 여러 분야에서 유학생(이민자)의 활약</h1>", unsafe_allow_html=True)

col1, col2, col3, col4, col5, col6, col7 = st.columns([1, 3, 1, 3, 1,3,1])
with col2:
    st.subheader("유니콘 기업")
    st.image("percent/25.png")
    st.markdown("<h5>2022년 기준 미국의 유니콘 기업(평가액 10억 이상 스타트업)은 총 582개입니다. " \
"이중 25%인 143개가 유학생들이 설립한 기업으로, 미국에 유학온 학생들이 졸업 후 H-1B비자 혹은 그린카드로 거주하며 창업활동을 이어나가고 있습니다.</h5>", unsafe_allow_html=True)


with col4:
    st.subheader("특허")
    st.image("percent/23.png")
    st.markdown("<h5>1990년부터 2016년까지 미국 내 특허 출원자수는 약 880,000명입니다. 이중 이민자는 16%밖에 차지하지 않지만, 전체 특허 중 23%가 이민자들에 의해 출원된 것입니다.</h5>", unsafe_allow_html=True)
    st.text('*유학생이 아니라 이민자들의 비율입니다')

with col6:
    st.subheader("노벨상")
    st.image("percent/40.png")
    st.markdown("<h5>2000년부터 2023년까지 미국은 물리학, 화학, 의학 분야에서 노벨상을 각각 38개, 39개, 35개 수상하였습니다."
"<br>물리학의 경우 전체 노벨상 수상자 38인 중 이민자는 17명으로 전체의 45%를 차지합니다.화학의 경우 전체 수상자 39명 중 16명이 이민자로 41%를 차지했으며, 화학 분야는 35명의 34%인 12명이 이민자였습니다.</h5>", unsafe_allow_html=True)
    st.text('*유학생이 아니라 이민자들의 비율입니다')
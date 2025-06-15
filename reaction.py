import streamlit as st

# Custom CSS 적용
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

# 타이틀 및 설명 표시 (h1으로)
st.markdown("<h1>유학생, 교수, 대학교의 반응은?</h1>", unsafe_allow_html=True)
st.write("클릭해서 한명 한명의 이야기를 확인해보세요")

# 이모지 URL 리스트
emojis = [
    "https://em-content.zobj.net/source/apple/419/man-teacher-medium-light-skin-tone_1f468-1f3fc-200d-1f3eb.png",
    "https://em-content.zobj.net/source/apple/419/person-frowning_light-skin-tone_1f64d-1f3fb_1f3fb.png",
    "https://em-content.zobj.net/source/apple/419/woman-frowning-light-skin-tone_1f64d-1f3fb-200d-2640-fe0f.png",
    "https://em-content.zobj.net/source/apple/419/teacher-light-skin-tone_1f9d1-1f3fb-200d-1f3eb.png",
    "https://em-content.zobj.net/source/apple/419/man-frowning-medium-light-skin-tone_1f64d-1f3fc-200d-2642-fe0f.png",
    "https://em-content.zobj.net/source/apple/419/person-pouting_medium-light-skin-tone_1f64e-1f3fc_1f3fc.png",
    "https://em-content.zobj.net/source/apple/419/person-frowning_medium-dark-skin-tone_1f64d-1f3fe_1f3fe.png",
    "https://em-content.zobj.net/source/apple/419/man-gesturing-no-medium-light-skin-tone_1f645-1f3fc-200d-2642-fe0f.png",
    "https://em-content.zobj.net/source/apple/419/man-pouting-medium-skin-tone_1f64e-1f3fd-200d-2642-fe0f.png",
    "https://em-content.zobj.net/source/apple/419/man-teacher-light-skin-tone_1f468-1f3fb-200d-1f3eb.png",
    "https://em-content.zobj.net/source/apple/419/man-frowning-light-skin-tone_1f64d-1f3fb-200d-2642-fe0f.png",
    "https://em-content.zobj.net/source/apple/419/judge-medium-skin-tone_1f9d1-1f3fd-200d-2696-fe0f.png",
    "https://em-content.zobj.net/source/apple/419/man-pouting-medium-light-skin-tone_1f64e-1f3fc-200d-2642-fe0f.png",
    "https://em-content.zobj.net/source/apple/419/school_1f3eb.png",
    "https://em-content.zobj.net/source/apple/419/department-store_1f3ec.png"
]

# 타이틀 리스트
titles = [
    "미국 교수A", "1년 동안 미국 유학 준비중인 한국인 학생 B", "회사를 그만두고 유학 준비중인 한국인 학생 C", "49년째 유학 업체를 운영 중인 한국인 D",
    "캐나다 출신 하버드 유학생 E", "유럽 출신 하버드 유학생 F", "시에라리온 출신 하버드 유학생 G", "하버드 유학생 H",
    "강제송환 대상이 되어 스스로 미국을 출국한 인도 국적 유학생 I", "하버드 교수진", "일본 출신 하버드 유학생 J",
    "하버드 로스쿨 재학 중인 유학생 K", "항의 인해 비자가 취소된 코넬대 재학 유학생 L", "하버드대학교", "컬럼비아대학교"
]

# 발언 리스트
speeches = [
    "하버드는 버텨낼 수 있을 겁니다. 물론 힘들겠지만요. 제가 더 걱정하는 건 등록금과 수업료에서 나오는 수익에 크게 의존하는 공립대학들입니다.",
    "유학을 결정한 후 별다른 구직 활동 없이 공부만 했는데 결국 유학을 포기해야 하는 상황이 닥쳐올까 봐 두렵다. 지금 미 정부의 기조를 보면 유학을 가더라도 언제 추방될지 몰라 불안해해야 할 것 같다.",
    "미 대학원 입학이 거의 확정돼 퇴사했는데 유학생 비자 발급 절차가 까다로워져 제때 입학을 못 하게 될까 봐 걱정이 된다.",
    "유학생 비자 발급 심사를 강화한다는 보도가 나온 뒤, 불안해하며 ‘비자가 안 나오면 어떡하느냐’고 묻는 전화가 계속 걸려오고 있다. ‘기다려 봅시다’ ‘괜찮을 겁니다’ 같은, 심리적인 안정을 주는 말밖에는 해 줄 것이 없어 난감하다” “트럼프 대통령 1기(2017~2021년) 때부터 소셜미디어를 검열할 수 있다는 소문이 돌아서 우리 유학원은 학생들한테 웬만하면 소셜미디어를 하지 말고, 하려면 미국에 대해 안 좋은 얘기는 게시하지 말라고 교육해 왔다.",
    "연구뿐만 아니라 대학원생으로서 가르치고, 튜터링하고, 연구 보조원 일까지 하면서 그렇게 많은 노력을 했는데도 박사 학위를 마칠 수 없을 거라는 생각은 정말 절망적이었습니다. 그 모든 노력이 헛수고가 될 수도 있다는 생각에 정말 낙담했습니다.",
    "제 비자가 취소되어 하버드에 계속 등록할 수 있게 된다 하더라도(학교 측에서 아직 확인하지 않은 가능성) 제 신분이 위험에 처할 수 있는 다른 대학으로 전학을 가야 하거나, 아니면 본국에서 박사 학위를 마쳐야 합니다.",
    "아픈 일입니다. 저뿐만 아니라 이번 일이 의미하는바 때문입니다. 아프리카 학생들에게는 안 그래도 좁은 글로벌 교육의 문이었는데, 그 문마저 닫히면 우리 존재는 조건부였음을 느끼게 될 것 같습니다.",
    "우리 없이 하버드는 하버드가 아니다.",
    "나는 테러리스트 지지자가 아니다.",
    "트럼프 행정부는 이미 20억 달러 이상의 보조금 지원을 중단했고, 대학의 면세 지위를 박탈하는 것을 고려하고 있으며, 외국인 학생 입학 허가를 취소하겠다고 위협했습니다.",
    "물론 깜짝 놀라긴 했지만, 그렇다고 해서 ‘청천벽력’이라고 할 정도는 아니었습니다. 사실 올해 4월쯤부터 교내 신문 등에서 하버드와 정권의 관계가 좋지 않은 것 같다는 소문이 돌고 있었거든요.",
    "아직 모든 절차가 명확히 정리된 것이 아니어서 법적인 도움을 받고 있습니다. 미국에 계속 남을 수 있을지 장담할 수 없습니다.",
    "비자 발급 문제로 인해 수업을 들을 수 없게 되었고, 이로 인해 등록금 환불 요청을 하고 있습니다.",
    "학교 측에서는 상황을 예의주시하고 있으며 학생 보호 방안을 모색 중입니다.",
    "학교는 공식 입장을 내지 않고 있으며 사태 추이를 지켜보고 있습니다."
]


if "selected" not in st.session_state:
    st.session_state.selected = None

cols = st.columns(5)
for idx in range(len(emojis)):
    col = cols[idx % 5]
    with col:
        st.image(emojis[idx], width=80)
        if st.button("💬", key=idx):
            st.session_state.selected = idx

if st.session_state.selected is not None:
    st.markdown(
        f"""
        <h3 style='text-align: left;'>
            {titles[st.session_state.selected]}
        </h3>
        <div style='
            position: relative; 
            display: flex; 
            justify-content: center; 
            margin-top: 0;
        '>
            <div style='
                display: inline-block; 
                padding: 10px; 
                border: 1px solid #ddd; 
                border-radius: 10px; 
                background-color: #0F3DF5; 
                color: white;
                text-align: center;
                position: relative;
            '>
                {speeches[st.session_state.selected]}
                <div style='
                    content: ""; 
                    position: absolute; 
                    top: -10px; 
                    left: 20; 
                    width: 0; 
                    height: 10; 
                    border-right: 15px solid #0F3DF5; 
                    border-top: 15px solid transparent; 
                    border-bottom: 15px solid transparent;
                '></div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )



st.markdown("---")
st.title("SNS에서 사람들의 반응은?")
st.write("한국, 미국에서 사람들은 이 정책에 대해서 어떻게 반응하고 있을까요? 뉴스, Instagram, Youtube, X 댓글에서 많이 언급된 단어를 확인해보세요!")

option = st.selectbox(
    "보고 싶은 워드클라우드를 선택해주세요",
    ("한국 뉴스 댓글에서 가장 언급된 단어는?", "한국 사람들은 어떤 감정을 보이고 있을까?")
)
if option == "한국에서 많이 언급된 단어는?":
    st.image("korea_noun.png", caption="뉴스 댓글 명사 워드클라우드")
elif option == "한국 사람들의 반응은?":
    st.image("korea_adj.png", caption="뉴스 댓글 형용사 워드클라우드")


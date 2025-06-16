import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Trump Timeline", layout="wide")
st.image("assets/heading.png")

st.markdown("""
    <style>
    body {
        background-color: #1D1D1B;
        color: white;
    }
    .container {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-top: 30px;
    }
    .text-col {
        width: 30%;
        padding: 0 20px;
        line-height: 1.8;
        font-size: 18px;
    }
    .gif-col {
        width: 30%;
        text-align: center;
    }
    h1 {
        text-align: center;
        color: white;
        margin-top: 50px;
    }
    </style>

    <h1>미국의 유학생 비자 정책 도대체 무슨 일?</h1>

    <div class="container">
        <div class="text-col">
            2025년 트럼프 대통령은 재임과 동시에 하버드를 포함한 미국 주요 대학들의 다양성(DEI) 프로그램과
            팔레스타인 지지 시위에 대해 강경 대응하며,<br><br>
            연방 보조금 삭감, 세제 혜택 박탈 위협, 외국인 유학생 프로그램 인증 취소 등 전방위적인 압박을 가하고 있습니다.
            하버드는 이에 반발해 정부를 상대로 소송을 제기하며, 국제 유학생 보호를 위한 싸움을 이어가고 있습니다.
        </div>
        <div class="gif-col">
            <img src="https://interactives.dallasnews.com/2019/annotating-donald-trumps-dallas-speech/images/trump2.gif" width="100%">
        </div>
        <div class="text-col">
            이 정책으로 인해 수많은 유학생들은 학교를 떠나야 할 위기에 쳐했습니다. 
            트럼프는 이러한 정책은 "Make America Great Again"의 일환으로 실시하는 것으로 보입니다.
            <br><br>그런데 과연 유학생들을 쫓아냄으로써 미국을 더 "위대하게" 만들 수 있을까요? 
            그럼 지금부터 트럼프 행정부의 비자 정책이 어떻게 진행되어 왔고, 어떤 반응을 일으키고 있으며, 잠재적으로 어떤 결과를 초래할 수 있을지 데이터를 통해 살펴봅시다!
        </div>
    </div>
""", unsafe_allow_html=True)

st.markdown('---')

st.title("Trump vs International Students Timeline")

html_code = """
<!DOCTYPE html>
<html>
  <head>
    <!-- TimelineJS -->
    <link rel="stylesheet" href="https://cdn.knightlab.com/libs/timeline3/latest/css/timeline.css">
    <script src="https://cdn.knightlab.com/libs/timeline3/latest/js/timeline.js"></script>

    <!-- Load Google Fonts -->
    <link href="https://fonts.googleapis.com/css2?family=Do+Hyeon&family=Noto+Sans+KR&display=swap" rel="stylesheet">

    <style>
      html, body {
        margin: 0;
        padding: 0;
        height: 100%;
      }

      /* Title / Headline */
      .tl-headline, .tl-title, .tl-slide .tl-text h2 {
        font-family: 'Do Hyeon', sans-serif !important;
        # letter-spacing: 0.03em !important;
        line-height: 1.5 !important;
        font-weight: normal;
      }

      /* Body Text */
      .tl-text-content, .tl-text-content p, .tl-text-content li {
        font-family: 'Noto Sans KR', sans-serif !important;
        line-height: 1.5 !important;
        font-weight: 400;
      }
       /* Media caption and credit */
  .tl-media .tl-caption,
  .tl-media .tl-credit {
    font-family: 'Noto Sans KR', sans-serif !important;
    font-size: 14px;
    font-weight: 400;
    line-height: 1.5 !important;
  }

      #timeline-embed {
        width: 100%;
        height: 100vh;
      }
    </style>
  </head>
  <body>
    <div id="timeline-embed"></div>
    <script>
      var additionalOptions = {
        initial_zoom: 5
      };
      window.timeline = new TL.Timeline(
        'timeline-embed',
        'https://raw.githubusercontent.com/hana1101/trump_timeline/refs/heads/main/timeline.json',
        additionalOptions
      );
    </script>
  </body>
</html>
"""

components.html(html_code, height=800)

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
st.write(""" 지난 트럼프 행정부때로 거슬러 올라가 Proclamation 10043에서부터 유학생 대상 정책이 시작되었습니다. 이는 중국 대학원생 및 연구자의 비자 발급을 제재하는 내용을 담고 있었으며, 역 1,000명의 중국 유학생의 비자가 취소되었습니다.
         2025년 1월 트럼프 취임 이후, 트럼프의 대학교 DEI 프로그램과 빈유대주의 대응 강화 지시를 시작으로 강한 유학생 대상 정책이 시작되었습니다. 미국 법무부는 하버드, 콜롬비아, 조지 워싱턴 대학 등 미국 유명 대학을 대상으로 반유대주의 대응에 대한 조사를 착수하였고, 콜럼비아 대학교에게 연방 지원금을 4억 달러 삭감하는 등 강경한 조치를 이어나갔습니다.
         그 결과 콜럼비아 대학은 트럼프의 요구를 수용하였습니다. 트럼프는 하버드로 눈을 돌렸습니다. 하버드가 미국 교육부(ED), 보건복지부(HHS) 등과 맺은 대규모 계약을 검토하면서 '학생과 교직원 권한 축소를 위한 거버넌스 개편', '다양성 프로그램 폐지' 등을 요구하였고 하버드 측은 트럼프의 요구를 거부하였습니다.
         트럼프는 하버드 거부를 비판하며 과세 지위 박탈 가능성을 언급했으며 국토안보부(DHS)는 하버드 측에 유학생의 폭력적 활동에 관한 자료를 요구했으며, 이에 응하지 않을 시 학생 및 교환방문자 프로그램(SEVP)인증을 취소할 수 있다고 경고했습니다.
         하버드는 트럼프 행정부를 상대로 소송을 제기하였고, 하버드가 유학생 정보를 제공했음에도 트럼프 행정부는 하버드에 대한 신규 연방 보조금을 중단하였습니다. 또한 하버드의 유학생 및 교환 방문자 프로그램(SEVP) 인증 취소 통보했고, 연방 기관들과 하버드 간의 약 1억달러 계약 혜지를 요청하는 등 하버드에 압박을 가했습니다.
        법원은 정부의 비자 관련 조치에 가처분 명령을 내렸지만, 트럼프는 하버드 대학 유학생을 대상으로 6개월간 입국 중단을 명령했으며, 일부 유학생의 비자 취소 여부 검토 또한 지시하였습니다. 2025년 6월 5일, 미국 법원은 하버드 대학교에 대한 입국 금지 조치에 대한 임시 중단을 명령했지만 트럼프의 유학생 대상 비자 제한 정책과 하버드와의 갈등은 계속되고 있습니다.""")

st.markdown('---')

# 타이틀 및 설명 표시 (h1으로)
st.markdown("<h1>유학생, 교수, 대학교의 반응은?</h1>", unsafe_allow_html=True)
st.markdown("<h5>트럼프 유학생 비자 정책의 영향은 소수의 유학생들에게만 국한되지 않습니다. 현 유학생, 예비 유학생, 교수진 등 다양한 개인에게 영향을 미치고 있습니다.트럼프 유학생 비자 정책으로 유학생, 예비 유학생, 교수진 등 다양한 개인들이 영향을 받고 있습니다. 이들은 인터뷰에서 무엇을 말했을까요?</h5>", unsafe_allow_html=True)

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
    "유학생 비자 발급 심사를 강화한다는 보도가 나온 뒤, 불안해하며 ‘비자가 안 나오면 어떡하느냐’고 묻는 전화가 계속 걸려오고 있다. ‘기다려 봅시다’ ‘괜찮을 겁니다’ 같은, 심리적인 안정을 주는 말밖에는 해 줄 것이 없어 난감하다. 트럼프 대통령 1기 때부터 소셜미디어를 검열할 수 있다는 소문이 돌아서 우리 유학원은 학생들한테 웬만하면 소셜미디어를 하지 말고, 하려면 미국에 대해 안 좋은 얘기는 게시하지 말라고 교육해 왔다.",
    "연구뿐만 아니라 대학원생으로서 가르치고, 튜터링하고, 연구 보조원 일까지 하면서 그렇게 많은 노력을 했는데도 박사 학위를 마칠 수 없을 거라는 생각은 정말 절망적이었습니다. 그 모든 노력이 헛수고가 될 수도 있다는 생각에 정말 낙담했습니다.",
    "제 비자가 취소되어 하버드에 계속 등록할 수 있게 된다 하더라도 제 신분이 위험에 처할 수 있는 다른 대학으로 전학을 가야 하거나, 아니면 본국에서 박사 학위를 마쳐야 합니다.",
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
                background-color: #30A8F2; 
                color: white;
                text-align: center;
                position: relative;
                font-size: 18px;
            '>
                {speeches[st.session_state.selected]}
                <div style='
                    content: ""; 
                    position: absolute; 
                    top: -10px; 
                    left: 20; 
                    width: 0; 
                    height: 10; 
                    border-right: 15px solid #30A8F2; 
                    border-top: 15px solid transparent; 
                    border-bottom: 15px solid transparent;
                '></div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

st.write("트럼프 정부의 유학생 비자 정책 강화로 인해 유학생들은 학업 지속 여부, 졸업 가능성, 신분 유지 문제 등으로 깊은 불안을 호소하고 있습니다. 교수진과 학교 측도 이 상황을 예의주시하며 법적 대응과 학생 보호 방안을 모색 중이지만, 확실한 해결책은 없는 상황인데요. 안전해야 할 학문의 장이 정치적 변수로 위협받고 있으며, 유학생들은 추방·입학 취소 등의 불안 속에서 심리적·경제적 부담까지 떠안고 있습니다. ")
import streamlit as st
import base64

def img_to_base64(img_path):
    with open(img_path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

st.markdown("---")
st.title("SNS에서 사람들의 반응은?")
st.markdown("<h5>한국, 미국에서는 이 정책에 대해 사람들이 어떻게 반응하고 있을까요? <br>뉴스, Instagram, Youtube 댓글에서 많이 언급된 단어와 사람들이 보인 감정을 확인해보세요!</h5>", unsafe_allow_html=True)

# 명사 or 형용사 선택
word_type = st.selectbox("어떤 반응을 보고 싶은가요?", ("💬 많이 언급된 단어는?", "🔥 사람들의 감정은?"))

# 선택에 따라 파일명 지정
def get_image_filenames(word_type):
    if word_type == "💬 많이 언급된 단어는?":
        return "assets/korea_noun.png", "assets/usa_noun.png"
    else:
        return "assets/korea_adj.png", "assets/usa_adj.png"

img1_path, img2_path = get_image_filenames(word_type)

# 이미지 base64 인코딩
img1_base64 = img_to_base64(img1_path)
img2_base64 = img_to_base64(img2_path)

# 두 이미지 나란히 보여주기
st.markdown(f"""
<div style="display: flex; justify-content: center; gap: 40px;">
    <div style="text-align: center;">
        <h5>🇰🇷 한국</h5>
        <img src="data:image/png;base64,{img1_base64}" style="width: 600px;" />
    </div>
    <div style="text-align: center;">
        <h5>🇺🇸 미국</h5>
        <img src="data:image/png;base64,{img2_base64}" style="width: 600px;" />
    </div>
</div>
""", unsafe_allow_html=True)
st.write("")

st.write("""한국 측 워드클라우드에서는 ‘미국’, ‘트럼프’, ‘하버드’, ‘중국’, ‘유학생’ 등의 단어가 두드러지게 나타났습니다. 흥미로운 점은 유학생 비자 정책임에도 불구하고 ‘중국’이라는 특정 국가명이 주요 키워드로 등장했다는 사실입니다. 이는 많은 사람들이 이번 조치를 단순한 비자 정책이 아닌 미·중 갈등의 연장선으로 해석하고 있다는 점을 보여줍니다. 실제로 트럼프 행정부가 중국 출신 유학생을 겨냥한 발언이나 정책을 내놓은 바 있기 때문에 이러한 인식이 반영된 것으로 보입니다.
         반면 미국 측 워드클라우드에서는 ‘student’, ‘harvard’라는 단어가 가장 많이 등장했습니다. 이를 통해 미국 내에서는 이번 사안을 ‘유학생 개인’과 ‘하버드 등 주요 대학’의 문제로 인식하고 있으며, 트럼프 행정부와 하버드 대학 간 대립 구도가 부각되고 있음을 알 수 있습니다.
         형용사 분석 결과에서도 두 나라의 시각 차이가 드러납니다. 한국에서는 ‘미친’, ‘어떻게’와 같은 다소 감정적이고 우려 섞인 표현이 많아 이번 정책이 불러온 충격과 당혹감을 보여주었습니다. 반면 미국에서는 ‘federal’, ‘free’, ‘anti’ 등의 단어가 등장해 정책의 법적·제도적 측면이나 ‘자유’, ‘반대’라는 가치 판단과 관련된 논의가 활발하게 이루어지고 있는 것으로 나타났습니다.""")


##### 현재 유학생 수치#####
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np
import plotly.express as px

st.markdown("---")

# 제목
st.title("미국 유학생 현황")

@st.cache_data
def load_country_data():
    """국가별 유학생 데이터를 로드하고 정리"""
    try:
        df = pd.read_excel('data/st_nation.xlsx', 
                          sheet_name='Intl Students Place of Origin',
                          header=2)
        
        # 컬럼명 정리
        columns = df.columns.tolist()
        
        # 연도 컬럼들 찾기 (1949/50 형태)
        year_columns = []
        for i, col in enumerate(columns):
            if isinstance(col, str) and '/' in col and len(col.split('/')) == 2:
                try:
                    year_part = col.split('/')[0]
                    if year_part.isdigit() and len(year_part) == 4:
                        year_columns.append(col)
                except:
                    continue
        
        # 국가 데이터만 필터링 (첫 번째 컬럼이 숫자인 행들)
        numeric_mask = pd.to_numeric(df.iloc[:, 0], errors='coerce').notna()
        country_df = df[numeric_mask].copy()
        
        # 국가명 컬럼명 설정
        country_df.columns = ['Code'] + ['Country'] + [col for col in columns[2:]]
        
        # 연도별 총합 계산
        year_totals = {}
        for year in year_columns:
            total = 0
            for _, row in country_df.iterrows():
                val = row[year]
                if pd.notna(val) and str(val) != '-' and isinstance(val, (int, float)):
                    total += val
            year_totals[year] = total
        
        return country_df, year_columns, year_totals
        
    except Exception as e:
        st.error(f"❌ 데이터 로딩 중 오류 발생: {str(e)}")
        return None, None, None

@st.cache_data
def get_top_countries_for_year(country_df, year_columns, selected_year, top_n=15):
    """특정 연도의 상위 N개 국가 데이터 반환"""
    if selected_year not in year_columns:
        return pd.DataFrame()
    
    # 해당 연도 데이터 추출
    year_data = []
    total_students = 0

    # 제외할 키워드들
    exclude_keywords = [
        'TOTAL', '총', 'Total', 'AFRICA, SUB-SAHARAN','East Africa', 'Central Africa', 
        'Southern Africa', 'West Africa', 'ASIA', 'East Asia','South and Central Asia', 
        'Southeast Asia', 'EUROPE', 'LATIN AMERICA & CARIBBEAN', 'Caribbean', 'Mexico and Central America',
        'South America', 'MIDDLE EAST & NORTH AFRICA', 'MIDDLE EAST', 'North Africa', 'NORTH AMERICA', 'OCEANIA',
        
    ]
    
    for _, row in country_df.iterrows():
        country_name = str(row['Country']).strip()
        
        # 제외할 키워드가 포함된 항목들 스킵
        if any(keyword.upper() in country_name.upper() for keyword in exclude_keywords):
            continue
            
        # 너무 짧은 이름이나 숫자로만 된 이름 스킵
        if len(country_name) < 3 or country_name.isdigit():
            continue
            
        val = row[selected_year]
        if pd.notna(val) and str(val) != '-' and isinstance(val, (int, float)) and val > 0:
            year_data.append({
                'Country': country_name,
                'Students': val
            })
            total_students += val
    
    # DataFrame 생성 및 정렬
    year_df = pd.DataFrame(year_data)
    if year_df.empty:
        return pd.DataFrame()
    
    year_df = year_df.sort_values('Students', ascending=False)
    
    # 상위 N개만 (기타 제거)
    top_countries = year_df.head(top_n).copy()
    
    # 비율 계산
    top_countries['Percentage'] = (top_countries['Students'] / total_students * 100).round(1)
    
    return top_countries

# 데이터 로드
country_df, year_columns, year_totals = load_country_data()

if country_df is not None and year_columns is not None:
    
    # 세션 상태 초기화
    if 'selected_year' not in st.session_state:
        st.session_state.selected_year = year_columns[-1]  # 최신 연도로 초기화
    
    # 년도를 정수로 변환하여 총합 데이터프레임 생성
    totals_data = []
    for year_str, total in year_totals.items():
        year_int = int(year_str.split('/')[0])
        totals_data.append({'Year': year_int, 'Year_Str': year_str, 'Total_Students': total})
    
    totals_df = pd.DataFrame(totals_data).sort_values('Year')
    
    # 증가율 계산
    totals_df['Growth_Rate'] = totals_df['Total_Students'].pct_change() * 100
    
    # 메인 그래프 - 전체 유학생 수 변화
    st.subheader("연도별 전체 미국 유학생 수 변화")
    
    # 현재 선택된 연도 표시
    current_year_int = int(st.session_state.selected_year.split('/')[0])
    #st.info(f"🎯 **현재 선택된 연도: {st.session_state.selected_year}** (그래프의 점을 클릭하여 다른 연도 선택)")
    
    # Plotly 그래프 생성
    fig_main = go.Figure()
    
    # 기본 라인 추가
    fig_main.add_trace(go.Scatter(
        x=totals_df['Year'],
        y=totals_df['Total_Students'],
        mode='lines+markers',
        name='전체 유학생 수',
        line=dict(color='#275a7e', width=3),
        marker=dict(size=8, color="#275a7e"),
        hovertemplate='<b>%{x}년</b><br>전체 유학생: %{y:,.0f}명<br><i>클릭하여 선택</i><extra></extra>',
        customdata=totals_df['Year_Str']
    ))
    
    # 선택된 연도 강조표시
    selected_data = totals_df[totals_df['Year'] == current_year_int]
    if not selected_data.empty:
        fig_main.add_trace(go.Scatter(
            x=[current_year_int],
            y=[selected_data['Total_Students'].iloc[0]],
            mode='markers',
            name='선택된 연도',
            marker=dict(size=15, color='#FF6B6B', symbol='circle'),
            hovertemplate=f'<b>선택된 연도: {current_year_int}년</b><br>전체 유학생: {selected_data["Total_Students"].iloc[0]:,.0f}명<extra></extra>',
            showlegend=False
        ))
    
    fig_main.update_layout(
        title="미국 전체 유학생 수 변화 추이",
        title_font_size=18,
        hovermode='closest',
        height=500,
        showlegend=False,
        yaxis=dict(tickformat=","),
        xaxis=dict(tickmode='linear', dtick=5)
    )
    
    # 메인 그래프 표시 및 클릭 이벤트 처리
    selected_points = st.plotly_chart(
        fig_main, 
        use_container_width=True, 
        key="main_chart",
        on_select="rerun",
        config={
        'scrollZoom': False,  # 스크롤 줌 비활성화
        'doubleClick': False,  # 더블클릭 줌 비활성화
        'displayModeBar': False,  # 툴바 숨기기
        'showTips': False   # 팁 숨기기
        }
    )
    
    # 클릭 이벤트 처리
    if st.session_state.get("main_chart", {}).get("selection", {}).get("points"):
        clicked_point = st.session_state["main_chart"]["selection"]["points"][0]
        
        # 클릭된 점의 x값(연도) 가져오기
        clicked_year_int = int(clicked_point["x"])
        
        # 해당하는 Year_Str 찾기
        corresponding_year_str = totals_df[totals_df['Year'] == clicked_year_int]['Year_Str'].iloc[0]
        
        # 세션 상태 업데이트
        if corresponding_year_str != st.session_state.selected_year:
            st.session_state.selected_year = corresponding_year_str
            st.success(f"📅 {corresponding_year_str}년도가 선택되었습니다!")
            st.rerun()
    
    # 연도별 국가 비율 분석
    st.subheader("연도별 국가 비율 분석")
    
    # 선택된 연도의 국가별 데이터 가져오기 (모든 국가)
    top_countries = get_top_countries_for_year(country_df, year_columns, st.session_state.selected_year, top_n=100)
    
    if not top_countries.empty:
        total_for_year = year_totals[st.session_state.selected_year]
        
        st.info(f"📅 **{st.session_state.selected_year}년도** 총 유학생: **{total_for_year:,.0f}명**")
        
        # 국가별 비율 스택 막대 그래프 (모든 국가 표시)
        # 데이터를 올바른 형태로 변환
        bar_data = []
        for _, row in top_countries.iterrows():
            bar_data.append({
                'Category': '국가별 비율',
                'Country': row['Country'],
                'Percentage': row['Percentage'],
                'Students': row['Students']
            })
        
        bar_df = pd.DataFrame(bar_data)
        
        # 색상 팔레트 미리 정의
        color_palette = px.colors.qualitative.Set3 + px.colors.qualitative.Pastel + px.colors.qualitative.Set1
        
        # 스택 막대 그래프 생성
        fig_bar = px.bar(
            bar_df,
            x='Percentage',
            y='Category',
            color='Country',
            orientation='h',
            title=f"{st.session_state.selected_year}년도 전체 국가별 유학생 비율",
            color_discrete_sequence=color_palette
        )
        
        # 각 trace(국가)별로 개별적으로 hover 데이터 설정
        for i, trace in enumerate(fig_bar.data):
            country_data = bar_df[bar_df['Country'] == trace.name]
            if not country_data.empty:
                trace.customdata = [[country_data.iloc[0]['Country'], country_data.iloc[0]['Students']]]
                trace.hovertemplate = '<b>%{customdata[0]}</b><br>비율: %{x:.1f}%<br>학생 수: %{customdata[1]:,}명<extra></extra>'
        
        fig_bar.update_layout(
            title_font_size=16,
            xaxis_title="비율 (%)",
            yaxis_title="",
            height=200,
            showlegend=False,
            xaxis=dict(range=[0, 100])
        )
        
        st.plotly_chart(fig_bar, use_container_width=True, config={
            'scrollZoom': False,  # 스크롤 줌 비활성화
            'doubleClick': False,  # 더블클릭 줌 비활성화
            'displayModeBar': False,  # 툴바 숨기기
            'dragMode': False  # 드래그 비활성화
        })        
    
    else:
        st.warning(f"❌ {st.session_state.selected_year}년도 데이터를 찾을 수 없습니다.")

else:
    st.error("❌ 데이터를 로드할 수 없습니다. 'st_nation.xlsx' 파일이 data 폴더에 있는지 확인하세요.")

@st.cache_data
def load_data():
    # Excel 파일 읽기
    df = pd.read_excel('data/us_intstud.xlsx')
    
    # Total 행 분리
    total_row = df[df['State'] == 'Total'].iloc[0] if len(df[df['State'] == 'Total']) > 0 else None
    
    # Total 행 제외한 실제 주 데이터만 필터링
    df = df[df['State'] != 'Total'].reset_index(drop=True)
    
    # 주 이름을 주 코드로 매핑하는 딕셔너리
    state_to_code = {
        'Alabama': 'AL', 'Alaska': 'AK', 'Arizona': 'AZ', 'Arkansas': 'AR', 'California': 'CA',
        'Colorado': 'CO', 'Connecticut': 'CT', 'Delaware': 'DE', 'Florida': 'FL', 'Georgia': 'GA',
        'Hawaii': 'HI', 'Idaho': 'ID', 'Illinois': 'IL', 'Indiana': 'IN', 'Iowa': 'IA',
        'Kansas': 'KS', 'Kentucky': 'KY', 'Louisiana': 'LA', 'Maine': 'ME', 'Maryland': 'MD',
        'Massachusetts': 'MA', 'Michigan': 'MI', 'Minnesota': 'MN', 'Mississippi': 'MS', 'Missouri': 'MO',
        'Montana': 'MT', 'Nebraska': 'NE', 'Nevada': 'NV', 'New Hampshire': 'NH', 'New Jersey': 'NJ',
        'New Mexico': 'NM', 'New York': 'NY', 'North Carolina': 'NC', 'North Dakota': 'ND', 'Ohio': 'OH',
        'Oklahoma': 'OK', 'Oregon': 'OR', 'Pennsylvania': 'PA', 'Rhode Island': 'RI', 'South Carolina': 'SC',
        'South Dakota': 'SD', 'Tennessee': 'TN', 'Texas': 'TX', 'Utah': 'UT', 'Vermont': 'VT',
        'Virginia': 'VA', 'Washington': 'WA', 'West Virginia': 'WV', 'Wisconsin': 'WI', 'Wyoming': 'WY',
        'District of Columbia': 'DC'
    }
    
    # 주 코드 추가
    df['state_code'] = df['State'].map(state_to_code)
    
    # 경제적 기여도 컬럼의 문자열을 숫자로 변환
    def convert_money_string(money_str):
        if pd.isna(money_str) or money_str == 0:
            return 0
        if isinstance(money_str, str):
            # '$6.2 million' -> 6.2, '$43.8 billion' -> 43800
            money_str = money_str.replace('$', '').replace(',', '')
            if 'billion' in money_str:
                money_str = money_str.replace('billion', '').strip()
                try:
                    return float(money_str) * 1000  # billion을 million 단위로 변환
                except:
                    return 0
            elif 'million' in money_str:
                money_str = money_str.replace('million', '').strip()
                try:
                    return float(money_str)
                except:
                    return 0
        return money_str
    
    df['total_contri_numeric'] = df['total_contri'].apply(convert_money_string)
    df['comm_contri_numeric'] = df['comm_contri'].apply(convert_money_string)
    
    return df, total_row

st.write('미국 내 유학생 수는 전반적으로 꾸준한 증가세를 보여왔으며, 2020년 코로나19 팬데믹의 여파로 일시적으로 감소한 것을 제외하면 지속적인 성장 흐름을 유지하고 있습니다.' \
'연도별 변화를 살펴보면 이러한 증가세가 더욱 뚜렷하게 드러나며, 국가별로는 중국, 인도, 한국 출신 유학생의 비중이 특히 높게 나타나 미국 내 유학생 커뮤니티의 규모와 다양성을 잘 보여줍니다. 이처럼 많은 유학생들이 미국에 체류하고 있는 상황에서, 이들이 미국 사회에 어떤 영향을 미치고 있는지를 살펴보는 것은 중요한 질문입니다. 미국의 비영리 교육 단체 NAFSA(National Association of Foreign Student Advisers)의 자료에 따르면, 유학생들은 미국 경제와 학문 분야에 상당한 기여를 하고 있습니다.')

# 데이터 로드
df, total_row = load_data()

# 제목
st.subheader("미국 주별 유학생의 영향력")
st.markdown("<h5>유학생과 이민자는 창업 및 혁신을 통해 총 378,175개의 일자리를 창출하며 다양한 산업 분야에 기여하고 있습니다.<h5>", unsafe_allow_html=True)
st.markdown('---')
# 전체 통계 표시 (지도 위에)
if total_row is not None:
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric(
            label="👥 총 유학생 수", 
            value=f"{total_row['total_st']:,}명"
        )
    
    with col2:
        # Total 행의 경제적 기여도는 이미 billion 단위이므로 그대로 표시
        contrib_value = total_row['total_contri']
        st.metric(
            label="💰 총 경제적 기여도", 
            value=contrib_value
        )
    
    with col3:
        st.metric(
            label="🏢 총 일자리 창출 및 기여도", 
            value=f"{total_row['total_jobs']:,}개"
        )

st.markdown('---')
# 지도 시각화
fig_map = go.Figure(data=go.Choropleth(
    locations=df['state_code'],
    z=df['total_st'],
    locationmode='USA-states',
    colorscale='Blues',
    text=df['State'],
    hovertemplate='<b>%{text}</b><br>' +
                  '전체 유학생 수: %{z:,}명<br>' +
                  '경제적 기여도: $%{customdata[0]:.1f} million<br>' +
                  '일자리 창출: %{customdata[1]:,}개<br>' +
                  '<extra></extra>',
    customdata=list(zip(df['total_contri_numeric'], df['total_jobs'])),
    showscale=False
))

fig_map.update_layout(
    title='미국 주별 유학생 현황',
    geo_scope='usa',
    height=500,
    margin=dict(l=0, r=0, t=50, b=0),
    geo=dict(
        projection_type='albers usa',
        showframe=False,
        projection_scale=1,  # 고정된 스케일
        center=dict(lat=38, lon=-98.5),  # 미국 중심 좌표
        scope='usa',
        bgcolor='rgba(0,0,0,0)' 
    ),
    dragmode=False
)

st.plotly_chart(fig_map, use_container_width=True, config={
    'scrollZoom': False,  # 스크롤 줌 비활성화
    'doubleClick': False,  # 더블클릭 줌 비활성화
    'displayModeBar': False  # 툴바 숨기기 (선택사항)
})

# 테이블 섹션
st.write('')
# 버튼 생성
col1, col2, col3 = st.columns(3)

with col1:
    btn_students = st.button("학생 수", key="students", use_container_width=True)
with col2:
    btn_contribution = st.button("경제적 기여", key="contribution", use_container_width=True)
with col3:
    btn_jobs = st.button("일자리 창출 및 기여", key="jobs", use_container_width=True)
st.write('')
# 기본적으로 학생 수로 정렬된 테이블 표시
if 'selected_metric' not in st.session_state:
    st.session_state.selected_metric = 'students'

if btn_students:
    st.session_state.selected_metric = 'students'
elif btn_contribution:
    st.session_state.selected_metric = 'contribution'
elif btn_jobs:
    st.session_state.selected_metric = 'jobs'

# 선택된 메트릭에 따라 데이터 정렬 및 표시
if st.session_state.selected_metric == 'students':
    top_5 = df.nlargest(5, 'total_st')[['State', 'total_st']].reset_index(drop=True)
    top_5.columns = ['주', '전체 유학생 수']
    top_5['전체 유학생 수'] = top_5['전체 유학생 수'].apply(lambda x: f"{x:,}명")
    st.markdown("<h3 style='text-align: center;'>전체 유학생 수 상위 5개 주</h3>", unsafe_allow_html=True)
    
elif st.session_state.selected_metric == 'contribution':
    top_5 = df.nlargest(5, 'total_contri_numeric')[['State', 'total_contri_numeric']].reset_index(drop=True)
    top_5.columns = ['주', '경제적 기여도']
    top_5['경제적 기여도'] = top_5['경제적 기여도'].apply(lambda x: f"${x:.1f} million")
    st.markdown("<h3 style='text-align: center;'>경제적 기여도 상위 5개 주</h3>", unsafe_allow_html=True)
    
else:  # jobs
    top_5 = df.nlargest(5, 'total_jobs')[['State', 'total_jobs']].reset_index(drop=True)
    top_5.columns = ['주', '일자리 창출 및 기여']
    #top_5['일자리 창출'] = top_5['일자리 기여'].apply(lambda x: f"{x:,}개")
    st.markdown("<h3 style='text-align: center;'>일자리 창출 및 기여 상위 5개 주</h3>", unsafe_allow_html=True)

# 테이블 스타일링
st.markdown("""
<style>
.centered-table {
    margin: auto;
    text-align: center;
    width: 100% !important;
    max-width: 600px;
    border-collapse: collapse;
    border: 1px solid #ddd;
}
.centered-table th, .centered-table td {
    text-align: center !important;
    border: 1px solid #ddd;
    padding: 8px 12px;
}
.centered-table th {
    background-color: #f8f9fa;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# HTML 테이블로 표시 (가운데 정렬)
html_table = top_5.to_html(classes='centered-table', escape=False, table_id='ranking-table')
st.markdown(html_table, unsafe_allow_html=True)

st.write(' ')
st.write('최근 통계에 따르면, 미국 내 유학생 수는 약 1,126,690명에 이르며, 이들이 미국 경제에 미치는 직접적인 기여도는 438억 달러(약 43.8 billion USD)에 달합니다. 또한,유학생과 이민자는 총 378,175개의 일자리를 창출하거나 이에 기여하며, 다양한 산업 분야에서 경제적·일자리 기여를 하고 있습니다. ' \
'이러한 영향력은 주(State) 단위로도 확인할 수 있습니다. 특히 캘리포니아, 뉴욕, 매사추세츠 등 대학이 밀집된 주에서는 유학생 수는 물론, 경제적 기여도와 일자리 기여 모두 높은 수준을 보였습니다.')


st.markdown('---')
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



countries = [
    {
        "flag": "🇨🇳",
        "name": "중국",
        "balloon": "미국의 결정은 부당해!",
        "details": [
            "중국 정부는 미국의 비자 제한 조치에 대해 강하게 반발하며 자국 유학생 보호를 강조함.",
            "외교부 대변인은 미국이 중국 학생의 정당한 학업 기회를 박탈했다고 주장함."
        ]
    },
    {
        "flag": "🇭🇰",
        "name": "홍콩",
        "balloon": "꼭 우리한테 와!",
        "details": [
            "홍콩 주요 대학들, 중국 본토 학생 대상 장학금 확대 및 학비 지원 계획 발표.",
            "일부 학교는 해외 유학생 전형 요건 완화 검토 중.",
            "홍콩과학기술대학은 편입하고 싶어하는 모든 하버드대 재학생들을 받아들이겠다고 밝힘, 간소화한 편입 절차 등을 내세운 모집공고 발표. 이후 하버드생에게 편입 고려를 요청하는 편지를 보냄."
        ]
    },
    {
        "flag": "🇬🇧",
        "name": "영국",
        "balloon": "졸업 후 취업비자도 문제없어!",
        "details": [
            "영국 정부는 유학생 대상 2년 졸업 후 취업비자 제도 유지 방침 재확인.",
            "영국 대학들은 유학생 유치를 위한 온라인 설명회 개최 중."
        ]
    },
    {
        "flag": "🇰🇷",
        "name": "한국",
        "balloon": "맞춤형 지원 프로그램 준비 중이야!",
        "details": [
            "한국 대학들, 중국 유학생 대상 한국어·문화 적응 프로그램 확대 예정.",
            "일부 대학은 중국 현지 설명회 및 온라인 홍보 강화."
        ]
    },
    {
        "flag": "🇯🇵",
        "name": "일본",
        "balloon": "기숙사 지원 가능해!",
        "details": [
            "일본 대학들, 유학생 수용 확대 방안 검토.",
            "일부 대학은 신규 입학생에게 기숙사 우선 제공 계획 발표.",
            "도쿄대는 하버드생을 위한 별도 강의 개설을 통한 수용 방안 검토 중"
        ]
    }
]

st.markdown("""
    <style>
        /* 모든 컬럼 간격 통일 */
        .stColumns {
            gap: 10pt !important;
        }
        
        .stColumns > div {
            padding: 0 5pt !important;
        }
        
        /* 빈 카드 스타일 (배경색과 외부선 없음) */
        .empty-card {
            width: 100%;
            max-width: 400px;
            margin: 10px auto;
            height: 300px;
            background: transparent;
            border: none;
        }
        
        .country-card {
            width: 100%;
            max-width: 400px;
            margin: 10px auto;
            border: 1px solid #ddd;
            border-radius: 10px;
            padding: 15px;
            background-color: #f9f9f9;
            position: relative;
            min-height: 300px;
            height: auto;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }

        .country-header {
            display: flex;
            justify-content: center;
            align-items: center;
            margin-bottom: 10px;
            margin-top: -30px;
            gap: 20px;
        }
        .country-name {
            font-size: 24px;
            font-weight: bold;
            margin: 0;
            margin-top: 40px;
        }
        .country-flag {
            font-size: 100px;
        }
        .balloon {
            position: relative;
            background: #30A8F2;
            color: #FFFFFF;
            border-radius: .4em;
            padding: 10px;
            margin: -40px auto 0 auto !important;
            width: fit-content;
            max-width: 90%;
            text-align: left;
            font-weight: bold;
            font-size: 20px; 
        }
        .balloon:after {
            content: '';
            position: absolute;
            top: -10px;
            left: 10px;
            width: 0;
            height: 0;
            border: 10px solid transparent;
            border-right-color: #30A8F2;
        }
        .details {
            margin-top: 10px;
            font-size: 17px;
            color: #333;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown('---')

st.markdown("<h1>비자 정책에 대한 각국의 반응</h1>", unsafe_allow_html=True)
st.write('')
st.markdown("<h5>그렇다면 미국의 이번 비자 정책으로 가장 분주해진 곳은 어디일까요?<br>바로 미국 밖 다른 나라들입니다. 여러 국가들이 미국에서 ‘방출’되는 인재들을 유치하기 위해 분주히 움직이고 있습니다. 그렇다면 이들은 어떤 방식으로 접근하고 있을까요?</h5>", unsafe_allow_html=True)

# 첫 번째 줄: 3개 카드
cols1 = st.columns(3)
for idx in range(3):
    country = countries[idx]
    with cols1[idx]:
        st.markdown(
            f"""
            <div class='country-card'>
                <div class='country-header'>
                    <h3 class='country-name'>{country["name"]}</h3>
                    <span class='country-flag'>{country["flag"]}</span>
                </div>
                <div class='balloon'>{country["balloon"]}</div>
                <div class='details'>
                    {"<br>".join(["- " + detail for detail in country["details"]])}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

# 두 번째 줄: 3개 카드 (마지막은 빈 카드)
cols2 = st.columns(3)
for idx in range(3, 5):
    country = countries[idx]
    with cols2[idx - 3]:
        st.markdown(
            f"""
            <div class='country-card'>
                <div class='country-header'>
                    <h3 class='country-name'>{country["name"]}</h3>
                    <span class='country-flag'>{country["flag"]}</span>
                </div>
                <div class='balloon'>{country["balloon"]}</div>
                <div class='details'>
                    {"<br>".join(["- " + detail for detail in country["details"]])}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

# 세 번째 컬럼은 빈 카드 (배경색과 외부선 없음)
with cols2[2]:
    st.markdown(
        """
        <div class='empty-card'></div>
        """,
        unsafe_allow_html=True
    )
st.write('')
st.write('미국의 이번 유학생 비자 정책은 안보를 강화하려는 목적에서 추진되고 있지만, 그 부작용에 대해서는 충분히 인지하지 못하고 있는 것으로 보입니다. 단기적으로는 비자 제한을 통해 일부 우려를 해소할 수 있으나, 장기적으로는 미국 경제와 학문의 근간이 되는 우수 인재들이 다른 나라로 빠져나가면서 경쟁력이 약화될 위험이 큽니다. 실제로 홍콩, 영국, 한국, 일본 등 여러 국가들은 미국에서 방출되는 인재들을 적극적으로 유치하기 위해 맞춤형 지원 프로그램, 장학금 확대, 기숙사 지원, 취업비자 보장 등 각기 다른 방식으로 대응하고 있습니다. 결국 이번 정책은 미국 스스로 자신의 미래 성장 동력을 약화시키는 역효과를 낳을 가능성이 크다고 할 수 있습니다.')

st.markdown('---')
st.markdown('<h1>미국 비자 정책의 역설</h1>', unsafe_allow_html=True)
st.markdown('<h5>현재 트럼프의 유학생 대상 비자 정책과 유사한 정책이 과거에도 있었습니다. 2020년, 트럼프 정부는 Proclamation 10043을 통해 중국 인민해방군과 연계된 연구자 및 대학원생 약 1000명의 비자를 취소했습니다. 이는 미-중 간 기술 경쟁의 일환이자, 미국 내 첨단기술 유출을 막기 위한 조치였습니다. 그런데 이는 오히려 많은 중국인 인재들이 미국 밖으로 유출되는 결과를 초래했는데요. 이 시기와 맞물려서 중국 내 학계는 눈에 띄는 발전을 이루었습니다. 이것은 과연 우연일까요?<h5>', unsafe_allow_html=True)
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

st.write("비자 정지 정책으로 인해 중국인 학자가 중국으로 귀국하는 것은 '우수한 인재들'의 유출로 볼 수도 있습니다.실제로 미국에서 중국으로 돌아간 학자가 중국 과학 기술의 발전에 기여한 사례도 있습니다.")

st.markdown('<h3>미국이 놓친 인재 : 송춘주 교수</h3>', unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)

with col1:
    st.image("assets/ucla.gif")
    st.markdown("<h2 style='text-align: center;'>UCLA</h2>", unsafe_allow_html=True)
    st.markdown("""
        <div style="background-color: #E5DDDA; padding: 10px; border-radius: 5px; text-align: center;">
            AI&CI 연구
        </div>
    """, unsafe_allow_html=True)
with col2:
    st.image("assets/china.gif")
    st.markdown("<h2 style='text-align: center;'>China</h2>", unsafe_allow_html=True)
    st.markdown("""
        <div style="background-color: #E5DDDA; padding: 10px; border-radius: 5px; text-align: center;">
            비자 정지 정책으로 인해 귀국
        </div>
    """, unsafe_allow_html=True)
with col3:
    st.image("assets/bigai.gif")
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
                미국을 떠난 송춘주 교수님은 중국 배이징에 일반 인공지능 연구소를 설립!<br>
                이 연구소는 최근에 세계 최초 기술을 개발하는 등 중국의 기술력에 크게 기여하고 있어요.
            </b>
            <div style="content: ''; position: absolute; top: -10px; right: 20px; border-width: 0 10px 10px 10px; border-style: solid; border-color: transparent transparent #2196F3 transparent;"></div>
        </div>
    </div>
""", unsafe_allow_html=True)

st.write('송 교수님은 미국을 떠나 중국 베이징에 일반 인공지능 연구소(BIGAI)를 설립했고, 현재는 중국의 AI 기술력 향상에 크게 기여하고 계십니다. 일반 인공지능 연구소는 최근에 인간의 손 감각을 지닌 ‘로봇 손’ 개발에 성공하며 로봇 공학의 한 획을 그었습니다.')
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





st.markdown('<h3>이번 미국의 비자 제한 조치, 자충수일수도...?</h3>', unsafe_allow_html=True)
st.write("과거에는 중국을 대상으로만 한 제재이지만 지금의 비자 정책은 모든 국적의 유학생을 대상으로 하고 있습니다. 우수한 유학생들, 연구진들이 미국 밖으로 유출이 된다면 미국 내 이들의 빈 자리는 어떻게 채울 수 있을까요?")
st.write()
st.markdown("---")
st.markdown('<h4>[참고문헌]<h4>', unsafe_allow_html=True)
st.write('[1]')
st.write('[2]')
st.write('[3]')
st.write('[4]')
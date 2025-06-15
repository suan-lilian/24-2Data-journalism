import streamlit as st

# 말풍선 및 레이아웃 CSS
st.markdown("""
    <style>
        /* 기본 h1 스타일 */
        h1 {
            font-family: 'Black Han Sans', sans-serif !important;
            font-weight: 400 !important;
            font-size: 50px !important;
            margin-bottom: 0 !important;
            color: #0F3DF5 !important;
        }

        .flag {
            font-size: 100px;
            text-align: center;
        }

        .balloon {
            position: relative;
            background: #0F3DF5;
            color: #FFFFFF;
            border-radius: .4em;
            padding: 15px;
            margin: 10px 0;
            font-size: 20px;
            font-weight: bold;
            width: fit-content;
            max-width: 400px;
        }

        .balloon:after {
            content: '';
            position: absolute;
            top: 20px;
            left: -20px;
            width: 0;
            height: 0;
            border: 10px solid transparent;
            border-right-color: #0F3DF5;
        }

        .detail {
            font-size: 14px;
            color: #555;
            margin-top: 10px;
        }
    </style>
    <!-- Black Han Sans 폰트 불러오기 -->
    <link href="https://fonts.googleapis.com/css2?family=Black+Han+Sans&display=swap" rel="stylesheet">
""", unsafe_allow_html=True)

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
            "일부 학교는 해외 유학생 전형 요건 완화 검토 중."
        ]
    },
    {
        "flag": "🇬🇧",
        "name": "영국",
        "balloon": "졸업 후 취업비자도 문제없어!",
        "details": [
            "영국 정부는 유학생 대상 2년 졸업 후 취업비자 제도 유지 방침 재확인.",
            "영국 대학들은 중국 유학생 유치를 위한 온라인 설명회 개최 중."
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
            "일본 대학들, 중국 유학생 수용 확대 방안 검토.",
            "일부 대학은 신규 입학생에게 기숙사 우선 제공 계획 발표."
        ]
    }
]

st.markdown("<h1>비자 정책에 대한 각국의 반응</h1>", unsafe_allow_html=True)

for country in countries:
    col1, col2 = st.columns([1, 4])  # 국기:내용 비율

    with col1:
        st.markdown(
            f"<div class='flag'>{country['flag']}</div>",
            unsafe_allow_html=True
        )

    with col2:
        st.subheader(country["name"])
        st.markdown(
            f"<div class='balloon'>{country['balloon']}</div>",
            unsafe_allow_html=True
        )
        for detail in country["details"]:
            st.markdown(
                f"<div class='detail'>- {detail}</div>",
                unsafe_allow_html=True
            )

    st.markdown("---")  # 구분선

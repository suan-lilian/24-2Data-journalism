import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np
import plotly.express as px

# 페이지 설정
st.set_page_config(
    page_title="미국 유학생 인터랙티브 대시보드",
    page_icon="🌍",
    layout="wide"
)



# 제목
st.title("🌍 미국 유학생 현황")
st.markdown("---")

@st.cache_data
def load_country_data():
    """국가별 유학생 데이터를 로드하고 정리"""
    try:
        df = pd.read_excel('st_nation.xlsx', 
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
    st.subheader("📈 연도별 전체 미국 유학생 수 변화")
    
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
    st.subheader("🎯 연도별 국가 비율 분석")
    
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
    st.error("❌ 데이터를 로드할 수 없습니다. 'st_nation.xlsx' 파일이 같은 폴더에 있는지 확인하세요.")

@st.cache_data
def load_data():
    # Excel 파일 읽기
    df = pd.read_excel('us_intstud.xlsx')
    
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

# 데이터 로드
df, total_row = load_data()

# 제목
st.subheader("🎓 미국 주별 유학생의 영향력")
st.markdown("---")

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
            label="🏢 총 일자리 창출", 
            value=f"{total_row['total_jobs']:,}개"
        )
    
    st.markdown("---")

# 지도 생성
st.subheader("📍 미국 주별 유학생의 영향력")

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
st.markdown("---")

# 버튼 생성
col1, col2, col3 = st.columns(3)

with col1:
    btn_students = st.button("학생 수", key="students", use_container_width=True)
with col2:
    btn_contribution = st.button("경제적 기여도", key="contribution", use_container_width=True)
with col3:
    btn_jobs = st.button("일자리 기여", key="jobs", use_container_width=True)

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
    top_5.columns = ['주', '일자리 기여']
    #top_5['일자리 창출'] = top_5['일자리 기여'].apply(lambda x: f"{x:,}개")
    st.markdown("<h3 style='text-align: center;'>일자리 창출 상위 5개 주</h3>", unsafe_allow_html=True)

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
import streamlit as st
from PIL import Image
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from streamlit_lottie import st_lottie
import requests
import json
import base64
from datetime import datetime
import time

# 페이지 설정
st.set_page_config(
    page_title="김하늘 자기소개",
    page_icon="🔥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 사이드바 이미지 로드 함수 (사용자 이미지로 교체 필요)
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# CSS 스타일 적용
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
        
# 사용할 경우 CSS 파일 생성 필요
# try:
#     local_css("style.css")
# except:
#     pass

# 애니메이션 로드 함수
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Lottie 파일 로드
lottie_fire = load_lottieurl("https://lottie.host/1229648b-9fdd-4a5e-acff-f95a527be8d1/uYIcE6LSWd.json")
lottie_mma = load_lottieurl("https://lottie.host/a94a29b0-4f1f-407e-947c-5beef95711bc/ZyyLoFVHQi.json")

# 색상 테마
primary_color = "#FF5733"  # 소방서 빨간색
secondary_color = "#333333"
bg_color = "#F9F9F9"

# 배경색 설정
page_bg = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
    background-color: {bg_color};
}}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# 사이드바
with st.sidebar:
    st.title("💼 메뉴")
    st.markdown("---")
    
    menu = st.radio(
        "섹션 선택",
        ["🏠 홈", "👨‍🎓 학업 정보", "🔥 소방 관련 지식", "🎯 미래 계획", "📊 역량 분석"]
    )
    
    st.markdown("---")
    st.markdown("### 📮 연락처")
    st.info("📧 이메일: example@student.konyang.ac.kr")
    st.info("📱 전화번호: 010-XXXX-XXXX")
    
    with st.expander("📅 현재 시간"):
        now = datetime.now()
        st.write(f"📆 {now.strftime('%Y년 %m월 %d일')}")
        st.write(f"🕒 {now.strftime('%H시 %M분 %S초')}")
        if st.button("새로고침"):
            st.experimental_rerun()

# 홈 페이지
if menu == "🏠 홈":
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.image("https://cdn-icons-png.flaticon.com/512/4264/4264699.png", width=200)
        st.markdown("### 김하늘")
        st.markdown("**건양대학교 재난안전소방학과**")
        st.markdown("**3학년 재학중**")
        
        # 소셜 미디어 버튼
        col_sns1, col_sns2, col_sns3 = st.columns(3)
        with col_sns1:
            st.markdown("[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com)")
        with col_sns2:
            st.markdown("[![Instagram](https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://instagram.com)")
        with col_sns3:
            st.markdown("[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com)")
    
    with col2:
        st.markdown("""
        # 안녕하세요, 김하늘입니다! 👋
        
        ## 🔥 소방의 꿈을 향해 달려가는 재난안전소방학도
        
        저는 **건양대학교 재난안전소방학과 3학년** 학생으로, 미래의 소방관을 꿈꾸고 있습니다. 
        재난 상황에서 시민의 안전을 지키고 위기 상황을 효과적으로 관리하는 전문가가 되기 위해
        이론과 실무를 배우며 준비하고 있습니다.
        
        ### 📚 관심 분야
        - 화재 예방 및 안전 교육
        - 재난 대응 시스템
        - 응급 구조 기술
        - 소방 장비 기술 발전
        
        ### 💪 취미: 운동
        소방관의 체력은 매우 중요합니다. 저는 운동을 통해 체력을 단련하고 
        위기 상황에서의 판단력과 대응 능력을 키우고 있습니다.
        """)
        
# 학업 정보 페이지
elif menu == "👨‍🎓 학업 정보":
    st.title("👨‍🎓 학업 정보")
    st.markdown("---")
    
    st.markdown("""
    ## 건양대학교 재난안전소방학과
    
    재난안전소방학과에서는 화재 예방, 진압, 구조, 구급 등 소방의 전반적인 업무 수행을 위한 전문 지식과 기술을 배웁니다.
    또한 각종 재난 발생 시 인명 구조와 재산 피해를 최소화할 수 있는 현장 중심의 이론 교육과 실습을 병행하고 있습니다.
    """)
    
    # 학년별 커리큘럼
    st.subheader("📚 학년별 주요 커리큘럼")
    
    tab1, tab2, tab3, tab4 = st.tabs(["1학년", "2학년", "3학년", "4학년"])
    
    with tab1:
        st.markdown("""
        ### 1학년 주요 과목
        
        - **소방학개론**: 소방의 기초 이론과 개념 학습
        - **재난관리론**: 재난의 유형과 관리 시스템에 대한 이해
        - **일반화학**: 화학 반응과 물질의 성질에 대한 기초 지식
        - **소방 관련 법규**: 소방 법령과 규정에 대한 이해
        - **안전 공학 개론**: 안전에 대한 공학적 접근 방식 학습
        """)
        
    with tab2:
        st.markdown("""
        ### 2학년 주요 과목
        
        - **화재역학**: 화재 발생과 확산에 대한 과학적 이해
        - **소방전기시설론**: 소방 관련 전기 시스템 이해
        - **소방유체역학**: 소화 설비에 필요한 유체역학 이론
        - **위험물질론**: 다양한 위험물질의 특성과 취급 방법
        - **구조 및 구급론**: 인명 구조와 응급처치 이론 및 실습
        """)
        
    with tab3:
        st.markdown("""
        ### 3학년 주요 과목
        
        - **소방시설설계론**: 소방 시설의 설계 방법과 기준
        - **화재조사론**: 화재 원인 조사 및 분석 방법
        - **소방전술론**: 화재 진압 및 대응 전술
        - **재난심리학**: 재난 상황에서의 심리적 대응과 관리
        - **소방행정학**: 소방 조직 및 행정 시스템 이해
        """)
        
    with tab4:
        st.markdown("""
        ### 4학년 주요 과목
        
        - **소방 종합 설계**: 소방 시스템 종합 설계 프로젝트
        - **재난 시뮬레이션**: 컴퓨터를 활용한 재난 상황 분석
        - **현장 실습**: 소방서 및 관련 기관 현장 실습
        - **소방공무원 실무**: 소방공무원 시험 대비 및 실무 교육
        - **졸업 논문**: 소방 분야 연구 논문 작성
        """)
    
    # 대표 과목 성적
    st.subheader("📊 주요 과목 성적")
    
    # 성적 데이터 (예시)
    grades_data = {
        '과목명': ['소방학개론', '재난관리론', '화재역학', '소방전기시설론', '구조 및 구급론', 
                 '화재조사론', '소방전술론', '재난심리학'],
        '학년/학기': ['1-1', '1-2', '2-1', '2-2', '2-2', '3-1', '3-1', '3-1'],
        '성적': ['A+', 'A0', 'B+', 'A+', 'A0', 'B+', 'A0', 'A+'],
        '성적점수': [4.5, 4.0, 3.5, 4.5, 4.0, 3.5, 4.0, 4.5]
    }
    
    grades_df = pd.DataFrame(grades_data)
    
    col_grade1, col_grade2 = st.columns([2, 3])
    
    with col_grade1:
        st.dataframe(grades_df, use_container_width=True)
    
    with col_grade2:
        fig = px.bar(
            grades_df, 
            x='과목명', 
            y='성적점수',
            color='성적점수',
            color_continuous_scale='reds',
            title='주요 과목별 성적',
            labels={'성적점수': '점수 (4.5 만점)', '과목명': '과목명'}
        )
        st.plotly_chart(fig, use_container_width=True)
    
    # 학업 활동
    st.subheader("🏫 학업 관련 활동")
    
    col_act1, col_act2 = st.columns(2)
    
    with col_act1:
        st.markdown("""
        ### 소방 관련 소모임
        
        - **화재 분석 스터디**: 다양한 화재 사례를 분석하고 토론하는 소규모 스터디 그룹에서 활동했습니다.
        - **소방 장비 연구 모임**: 최신 소방 장비의 동향과 기술을 연구하고 공유하는 모임에 참여했습니다.
        - **응급처치 실습 모임**: 기본적인 응급처치 기술을 익히고 실습하는 모임에 정기적으로 참여했습니다.
        """)
    
    with col_act2:
        st.markdown("""
        ### 소방 관련 컨퍼런스 및 세미나 참석
        
        - **전국 대학생 소방 학술제**: 대학생들의 소방 관련 연구를 공유하는 학술제에 참관했습니다.
        - **재난 안전 기술 포럼**: 최신 재난 안전 기술에 대한 포럼에 참석하여 지식을 넓혔습니다.
        - **소방 장비 전시회**: 최신 소방 장비와 기술을 소개하는 전시회에 참관했습니다.
        """)
    
    # 학업 목표
    st.subheader("🎯 학업 목표")
    
    st.markdown("""
    ### 단기 목표 (1년 이내)
    
    - 소방 관련 자격증 2개 이상 취득 (소방설비기사, 위험물 기능사 등)
    - 전공 과목 평점 3.5 이상 유지
    - 소방 관련 봉사활동 참여 (20시간 이상)
    
    ### 중장기 목표
    
    - 소방공무원 시험 합격을 위한 전문 지식 습득
    - 소방 관련 학술 대회 참여 및 논문 발표
    - 응급구조사 자격증 취득
    """)

# 소방 관련 지식 페이지
elif menu == "🔥 소방 관련 지식":
    st.title("🔥 소방 관련 지식")
    st.markdown("---")
    
    st.markdown("""
    ## 소방직 공무원을 향한 전문 지식
    
    소방관이 되기 위해서는 화재 진압 기술뿐만 아니라 안전 관리, 구조 활동, 응급 처치, 
    재난 대응 등 다양한 분야의 전문 지식이 필요합니다. 이 페이지에서는 제가 학습하고 있는
    소방 관련 주요 지식을 정리했습니다.
    """)
    
    # 소방 분야 지식
    knowledge_tab1, knowledge_tab2, knowledge_tab3, knowledge_tab4 = st.tabs(
        ["화재 예방 및 진압", "구조 및 구급", "소방 법규", "재난 관리"]
    )
    
    with knowledge_tab1:
        st.subheader("🔥 화재 예방 및 진압")
        
        st.markdown("""
        ### 화재의 이해
        
        화재는 연소의 3요소(연료, 산소, 열)가 적절히 결합했을 때 발생합니다. 화재 진압은 이 3요소 중 하나 이상을 제거하는 
        방식으로 이루어집니다.
        
        #### 화재의 종류
        
        | 분류 | 종류 | 특성 | 소화 방법 |
        |------|------|------|------|
        | A급 화재 | 일반 화재 | 나무, 종이, 직물 등 일반 가연물 화재 | 물, 포말소화기 |
        | B급 화재 | 유류 화재 | 가연성 액체, 가스 등의 화재 | 분말, 이산화탄소, 포말소화기 |
        | C급 화재 | 전기 화재 | 전기 설비, 장치 등의 화재 | 이산화탄소, 할론소화기 |
        | D급 화재 | 금속 화재 | 마그네슘, 나트륨 등 금속 화재 | 분말소화기, 마른모래 |
        | K급 화재 | 주방 화재 | 식용유, 동물성지방 등의 화재 | 습식화학소화기 |
        
        ### 화재 진압 기술
        
        화재 진압은 화재의 종류와 상황에 따라 적절한 소화약제와 방법을 선택하는 것이 중요합니다.
        
        1. **직접 공격법**: 화재 원점을 직접 공격하는 방법
        2. **간접 공격법**: 직접 접근이 어려울 때 천장이나 벽을 통해 간접적으로 소화
        3. **입체 공격법**: 여러 방향에서 동시에 진압하는 방법
        4. **진압 철수법**: 위험 상황에서 안전하게 철수하는 방법
        
        ### 화재 예방
        
        화재 예방은 화재 발생을 미리 방지하는 활동으로, 다음과 같은 방법이 있습니다.
        
        - 정기적인 전기 설비 점검
        - 가연물 관리와 적절한 보관
        - 화재 감지 시스템 설치 및 관리
        - 소방 시설 정기 점검 및 유지 보수
        - 화재 예방 교육 및 훈련 실시
        """)
    
    with knowledge_tab2:
        st.subheader("🚑 구조 및 구급")
        
        st.markdown("""
        ### 인명 구조 기술
        
        재난 상황에서 인명을 구조하는 기술은 소방관의 핵심 역량입니다.
        
        #### 주요 구조 기술
        
        1. **로프 구조 기술**: 고층 건물이나 절벽 등에서의 구조
        2. **수난 구조 기술**: 물에 빠진 사람을 구조하는 기술
        3. **붕괴 구조 기술**: 건물 붕괴 현장에서의 구조 활동
        4. **산악 구조 기술**: 산악 지형에서의 인명 구조
        5. **밀폐 공간 구조**: 좁은 공간에 갇힌 사람 구조
        
        ### 응급 처치
        
        소방관은 전문적인 응급 처치 기술을 통해 생명을 구합니다.
        
        #### 기본 응급 처치
        
        - **심폐소생술(CPR)**: 심장 정지 상황에서의 응급 처치
        - **자동제세동기(AED) 사용법**: 심장 리듬 회복을 위한 장비 사용
        - **기도 확보 방법**: 호흡 곤란 상황에서의 응급 조치
        - **지혈 및 상처 처치**: 외상 환자 처치
        - **골절 처치**: 골절 환자의 응급 처치
        
        ### 구급 장비
        
        효과적인 응급 처치를 위해 다양한 구급 장비를 숙지해야 합니다.
        
        - 구급함과 기본 의료 용품
        - 들것 및 환자 이송 장비
        - 목 보호대와 척추 보호 장비
        - 산소 공급 장치
        - 자동제세동기(AED)
        """)
    
    with knowledge_tab3:
        st.subheader("📜 소방 법규")
        
        st.markdown("""
        ### 소방 관련 법규 체계
        
        소방 활동은 다양한 법규와 규정에 의해 관리됩니다.
        
        #### 주요 소방 법규
        
        1. **소방기본법**: 소방의 기본적인 사항을 규정한 법률
        2. **화재예방, 소방시설 설치·유지 및 안전관리에 관한 법률**: 소방시설 관련 법규
        3. **위험물안전관리법**: 위험물 취급과 관리에 관한 법률
        4. **다중이용업소의 안전관리에 관한 특별법**: 다중이용시설 안전 관리 규정
        5. **소방시설공사업법**: 소방시설 공사에 관한 법률
        
        ### 소방 점검과 검사
        
        법규에 따른 소방 점검과 검사의 종류와 주기:
        
        | 점검 종류 | 대상 | 주기 | 점검자 |
        |-----------|------|------|--------|
        | 자체점검 | 모든 특정소방대상물 | 매월 | 관계인 |
        | 정기점검 | 일정 규모 이상 건축물 | 연 1~2회 | 소방시설관리업자 |
        | 특별점검 | 다중이용시설 등 | 필요시 | 소방공무원 |
        | 종합정밀점검 | 대형 건축물 | 연 1회 | 소방시설관리업자 |
        
        ### 소방공무원 관련 법령
        
        소방공무원의 직무와 권한, 의무 등을 규정한 법령:
        
        - 소방공무원법
        - 소방공무원 임용령
        - 소방공무원 징계령
        - 소방공무원 복무규정
        """)
    
    with knowledge_tab4:
        st.subheader("🌪 재난 관리")
        
        st.markdown("""
        ### 재난의 이해
        
        재난은 자연재난과 사회재난으로 구분됩니다.
        
        #### 재난의 종류
        
        **자연재난**:
        - 지진, 태풍, 홍수, 폭설 등 자연현상으로 인한 재난
        
        **사회재난**:
        - 화재, 붕괴, 폭발, 교통사고, 환경오염 등 인위적 요인에 의한 재난
        
        ### 재난 관리 시스템
        
        재난 관리는 예방-대비-대응-복구의 4단계로 구성됩니다.
        
        1. **예방 단계**: 재난 발생을 막기 위한 활동
           - 위험요소 제거
           - 안전 시설 보강
           - 안전 문화 확산
           
        2. **대비 단계**: 재난 발생에 대비한 준비
           - 재난 훈련 실시
           - 장비 및 인력 확보
           - 대응 매뉴얼 개발
           
        3. **대응 단계**: 재난 발생 시 즉각적인 조치
           - 초기 대응 및 현장 통제
           - 인명 구조 및 대피
           - 긴급 구호 활동
           
        4. **복구 단계**: 재난 이후 정상화 활동
           - 피해 조사 및 복구 계획
           - 시설 복구 및 재건
           - 심리적 회복 지원
        
        ### 재난 대응 체계
        
        효과적인 재난 대응을 위한 국가 및 지역 체계:
        
        - 중앙재난안전대책본부
        - 지역재난안전대책본부
        - 소방재난본부
        - 긴급구조통제단
        - 재난현장지휘체계(ICS)
        """)
    
    # 소방 자격증
    st.subheader("📋 소방 관련 자격증")
    
    cert_col1, cert_col2 = st.columns(2)
    
    with cert_col1:
        st.markdown("""
        ### 취득 예정 자격증
        
        1. **소방설비기사(전기)**
           - 소방전기시설의 설계, 시공, 감리, 점검 등에 필요한 자격증
           - 필기: 소방관계법규, 전기공학, 소방전기시설의 구조원리 등
           - 실기: 소방전기시설 설계 및 시공
        
        2. **소방설비기사(기계)**
           - 소방기계시설의 설계, 시공, 감리, 점검 등에 필요한 자격증
           - 필기: 소방관계법규, 유체역학, 소방기계시설의 구조원리 등
           - 실기: 소방기계시설 설계 및 시공
        3. **위험물취급기능사**
           - 위험물의 취급, 저장, 관리에 필요한 자격증
           - 필기: 위험물 관련 법규, 위험물의 성질과 취급
           - 실기: 위험물 취급 실무
        
        4. **응급구조사 2급**
           - 응급환자에 대한 응급처치 및 이송에 필요한 자격증
           - 필기: 응급환자 평가 및 응급처치, 응급의료 관련 법규
           - 실기: 기본 응급처치 술기
        """)
    
    with cert_col2:
        st.markdown("""
        ### 자격증 취득 계획
        
        | 자격증명 | 응시 예정 시기 | 준비 상태 |
        |----------|----------------|----------|
        | 소방설비기사(전기) | 2025년 상반기 | 기초 이론 학습 중 |
        | 위험물취급기능사 | 2025년 하반기 | 준비 예정 |
        | 소방설비기사(기계) | 2026년 상반기 | 준비 예정 |
        | 응급구조사 2급 | 2026년 하반기 | 준비 예정 |
        
        ### 학습 자료
        
        - 소방설비기사 수험서
        - 위험물 관리론 교재
        - 온라인 소방 관련 강의
        - 소방 관련 법규집
        - 응급구조 실습 교재
        """)
    
    # 소방공무원 시험 정보
    st.subheader("📝 소방공무원 시험 정보")
    
    st.markdown("""
    ### 소방공무원 시험 과목
    
    **1차 시험 (필기)**:
    - 국어
    - 영어
    - 한국사
    - 소방학개론
    - 소방관계법규
    
    **2차 시험 (체력)**:
    - 악력
    - 배근력
    - 앉아 윗몸 앞으로 굽히기
    - 제자리 멀리뛰기
    - 왕복 오래 달리기
    
    **3차 시험 (신체/면접)**:
    - 신체검사
    - 인·적성 검사
    - 면접시험
    """)
    
    # 소방 장비 지식
    st.subheader("🧯 소방 장비 지식")
    
    equipment_tab1, equipment_tab2 = st.tabs(["개인 보호장비", "소방 활동 장비"])
    
    with equipment_tab1:
        st.markdown("""
        ### 소방관 개인 보호장비(PPE)
        
        소방관의 안전을 지키는 필수 장비입니다.
        
        1. **방화복(Turn-out Gear)**
           - 화재 현장에서 고열과 화염으로부터 소방관을 보호
           - 내열성, 내수성 소재로 제작
           
        2. **공기호흡기(SCBA)**
           - 유해가스와 연기로부터 호흡기를 보호
           - 약 30-45분 사용 가능한 압축공기 탱크 포함
           
        3. **헬멧(Helmet)**
           - 낙하물 및 충격으로부터 머리 보호
           - 일부 모델은 조명, 통신 장비 장착 가능
           
        4. **장갑(Gloves)**
           - 열, 절단, 찢어짐으로부터 손 보호
           - 움직임을 방해하지 않는 디자인
           
        5. **안전화(Safety Boots)**
           - 열, 물, 날카로운 물체로부터 발 보호
           - 미끄럼 방지 기능 포함
        """)
    
    with equipment_tab2:
        st.markdown("""
        ### 소방 활동 장비
        
        화재 진압 및 구조 활동에 사용되는 장비들입니다.
        
        1. **소방 호스 및 노즐**
           - 화재 진압에 사용되는 기본 장비
           - 다양한 크기와 용도별 노즐 사용
           
        2. **사다리**
           - 고층 구조 및 진입에 사용
           - 고정식, 이동식, 굴절식 등 다양한 종류
           
        3. **유압 장비**
           - 구조용 스프레더, 커터, 램 등
           - 교통사고 구조 등에 활용
           
        4. **열화상 카메라**
           - 연기 속에서 열원과 요구조자 탐색
           - 잔불 확인 등에 활용
           
        5. **소방 펌프**
           - 물을 압송하는 장비
           - 고정식 또는 이동식으로 사용
        """)
        
    # 소방 기술 트렌드
    st.subheader("🔬 소방 기술 트렌드")
    
    st.markdown("""
    ### 최신 소방 기술 동향
    
    소방 분야에서도 첨단 기술의 도입이 활발해지고 있습니다.
    
    1. **드론을 활용한 화재 진압 및 구조**
       - 화재 현장 정찰 및 상황 파악
       - 위험 지역 접근이 어려운 곳에서 활용
       
    2. **AI 기반 화재 예측 시스템**
       - 빅데이터 분석을 통한 화재 위험 예측
       - 효율적인 소방력 배치에 활용
       
    3. **스마트 소방 장비**
       - IoT 기반 소방 시설 원격 모니터링
       - 웨어러블 장비를 통한 소방관 안전 관리
       
    4. **친환경 소화약제**
       - 환경 오염을 최소화하는 소화약제 개발
       - 오존층 파괴 물질 대체 약제 연구
       
    5. **가상현실(VR) 훈련 시스템**
       - 실제 화재 상황을 모사한 훈련 환경
       - 다양한 재난 상황 시뮬레이션을 통한 대응 훈련
    """)


# 미래 계획 페이지
elif menu == "🎯 미래 계획":
    st.title("🎯 미래 계획")
    st.markdown("---")
    
    st.markdown("""
    ## 소방관의 길을 향한 여정
    
    소방관이 되어 시민의 안전과 생명을 지키는 것이 저의 궁극적인 목표입니다.
    이를 위한 단계별 계획을 수립했습니다.
    """)
    
    # 타임라인 구성
    st.subheader("⏱️ 소방관 진로 타임라인")
    
    timeline_data = {
        '기간': ['2024-2025', '2025-2026', '2026-2027', '2027 이후'],
        '단계': ['대학 학습 및 기초 역량 강화', '소방공무원 시험 준비', '소방공무원 시험 및 임용', '소방관 경력 개발'],
        '주요 계획': [
            '- 전공 과목 성적 향상\n- 소방 관련 자격증 기초 취득\n- 체력 단련 및 격투기 훈련 지속',
            '- 소방공무원 시험 과목 집중 학습\n- 주요 자격증 취득 완료\n- 체력 시험 기준 통과 준비',
            '- 소방공무원 시험 응시\n- 면접 및 체력 시험 대비\n- 임용 후 초기 적응 훈련',
            '- 현장 경험 축적\n- 전문 분야 개발\n- 추가 역량 강화'
        ]
    }
    
    timeline_df = pd.DataFrame(timeline_data)
    
    # 타임라인 시각화
    fig = go.Figure()
    
    for i, row in timeline_df.iterrows():
        fig.add_trace(go.Scatter(
            x=[i, i],
            y=[0, 1],
            mode='lines',
            line=dict(color='#FF5733', width=10),
            showlegend=False
        ))
        
        fig.add_trace(go.Scatter(
            x=[i],
            y=[1],
            mode='markers',
            marker=dict(size=20, color='#FF5733', symbol='circle'),
            showlegend=False
        ))
        
        fig.add_annotation(
            x=i,
            y=1.1,
            text=row['기간'],
            showarrow=False,
            font=dict(size=14, color='#333333')
        )
        
        fig.add_annotation(
            x=i,
            y=0.8,
            text=row['단계'],
            showarrow=False,
            font=dict(size=12, color='#333333', family='Arial')
        )
    
    fig.update_layout(
        height=200,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        yaxis=dict(
            showgrid=False,
            zeroline=False,
            showticklabels=False,
            range=[-0.1, 1.3]
        ),
        xaxis=dict(
            showgrid=False,
            zeroline=False,
            showticklabels=False,
            range=[-0.5, len(timeline_df)-0.5]
        ),
        margin=dict(l=20, r=20, t=80, b=20)
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    for i, row in timeline_df.iterrows():
        st.subheader(f"{row['기간']}: {row['단계']}")
        st.markdown(row['주요 계획'])
        st.markdown("---")
    
    # 소방공무원 임용 후 계획
    st.subheader("🚒 소방공무원 임용 후 계획")
    
    career_tab1, career_tab2 = st.tabs(["단기 계획 (1-5년)", "장기 계획 (5-10년)"])
    
    with career_tab1:
        st.markdown("""
        ### 임용 초기 적응 (1-2년)
        
        - 다양한 현장 경험 축적
        - 선임 소방관의 지도 적극 수용
        - 실제 현장에서의 소방 장비 활용 능력 향상
        - 팀워크 및 조직 문화 적응
        
        ### 전문성 개발 (3-5년)
        
        - 특수 구조 대응팀 자격 취득
        - 화재조사 전문 교육 이수
        - 응급구조사 1급 자격 취득
        - 고층 구조, 수난 구조 등 전문 분야 훈련
        """)
    
    with career_tab2:
        st.markdown("""
        ### 전문가 단계 (5-7년)
        
        - 소방 전문 교육 과정 이수
        - 후임 소방관 훈련 및 멘토링
        - 특수 재난 대응 팀 참여
        - 해외 선진 소방 기술 연수
        
        ### 리더십 개발 (7-10년)
        
        - 소방 지휘 과정 이수
        - 소방 행정 역량 강화
        - 재난 관리 전문가 자격 취득
        - 지역 사회 소방 안전 교육 프로그램 개발 및 참여
        """)
    
    # 소방관 이외의 대안 계획
    st.subheader("🔄 대안 진로 계획")
    
    alternative_col1, alternative_col2 = st.columns(2)
    
    with alternative_col1:
        st.markdown("""
        ### 민간 소방 분야
        
        소방공무원이 아닌 민간 소방 분야에서도 전문성을 발휘할 수 있습니다.
        
        - **소방 시설 관리자**
          - 대형 건물이나 시설의 소방 안전 관리
          - 소방 시설 점검 및 유지보수
          
        - **소방 설비 기술자**
          - 소방 시설 설계 및 시공
          - 소방 장비 개발 및 유지보수
          
        - **소방 안전 교육 강사**
          - 기업 및 기관 소방 안전 교육
          - 대피 훈련 및 소화기 사용법 교육
        """)
    
    with alternative_col2:
        st.markdown("""
        ### 재난 안전 관련 분야
        
        재난 안전 전공을 살려 다른 분야로의 진출도 고려할 수 있습니다.
        
        - **재난 안전 컨설턴트**
          - 기업 및 기관의 재난 관리 체계 컨설팅
          - 안전 계획 수립 및 위험 평가
          
        - **산업 안전 관리자**
          - 산업 현장의 안전 관리
          - 사고 예방 및 안전 교육
          
        - **응급 구조사**
          - 병원 전 응급 처치
          - 재난 현장 의료 지원
        """)
    
    # 마무리 메시지
    st.markdown("---")
    st.markdown("""
    ## 미래를 향한 다짐
    
    소방관이라는 직업은 단순한 일자리가 아닌 사명입니다. 시민의 생명과 재산을 지키는 
    소방관으로서 항상 배우고 성장하며, 최고의 전문성과 인성을 갖추기 위해 노력하겠습니다.
    
    위기 상황에서 누군가에게 희망이 되고, 안전한 사회를 만드는 데 기여하는 소방관이 되는 것이
    저의 삶의 목표입니다. 이를 위해 대학 생활 동안 필요한 지식과 기술을 착실히 쌓아가겠습니다.
    """)


    st.markdown("""
    ## 소방관 필요 역량 분석
    
    소방관으로서 성공하기 위해 필요한 다양한 역량과 현재 저의 수준을 분석했습니다.
    지속적인 개발이 필요한 영역을 파악하고 체계적으로 준비하고 있습니다.
    """)
    
    # 역량 레이더 차트
    st.subheader("📊 역량 자가 평가")
    
    skills = ['체력', '소방 전문지식', '응급처치 기술', '의사소통 능력', 
              '문제해결 능력', '팀워크', '스트레스 관리', '장비 활용 능력']
    
    current_skills = [7, 6, 5, 7, 6, 8, 7, 5]  # 현재 역량 수준 (1-10)
    target_skills = [9, 9, 8, 8, 8, 9, 8, 8]   # 목표 역량 수준 (1-10)
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatterpolar(
        r=current_skills,
        theta=skills,
        fill='toself',
        name='현재 역량',
        line_color='#FF5733',
        fillcolor='rgba(255, 87, 51, 0.3)'
    ))
    
    fig.add_trace(go.Scatterpolar(
        r=target_skills,
        theta=skills,
        fill='toself',
        name='목표 역량',
        line_color='#3366FF',
        fillcolor='rgba(51, 102, 255, 0.3)'
    ))
    
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 10]
            )
        ),
        showlegend=True,
        height=500
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # 역량 상세 설명
    st.subheader("💪 역량 개발 계획")
    
    skills_data = {
        '역량 분야': ['체력', '소방 전문지식', '응급처치 기술', '의사소통 능력', '문제해결 능력', '팀워크', '스트레스 관리', '장비 활용 능력'],
        '현재 수준': ['격투기 훈련 중, 기본 체력 양호', '학과 수업 통한 기초 지식 보유', '기본적인 응급처치 지식 보유', '원활한 소통 가능', '논리적 문제 해결 가능', '팀 프로젝트 경험 다수', '격투기 통한 스트레스 관리', '기본 장비 사용법 숙지'],
        '개발 계획': ['소방 특화 체력 훈련 강화', '전공 심화 학습 및 자격증 취득', '응급구조사 자격증 준비', '위기 상황 커뮤니케이션 훈련', '화재 시나리오 대응 훈련', '팀 훈련 참여 확대', '고강도 훈련 상황 경험', '다양한 소방 장비 실습']
    }
    
    skills_df = pd.DataFrame(skills_data)
    
    for i in range(len(skills_df)):
        with st.expander(f"{skills_df.iloc[i]['역량 분야']}"):
            col1, col2 = st.columns(2)
            with col1:
                st.markdown("#### 현재 수준")
                st.markdown(skills_df.iloc[i]['현재 수준'])
            with col2:
                st.markdown("#### 개발 계획")
                st.markdown(skills_df.iloc[i]['개발 계획'])
    
    # 소방공무원 채용 적합성 분석
    st.subheader("🎯 소방공무원 채용 적합성 분석")
    
    col_fit1, col_fit2 = st.columns(2)
    
    with col_fit1:
        st.markdown("""
        ### 강점
        
        - **체력 우수성**: 격투기 훈련을 통한 신체 능력
        - **위기 대응 능력**: 격투기에서 배운 순간 판단력
        - **인내심**: 지속적인 훈련을 통해 개발된 정신력
        - **팀워크**: 단체 훈련을 통한 협동 정신
        - **학습 의지**: 소방관련 지식 습득 열정
        """)
    
    with col_fit2:
        st.markdown("""
        ### 개발 필요 영역
        
        - **전문 지식 심화**: 전공 과목 심층 학습 필요
        - **소방 장비 활용 능력**: 실제 장비 사용 경험 확대
        - **응급 처치 기술**: 전문적인 응급처치 기술 습득
        - **법규 이해도**: 소방 관련 법규 심층 학습
        - **행정 능력**: 소방 행정 및 보고서 작성 능력
        """)
    
    # 소방공무원 시험 대비 현황
    st.subheader("📝 소방공무원 시험 대비 현황")
    
    exam_data = {
        '시험 과목': ['국어', '영어', '한국사', '소방학개론', '소방관계법규'],
        '준비 상태 (%)': [70, 65, 60, 75, 55],
        '목표 달성율 (%)': [70, 65, 60, 75, 55]
    }
    
    exam_df = pd.DataFrame(exam_data)
    
    fig = px.bar(
        exam_df, 
        x='시험 과목', 
        y='준비 상태 (%)',
        color='준비 상태 (%)',
        color_continuous_scale='reds',
        title='소방공무원 시험 과목별 준비 상태',
        text='준비 상태 (%)'
    )
    
    fig.update_traces(texttemplate='%{text}%', textposition='outside')
    
    st.plotly_chart(fig, use_container_width=True)
    
    # 체력 시험 대비 현황
    st.subheader("💪 소방공무원 체력 시험 대비 현황")
    
    fitness_data = {
        '체력 항목': ['악력', '배근력', '앉아윗몸앞으로굽히기', '제자리멀리뛰기', '윗몸일으키기', '왕복오래달리기'],
        '현재 기록': ['58kg', '150kg', '13cm', '235cm', '46회/분', '64회'],
        '목표 기록': ['60kg', '160kg', '15cm', '240cm', '50회/분', '70회'],
        '달성율': [96, 94, 87, 98, 92, 91]
    }
    
    fitness_df = pd.DataFrame(fitness_data)
    
    fig = px.line(
        fitness_df, 
        x='체력 항목', 
        y='달성율',
        markers=True,
        line_shape='spline',
        title='체력 시험 항목별 목표 달성율 (%)'
    )
    
    fig.update_traces(line=dict(color='#FF5733', width=4), marker=dict(size=12, color='#FF5733'))
    fig.update_layout(yaxis_range=[80, 100])
    
    st.plotly_chart(fig, use_container_width=True)
    
    # 자기 개발 계획
    st.subheader("📈 자기 개발 계획")
    
    development_data = {
        '개발 영역': ['소방 전문 지식', '체력 단련', '자격증 취득', '실무 경험', '소통 능력'],
        '중요도': [5, 5, 4, 3, 4],
        '현재 수준': [3, 4, 2, 1, 3],
        '목표 수준': [5, 5, 5, 4, 4],
        '우선순위': [1, 2, 3, 4, 5]
    }
    
    development_df = pd.DataFrame(development_data)
    
    fig = px.scatter(
        development_df,
        x='중요도',
        y='현재 수준',
        size='우선순위',
        size_max=15,
        color='개발 영역',
        labels={'중요도': '중요도 (1-5)', '현재 수준': '현재 수준 (1-5)'},
        title='개발 영역별 현재 수준과 중요도 분석'
    )
    
    fig.update_layout(
        xaxis_range=[0, 6],
        yaxis_range=[0, 6],
        xaxis=dict(tickvals=[1, 2, 3, 4, 5]),
        yaxis=dict(tickvals=[1, 2, 3, 4, 5])
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # 전공 지식 심화 계획
    st.markdown("### 🎓 전공 지식 심화 계획")
    
    knowledge_plan = {
        '학습 영역': ['화재 역학', '소방 시설', '위험물 관리', '재난 관리', '구조 구급'],
        '우선순위': [1, 2, 3, 4, 5],
        '학습 방법': ['전공 심화 수업, 관련 도서 학습', '소방 시설 견학, 도면 분석 연습', '위험물 관련 자격증 준비, 실험실 연습', '재난 사례 분석, 관련 세미나 참석', '응급구조 실습, 관련 자격증 준비'],
        '목표 성과': ['화재 현상 이해도 향상', '소방 시설 설계 및 점검 능력 향상', '위험물 특성 및 대응 방법 숙지', '재난 유형별 대응 전략 수립', '기본 응급처치 능력 향상']
    }
    
    knowledge_df = pd.DataFrame(knowledge_plan)
    
    st.table(knowledge_df)

# 메인 푸터
st.markdown("---")

footer_col1, footer_col2, footer_col3 = st.columns([1, 2, 1])

with footer_col1:
    st.markdown("### 김하늘")
    st.markdown("건양대학교 재난안전소방학과")
    st.markdown("3학년 재학중")
    
with footer_col2:
    st.markdown("### 연락처")
    st.markdown("📧 이메일: example@student.konyang.ac.kr")
    st.markdown("📱 전화번호: 010-XXXX-XXXX")
    st.markdown("🏫 학교: 건양대학교")
    
with footer_col3:
    st.markdown("### 소셜 미디어")
    st.markdown("[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com)")
    st.markdown("[![Instagram](https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://instagram.com)")
    st.markdown("[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com)")


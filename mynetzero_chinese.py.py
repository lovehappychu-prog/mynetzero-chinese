import streamlit as st
import plotly.graph_objects as go
import numpy as np
import pandas as pd
import requests

# =========================
# NATION DATA
# =========================

nation_data = pd.read_excel("網路APP檔案.xlsx")

countries = sorted(
    nation_data["Country"]
    .dropna()
    .astype(str)
    .str.strip()
    .tolist()
)

# =========================
# PAGE SETUP
# =========================
st.set_page_config(
    page_title="MY NET ZERO | GNPA",

    layout="wide"
)


# =========================
# HERO VIDEO
# =========================
if st.session_state.get("hero_visible", True):
    st.video(
        "hero.mp4",
        autoplay=True,
        muted=True,
        loop=False
    )

# =========================
# COLORS / STYLE
# =========================
st.markdown("""
<style>

.stApp {
    background-color: #FAFAF7;
}

.block-container {
    max-width: 1150px;
    padding-top: 45px;
    padding-bottom: 80px;
}

.gnpa {
    color: #2F765D;
    font-size: 14px;
    font-weight: 700;
    letter-spacing: 3px;
}

.agency {
    color: #68757D;
    font-size: 15px;
    margin-top: 5px;
}

.main-title {
    color: #123047;
    font-size: 70px;
    font-weight: 750;
    letter-spacing: -3px;
    margin-top: 55px;
    margin-bottom: 5px;
}

.world-title {
    color: #2F765D;
    font-size: 18px;
    font-weight: 700;
    letter-spacing: 4px;
    margin-bottom: 70px;
}

.small-title {
    color: #68757D;
    font-size: 14px;
    font-weight: 700;
    letter-spacing: 2px;
    text-transform: uppercase;
}

.formula {
    color: #123047;
    font-size: 42px;
    font-weight: 650;
    margin-top: 10px;
    margin-bottom: 35px;
}

.divider {
    height: 1px;
    background-color: #D9DEDB;
    margin-top: 25px;
    margin-bottom: 50px;
}

.diet-title {
    color: #123047;
    font-size: 32px;
    font-weight: 750;
    letter-spacing: 3px;
}

.number-title {
    color: #68757D;
    font-size: 13px;
    font-weight: 700;
    letter-spacing: 2px;
}

.big-number {
    color: #123047;
    font-size: 43px;
    font-weight: 700;
}

.small-number {
    color: #68757D;
    font-size: 14px;
}

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

</style>
""", unsafe_allow_html=True)

# =========================
# GNPA
# =========================
st.markdown(
    '<div style="font-size:24px; font-weight:800; color:#2F765D; '
    'letter-spacing:6px; margin-top:28px; margin-bottom:6px;">'
    'GNPA'
    '</div>'
    '<div style="font-size:14px; font-weight:600; color:#123047; '
    'letter-spacing:1.6px; text-transform:uppercase; margin-bottom:34px;">'
    'Global Nature & Plant-based 飲食轉型 Agency'
    '</div>',
    unsafe_allow_html=True
)

# =========================
# 關於 GNPA
# =========================

with st.expander("關於 GNPA"):
    st.markdown(
        """
**Global Nature & Plant-based 飲食轉型 Agency (GNPA)**  
**全球自然與植物性飲食轉型總署**

GNPA 是一項以研究為核心的倡議，探索食物系統、自然復育、
氣候變遷與通往淨零之間的關係。

**MY NET ZERO** 將這項研究轉化為互動式平台，
讓個人、國家與全球使用者探索飲食轉型與自然復育
如何影響氣候結果。

本平台旨在連結科學研究、公眾理解與政策討論。
        """
    )

# =========================
# 聯絡我們 / 提出問題
# =========================

with st.expander("聯絡我們 / 提出問題"):

    with st.form("contact_form"):

        contact_name = st.text_input("姓名")
        contact_organization = st.text_input("組織")
        contact_country = st.text_input("國家")
        contact_email = st.text_input("電子郵件")
        contact_message = st.text_area("問題 / 留言")

        contact_submit = st.form_submit_button("送出")

    if contact_submit:

        if not contact_name or not contact_email or not contact_message:
            st.warning(
                "請填寫您的姓名、電子郵件及問題／留言。"
            )

        else:
            form_data = {
                "name": contact_name,
                "organization": contact_organization,
                "country": contact_country,
                "email": contact_email,
                "message": contact_message
            }

            try:
                response = requests.post(
                    "https://formspree.io/f/xeaobwry",
                    data=form_data,
                    timeout=10
                )

                if response.ok:
                    st.success(
                        "謝謝您。您的訊息已成功送出。"
                    )
                else:
                    st.error(
                        "訊息無法送出，請再試一次。"
                    )

            except requests.RequestException:
                st.error(
                    "訊息無法送出，請再試一次。"
                )

    st.caption(
        "您的資料僅用於回覆您的詢問。"
    )

# =========================
# MY NET ZERO
# =========================
st.markdown(
    '<div class="main-title">MY NET ZERO</div>',
    unsafe_allow_html=True
)

# =========================
# MAIN NAVIGATION
# =========================

nav1, nav2, nav3, nav4 = st.columns(4)

with nav1:
    for_me = st.button(
        "我的淨零",
        use_container_width=True
    )

with nav2:
    my_nation = st.button(
        "我的國家",
        use_container_width=True
    )

with nav3:
    our_world = st.button(
        "我們的世界",
        use_container_width=True
    )

with nav4:
    beyond_net_zero = st.button(
        "超越淨零",
        use_container_width=True
    )


# =========================
# 我的國家 SELECTOR
# =========================

# =========================
# PAGE SELECTION
# =========================

if "show_nation" not in st.session_state:
    st.session_state.show_nation = False

if "show_for_me" not in st.session_state:
    st.session_state.show_for_me = False

if "show_beyond" not in st.session_state:
    st.session_state.show_beyond = False

if "hero_visible" not in st.session_state:
    st.session_state.hero_visible = True

if for_me:
    st.session_state.show_for_me = True
    st.session_state.show_nation = False
    st.session_state.show_beyond = False
    st.session_state.hero_visible = False

if my_nation:
    st.session_state.show_for_me = False
    st.session_state.show_nation = True
    st.session_state.show_beyond = False
    st.session_state.hero_visible = False

if our_world:
    st.session_state.show_for_me = False
    st.session_state.show_nation = False
    st.session_state.show_beyond = False
    st.session_state.hero_visible = False

if beyond_net_zero:
    st.session_state.show_for_me = False
    st.session_state.show_nation = False
    st.session_state.show_beyond = True
    st.session_state.hero_visible = False

# =========================
# PAGE BACKGROUND
# =========================

if st.session_state.show_for_me:
    page_bg = "#FCECEF"

elif st.session_state.show_nation:
    page_bg = "#F6F0DF"

elif st.session_state.show_beyond:
    page_bg = "#EAF5ED"

else:
    page_bg = "#EAF4F8"

st.markdown(
    f"""
    <style>
    .stApp {{
        background-color: {page_bg};
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# =========================
# 超越淨零
# =========================

if st.session_state.show_beyond:

    st.markdown(
        '<div style="font-size:48px; font-weight:750; color:#123047; '
        'margin-top:55px; letter-spacing:-1px;">'
        '超越淨零'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div style="font-size:30px; font-weight:700; color:#2F765D; '
        'margin-top:8px; margin-bottom:35px;">'
        '繁榮的未來'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div style="font-size:21px; line-height:1.8; color:#123047; '
        'max-width:850px; margin-bottom:50px;">'
        'Changing an unsustainable system is not about giving up the future.<br>'
        'It is about unlocking a future more abundant, more advanced, '
        'and more exciting than we imagined.'
        '</div>',
        unsafe_allow_html=True
    )

    future1, future2, future3, future4 = st.columns(4)

    with future1:
        st.markdown("### 糧食安全")

    with future2:
        st.markdown("### 復育的地球")

    with future3:
        st.markdown("### 氣候穩定")

    with future4:
        st.markdown("### 人類進步")
     
# =========================
# 我的淨零
# =========================

if st.session_state.show_for_me:

    st.markdown(
        '<div style="font-size:32px; font-weight:700; color:#123047; '
        'margin-top:30px;">我的淨零</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div style="color:#2F765D; font-size:15px; font-weight:700; '
        'letter-spacing:2px; margin-top:25px;">MY NET ZERO INDEX</div>',
        unsafe_allow_html=True
    )

    if "diet_choice" not in st.session_state:
        st.session_state.diet_choice = "動物性飲食"

    if st.session_state.diet_choice == "植物性飲食":
        my_net_zero_index = -6
    else:
        my_net_zero_index = 10

    st.markdown(
        f'<div style="font-size:64px; font-weight:750; color:#123047; '
        f'margin-top:5px; margin-bottom:30px;">{my_net_zero_index}</div>',
        unsafe_allow_html=True
    )
    
    st.markdown(
        '<div style="font-size:14px; line-height:1.6; color:#68757D; '
        'max-width:760px; margin-top:-15px; margin-bottom:25px;">'
        '<b>關於這項指數</b><br>'
        'MY NET ZERO INDEX is a standardized research indicator based on an '
        '<b>Earth-system accounting framework</b>. Unlike conventional carbon-footprint '
        'approaches that focus primarily on anthropogenic emissions, this model also '
        'accounts for the loss and recovery of natural CO₂-removal capacity across '
        'forests, land and oceans.'
        '</div>',
        unsafe_allow_html=True
    )
    personal1, personal2 = st.columns(2)

    with personal1:
        st.markdown(
            '<div class="number-title">日常生活</div>',
            unsafe_allow_html=True
        )
        st.markdown(
            '<div style="font-size:46px; font-weight:700; color:#123047; '
            'margin-top:10px;">2</div>',
            unsafe_allow_html=True
        )
        st.markdown(
            '<div class="small-number">'
            '能源 · 交通 · 烹飪 · 家電'
            '</div>',
            unsafe_allow_html=True
        )

    with personal2:

        st.markdown(
            '<div class="number-title">食物</div>',
            unsafe_allow_html=True
        )
        st.markdown(
            '<div style="font-size:46px; font-weight:700; color:#123047; '
            'margin-top:10px;">8</div>',
            unsafe_allow_html=True
        )
        st.markdown(
            '<div class="small-number">'
            '動物性食物系統'
            '</div>',
            unsafe_allow_html=True
        )

    st.markdown(
        '<div style="height:35px;"></div>',
        unsafe_allow_html=True
    )

    with st.expander("這項指數如何計算？"):
        st.markdown(
            """
**MY NET ZERO INDEX** 是一項標準化研究指標。  
它不是傳統的個人碳足跡計算器。

**日常生活 = 2**  
能源、交通、烹飪與家電，在本研究模型的標準化氣候負擔中約占 **20%**。

**食物與自然 = 8**  
其餘 **80%** 代表本研究模型歸因於畜牧相關的氣候負擔，包括食物系統能源使用、土地壓力，以及自然 CO₂ 移除能力的喪失。

**動物性飲食**

**2 + 8 = 10**

因此，動物性飲食基準的 MY NET ZERO INDEX 為 **10**。

**植物性飲食**

**2 − 8 = −6**

在本模型中，飲食轉型可降低畜牧相關壓力，使自然碳匯恢復。負值代表恢復的自然 CO₂ 移除能力對地球系統平衡的貢獻，而不是宣稱個人直接產生負排放。
            """
        )
    st.markdown(
        '<div style="color:#2F765D; font-size:15px; font-weight:700; '
        'letter-spacing:2px;">您的飲食</div>',
        unsafe_allow_html=True
    )

    diet1, diet2 = st.columns(2)

    if "diet_choice" not in st.session_state:
        st.session_state.diet_choice = "動物性飲食"

    with diet1:
        plant_based = st.button(
            "植物性飲食",
            use_container_width=True
        )

        if plant_based:
            st.session_state.diet_choice = "植物性飲食"
            st.rerun()

    with diet2:
        animal_based = st.button(
            "動物性飲食",
            use_container_width=True
        )

        if animal_based:
            st.session_state.diet_choice = "動物性飲食"
            st.rerun()

  
    if st.session_state.diet_choice == "植物性飲食":

        st.markdown(
            '<div style="height:35px;"></div>',
            unsafe_allow_html=True
        )

        st.markdown(
            '<div style="color:#2F765D; font-size:15px; font-weight:700; '
            'letter-spacing:2px; margin-bottom:20px;">會改變什麼？</div>',
            unsafe_allow_html=True
        )

        # FIRST ROW
        change1, change2, change3 = st.columns(3)

        with change1:
            st.markdown(
                '<div class="number-title">甲烷減量</div>',
                unsafe_allow_html=True
            )
            st.markdown(
                '<div style="font-size:27px; font-weight:700; color:#123047; '
                'margin-top:10px;">降低</div>',
                unsafe_allow_html=True
            )
            st.markdown(
                '<div class="small-number">畜牧相關甲烷排放</div>',
                unsafe_allow_html=True
            )

        with change2:
            st.markdown(
                '<div class="number-title">釋放土地</div>',
                unsafe_allow_html=True
            )
            st.markdown(
                '<div style="font-size:32px; font-weight:700; color:#123047; '
                'margin-top:10px;">78%</div>',
                unsafe_allow_html=True
            )
            st.markdown(
                '<div class="small-number">全球農業用地</div>',
                unsafe_allow_html=True
            )

        with change3:
            st.markdown(
                '<div class="number-title">森林恢復</div>',
                unsafe_allow_html=True
            )
            st.markdown(
                '<div style="font-size:32px; font-weight:700; color:#123047; '
                'margin-top:10px;">41%</div>',
                unsafe_allow_html=True
            )
            st.markdown(
                '<div class="small-number">熱帶森林砍伐與牛肉生產相關的比例</div>',
                unsafe_allow_html=True
            )

        # SPACE BETWEEN TWO ROWS
        st.markdown(
            '<div style="height:30px;"></div>',
            unsafe_allow_html=True
        )

        # SECOND ROW
        change4, change5, change6 = st.columns(3)

        with change4:
            st.markdown(
                '<div class="number-title">自然 CO₂ 吸收</div>',
                unsafe_allow_html=True
            )
            st.markdown(
                '<div style="font-size:27px; font-weight:700; color:#123047; '
                'margin-top:10px;">恢復</div>',
                unsafe_allow_html=True
            )
            st.markdown(
                '<div class="small-number">透過生態系統恢復</div>',
                unsafe_allow_html=True
            )

        with change5:
            st.markdown(
                '<div class="number-title">海洋死區恢復</div>',
                unsafe_allow_html=True
            )
            st.markdown(
                '<div style="font-size:32px; font-weight:700; color:#123047; '
                'margin-top:10px;">80%</div>',
                unsafe_allow_html=True
            )
            st.markdown(
                '<div class="small-number">死區恢復，沿海海洋森林重新吸收 CO₂</div>',
                unsafe_allow_html=True
            )

        with change6:
            st.markdown(
                '<div class="number-title">化石能源減量</div>',
                unsafe_allow_html=True
            )
            st.markdown(
                '<div style="font-size:32px; font-weight:700; color:#123047; '
                'margin-top:10px;">41%</div>',
                unsafe_allow_html=True
            )
            st.markdown(
                '<div class="small-number">歸因於畜牧系統能源使用</div>',
                unsafe_allow_html=True
            )

if st.session_state.show_nation:
    selected_country = st.selectbox(
        "選擇您的國家",
        countries
    )

    selected_row = nation_data[
        nation_data["Country"].astype(str).str.strip() == selected_country
    ].iloc[0]

    selected_region = selected_row["Groups"]

    st.markdown(
        f'<div style="font-size:32px; font-weight:700; color:#123047; '
        f'margin-top:25px;">{selected_country.upper()}</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        f'<div style="font-size:16px; color:#68757D; '
        f'margin-top:5px;">{selected_region}</div>',
        unsafe_allow_html=True
    )
    
     
    co2_impact = selected_row["Cow's CO2  impact "]
    gdp_impact = selected_row["COW's GDP impacts"]

  
    # =========================
    # 淨零評分
    # =========================

    ghg_net_zero = selected_row["Net Zero Score --GHG-IPCC"]
    my_net_zero = selected_row["MY NZ Research Model Outome"]

    st.markdown(
        '<div style="font-size:20px; font-weight:800; color:#2F765D; '
        'letter-spacing:2px; margin-top:40px; margin-bottom:18px;">'
        '淨零評分'
        '</div>',
        unsafe_allow_html=True
    )

    with st.container(border=True):

        score1, score2 = st.columns(2)

        with score1:
            st.markdown(
                '<div style="font-size:14px; font-weight:700; color:#2F765D; '
                'letter-spacing:2px;">溫室氣體 — IPCC 模型</div>',
                unsafe_allow_html=True
            )
            st.markdown(
                f'<div style="font-size:30px; font-weight:700; color:#123047; '
                f'margin-top:18px; margin-bottom:18px;">{ghg_net_zero}</div>',
                unsafe_allow_html=True
            )

        with score2:
            st.markdown(
                '<div style="font-size:14px; font-weight:700; color:#2F765D; '
                'letter-spacing:2px;">MY NET ZERO 研究模型</div>',
                unsafe_allow_html=True
            )
            st.markdown(
                f'<div style="font-size:30px; font-weight:700; color:#123047; '
                f'margin-top:18px; margin-bottom:18px;">{my_net_zero}</div>',
                unsafe_allow_html=True
            )

    st.markdown(
        '<div style="height:35px;"></div>',
        unsafe_allow_html=True
    )






    result1, result2 = st.columns(2)

    with result1:
        st.markdown(
            '<div class="number-title">畜牧 CO₂ 影響</div>',
            unsafe_allow_html=True
        )
        st.markdown(
            f'<div style="font-size:38px; font-weight:700; '
            f'color:#123047; margin-top:10px;">{co2_impact*100:,.0f}%</div>',
            unsafe_allow_html=True
        )

    with result2:
        st.markdown(
            '<div class="number-title">畜牧 GDP 影響</div>',
            unsafe_allow_html=True
        )
        st.markdown(
            f'<div style="font-size:38px; font-weight:700; '
            f'color:#123047; margin-top:10px;">{gdp_impact*100:,.0f}%</div>',
            unsafe_allow_html=True
        )

    regional_co2 = selected_row["Livestock CO2 Region"]
    regional_gdp = selected_row["Livestock GDP Region"]

    st.markdown(
        f'<div style="font-size:15px; font-weight:700; color:#2F765D; '
        f'letter-spacing:2px; margin-top:35px;">'
        f'{selected_region.upper()} — 區域比較</div>',
        unsafe_allow_html=True
    )

    region1, region2 = st.columns(2)

    with region1:
        st.markdown(
            '<div class="number-title">區域 CO₂ 影響</div>',
            unsafe_allow_html=True
        )
        st.markdown(
            f'<div style="font-size:30px; font-weight:700; color:#123047; '
            f'margin-top:8px;">{regional_co2 * 100:,.0f}%</div>',
            unsafe_allow_html=True
        )

    with region2:
        st.markdown(
            '<div class="number-title">區域 GDP 影響</div>',
            unsafe_allow_html=True
        )
        st.markdown(
            f'<div style="font-size:30px; font-weight:700; color:#123047; '
            f'margin-top:8px;">{regional_gdp * 100:,.0f}%</div>',
            unsafe_allow_html=True
        )


    # =========================
    # 計算基礎
    # =========================

    st.markdown(
        '<div style="height:25px;"></div>',
        unsafe_allow_html=True
    )

    basis1, basis2 = st.columns(2)

    with basis1:
        st.markdown(
            '<div style="border:1px solid #D9DEDB; border-radius:8px; padding:20px 24px; min-height:250px;">'
            '<div style="color:#123047; font-size:15px; font-weight:700; letter-spacing:1.5px; margin-bottom:18px;">CO₂ 影響 — 計算基礎</div>'
            '<div style="color:#68757D; font-size:15px; line-height:2;">甲烷排放<br>放牧土地<br>森林砍伐<br>能源使用<br>化石燃料</div>'
            '</div>',
            unsafe_allow_html=True
        )

    with basis2:
        st.markdown(
            '<div style="border:1px solid #D9DEDB; border-radius:8px; padding:20px 24px; min-height:250px;">'
            '<div style="color:#123047; font-size:15px; font-weight:700; letter-spacing:1.5px; margin-bottom:18px;">GDP 影響 — 計算基礎</div>'
            '<div style="color:#68757D; font-size:15px; line-height:2;">甲烷排放<br>水資源<br>土壤侵蝕<br>森林砍伐<br>飼料作物</div>'
            '</div>',
            unsafe_allow_html=True
        )

    st.markdown(
        '<div style="color:#68757D; font-size:13px; margin-top:12px;">'
        '結果依 MY NET ZERO 研究模型計算。'
        '</div>',
        unsafe_allow_html=True
    )
    
    # =========================
    # 國家重點訊息
    # =========================

    national_message = selected_row["Key national message"]

    st.markdown(
        '<div style="height:30px;"></div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div style="color:#2F765D; font-size:14px; font-weight:700; '
        'letter-spacing:2px;">國家重點訊息</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        f'<div style="color:#123047; font-size:20px; line-height:1.7; '
        f'margin-top:12px; margin-bottom:20px;">{national_message}</div>',
        unsafe_allow_html=True
    )



st.markdown(
    '<div class="world-title">全球淨零</div>',
    unsafe_allow_html=True
)


# =========================
# NET ZERO FORMULAS
# =========================

st.markdown(
    """
### 兩種淨零核算方式

**傳統淨零**主要問：為了平衡人為造成的排放，需要減少或移除多少人為排放。

**MY NET ZERO** 將核算邊界擴展至地球系統：它同時追問，當森林、土地與海洋承受的壓力降低時，可以恢復多少自然 CO₂ 移除能力。

兩者的差異不只是另一種排放估算，而是**不同的核算邊界**。
    """
)
col1, col2 = st.columns(2)

with col1:

    st.markdown(
        '<div class="small-title">'
        '傳統淨零'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="formula">'
        '1 − 1 = 0'
        '</div>',
        unsafe_allow_html=True
    )

with col2:

    st.markdown(
        '<div class="small-title">'
        '實際淨零差距'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '''
        <div style="
            color:#123047;
            font-size:34px;
            font-weight:600;
            margin-top:10px;
            line-height:1.25;
            white-space:nowrap;
        ">
            Net Zero = 1 − (0.25 − 11.87)
        </div>

        <div style="
            color:#123047;
            font-size:58px;
            font-weight:750;
            letter-spacing:-2px;
            margin-top:12px;
            margin-bottom:25px;
        ">
            = 12.62
        </div>
        ''',
        unsafe_allow_html=True
    )

  


# =========================
# WHY
# =========================
with st.expander("為什麼？"):

    st.image(
        "net_zero_gap.png.png",
        caption="圖 1.1　衡量從目前狀態到氣候成功的距離。",
        use_container_width=True
    )

    st.markdown("""
### 淨零差距

**大氣 CO₂ 差距**

426 ppm − 350 ppm ≈ **76 ppm**

**CO₂ 當量**

76 ppm × 7.81 GtCO₂/ppm ≈ **593 GtCO₂**

**相當於全球排放年數**

593 GtCO₂ ÷ 50 GtCO₂/年 ≈ **11.87 年**

**MY NET ZERO 模型**

1 − (0.25 − 11.87) ≈ **12.62**

*換算基礎：Poljak（2023），每 1 ppm 大氣 CO₂ 約等於 7.81 GtCO₂。*
""")

st.markdown(
    '<div class="divider"></div>',
    unsafe_allow_html=True
)


# =========================
# 飲食轉型
# =========================
st.markdown(
    '<div class="diet-title">飲食轉型</div>',
    unsafe_allow_html=True
)


diet_shift = st.slider(
    "飲食轉型",
    0,
    100,
    0,
    1,
    label_visibility="collapsed"
)


# =========================
# CALCULATION
# =========================

MAX_CO2 = 643.0

START_PPM = 426.0
TARGET_PPM = 350.0

co2_reduced = MAX_CO2 * diet_shift / 100

co2_剩餘 = MAX_CO2 - co2_reduced

current_ppm = (
    START_PPM
    - (START_PPM - TARGET_PPM)
    * diet_shift / 100
)

ppm_reduced = START_PPM - current_ppm


# =========================
# 結果S
# =========================
col3, col4 = st.columns(2)

with col3:

    st.markdown(
        '<div class="number-title">'
        'CO₂ 減量'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        f'<div class="big-number">'
        f'{co2_reduced:.1f} GtCO₂'
        f'</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        f'<div class="small-number">'
        f'{co2_剩餘:.1f} 剩餘 GtCO₂'
        f'</div>',
        unsafe_allow_html=True
    )


with col4:

    st.markdown(
        '<div class="number-title">'
        '大氣 CO₂'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        f'<div class="big-number">'
        f'{current_ppm:.1f} ppm'
        f'</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        f'<div class="small-number">'
        f'426 → {current_ppm:.1f} ppm'
        f'</div>',
        unsafe_allow_html=True
    )


# =========================
# CHART DATA
# =========================

x = np.arange(0, 101)

carbon_curve = MAX_CO2 * (1 - x / 100)

ppm_curve = (
    START_PPM
    - (START_PPM - TARGET_PPM)
    * x / 100
)


# =========================
# CHART 1
# =========================

chart1, chart2 = st.columns(2)


with chart1:

    fig1 = go.Figure()

    fig1.add_trace(
        go.Scatter(
            x=x,
            y=carbon_curve,
            mode="lines",
            line=dict(
                color="#123047",
                width=4
            )
        )
    )

    fig1.add_trace(
        go.Scatter(
            x=[diet_shift],
            y=[co2_剩餘],
            mode="markers",
            marker=dict(
                size=13,
                color="#2F765D"
            )
        )
    )

    fig1.update_layout(
        title="CO₂ 差距",
        height=330,
        showlegend=False,
        paper_bgcolor="#FAFAF7",
        plot_bgcolor="#FAFAF7",
        xaxis_title="飲食轉型 (%)",
        yaxis_title="剩餘 GtCO₂",
        margin=dict(
            l=20,
            r=20,
            t=55,
            b=30
        )
    )

    st.plotly_chart(
        fig1,
        use_container_width=True,
        config={
            "displayModeBar": False
        }
    )


# =========================
# CHART 2
# =========================

with chart2:

    fig2 = go.Figure()

    fig2.add_trace(
        go.Scatter(
            x=x,
            y=ppm_curve,
            mode="lines",
            line=dict(
                color="#2F765D",
                width=4
            )
        )
    )

    fig2.add_trace(
        go.Scatter(
            x=[diet_shift],
            y=[current_ppm],
            mode="markers",
            marker=dict(
                size=13,
                color="#123047"
            )
        )
    )

    fig2.update_layout(
        title="大氣 CO₂",
        height=330,
        showlegend=False,
        paper_bgcolor="#FAFAF7",
        plot_bgcolor="#FAFAF7",
        xaxis_title="飲食轉型 (%)",
        yaxis_title="ppm",
        margin=dict(
            l=20,
            r=20,
            t=55,
            b=30
        )
    )

    st.plotly_chart(
        fig2,
        use_container_width=True,
        config={
            "displayModeBar": False
        }
    )

# =========================
# KEY IMPACTS
# =========================

st.markdown(
    '<div class="divider"></div>',
    unsafe_allow_html=True
)

impact1, impact2, impact3 = st.columns(3)

with impact1:
    st.markdown(
        '<div class="number-title">釋放土地</div>',
        unsafe_allow_html=True
    )
    st.markdown(
        '<div style="font-size:32px; font-weight:700; color:#123047; '
        'margin-top:12px; white-space:nowrap;">37 million km²</div>',
        unsafe_allow_html=True
    )
    st.markdown(
        '<div class="small-number">78% 全球農業用地</div>',
        unsafe_allow_html=True
    )

with impact2:
    st.markdown(
        '<div class="number-title">溫室氣體減量</div>',
        unsafe_allow_html=True
    )
    st.markdown(
        '<div style="font-size:32px; font-weight:700; color:#123047; '
        'margin-top:12px;">166%</div>',
        unsafe_allow_html=True
    )
    st.markdown(
        '<div class="small-number">相當於 2020 年全球溫室氣體</div>',
        unsafe_allow_html=True
    )

with impact3:
    st.markdown(
        '<div class="number-title">經濟成本減少</div>',
        unsafe_allow_html=True
    )
    st.markdown(
        '<div style="font-size:32px; font-weight:700; color:#123047; '
        'margin-top:12px;">163%</div>',
        unsafe_allow_html=True
    )
    st.markdown(
        '<div class="small-number">相當於 2020 年全球 GDP</div>',
        unsafe_allow_html=True
    )

# =========================
# SECOND WHY
# =========================

with st.expander(
    "為什麼飲食轉型會改變 CO₂？"
):

    st.markdown(
        '<div style="font-size:22px; font-weight:700; color:#123047; '
        'margin-bottom:15px;">資料模型</div>',
        unsafe_allow_html=True
    )

    st.image(
        "data model.png",
        caption="MY NET ZERO 研究資料模型",
        use_container_width=True
    )


    st.markdown(
        '<div style="font-size:22px; font-weight:700; color:#123047; '
        'margin-top:35px; margin-bottom:15px;">'
        '研究架構'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
**第三章 — 資料與方法**  
研究框架 · 資料 · 變數 · 方程式 · 自然復育模型

**第四章 — 排放與自然 CO₂ 吸收**  
模型有效性 · 預測 · 敏感度分析 · 氣候情境

**第五章 — 化石燃料與畜牧業的外部成本**  
畜牧外部性 · 能源 · 經濟成本

**第六章 — 化石燃料與畜牧業的 CO₂ 責任**  
排放 · CO₂ 移除能力損失 · 能源消耗 · 土地與森林敏感度分析 · 調整後責任

**第七章 — 應用與自然復育模型**  
美國 · 中國 · 全球氣候政策 · 自然復育
        """
    )

    st.caption(
        "Detailed methodology, calculations, sensitivity analyses and "
        "underlying data are documented in the full research."
    )

# =========================
# RESEARCH BRIEF
# =========================

st.markdown(
    """
### 研究簡報

**淨零的地球系統核算**

MY NET ZERO 研究框架的一頁摘要，包括核算邊界、氣候負擔歸因，以及從飲食轉型到恢復自然 CO₂ 移除能力的路徑。
    """
)

with st.expander("查看研究簡報"):
    st.image(
        "research_brief.png",
        use_container_width=True
    )

with open("Net_Zero_Research_Summary_QR_FIXED.pdf", "rb") as pdf_file:
    st.download_button(
        label="下載研究簡報（PDF）",
        data=pdf_file,
        file_name="MY_NET_ZERO_Research_Brief.pdf",
        mime="application/pdf",
        use_container_width=True
    )



    st.markdown(
        '<div style="font-size:22px; font-weight:700; color:#123047; '
        'margin-top:40px; margin-bottom:15px;">'
        '計算基礎'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
**能源 — 41%**

**資料來源**  
Global meat consumption by meat type · Energy requirements by meat type · Global population · Global electricity consumption

**MY NET ZERO 計算**  
Meat consumption × energy requirement by meat type × global population  
→ estimated global meat-industry electricity consumption  
→ compared with total global electricity consumption

**結果**  
Estimated meat-industry electricity consumption = **41% of global electricity consumption**
        """
    )

    st.caption(
        "Derived indicator calculated by the MY NET ZERO research model "
        "from underlying source data."
    )

    st.markdown(
        """
**甲烷 — 31%**

**資料來源**  
Cattle population · Annual methane emissions per cow

**MY NET ZERO MODEL ASSUMPTION**  
Methane = **100× CO₂-equivalent** to represent its strong near-term warming impact

**MY NET ZERO 計算**  
Cattle population × methane emissions per cow × 100 CO₂-equivalent  
→ approximately **15.2 GtCO₂-equivalent**

**結果**  
15.2 GtCO₂-eq. ÷ 50 GtCO₂-eq. global annual emissions  
→ **≈ 31%**
        """
    )

    st.caption(
        "The 100× methane factor is a MY NET ZERO model assumption. "
        "It is not the conventional 100-year GWP factor."
    )
 
    st.markdown(
        """
**土地 — 11%**

**資料來源**  
Livestock land use = **37 million km²**

**MY NET ZERO 計算**  
37 million km² × estimated CO₂ absorption capacity of released land  
→ approximately **5.17 GtCO₂ per year**

**結果**  
5.17 GtCO₂ ÷ 50 GtCO₂ global annual emissions  
→ **≈ 11%**
        """
    )

    st.caption(
        "The 37 million km² livestock land-use estimate is source data. "
        "The 11% indicator is derived by the MY NET ZERO research model."
    )

    st.markdown(
        """
**森林 — 91%**

**模型邊界**  
Conservative estimate using cattle in **Amazon nations and one Congo Basin country**, rather than global cattle populations

**MY NET ZERO 計算**  
Cattle population in the selected tropical-forest regions × forest area impact × estimated tropical-forest CO₂ absorption capacity  
→ approximately **45.34 GtCO₂ per year**

**結果**  
45.34 GtCO₂ ÷ 50 GtCO₂ global annual emissions  
→ **≈ 91%**
        """
    )

    st.caption(
        "The forest estimate uses a deliberately restricted tropical-forest "
        "boundary to avoid applying one CO₂ absorption rate to forests "
        "across different climatic regions."
    )

    st.markdown(
        """
**畜牧業 CO₂ 總責任 — 166%**

**能源重新歸因**  
Meat-industry energy use = **41%** of global electricity  
Applied to the **78% fossil-fuel baseline**  
→ 78% × 41% ≈ **32%**

**MY NET ZERO 整合計算**  
Methane **31%** + Land **11%** + Forest **91%** + Energy **32%**

**結果**  
31% + 11% + 91% + 32% ≈ **166%**
        """
    )

    st.caption(
        "The 166% result is an integrated MY NET ZERO research-model "
        "estimate relative to the 50 GtCO₂-eq. annual global emissions baseline."
    )


    st.markdown(
        '<div style="font-size:22px; font-weight:700; color:#123047; '
        'margin-top:40px; margin-bottom:15px;">'
        '資料來源'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
**核心資料來源**

**FAO / UNFAO**  
Livestock, food consumption and agricultural land-use data

**Energypedia**  
Energy requirements within food and agricultural value chains

**U.S. Energy Information Administration (EIA)**  
Global energy and electricity data

**IPCC**  
Conventional greenhouse-gas accounting and climate assessment framework
        """
    )

    st.caption(
        "Source data are used as inputs. Calculations, integration and "
        "derived indicators are produced by the MY NET ZERO research model."
    )
    st.markdown(
        """
**查看原始資料來源**

[FAO / FAOSTAT — Global Food & Agriculture Data](https://www.fao.org/faostat/)

[Energypedia — Energy within Food and Agricultural Value Chains](https://energypedia.info/wiki/Energy_within_Food_and_Agricultural_Value_Chains)

[U.S. Energy Information Administration (EIA) — Electricity Data](https://www.eia.gov/electricity/data.php)

[Gatti et al. (2021), Nature — Amazonia as a carbon source linked to deforestation and climate change](https://www.nature.com/articles/s41586-021-03629-6)
        """
    )

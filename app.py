import streamlit as st

# --- ページ設定 ---
st.set_page_config(page_title="質量計算アシスト", layout="centered")

# --- 見た目の設定（CSS） ---
st.markdown("""
    <style>
    /* クレジット表示用のCSS */
    .credit {
        text-align: right;
        font-size: 14px;
        color: #666;
        margin-bottom: -20px;
    }
    /* 入力欄のラベルスタイル */
    .stNumberInput label {
        font-size: 20px !important;
        color: #CD7F32 !important; 
        font-weight: 800 !important;
    }
    .stSelectbox label {
        font-size: 20px !important;
        color: #FF4B4B !important;
        font-weight: 800 !important;
    }
    /* 計算結果ボックス */
    .result-box {
        background-color: #fdfaf5;
        padding: 15px;
        border-radius: 10px;
        border-left: 5px solid #CD7F32;
        margin-top: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# 右上にクレジットを表示
st.markdown('<p class="credit">開発/制作：緒方</p>', unsafe_allow_html=True)

st.title('⚖️ 質量・重量計算アシスト')
st.markdown("---")

# --- 1. 材質と比重の設定 ---
# 一般的な比重データ（コンクリートを追加）
material_data = {
    "鉄 (SS400相当)": 7.85,
    "銅": 8.96,
    "アルミ": 2.70,
    "ステンレス (SUS304)": 7.93,
    "しんちゅう": 8.45,
    "コンクリート (一般)": 2.35,  # 追加
    "水": 1.00,
    "油 (作動油等目安)": 0.87
}

selected_material = st.selectbox("材質を選択してください", list(material_data.keys()))
base_density = material_data[selected_material]

# 比重の手動微調整用
density = st.number_input(f"{selected_material} の比重 (g/cm³)", value=base_density, format="%.3f")

st.markdown("---")

# --- 2. サイズ入力 ---
st.subheader("サイズを入力 (mm単位)")
col1, col2, col3 = st.columns(3)

with col1:
    length_mm = st.number_input("縦 (mm)", value=100.0, min_value=0.0, step=1.0)
with col2:
    width_mm = st.number_input("横 (mm)", value=100.0, min_value=0.0, step=1.0)
with col3:
    thickness_mm = st.number_input("厚み/深さ (mm)", value=10.0, min_value=0.0, step=0.1)

# --- 3. 計算ロジック ---
# 体積 (cm³) = (mm * mm * mm) / 1000
volume_cm3 = (length_mm * width_mm * thickness_mm) / 1000.0

# 質量 (g) = 体積 (cm³) * 比重
mass_g = volume_cm3 * density
mass_kg = mass_g / 1000.0

# --- 4. 結果表示 ---
st.markdown('<div class="result-box">', unsafe_allow_html=True)
st.subheader("📊 計算結果")

c_res1, c_res2 = st.columns(2)
with c_res1:
    st.metric("質量 (kg)", f"{mass_kg:.3f} kg")
with c_res2:
    st.metric("質量 (g)", f"{mass_g:,.1f} g")

st.write(f"（参考）体積: **{volume_cm3:,.2f} cm³**")
st.markdown('</div>', unsafe_allow_html=True)

# 補足
st.caption("※コンクリートの比重は、配合や骨材により 2.3〜2.45 程度まで変動します。")


# --- 画面下部中央に「戻る」ボタンを配置 ---
st.markdown("---")  # 区切り線
col1, col2, col3 = st.columns([1, 1, 1])

with col2:  # 中央の列を使用
    # 水色のアイコン（🏠）と「戻る」を表示するボタン
    if st.link_button("🏠\n\n戻る", "https://7fjndw39dicdzckugyepb2.streamlit.app/", use_container_width=True):
        pass

# ボタンの色（水色）を調整するカスタム設定
st.markdown("""
    <style>
    div.stLinkButton > a {
        background-color: #00BFFF !important; /* 水色（DeepSkyBlue） */
        color: white !important;
        border-radius: 10px;
        text-align: center;
        border: none;
    }
    </style>
    """, unsafe_allow_html=True)

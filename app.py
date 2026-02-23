import streamlit as st

# Seiteneinstellungen für das Browser-Feeling
st.set_page_config(page_title="HV 2024", layout="wide")

# Custom CSS für das exakte Styling der Boxen
st.markdown("""
    <style>
    .main { background-color: #ffffff; }
    .sidebar-box {
        border: 2px solid #000000;
        padding: 10px;
        margin-bottom: 10px;
        border-radius: 5px;
    }
    .stButton>button { width: 100%; border: 2px solid #000; }
    </style>
    """, unsafe_allow_html=True)

# 1. Header Bereich
col_logo, col_nav, col_user = st.columns([1, 4, 2])
with col_logo:
    st.markdown("### 📄 HV 2024")
with col_nav:
    st.write("Home | Aktuelles | Veranstaltungen | Dokumente | Meine Daten")
with col_user:
    st.write(f"👤 Max Mustermann")

st.divider()

# 2. Haupt-Layout (Links Stream, Rechts Sidebar)
col_left, col_right = st.columns([3, 1])

with col_left:
    st.subheader("▶️ Live: Hauptversammlung 2024")
    # Platzhalter für den Video-Stream (X-Box aus deinem Mockup)
    st.video("https://www.youtube.com")  # Beispiel-URL

    # Fortschrittsbalken / Player-Controls Mockup
    st.slider("", 0, 100, 30, label_visibility="collapsed")

with col_right:
    # Box: Fragen an den Vorstand
    st.markdown('<div class="sidebar-box">', unsafe_allow_html=True)
    st.write("**Fragen an den Vorstand**")
    user_question = st.text_area("Ihre Frage hier eingeben...", height=150, label_visibility="collapsed")
    if st.button("Frage absenden"):
        st.success("Frage wurde übermittelt!")
    st.markdown('</div>', unsafe_allow_html=True)

    # Box: Schnellzugriff Dokumente
    st.markdown('<div class="sidebar-box">', unsafe_allow_html=True)
    st.write("**Schnellzugriff Dokumente**")
    st.button("📄 Beispiel 0012.pdf")
    st.button("📄 Beispiel 002.pdf")
    st.button("📄 Beispiel 003.doc")
    st.markdown('</div>', unsafe_allow_html=True)

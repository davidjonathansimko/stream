import streamlit as st
import random
import time

# 1. Konfiguration für Auto-Stretch & No-Scroll
st.set_page_config(page_title="HV 2024 Portal", layout="wide", initial_sidebar_state="collapsed")

# 2. High-End Custom CSS (Modern UI/UX)
st.markdown("""
    <style>
    /* Globales Design & Schriftart */
    @import url('https://fonts.googleapis.com');
    html, body, [class*="st-"] { font-family: 'Inter', sans-serif; background-color: #F8FAFC; }

    /* Layout-Fixing: Alles auf eine Seite ohne Scrollen */
    .block-container { padding: 1rem 2rem; max-height: 100vh; overflow: hidden; }

    /* Box-Styling */
    .sidebar-box {
        background: white; border: 1px solid #E2E8F0; padding: 15px;
        border-radius: 12px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1); margin-bottom: 10px;
    }

    /* Live-Button in Rot statt Blau */
    .stButton>button { border-radius: 8px; font-weight: 600; transition: all 0.2s; border: 1px solid #D1D5DB; }
    div[data-testid="stVerticalBlock"] > div:nth-child(1) button { background-color: #EF4444 !important; color: white !important; border: none !important; }

    /* Chat & Container Höhenbegrenzung */
    .stTextArea textarea { border-radius: 8px; }
    </style>
    """, unsafe_allow_html=True)

# 3. Session State für Navigation & Chat
if 'page' not in st.session_state: st.session_state.page = "Hauptversammlung"
if 'chat' not in st.session_state: st.session_state.chat = []


# 4. Modaler Dialog für Dokumente
@st.dialog("Dokumenten-Vorschau")
def open_doc(title):
    st.write(f"### {title}")
    st.markdown("---")
    st.write(
        "**Lorem ipsum dolor sit amet**, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua.")
    st.write("1. Protokoll der Sitzung vom Vorjahr")
    st.write("2. Bericht zur Gewinnverwendung")
    st.write("3. Entlastung des Aufsichtsrats")
    if st.button("Schließen"): st.rerun()


# 5. Header (Interaktive Navigation)
c1, c2, c3 = st.columns([1, 4, 1.5])
with c1: st.markdown("### 🏛️ HV 2024")
with c2:
    nav_cols = st.columns(5)
    nav_items = ["Home", "Aktuelles", "Veranstaltungen", "Dokumente", "Meine Daten"]
    for i, item in enumerate(nav_items):
        if nav_cols[i].button(item, key=f"nav_{item}", use_container_width=True):
            st.session_state.page = item
with c3: st.markdown(f"<div style='text-align:right;'>👤 <b>Max Mustermann</b></div>", unsafe_allow_html=True)

st.divider()

# 6. Seiten-Logik
if st.session_state.page != "Hauptversammlung":
    st.warning(f"Der Bereich **{st.session_state.page}** befindet sich aktuell noch **in Bearbeitung**.")
    if st.button("⬅ Zurück zur Hauptversammlung"):
        st.session_state.page = "Hauptversammlung"
        st.rerun()
else:
    # Haupt-Layout: Links Video (groß), Rechts Interaktion
    col_left, col_right = st.columns([3, 1.2], gap="medium")

    with col_left:
        # Live-Indikator & Überschrift
        st.markdown("<span style='color:red; font-weight:bold;'>● LIVE</span> ÜBERTRAGUNG", unsafe_allow_html=True)
        # Video wird durch das Spaltenverhältnis nach unten gestreckt
        st.video("https://www.youtube.com")
        st.info("**TOP 3:** Bericht des Vorstands über die strategische Neuausrichtung 2024/25.")

    with col_right:
        # Box 1: Fragen & Chat-Antwort
        st.markdown('<div class="sidebar-box">', unsafe_allow_html=True)
        st.write("**Fragen an den Vorstand**")

        # Kleiner Chat-Verlauf (Mockup)
        chat_placeholder = st.container(height=180)
        for m in st.session_state.chat:
            chat_placeholder.chat_message(m["role"]).write(m)

        user_q = st.text_input("Ihre Frage eingeben...", key="q_input", label_visibility="collapsed")
        if st.button("Absenden", use_container_width=True):
            if user_q:
                st.session_state.chat.append({"role": "user", "text": user_q})
                responses = ["Vielen Dank für Ihre Frage.", "Der Vorstand wird darauf gleich eingehen.",
                             "Dazu finden Sie Infos im Bericht."]
                st.session_state.chat.append({"role": "assistant", "text": random.choice(responses)})
                st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

        # Box 2: Dokumente (Modal)
        st.markdown('<div class="sidebar-box">', unsafe_allow_html=True)
        st.write("**Schnellzugriff Dokumente**")
        if st.button("📄 Tagesordnung.pdf", use_container_width=True): open_doc("Tagesordnung")
        if st.button("📊 Jahresbericht.pdf", use_container_width=True): open_doc("Jahresbericht")
        if st.button("⚖️ Satzung.doc", use_container_width=True): open_doc("Satzung der AG")
        st.markdown('</div>', unsafe_allow_html=True)

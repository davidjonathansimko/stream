import streamlit as st
import time

# 1. Konfiguration für Desktop-Optimierung
st.set_page_config(page_title="HV 2024 - Aktionärsportal", layout="wide", initial_sidebar_state="collapsed")

# 2. Modernes UI/UX Custom CSS
st.markdown("""
    <style>
    /* Hintergrund und Schrift */
    .stApp { background-color: #f8f9fa; }

    /* Header Styling */
    .nav-bar {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 10px 20px;
        background-color: white;
        border-bottom: 1px solid #e0e0e0;
        margin-bottom: 20px;
    }

    /* Sidebar Boxen Styling */
    .sidebar-box {
        background-color: white;
        border: 1px solid #dcdcdc;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        margin-bottom: 20px;
    }

    /* Button Styling */
    .stButton>button {
        width: 100%;
        border-radius: 8px;
        border: 1px solid #007bff;
        transition: all 0.3s;
    }
    .stButton>button:hover {
        background-color: #007bff;
        color: white;
        transform: translateY(-2px);
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Interaktive Navigation (State Management)
if 'page' not in st.session_state:
    st.session_state.page = "Hauptversammlung"

# Header Simulation
col_l, col_m, col_r = st.columns([1, 3, 1])
with col_l:
    st.markdown("### 🏛️ HV 2024")
with col_m:
    # Interaktive Navigations-Buttons
    nav_cols = st.columns(5)
    pages = ["Home", "Aktuelles", "Hauptversammlung", "Dokumente", "Meine Daten"]
    for i, p in enumerate(pages):
        if nav_cols[i].button(p, key=f"nav_{p}"):
            st.session_state.page = p
with col_r:
    st.markdown("<p style='text-align:right;'>👤 <b>Max Mustermann</b><br><small>Aktionärsnummer: 88231</small></p>",
                unsafe_allow_html=True)

st.divider()


# 4. Modal-Funktion für Dokumente
@st.dialog("Dokumenten-Vorschau")
def open_document(title):
    st.write(f"### {title}")
    st.info("Status: Offizielles Dokument der HV 2024")
    st.markdown("""
    **Lorem ipsum dolor sit amet**, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. 

    *   Punkt 1: Entlastung des Vorstands
    *   Punkt 2: Gewinnverwendung
    *   Punkt 3: Wahl des Abschlussprüfers

    At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.
    """)
    if st.button("Als PDF herunterladen"):
        st.toast("Download gestartet...")
        time.sleep(1)
        st.success("Datei gespeichert!")


# 5. Main Content Logic
if st.session_state.page == "Hauptversammlung":
    col_left, col_right = st.columns([2.5, 1])

    with col_left:
        st.markdown(f"#### 📺 Live-Übertragung")
        # Professioneller Video-Container
        st.video("https://www.youtube.com")

        with st.expander("Details zur Übertragung"):
            st.write("Sprecher: Dr. h.c. Hans Vorstand (Vorsitzender)")
            st.write("Thema: Jahresabschlussanalyse Q4/2023")

    with col_right:
        # Interaktive Sidebar-Box 1: Fragen
        st.markdown('<div class="sidebar-box">', unsafe_allow_html=True)
        st.markdown("##### 💬 Fragen an den Vorstand")
        q_text = st.text_area("Ihre Frage...", placeholder="Tippen Sie hier Ihre Frage zur Tagesordnung...", height=100)
        if st.button("Frage jetzt einreichen"):
            if q_text:
                with st.spinner('Übermittlung...'):
                    time.sleep(1.5)
                    st.success("Frage eingereicht! (Nr. #412)")
            else:
                st.warning("Bitte geben Sie einen Text ein.")
        st.markdown('</div>', unsafe_allow_html=True)

        # Interaktive Sidebar-Box 2: Dokumente mit Modal
        st.markdown('<div class="sidebar-box">', unsafe_allow_html=True)
        st.markdown("##### 📂 Relevante Unterlagen")
        st.caption("Klicken für Vorschau")

        if st.button("📄 Tagesordnung.pdf"):
            open_document("Tagesordnung - HV 2024")
        if st.button("📄 Geschäftsbericht.pdf"):
            open_document("Geschäftsbericht 2023")
        if st.button("📄 Abstimmungsregeln.pdf"):
            open_document("Leitfaden zur Abstimmung")
        st.markdown('</div>', unsafe_allow_html=True)

else:
    # Platzhalter für andere Seiten
    st.title(f"Bereich: {st.session_state.page}")
    st.info("Dieser Bereich wird geladen...")
    if st.button("Zurück zum Live-Stream"):
        st.session_state.page = "Hauptversammlung"
        st.rerun()

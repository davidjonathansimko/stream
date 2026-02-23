import streamlit as st
import time

# 1. Page Configuration
st.set_page_config(
    page_title="Investor Relations | Hauptversammlung 2024",
    page_icon="🏛️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. Professional Enterprise CSS
st.markdown("""
    <style>
    /* Global Styles */
    @import url('https://fonts.googleapis.com');
    html, body, [class*="st-"] { font-family: 'Inter', sans-serif; }
    .stApp { background-color: #fcfcfd; }

    /* Header & Navigation */
    .main-header {
        background-color: white;
        padding: 1rem 2rem;
        border-bottom: 1px solid #edf2f7;
        display: flex;
        justify-content: space-between;
        align-items: center;
        box-shadow: 0 2px 4px rgba(0,0,0,0.02);
    }

    /* Modern Cards (Sidebar-Boxen) */
    .ui-card {
        background: white;
        padding: 1.5rem;
        border-radius: 16px;
        border: 1px solid #f1f3f5;
        box-shadow: 0 10px 15px -3px rgba(0,0,0,0.05);
        margin-bottom: 1.5rem;
    }

    /* Status Badge */
    .live-badge {
        background-color: #fee2e2;
        color: #ef4444;
        padding: 4px 12px;
        border-radius: 20px;
        font-weight: 600;
        font-size: 12px;
        display: inline-block;
        margin-bottom: 8px;
        border: 1px solid #fecaca;
    }

    /* Professional Buttons */
    .stButton>button {
        border-radius: 10px;
        border: 1px solid #e2e8f0;
        background-color: white;
        color: #1e293b;
        font-weight: 500;
        height: 45px;
        transition: all 0.2s ease;
    }
    .stButton>button:hover {
        border-color: #3b82f6;
        color: #3b82f6;
        background-color: #eff6ff;
        transform: translateY(-1px);
    }

    /* Input Fields */
    .stTextArea textarea {
        border-radius: 10px;
        border: 1px solid #e2e8f0;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. State Management
if 'active_tab' not in st.session_state:
    st.session_state.active_tab = "Hauptversammlung"

# 4. Top Navigation Bar
with st.container():
    c1, c2, c3 = st.columns([1.5, 5, 2])
    with c1:
        st.markdown("## 🏢 **HV**2024")
    with c2:
        # Horizontales Menü
        tabs = st.columns(5)
        menu = ["Home", "Aktuelles", "Hauptversammlung", "Dokumente", "Konto"]
        for i, item in enumerate(menu):
            if tabs[i].button(item, key=f"btn_{item}", use_container_width=True):
                st.session_state.active_tab = item
    with c3:
        st.markdown(
            "<div style='text-align: right; padding-top: 10px;'><b>Max Mustermann</b><br><span style='color: #64748b; font-size: 0.8rem;'>Aktionär #4412-9</span></div>",
            unsafe_allow_html=True)

st.divider()


# 5. Modal für Dokumentenvorschau
@st.dialog("Dokumenten-Vorschau")
def show_doc(title):
    st.markdown(f"### {title}")
    st.caption("Veröffentlichung: 23. Februar 2024 | Version 1.2")
    st.markdown("---")
    st.markdown("""
    **Präambel:**

    *Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua.*

    **Inhaltliche Schwerpunkte:**
    1. Analyse der Marktpositionierung im Bereich Cloud-Services.
    2. Strategische Neuausrichtung der Logistikketten.
    3. Vorschlag zur Dividendenanpassung für das Fiskaljahr 2023.

    *At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.*
    """)
    if st.button("Dokument herunterladen (PDF)", type="primary"):
        st.toast("Download wird vorbereitet...")
        time.sleep(1)
        st.success("Download abgeschlossen.")


# 6. Main App Logic
if st.session_state.active_tab == "Hauptversammlung":
    left_col, right_col = st.columns([2.2, 1], gap="large")

    with left_col:
        st.markdown('<span class="live-badge">● LIVE ÜBERTRAGUNG</span>', unsafe_allow_html=True)
        st.markdown("### Strategische Ausrichtung & Jahresbericht")

        # High-Quality Video Placeholder
        st.video("https://www.youtube.com")

        # Speaker Info Card
        with st.expander("Informationen zum aktuellen Sprecher", expanded=True):
            st.markdown("""
            **Referent:** Dr. h.c. Sarah Schmidt-Verley  
            **Position:** Chief Financial Officer (CFO)  
            **Thema:** Finanzielle Performance und Nachhaltigkeitsbericht 2023
            """)

    with right_col:
        # Card 1: Fragen
        st.markdown('<div class="ui-card">', unsafe_allow_html=True)
        st.markdown("#### 💬 Dialog & Fragen")
        st.write("Stellen Sie Ihre Frage direkt an das Präsidium.")
        q = st.text_area("Ihre Anfrage", placeholder="Formulieren Sie hier Ihre Frage...", height=120,
                         label_visibility="collapsed")
        if st.button("Frage jetzt einreichen", type="primary", use_container_width=True):
            if q:
                with st.spinner("Wird übermittelt..."):
                    time.sleep(1)
                    st.success("Übermittelt. Ihre Frage wurde der Warteschlange hinzugefügt.")
            else:
                st.error("Bitte Text eingeben.")
        st.markdown('</div>', unsafe_allow_html=True)

        # Card 2: Dokumente
        st.markdown('<div class="ui-card">', unsafe_allow_html=True)
        st.markdown("#### 📂 Begleitunterlagen")
        st.write("Relevante Dokumente zur aktuellen Sitzung.")
        if st.button("📋 Tagesordnung & Agenda", use_container_width=True):
            show_doc("Tagesordnung & Agenda")
        if st.button("📊 Quartalszahlen Q4 (PDF)", use_container_width=True):
            show_doc("Quartalszahlen Q4 / 2023")
        if st.button("⚖️ Satzungsänderung v2", use_container_width=True):
            show_doc("Vorschlag zur Satzungsänderung")
        st.markdown('</div>', unsafe_allow_html=True)

else:
    # Andere Seiten Simulation
    st.container()
    st.title(f"Portal-Bereich: {st.session_state.active_tab}")
    st.info("Dieses Modul wird gerade für Ihren Account synchronisiert.")
    if st.button("← Zurück zur Übertragung"):
        st.session_state.active_tab = "Hauptversammlung"
        st.rerun()

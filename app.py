import streamlit as st
import time
import random

# 1. Konfiguration für Full-Width & Auto-Stretch
st.set_page_config(page_title="Investor Relations Portal", layout="wide", initial_sidebar_state="collapsed")

# 2. Advanced CSS für ein nahtloses "One-Page" Design
st.markdown("""
    <style>
    /* Hintergrund und globale Schrift */
    @import url('https://fonts.googleapis.com');
    html, body, [class*="st-"] { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; }
    .stApp { background-color: #f4f7f9; }

    /* Fixiertes Layout ohne Scrollen */
    .block-container { padding-top: 1rem; padding-bottom: 0rem; height: 100vh; }

    /* Moderne Karten-Optik */
    .ui-card {
        background: white;
        padding: 1.5rem;
        border-radius: 12px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05);
        border: 1px solid #e1e4e8;
        height: 100%;
    }

    /* Live Badge Pulsierend */
    .live-indicator {
        background: #ff4b4b;
        color: white;
        padding: 2px 10px;
        border-radius: 4px;
        font-size: 11px;
        font-weight: bold;
        animation: blink 2s infinite;
    }
    @keyframes blink { 0% {opacity: 1;} 50% {opacity: 0.5;} 100% {opacity: 1;} }

    /* Button Styling */
    .stButton>button {
        border-radius: 8px;
        font-weight: 600;
        transition: all 0.2s;
        border: 1px solid #d1d5db;
    }
    .stButton>button:hover {
        border-color: #007bff;
        color: #007bff;
        background: #f0f7ff;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Session State für Chat-Verlauf und User
if 'messages' not in st.session_state:
    st.session_state.messages = []
if 'user_name' not in st.session_state:
    st.session_state.user_name = "Max Mustermann"

# 4. Header (Top Navigation)
with st.container():
    h_col1, h_col2, h_col3 = st.columns([1, 4, 1.5])
    with h_col1:
        st.markdown("### 🏛️ IR-PORTAL")
    with h_col2:
        st.write("")  # Platzhalter
    with h_col3:
        st.markdown(
            f"<div style='text-align:right;'><b>{st.session_state.user_name}</b><br><small>Aktionär ID: #4412-0</small></div>",
            unsafe_allow_html=True)

st.divider()

# 5. Haupt-Dashboard (Zwei Spalten Layout)
col_stream, col_interact = st.columns([2, 1], gap="medium")

# --- LINKE SPALTE: STREAM ---
with col_stream:
    st.markdown('<div class="ui-card">', unsafe_allow_html=True)
    st.markdown('<span class="live-indicator">LIVE</span> <b>HAUPTVERSAMMLUNG 2024</b>', unsafe_allow_html=True)

    # Video mit Auto-Stretch (Streamlit macht das automatisch)
    st.video("https://www.youtube.com")

    st.markdown("#### Aktueller Tagesordnungspunkt")
    st.info("**TOP 3:** Bericht des Vorstands über das Geschäftsjahr 2023 und Ausblick 2024.")
    st.markdown('</div>', unsafe_allow_html=True)

# --- RECHTE SPALTE: INTERAKTION ---
with col_interact:
    # BOX 1: Interaktive Fragen (Mockup-Chat)
    st.markdown('<div class="ui-card">', unsafe_allow_html=True)
    st.markdown("#### 💬 Live-Fragen")

    # Chat-Verlauf Anzeige
    chat_container = st.container(height=250)
    for msg in st.session_state.messages:
        with chat_container.chat_message(msg["role"]):
            st.write(f"**{msg['author']}:** {msg['content']}")

    # Eingabefeld
    if prompt := st.chat_input("Formulieren Sie hier Ihre Frage..."):
        # User Nachricht hinzufügen
        st.session_state.messages.append({"role": "user", "author": st.session_state.user_name, "content": prompt})

        # Automatische Antwort generieren
        with st.spinner("Vorstand tippt..."):
            time.sleep(2)
            responses = [
                "Vielen Dank für Ihre Frage. Wir werden diese im nächsten Q&A-Block behandeln.",
                "Eine sehr relevante Frage! Der CFO wird darauf gleich im Detail eingehen.",
                "Dazu finden Sie detaillierte Informationen auf Seite 42 des Geschäftsberichts.",
                "Ihre Anfrage wurde an das Protokoll-Team weitergeleitet."
            ]
            bot_msg = random.choice(responses)
            st.session_state.messages.append({"role": "assistant", "author": "System-Bot", "content": bot_msg})
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

    st.write("")  # Spacer

    # BOX 2: Dokumente
    st.markdown('<div class="ui-card">', unsafe_allow_html=True)
    st.markdown("#### 📂 Unterlagen")

    d1, d2 = st.columns(2)
    if d1.button("📄 Tagesordnung", use_container_width=True):
        st.toast("Öffne Tagesordnung...")
    if d2.button("📊 Q4 Bericht", use_container_width=True):
        st.toast("Öffne Quartalszahlen...")

    if st.button("⚖️ Abstimmungsregeln einsehen", use_container_width=True):
        st.toast("Lade PDF...")
    st.markdown('</div>', unsafe_allow_html=True)

# 6. Footer (Mini)
st.markdown(
    "<div style='text-align:center; padding-top: 20px; font-size: 10px; color: gray;'>© 2024 Investor Relations Service Plattform - Alle Rechte vorbehalten</div>",
    unsafe_allow_html=True)

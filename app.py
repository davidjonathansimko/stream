import streamlit as st
import random
import time

# 1. Konfiguration für Full-Screen (Auto-Stretch)
st.set_page_config(page_title="HV 2024 Portal", layout="wide", initial_sidebar_state="collapsed")

# 2. "Perfekt-Design" CSS (Kein Scrollen, Corporate Look)
st.markdown("""
    <style>
    /* Versteckt Standard-Header und Footer */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* Hintergrund & Font */
    .stApp { background-color: #F8FAFC; font-family: 'Inter', sans-serif; }

    /* One-Page Layout: Verhindert vertikales Scrollen */
    .block-container { padding: 1rem 2rem; max-height: 100vh; overflow: hidden; }

    /* Card Design */
    .card {
        background: white;
        padding: 1.5rem;
        border-radius: 12px;
        border: 1px solid #E2E8F0;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
        height: 100%;
    }

    /* Live Pulsator */
    .live-dot {
        height: 10px; width: 10px; background-color: #EF4444;
        border-radius: 50%; display: inline-block; margin-right: 5px;
        animation: blinker 1.5s linear infinite;
    }
    @keyframes blinker { 50% { opacity: 0; } }
    </style>
    """, unsafe_allow_html=True)

# 3. Session State für Chat & User
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
user_name = "Max Mustermann"  # Dein Account Name

# 4. Header Bar
h1, h2 = st.columns([1, 1])
with h1:
    st.markdown(f"### 🏛️ **HV**2024 <small>| Hauptversammlung</small>", unsafe_allow_html=True)
with h2:
    st.markdown(
        f"<div style='text-align: right;'><b>{user_name}</b><br><span style='color: #64748B; font-size: 0.8rem;'>Aktionär ID: #4412-0</span></div>",
        unsafe_allow_html=True)

st.divider()

# 5. Dashboard Spalten (Links: Stream | Rechts: Interaktion)
# Das Verhältnis [3, 1] sorgt für den "Auto-Stretch" Effekt des Videos
col_left, col_right = st.columns([3, 1.2], gap="large")

with col_left:
    st.markdown('<div class="live-dot"></div><b>LIVE-ÜBERTRAGUNG</b>', unsafe_allow_html=True)
    # Video skaliert automatisch auf Spaltenbreite
    st.video("https://www.youtube.com")

    # Infobox unter dem Video
    st.info("**Aktueller Sprecher:** Dr. h.c. Hans Vorstand — *Tagesordnungspunkt 3: Entlastung*")

with col_right:
    # --- FRAGEN SEKTION (CHAT MOCKUP) ---
    st.markdown("#### 💬 Fragen an den Vorstand")

    # Chat-Verlauf mit fester Höhe (verhindert Scrollen der ganzen Seite)
    chat_box = st.container(height=300)
    for msg in st.session_state.chat_history:
        with chat_box.chat_message(msg["role"]):
            st.write(f"**{msg['user']}:** {msg}")

    # Eingabefeld
    if prompt := st.chat_input("Ihre Frage..."):
        # User Frage hinzufügen
        st.session_state.chat_history.append({"role": "user", "user": user_name, "text": prompt})

        # Automatische Antwort generieren (Random Mockup)
        responses = [
            "Vielen Dank. Wir nehmen Ihre Frage in die Liste auf.",
            "Der Vorstand wird diesen Punkt im nächsten Abschnitt erläutern.",
            "Ihre Frage wurde erfolgreich an das Präsidium übermittelt.",
            "Dazu finden Sie Details im Geschäftsbericht (S. 14)."
        ]
        time.sleep(1)  # Simulation
        st.session_state.chat_history.append({"role": "assistant", "user": "System", "text": random.choice(responses)})
        st.rerun()

    st.write("---")

    # --- DOKUMENTE SEKTION ---
    st.markdown("#### 📂 Dokumente")
    d_col1, d_col2 = st.columns(2)
    with d_col1:
        st.button("📄 Agenda", use_container_width=True)
    with d_col2:
        st.button("📊 Bericht", use_container_width=True)
    st.button("⚖️ Abstimmungsregeln (PDF)", use_container_width=True)

# 6. Footer (nur Text)
st.markdown(
    "<p style='text-align: center; color: #94A3B8; font-size: 0.7rem; margin-top: 1rem;'>Sichere Verbindung | © 2024 AG Service Portal</p>",
    unsafe_allow_html=True)

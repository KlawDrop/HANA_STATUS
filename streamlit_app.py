import streamlit as st
from PIL import Image

# Configurer la page
st.set_page_config(layout="wide")

# Ajouter du CSS personnalisé pour un meilleur style
st.markdown(
    """
    <style>
    body {
        background-color: black;
        color: white;
    }
    h1, h2 {
        text-align: center;
        color: white;
    }
    .status-table {
        margin-left: auto;
        margin-right: auto;
        width: 50%;
    }
    .status-table th, .status-table td {
        padding: 10px;
        text-align: left;
    }
    .status-table th {
        background-color: #333;
    }
    .status-table td {
        background-color: #222;
    }
    .status-online {
        color: #00FF00;
    }
    .status-updating {
        color: #FFA500;
    }
    .centered {
        display: flex;
        justify-content: center;
        align-items: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)
# Utilisation des colonnes pour le centrage
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st.markdown("<h1>Status</h1>", unsafe_allow_html=True)

# Status pour MWIII
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st.markdown("<h2>MWIII</h2>", unsafe_allow_html=True)

    # Créer la table de statuts
    mwiii_data = [
        ["IRIS CHAIR + WOOFER", "online"],
        ["IRIS CHAIR + WOOFER V2", "online"],
        ["IRIS UA + WOOFER V3", "updating"],
        ["IRIS AIO + WOOFER", "updating"],
        ["IRIS PRIVACY PROTECTOR", "online"],
    ]

    st.markdown("<table class='status-table'>", unsafe_allow_html=True)
    st.markdown("<tr><th>Loaders</th><th>Status</th></tr>", unsafe_allow_html=True)

    for loader, status in mwiii_data:
        status_color = "status-online" if status == "online" else "status-updating"
        st.markdown(f"<tr><td>{loader}</td><td class='{status_color}'>{status}</td></tr>", unsafe_allow_html=True)

    st.markdown("</table>", unsafe_allow_html=True)

# Status pour MW2019
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st.markdown("<h2>MW2019</h2>", unsafe_allow_html=True)

    # Créer la table de statuts pour MW2019
    mw2019_data = [
        ["MW19 AIO CHAIR", "online"],
    ]

    st.markdown("<table class='status-table'>", unsafe_allow_html=True)
    st.markdown("<tr><th>Loaders</th><th>Status</th></tr>", unsafe_allow_html=True)

    for loader, status in mw2019_data:
        status_color = "status-online" if status == "online" else "status-updating"
        st.markdown(f"<tr><td>{loader}</td><td class='{status_color}'>{status}</td></tr>", unsafe_allow_html=True)

    st.markdown("</table>", unsafe_allow_html=True)

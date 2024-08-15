import streamlit as st
from PIL import Image

# Set page config
st.set_page_config(layout="wide")

# Custom CSS for styling
st.markdown(
    """
    <style>
    body {
        background-color: black;
        color: white;
    }
    .centered {
        text-align: center;
    }
    .status-table {
        margin-left: auto;
        margin-right: auto;
        width: 50%;
    }
    .status-table table {
        width: 100%;
        border-collapse: collapse;
        margin-bottom: 20px;
    }
    .status-table th, .status-table td {
        padding: 10px;
        text-align: left;
        border-bottom: 1px solid #ddd;
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
    .eye-logo {
        width: 100px;
        display: block;
        margin-left: auto;
        margin-right: auto;
    }
    </style>
    """,
    unsafe_allow_html=True
)


st.markdown("<h1 class='centered'>Status</h1>", unsafe_allow_html=True)

# Status for MWIII
st.markdown("<h2 class='centered'>MWIII</h2>", unsafe_allow_html=True)

mwiii_data = [
    ["IRIS CHAIR + WOOFER", "online"],
    ["IRIS CHAIR + WOOFER V2", "online"],
    ["IRIS UA + WOOFER V3", "updating"],
    ["IRIS AIO + WOOFER", "updating"],
    ["IRIS PRIVACY PROTECTOR", "online"],
]

# Create a custom table layout
st.markdown("<div class='status-table'>", unsafe_allow_html=True)
st.markdown("<table>", unsafe_allow_html=True)
st.markdown("<tr><th>Loaders</th><th>Status</th></tr>", unsafe_allow_html=True)

for loader, status in mwiii_data:
    status_color = "status-online" if status == "online" else "status-updating"
    st.markdown(f"<tr><td>{loader}</td><td class='{status_color}'>{status}</td></tr>", unsafe_allow_html=True)

st.markdown("</table>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# Status for MW2019
st.markdown("<h2 class='centered'>MW2019</h2>", unsafe_allow_html=True)

mw2019_data = [
    ["MW19 AIO CHAIR", "online"],
]

# Create a custom table layout
st.markdown("<div class='status-table'>", unsafe_allow_html=True)
st.markdown("<table>", unsafe_allow_html=True)
st.markdown("<tr><th>Loaders</th><th>Status</th></tr>", unsafe_allow_html=True)

for loader, status in mw2019_data:
    status_color = "status-online" if status == "online" else "status-updating"
    st.markdown(f"<tr><td>{loader}</td><td class='{status_color}'>{status}</td></tr>", unsafe_allow_html=True)

st.markdown("</table>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

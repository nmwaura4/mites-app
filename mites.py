import streamlit as st
import pandas as pd
import numpy as np

st.title("🕷️ Predator Finder & Analysis App")
st.set_page_config(
    page_title="Predator Finder & Analysis App",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ---------------- STATE ----------------
if "submitted" not in st.session_state:
    st.session_state.submitted = False

# ---------------- INPUT FORM ----------------
if not st.session_state.submitted:

    st.subheader("🔎 Enter Search Criteria")

    # IMPORTANT: match values with dataset exactly
    search_size = st.selectbox("Size", ["small", "medium", "big"])
    search_shape = st.selectbox("Shape", ["pear_shaped", "oval_to_teardrop", "broad_oval", "oval_slender"])
    search_colour = st.selectbox("Colour", ["grey", "light_tan", "beige_tan", "cream_tan"])
    search_aggressive = st.selectbox("Aggressive?", ["True", "False"])
    search_development_speed = st.selectbox("Development Speed", ["fast", "moderate", "slow"])

    if st.button("Find Predator"):
        st.session_state.search_size = search_size
        st.session_state.search_shape = search_shape
        st.session_state.search_colour = search_colour
        st.session_state.search_aggressive = (search_aggressive == "True")
        st.session_state.search_development_speed = search_development_speed
        st.session_state.submitted = True
        st.rerun()

# ---------------- RESULT SECTION ----------------
else:
    st.subheader("📊 Result")

    # ---------------- CLASS ----------------
    class Predator:
        def __init__(self, name, size, shape, colour, aggressive, development_speed):
            self.name = name
            self.size = size
            self.shape = shape
            self.colour = colour
            self.aggressive = aggressive
            self.development_speed = development_speed

    # ---------------- DATA ----------------
    def get_calif():
        return Predator(
            "Neoseiulus californicus",
            "medium",
            "oval_to_teardrop",
            "grey",
            False,
            "moderate"
        )

    def get_monty():
        return Predator(
            "Typhlodromaris montdorensis",
            "medium",
            "oval_slender",
            "cream_tan",
            True,
            "fast"
        )

    def get_cucumeris():
        return Predator(
            "Amblyseius cucumeris",
            "medium",
            "pear_shaped",
            "beige_tan",
            False,
            "moderate"
        )

    def get_swirskii():
        return Predator(
            "Amblyseius swirskii",
            "medium",
            "broad_oval",
            "light_tan",
            True,
            "fast"
        )

    predators = [
        get_calif(),
        get_monty(),
        get_cucumeris(),
        get_swirskii()
    ]

    # ---------------- SEARCH ----------------
    found = None

    for p in predators:
        if (
            p.size == st.session_state.search_size and
            p.shape == st.session_state.search_shape and
            p.colour == st.session_state.search_colour and
            p.aggressive == st.session_state.search_aggressive and
            p.development_speed == st.session_state.search_development_speed
        ):
            found = p
            break

    # ---------------- RESULT ----------------
    if found:
        st.success(f"Identified Predator: {found.name}")

        st.write("### Details")
        st.write(f"Size: {found.size}")
        st.write(f"Shape: {found.shape}")
        st.write(f"Colour: {found.colour}")
        st.write(f"Aggressive: {found.aggressive}")
        st.write(f"Development Speed: {found.development_speed}")

    else:
        st.error("No predator found")

    # ---------------- RESET ----------------
    if st.button("🔄 New Search"):
        st.session_state.submitted = False
        st.rerun()
import math
import streamlit as st

st.set_page_config(
    page_title="Yarn Count Calculator",
    page_icon="🧵",
    layout="wide"
)

st.markdown("""
<style>
.stApp {
    background-color: #f5f7fb;
}
h1 {
    color: #153e75;
}
h2, h3 {
    color: #245b8f;
}
div.stButton > button {
    background-color: #153e75;
    color: white;
    border-radius: 8px;
    min-height: 45px;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

st.title("🧵 Yarn Count Calculator")
st.caption("A Textile Engineering Tool | Calculate and Convert Yarn Count")
st.divider()

COUNT_SYSTEMS = [
    "Tex",
    "Denier",
    "dtex",
    "Metric Count (Nm)",
    "English Cotton Count (Ne)",
    "Worsted Count (Nw)",
    "Woollen Count (Yorkshire)",
]


def get_counts(tex):
    """Convert Tex into common yarn count systems."""
    if not math.isfinite(tex) or tex <= 0:
        raise ValueError("Yarn count must be a positive number.")

    return {
        "Tex": tex,
        "Denier": tex * 9,
        "dtex": tex * 10,
        "Metric Count (Nm)": 1000 / tex,
        "English Cotton Count (Ne)": 590.541 / tex,
        "Worsted Count (Nw)": 885.8 / tex,
        "Woollen Count (Yorkshire)": 406.4 / tex,
    }


def show_counts(counts):
    st.subheader("Calculated Yarn Counts")

    columns = st.columns(2)

    for index, name in enumerate(COUNT_SYSTEMS):
        with columns[index % 2]:
            st.metric(name, f"{counts[name]:,.4f}")

    st.success("Calculation completed successfully.")


mode = st.radio(
    "Select Calculation Mode",
    ["Length & Weight Calculator", "Yarn Count Converter"],
    horizontal=True
)

if mode == "Length & Weight Calculator":

    st.subheader("Calculate Yarn Count from Length and Weight")
    st.write("Enter the yarn length and its corresponding weight.")

    col1, col2 = st.columns(2)

    with col1:
        length = st.number_input(
            "Yarn Length",
            min_value=0.0,
            value=1000.0,
            step=100.0,
            format="%.4f"
        )

        length_unit = st.selectbox(
            "Length Unit",
            [
                "meter (m)",
                "kilometer (km)",
                "yard (yd)",
                "foot (ft)",
                "centimeter (cm)"
            ]
        )

    with col2:
        weight = st.number_input(
            "Yarn Weight",
            min_value=0.0,
            value=1.0,
            step=0.1,
            format="%.4f"
        )

        weight_unit = st.selectbox(
            "Weight Unit",
            [
                "gram (g)",
                "kilogram (kg)",
                "milligram (mg)",
                "pound (lb)",
                "ounce (oz)"
            ]
        )

    if st.button("Calculate Yarn Count", use_container_width=True):

        if length <= 0 or weight <= 0:
            st.error(
                "Length and weight must both be greater than zero."
            )
        else:
            length_factors = {
                "meter (m)": 1.0,
                "kilometer (km)": 1000.0,
                "yard (yd)": 0.9144,
                "foot (ft)": 0.3048,
                "centimeter (cm)": 0.01,
            }

            weight_factors = {
                "gram (g)": 1.0,
                "kilogram (kg)": 1000.0,
                "milligram (mg)": 0.001,
                "pound (lb)": 453.59237,
                "ounce (oz)": 28.349523125,
            }

            try:
                length_m = length * length_factors[length_unit]
                weight_g = weight * weight_factors[weight_unit]

                if (
                    not math.isfinite(length_m)
                    or not math.isfinite(weight_g)
                    or length_m <= 0
                    or weight_g <= 0
                ):
                    raise ValueError(
                        "Converted length and weight must be valid "
                        "positive numbers."
                    )

                tex = (weight_g / length_m) * 1000
                counts = get_counts(tex)

                st.markdown("### Primary Result")
                st.metric("Yarn Count (Tex)", f"{tex:,.4f}")

                show_counts(counts)

                st.info(
                    f"**Formula:** Tex = Weight (g) / Length (m) × 1000\n\n"
                    f"**Converted length:** {length_m:,.4f} m\n\n"
                    f"**Converted weight:** {weight_g:,.4f} g"
                )

            except (ValueError, OverflowError, ZeroDivisionError):
                st.error(
                    "Unable to calculate. Please check the entered values."
                )

else:
    st.subheader("Convert an Existing Yarn Count")

    count_type = st.selectbox(
        "Select Existing Count System",
        COUNT_SYSTEMS
    )

    count_value = st.number_input(
        "Enter Yarn Count",
        min_value=0.0,
        value=20.0,
        step=1.0,
        format="%.6f"
    )

    if st.button("Convert Yarn Count", use_container_width=True):

        if count_value <= 0 or not math.isfinite(count_value):
            st.error("Please enter a valid count greater than zero.")
        else:
            try:
                # Convert the selected count into Tex.
                conversion_to_tex = {
                    "Tex": lambda x: x,
                    "Denier": lambda x: x / 9,
                    "dtex": lambda x: x / 10,
                    "Metric Count (Nm)": lambda x: 1000 / x,
                    "English Cotton Count (Ne)": lambda x: 590.541 / x,
                    "Worsted Count (Nw)": lambda x: 885.8 / x,
                    "Woollen Count (Yorkshire)": lambda x: 406.4 / x,
                }

                tex = conversion_to_tex[count_type](count_value)
                counts = get_counts(tex)

                st.markdown("### Conversion Results")
                st.metric("Equivalent Tex", f"{tex:,.4f}")

                show_counts(counts)

            except (ValueError, OverflowError, ZeroDivisionError):
                st.error(
                    "Conversion failed. Please check your count value."
                )

st.divider()

with st.expander("View Formulas"):
    st.markdown("""
    **Direct Count Systems**

    - Tex = Weight (g) / Length (m) × 1000
    - Denier = Weight (g) / Length (m) × 9000
    - dtex = Weight (g) / Length (m) × 10000

    **Indirect Count Systems**

    - Nm = 1000 / Tex
    - Ne ≈ 590.541 / Tex
    - Worsted Count (Nw) ≈ 885.8 / Tex
    - Yorkshire Woollen Count ≈ 406.4 / Tex

    **Important:** Worsted and Yorkshire woollen conversions use
    conventional approximate constants. Verify the count convention
    used by your textile laboratory or course.
    """)

st.caption(
    "Yarn Count Calculator | Educational Tool for Textile Engineering"
)

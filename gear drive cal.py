import streamlit as st

st.set_page_config(page_title="Gear Drive Calculator", page_icon="⚙️")

st.title("⚙️ Gear Drive Calculator")

# Sidebar or Tab selection for different calculations
calculation_type = st.sidebar.radio(
    "Choose Calculation",
    [
        "1. Calculate Gear Ratio",
        "2. Calculate Output Speed",
        "3. Calculate Torque Ratio",
        "4. Find Driven Gear Teeth"
    ]
)

st.markdown("---")

if calculation_type == "1. Calculate Gear Ratio":
    st.header("Calculate Gear Ratio")
    
    driver = st.number_input("Enter driver gear teeth:", min_value=1, step=1, value=10)
    driven = st.number_input("Enter driven gear teeth:", min_value=1, step=1, value=20)
    
    if st.button("Calculate Ratio"):
        ratio = driven / driver
        st.success(f"**Gear Ratio:** {round(ratio, 2)}")

elif calculation_type == "2. Calculate Output Speed":
    st.header("Calculate Output Speed")
    
    input_speed = st.number_input("Enter input speed (RPM):", min_value=0.0, step=10.0, value=1000.0)
    driver = st.number_input("Enter driver gear teeth:", min_value=1, step=1, value=10)
    driven = st.number_input("Enter driven gear teeth:", min_value=1, step=1, value=20)
    
    if st.button("Calculate Speed"):
        output_speed = input_speed * driver / driven
        st.success(f"**Output Speed:** {round(output_speed, 2)} RPM")

elif calculation_type == "3. Calculate Torque Ratio":
    st.header("Calculate Torque Ratio")
    
    driver = st.number_input("Enter driver gear teeth:", min_value=1, step=1, value=10)
    driven = st.number_input("Enter driven gear teeth:", min_value=1, step=1, value=20)
    
    if st.button("Calculate Torque Ratio"):
        torque_ratio = driven / driver
        st.success(f"**Torque Ratio:** {round(torque_ratio, 2)}")

elif calculation_type == "4. Find Driven Gear Teeth":
    st.header("Find Driven Gear Teeth")
    
    driver = st.number_input("Enter driver gear teeth:", min_value=1, step=1, value=10)
    desired_ratio = st.number_input("Enter required gear ratio:", min_value=0.01, step=0.1, value=2.0)
    
    if st.button("Calculate Teeth"):
        teeth = driver * desired_ratio
        st.success(f"**Required driven gear teeth:** {round(teeth, 2)}")
        st.info("💡 *Use a whole number of teeth in practice.*")

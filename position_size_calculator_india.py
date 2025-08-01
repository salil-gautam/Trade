
import streamlit as st

st.set_page_config(page_title="Position Size Calculator (India)", layout="centered")

st.title("📈 Position Size Calculator-Salil")
st.markdown("Stop Loss is based on **option premium**, not spot price.")

capital = st.number_input("Capital (₹)", min_value=0, value=100000, step=1000)
risk_percent = st.number_input("Risk per Trade (%)", min_value=0.0, max_value=100.0, value=2.0, step=0.1)
sl_premium = st.number_input("Stop Loss (On Option Premium)", min_value=0.0, value=30.0, step=1.0)
lot_size = st.number_input("Lot Size", min_value=1, value=75, step=1)
premium = st.number_input("Option Premium (Current Price)", min_value=0.0, value=800.0, step=1.0)

if sl_premium > 0 and lot_size > 0 and capital > 0 and risk_percent > 0:
    risk_amount = capital * (risk_percent / 100)
    risk_per_lot = sl_premium * lot_size
    lots_by_risk = int(risk_amount // risk_per_lot)

    st.markdown(f"### 🧮 Results")
    st.write(f"**Risk Amount:** ₹{risk_amount:,.2f}")
    st.write(f"**Risk per Lot:** ₹{risk_per_lot:,.2f}")
    st.write(f"**Max Lots by Risk:** {lots_by_risk}")

    if premium > 0:
        capital_per_lot = premium * lot_size
        lots_by_capital = int(capital // capital_per_lot)
        final_lots = min(lots_by_risk, lots_by_capital)
        capital_deployed = final_lots * capital_per_lot
        total_size = final_lots * lot_size

        st.write(f"**Capital per Lot (Premium × Lot Size):** ₹{capital_per_lot:,.2f}")
        st.write(f"**Max Lots by Capital:** {lots_by_capital}")
        st.write(f"✅ **Final Tradable Lots:** {final_lots}")
        st.write(f"📦 **Total Size (Final Lots × Lot Size):** {total_size} units")
        st.success(f"💰 **Capital Deployed:** ₹{capital_deployed:,.2f}")
    else:
        total_size = lots_by_risk * lot_size
        st.write(f"📦 **Total Size (Lots × Lot Size):** {total_size} units")
        st.success(f"✅ Final Tradable Lots (by risk only): {lots_by_risk}")
else:
    st.warning("Please fill in all required fields.")


import streamlit as st
import pandas as pd

st.title("🧠 Aviator Game Pattern Analyzer")

uploaded = st.file_uploader("📥 Upload Aviator Data (CSV)", type="csv")
if uploaded:
    df = pd.read_csv(uploaded)
    st.write("📊 First few rounds of your data:")
    st.write(df.head())
    
    # Moving Average Calculation
    df['MA_5'] = df['Crash Multiplier'].rolling(window=5).mean()
    st.line_chart(df[['Crash Multiplier', 'MA_5']])
    
    # Summary
    low = (df['Crash Multiplier'] <= 1.5).sum()
    high = (df['Crash Multiplier'] > 1.5).sum()
    avg = round(df['Crash Multiplier'].mean(), 2)
    max_val = df['Crash Multiplier'].max()
    min_val = df['Crash Multiplier'].min()
    
    st.markdown(f"""
- 🎯 **Total Rounds:** {len(df)}
- 🔴 **Low Crashes (≤1.5x):** {low}
- 🟢 **High Crashes (>1.5x):** {high}
- 📈 **Average Multiplier:** {avg}×
- 🚀 **Max Multiplier:** {max_val}×
- 💥 **Min Multiplier:** {min_val}×
""")
else:
    st.info("Upload a CSV file with a column named 'Crash Multiplier'.")

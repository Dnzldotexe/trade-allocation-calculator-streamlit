"""
n
"""
# n
import streamlit as st


# n
st.set_page_config(page_title="Degen Calculator", page_icon=":money_mouth_face:")


def size_calculator(balance: float, risk: int, leverage: int, stop_loss: int) -> float:
    """
    n
    """
    # n
    allocation = balance * (risk/100)
    
    # n
    size = allocation / ((leverage * stop_loss)/100)
    
    # n
    return float(f"{size:.1f}")


def main() -> None:
    """
    n
    """
    # n
    st.title("Your Position Size Calculator")

    # n
    balance = st.number_input(
        "Balance in USDT ($)",
        value=100
    )

    # n
    risk = st.number_input(
        "Risk in Percentage (%)",
        value=1
    )

    # n
    leverage = st.number_input(
        "Leverage (i.e. 100x, 75x, 50x, 10x)",
        value=100
    )
    
    # n
    stop_loss = st.number_input(
        "Stop Loss in Percentage (%)",
        value=0.30
    )

    # n
    if st.button("Calculate"):
        # n
        calculated_size = size_calculator(balance, risk, leverage, stop_loss)

        # n
        st.code(calculated_size)


# Run main function
if __name__ == "__main__":
    main()

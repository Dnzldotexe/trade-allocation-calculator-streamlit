"""
This python application is made to calculate the proper trading size with variable risk, leverage, and stop loss
"""
# Import streamlit framework
import streamlit as st


# Set the page title and page icon
st.set_page_config(page_title="Degen Calculator", page_icon=":money_mouth_face:")


def size_calculator(balance: float, risk: int, leverage: int, stop_loss: int) -> float:
    """
    Calculate the trading size based on four parameters
    """
    # Calculate allocation
    allocation = balance * (risk/100)
    
    # Calculate size
    size = allocation / ((leverage * stop_loss)/100)
    
    # Return size in float datatype
    return float(f"{size:.1f}")


def main() -> None:
    """
    Display the UI of the application and accept inputs from the user
    """
    # Show a title
    st.title("Your Position Size Calculator")

    # Get balance from the user
    balance = st.number_input(
        "Balance in USDT ($)",
        value=100
    )

    # Get risk from the user
    risk = st.number_input(
        "Risk in Percentage (%)",
        value=1
    )

    # Get leverage from the user
    leverage = st.number_input(
        "Leverage (i.e. 100x, 75x, 50x, 10x)",
        value=100
    )
    
    # Get stop loss from the user
    stop_loss = st.number_input(
        "Stop Loss in Percentage (%)",
        value=0.30
    )

    # Calculate button
    if st.button("Calculate"):
        # Store the output of the function call
        calculated_size = size_calculator(balance, risk, leverage, stop_loss)

        # Print the output
        st.code(calculated_size)


# Run main function
if __name__ == "__main__":
    main()

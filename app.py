import streamlit as st
from factorial import fact

def main():
    st.title("Basic Computing App")
    st.header("Calculating Factorial")
    st.write ("This application allows you to calculate factorial of a number")

    number = st.number_input("Input a value", min_value=0, max_value=20, value=0, step=1)

    if st.button("Calculate"):
        factorial = fact(number)
        st.write(f"The factorial: {number}! = {factorial}")

if __name__ == "__main__":
    main()
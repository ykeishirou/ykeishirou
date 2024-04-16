import streamlit as st
import random

def spin_slots():
    symbols = ["🍒", "🍊", "🍋", "🍇", "🍉"]
    result = [random.choice(symbols) for _ in range(3)]
    return result

def main():
    st.title("スロットゲーム")

    if st.button("スロットを回す"):
        slot_result = spin_slots()
        st.write(slot_result)

        if len(set(slot_result)) == 1:
            st.success("おめでとうございます！ジャックポットです！")
        elif len(set(slot_result)) == 2:
            st.warning("2つ揃いました！")
        else:
            st.error("残念！もう一度トライしましょう！")

if __name__ == "__main__":
    main()

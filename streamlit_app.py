import streamlit as st
import random

# スロットを回転させる関数
def spin_slots():
    symbols = ["🍒", "🍊", "🍋", "🍇", "🍉", "🍎", "🍓", "🍍", "🍐", "🥝"] + ["💎", "🔔", "💰", "🍀", "🎰", "🎲", "🃏", "🎯", "🎮", "🎈"] + ["🎁", "🚀", "🌈", "🌟", "🎈", "🎉", "🎊", "🎆", "🎇", "🎶"] + ["💡", "🔥", "💧", "🌊", "🌪️", "❄️", "☀️", "🌙", "⭐", "🌠"] + ["🍔", "🍕", "🍟", "🥪", "🍣", "🍦", "🍩", "🍪", "🍫", "🍬"] + ["🍭", "🥤", "🍺", "🍷", "🍸", "🍹", "🍾", "🥃", "🍯", "🥛"] + ["🍼", "☕", "🍵", "🥤", "🍻", "🥂", "🧊", "🧃", "🥤", "🍶"] + ["🍿", "🍦", "🍨", "🥧", "🍰", "🧁", "🎂", "🍧", "🍡", "🍭"] + ["🥠", "🍥", "🍙", "🍘", "🍣", "🍤", "🍱", "🍛", "🍚", "🍜"] + ["🍲", "🍢", "🍡", "🥮", "🍦", "🧆", "🥟", "🍺", "🍻", "🍷"] + ["🍾", "🍸", "🍹", "🍼", "🥂", "🍽️", "🍴", "🥢", "🧂", "🥄"]
    result = [random.choice(symbols) for _ in range(3)]
    return result

# メインのStreamlitアプリケーション
def main():
    st.title("スロットゲーム")
    st.write("### スロットを回して、結果を確認しましょう！")

    if st.button("スロットを回す", key="spin_button"):
        slot_result = spin_slots()

        # スロット結果を横に並べて表示
        slot_symbols = " ".join([f"<span style='font-size: 50px;'>{symbol}</span>" for symbol in slot_result])
        st.write(slot_symbols, unsafe_allow_html=True)

        # ジャックポットが発生する確率を20分の1に設定
        jackpot_probability = 20
        if all(symbol == slot_result[0] for symbol in slot_result) and random.randint(1, jackpot_probability) == 1:
            st.success("おめでとうございます！ジャックポットです！")
        elif len(set(slot_result)) == 2:
            st.warning("2つ揃いました！")
        else:
            st.error("残念！もう一度トライしましょう！")

if __name__ == "__main__":
    main()

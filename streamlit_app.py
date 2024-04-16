# Streamlitライブラリをインポート
import streamlit as st
import emoji

def main():
    st.title("Random Emoji Viewer")

    # ランダムな絵文字を取得
    random_emoji = emoji.emojize(emoji.random_emoji(), use_aliases=True)

    # 絵文字とその名称を表示
    st.markdown(f"**Random Emoji:** {random_emoji}")
    st.markdown(f"**Name:** {emoji.demojize(random_emoji)}")

if __name__ == "__main__":
    main()

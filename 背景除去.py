import streamlit as st
from PIL import Image
import io

# 背景除去関数の定義（仮の関数として実装）
def remove_background(image_data):
    # ここで画像の背景を除去する処理を実装します。
    # 例: 画像処理ライブラリを使用して背景を除去する。
    from rembg import remove
    output_data = remove(image_data)
    return output_data

# Streamlitアプリケーションの設定
def main():
    st.title('画像背景除去ツール')

    # ファイルアップロードセクション
    uploaded_file = st.file_uploader("画像をアップロードしてください", type=["png", "jpg", "jpeg"])

    if uploaded_file is not None:
        # アップロードされたファイルの表示
        st.image(uploaded_file, caption='アップロードされた画像', use_column_width=True)
        
        # 画像データの読み込み
        image_bytes = uploaded_file.read()
        input_image = Image.open(io.BytesIO(image_bytes))
        
        # 背景を除去する処理
        output_image_data = remove_background(image_bytes)
        output_image = Image.open(io.BytesIO(output_image_data))

        # 処理後の画像を表示
        st.image(output_image, caption='背景除去後の画像', use_column_width=True)

        # ダウンロード用リンクの作成
        output_path = io.BytesIO(output_image_data)
        st.download_button(label="画像をダウンロード", data=output_path, file_name="output_image.png", mime="image/png")

if __name__ == "__main__":
    main()

import streamlit as st
import pandas as pd

def st_set_function():
    similar_data = st.file_uploader("ファイルをアップロード")
    if similar_data is None:
        return
    similar_data_df = pd.read_csv(similar_data)
    
    for i, row in similar_data_df.iterrows():
        col1, col2, col3, col4 = st.columns([2, 1, 4, 4])
        with col1:
            # 初期値としてNoneを設定
            function_selection = st.radio(
                "関数", 
                ["ともに採用", "DB1のみ採用", "DB2のみ採用", "ともに不採用"],
                key=f'{row["ID1"]}_{row["ID2"]}',
                index=None  # デフォルトで選択されないようにする
            )
            
            # 未選択の場合に警告を出す
            if function_selection is None:
                st.warning("関数を選択してください。")

            # 選択されていれば値をDataFrameにセット
            if function_selection:
                similar_data_df.at[i, 'function'] = function_selection

            st.write(f'類似度: {row["title_similarity"]}')
        with col2:
            st.write('検索エンジン')
            st.write('ID')
            st.write('タイトル')
            st.write('判定')
            st.write('著者')
            st.write('ジャーナル')
            st.write('アブスト')
        with col3:
            st.write(row['db1'])
            st.write(str(row['ID1']))
            st.write(row['title1'])
            st.write(row['judgment1'])
            st.write(row['author1'])
            st.write(row['journal1'])
            
        with col4:
            st.write(row['db2'])
            st.write(str(row['ID2']))
            st.write(row['title2'])
            st.write(row['judgment2'])
            st.write(row['author2'])
            st.write(row['journal2'])

        _, _, col = st.columns([1, 1, 6])
        with col:
            with st.expander("abstract"):
                col1, col2 = st.columns(2)
                with col1:
                    st.write(row['abstract1'])
                with col2:
                    st.write(row['abstract2'])
                
        st.write('---')
    
    # dataframeをダウンロード
    st.download_button(
        label="Download(utf-8)",
        data=similar_data_df.to_csv().encode(),
        file_name='data_add_func.csv',
        mime='text/csv'
    )


if __name__ == "__main__":
    # wideモードにする
    st.set_page_config(layout="wide")
    st_set_function()

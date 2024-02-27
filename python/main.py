import streamlit as st
import time

st.title('Streamlit 超入門')

st.write('title')

'start!'
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i+1)
    time.sleep(0.5)


left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラムです')

expander = st.expander('問合せ')
expander.write('問合せ内容を書く')

# text = st.text_input('趣味は？')
# condition=st.slider('調子は？',0,100,50)
# '趣味：',text
# '調子：',condition


#if st.checkbox('Show image'):
#    img = Image.open('unnamed.jpg')
#    st.image(img, caption='ph', use_column_width=True)

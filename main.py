import streamlit as st
import numpy as np
import pandas as pd
# 画像読み込み
from PIL import Image

st.title('streamlit 超入門')

st.write('DataFrame')

df = pd.DataFrame(
  np.random.rand(20, 3),
  columns=['a', 'b', 'c']
)

# 折線グラフ
st.line_chart(df)
# 折線エリア塗り
st.area_chart(df)

# データフレームの表示について
# st.dataframe(df, width=100, height=100)
# st.dataframe(df.style.highlight_max(axis=0))
# df = pd.DataFrame({
#   '1列目': [1, 2, 3, 4],
#   '2列目': [10, 20, 30, 40]
# })

# マジックコマンド
"""
# 章
## 節
### 項


```python
import streamlit as st
import numpy as np
import pandas as pd
```

"""

# map
df = pd.DataFrame(
  np.random.rand(100, 2) + [35, 139],
  columns=['lat', 'lon']
)
st.map(df)

st.write('Display Image')

condition = st.slider('あなたの今の調子は？', 0, 100, 50)
'コンディション : ', condition

# テキスト入力
text = st.text_input('あなたの趣味を教えてください')
'あなたの趣味 : ', text

# 指定した値を表示
option = st.selectbox(
  'あなたが好きな数字を教えてください',
  list(range(1, 11))
)
'あなたが好きな数字は、', option, 'です。'

# チェックボックスで画像表示
if st.checkbox('Show Image'):
  img = Image.open('sample.jpg')
  st.image(img, caption='nagino', use_column_width=True)
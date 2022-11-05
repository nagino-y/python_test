import streamlit as st
import numpy as np
import pandas as pd

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

# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
from streamlit.logger import get_logger
import numpy as np
import pandas as pd

LOGGER = get_logger(__name__)

def run():
    st.set_page_config(
        page_title="Hello",
        page_icon="👋",
    )

    st.write("# 1학년 1반 레포트 👋")

    st.sidebar.success("Select a demo above.")

from urllib.error import URLError

import altair as alt
import pandas as pd

import streamlit as st
from streamlit.hello.utils import show_code

def data_frame_demo():
    def get_data():
        data = {
            '반': ['1반', '1반', '1반', '2반', '2반', '2반', '3반', '3반', '3반'],
            '학생': ['학생1', '학생2', '학생3', '학생4', '학생5', '학생6', '학생7', '학생8', '학생9'],
            '충동성 점수': np.random.randint(1, 60, 9)  # 1부터 100 사이의 랜덤 정수
        }
        df = pd.DataFrame(data)
        return df

    try:
        df = get_data()

        classes = st.multiselect("Choose Class", options=df['반'].unique(), default=['1반', '2반'])
        
        if not classes:
            st.error("Please select at least one class.")
        else:
            filtered_data = df[df['반'].isin(classes)]
            mean_scores = filtered_data.groupby('반')['충동성 점수'].mean().reset_index()
            
            chart = (
                alt.Chart(mean_scores)
                .mark_bar()
                .encode(
                    x='반:N',
                    y='충동성 점수:Q',
                    color='반:N'
                )
                .properties(title="반별 충동성 점수 평균")
            )
            st.altair_chart(chart, use_container_width=True)
    except Exception as e:
        st.error(f"An error occurred: {e}")

if __name__ == "__main__":
    data_frame_demo()


def generate_student_data():
    np.random.seed(0) 
    data = {
        '학생': np.repeat(['학생1', '학생2', '학생3', '학생4', '학생5', '학생6', '학생7', '학생8', '학생9'], 3),
        '시점': ['시점1', '시점2', '시점3'] * 9,
        '충동성 점수': np.random.randint(1, 100, 27)  # 각 학생별로 3개 시점의 충동성 점수
    }
    df = pd.DataFrame(data)
    return df

def plot_student_scores_change(df):
    chart = alt.Chart(df).mark_line(point=True).encode(
        x='시점:N',
        y='충동성 점수:Q',
        color='학생:N',
        tooltip=['학생', '시점', '충동성 점수']
    ).properties(
        title='학생별 충동성 점수 변화'
    ).interactive()
    
    st.altair_chart(chart, use_container_width=True)

def main():
    df = generate_student_data()
    st.write("## 학생별 충동성 점수 변화")
    plot_student_scores_change(df)

if __name__ == "__main__":
    main()

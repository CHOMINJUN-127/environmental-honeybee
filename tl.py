import plotly.express as px
import pandas as pd

# 샘플 데이터 (실제로는 연구 데이터 필요)
data = {
    'country': ['USA', 'China', 'India', 'Brazil', 'Germany', 'France', 'Spain', 'Italy', 'Japan', 'South Korea'],
    'iso_alpha': ['USA', 'CHN', 'IND', 'BRA', 'DEU', 'FRA', 'ESP', 'ITA', 'JPN', 'KOR'],
    'pollinator_dependency': [85, 92, 88, 80, 75, 78, 82, 76, 70, 73],  # 가상의 의존도 점수
}

df = pd.DataFrame(data)

# Choropleth 지도 생성
fig = px.choropleth(
    df,
    locations='iso_alpha',
    color='pollinator_dependency',
    hover_name='country',
    color_continuous_scale='Reds',
    labels={'pollinator_dependency': '꿀벌 의존도'},
    title='꿀벌 소멸 시 국가별 농업 피해 예상도'
)

fig.update_layout(
    geo=dict(
        showframe=False,
        showcoastlines=True,
        projection_type='natural earth'
    )
)

fig.show()
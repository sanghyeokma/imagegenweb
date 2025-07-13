import streamlit as st
from openai import OpenAI
import os

# Streamlit UI
st.title("🖼️ AI 이미지 생성기")
st.write("텍스트를 입력하면, 해당 내용을 바탕으로 이미지를 생성합니다.")

# 사이드바: API 키 입력
st.sidebar.title("🔑 설정")
openai_api_key = st.sidebar.text_input("OpenAI API 키를 입력하세요", type="password")
if not openai_api_key:
    st.sidebar.warning("OpenAI API 키를 입력하세요.")
    st.stop()

# OpenAI 클라이언트 설정
client = OpenAI(api_key=openai_api_key)



# 스타일 선택 버튼 (4가지)
st.subheader("🎨 이미지 스타일을 선택하세요")
style = st.radio(
    "스타일 선택",
    options=["리얼리즘", "만화", "수채화", "일러스트레이트"],
    horizontal=True,
    index=0,
    key="style_radio"
)

# 스타일별 프롬프트 문구
style_prompts = {
    "리얼리즘": "in realistic style",
    "만화": "as a cartoon illustration",
    "수채화": "in watercolor painting style",
    "일러스트레이트": "as an illustration"
}

# 프롬프트 입력
user_prompt = st.text_input("📝 이미지 설명을 입력하세요:", value="A cute dog")
# 스타일이 자동으로 프롬프트에 추가됨
full_prompt = f"{user_prompt}, {style_prompts[style]}"

# 전송 버튼
if st.button("이미지 생성하기"):
    with st.spinner("이미지를 생성 중입니다..."):
        try:
            response = client.images.generate(
                prompt=full_prompt,
                model="dall-e-3",  # 또는 "dall-e-2"
                size="1024x1024"
            )


            image_url1 = response.data[0].url
           

            st.image(image_url1, caption="생성된 이미지", use_container_width=True)
           
        except Exception as e:
            st.error(f"이미지 생성 중 오류가 발생했습니다: {e}")
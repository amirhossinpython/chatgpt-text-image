import requests
import streamlit as st
import datetime
from datetime import datetime
import  shutil
# streamlit run chatgpt.py


st.image('ceed3886-53db-4403-a7e5-42edfeff5ba3_neuronto.jpg', width=100)

# Set the title and input area for user's question
st.title('ChatGPT(0)')



    
st.subheader('Free-GPT-chat')




inp = st.text_input('درخواست خود را وارد کنید')
# st.image('bg.jpg', use_column_width=True)

    
ok = st.button('Send')
# Create a button to send the request


# Display the chatbot's response in a text area
if inp and ok:
    if inp.startswith("تصویر"):
        st.text('در حال بارگیری...')
        image = inp.replace("تصویر","").strip()
        try :
            response = requests.get(f"https://api.irateam.ir/Image/test.php?text={image}")
            response.raise_for_status()
            data = response.json()
            image_url = data["result"][0]
            response = requests.get(image_url, stream=True)
            response.raise_for_status()
            
            with open("downloaded_image.jpg", "wb") as out_file:
                shutil.copyfileobj(response.raw, out_file)
            
            st.image("downloaded_image.jpg", use_column_width=True)  
        except requests.exceptions.RequestException as e:
            
            st.error(f"خطا در دریافت تصویر: {e}")   
                  

    
    st.text("لطفاً منتظر بمانید...")
    try:
        
        req = requests.get(f"https://pyrubi.b80.xyz/chat.php/?text={inp}").json()
        res = req[0]["text"]
        st.text_area("Chatbot's Response", value=res, height=200)
    except Exception as e:
        st.text_area("Error", value=f"An error occurred: {e}", height=200)

# if inp.startswith('تصویر') :
#     st.text('در حال بارگیری...')
#     image = inp.replace("تصویر","").strip()
    
#     try:
#         response = requests.get(f"https://api.irateam.ir/Image/test.php?text={image}")
#         response.raise_for_status()
#         data = response.json()
#         image_url = data["result"][0]
        
#         response = requests.get(image_url, stream=True)
#         response.raise_for_status()
        
#         with open("downloaded_image.jpg", "wb") as out_file:
#             shutil.copyfileobj(response.raw, out_file)
        
#         st.image("downloaded_image.jpg", use_column_width=True)
        
#     except requests.exceptions.RequestException as e:
#         st.error(f"خطا در دریافت تصویر: {e}")    
#ligflgkfghl;p--------------------

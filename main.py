from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie


st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code!= 200:
        return None
    return r.json()

#Use Local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")

lottie_coding = load_lottieurl("https://assets4.lottiefiles.com/packages/lf20_iqzuhkgu.json")
img_contact_form = Image.open("C:/Users/user/PycharmProjects/Pandasfiles/images/img1.png")
img_lottie_animation = Image.open(("C:/Users/user/PycharmProjects/Pandasfiles/images/img2.png"))


with st.container():
    st.subheader("Hi, I am Yash :wave:")
    st.title("A Data Analyst From India")
    st.write("I am passionate about finding ways to use Python and VBA to be more efficient and effective in Business settings")
    st.write("[Learn More >](https://futureinventers.com/#/)")

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """
            On my Website I have displayed that what it looks like a attractive website:
            - First of all animations makes its attractive.
            - Background colors should suits the design.
            - Gradient backgrounds gives it a great look.
            - Smooth transactions and fast effects of Flutter gives it a plus point.
            """
        )
        st.write("[Website using Flutter >](https://futureinventers.com/#/)")
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")


with st.container():
    st.write("---")
    st.header("My Application")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_lottie_animation)
    with text_column:
        st.subheader("Integrate Lottie Animations Inside Your Streamlit Aoo")
        st.write(
            """
            Learn how to use Lottie files in Streamlit!
            Animations make our web app more engaging and fun, and lottie files are the easiest way to do this.
            In this tutorial, I'll show you exactly how to do it.
            """
        )
        st.markdown("[Launch my Android Application>](https://play.google.com/store/apps/details?id=com.yash.todo_application&hl=en&gl=US)")

with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_contact_form)
    with text_column:
        st.subheader("Integrate Lottie Animations Inside Your Streamlit Aoo")
        st.write(
            """
            Learn how to use Lottie files in Streamlit!
            Animations make our web app more engaging and fun, and lottie files are the easiest way to do this.
            In this tutorial, I'll show you exactly how to do it.
            """
        )
        st.markdown(
            "[Launch my Android Application>](https://play.google.com/store/apps/details?id=com.yash.todo_application&hl=en&gl=US)")

        # ----Contact form ---
with st.container():
    st.write("---")
    st.header("Get in Touch With Me!")
    st.write("##")

    contact_form = """
    <form action="https://formsubmit.co/yashkhandelwal170@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name"required>
        <input type="email" name="email" placeholder = "Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
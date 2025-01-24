import streamlit as st

# Set page configuration
st.set_page_config(page_title="Jagesh Seesar", page_icon="🙋‍♂️", layout="wide")

# Main container for the resume
with st.container():
    # Inject custom CSS directly
    st.markdown(
        """
        <style>
            #profile-pic {
                width: 150px;
                height: 150px;
                border-radius: 50%;
                overflow: hidden;
                margin: 1 auto;
            }
            #profile-pic img {
                width: 100%;
                height: 100%;
                object-fit: cover;
            }
        </style>
        """,
        unsafe_allow_html=True
    )
    
    # Use custom HTML for the image
    st.markdown(
        """
        <div id="profile-pic">
            <img src="https://raw.githubusercontent.com/JageshSeesar/Assets/refs/heads/main/facephoto.jpg" alt="Profile Picture">
        </div>
        """,
        unsafe_allow_html=True
    )
    st.title("Jagesh Seesar 🙋‍♂️")
    st.markdown(
        """👉 Data Engineer at [MariDeal](https://www.marideal.com/), Ex-student at [University of Mauritius](https://www.utm.ac.mu/) / [Polytechnics Mauritius](https://www.poly.ac.mu/)"""
    )
    st.markdown("👉 [ jageshseesar@gmail.com](mailto:jageshseesar@gmail.com)")

# Social links
with st.container():
    st.subheader("Social Links")
    col1, col2, col3, col4, col5, col6 = st.columns(6)
    with col1:
        #st.markdown("[YouTube](https://youtube.com/c/dennisivy)")
        st.markdown("📡 [GitHub](https://github.com/JageshSeesar)")
    with col2:
        #st.markdown("[Twitter](https://twitter.com/dennisivy11)")
        st.markdown("📡 [LinkedIn](https://www.linkedin.com/in/jseesar/)")
    with col3:
        st.markdown("📡 [Whatsapp](https://wa.me/qr/C3SDIB2GQ6PHO1/)")
    with col4:
        st.markdown("📡 [Facebook](https://www.facebook.com/jaggo10/)")
    with col5:
        st.markdown("📡 [Instagram](https://www.instagram.com/jagesh__s/)")
    with col6:
        st.markdown("📡 [Download Resume](#)")
        


# Work history
with st.container():
    st.header("Work History")
    st.markdown(
        """##### 🚧 Developer Advocate | Appwrite.io
**9/2023 - present**  
- Working to improve developer adoption and experience across all Appwrite SDKs.  
- Videos: +39 | Views: +136.6k  
- Articles: 9 | Events attended: 4  

---

##### 🚧 Developer Advocate | Agora.io
**11/2021 - 9/2023**  
- Made Agora’s Web-Based SDK more accessible through tutorials and educational content.  
- Doubled Web SDK’s monthly usage minutes from 15 million to 30 million in 4 months.  

---

##### 🚧 Instructor | YouTube, Udemy, Teachable
**11/2019 - Present**  
- Produced content showcasing new tech and tutorials.  
- 210k+ YouTube Subscribers, 30k course copies sold, 12M+ YouTube views.  

---

##### 🚧 Senior Developer | FOI Labs
**10/2017 - 10/2019**  
- Designed and developed a laboratory management system.  
- Onboarded and trained customers through webinars and conferences.  

---

##### 🚧 Digital Marketer | Unifive Digital
**2014 - 2017**  
- Organized SEO & SEM campaigns on local and global scales.  
- Built 70+ websites with a small team of developers."""
    )




# Qualification
with st.container():
    st.header("Qualification")
    st.markdown(
        """##### 🧱 Developer Advocate | Appwrite.io
**9/2023 - present**  
- Working to improve developer adoption and experience across all Appwrite SDKs.  
- Videos: +39 | Views: +136.6k  
- Articles: 9 | Events attended: 4  

---

##### 🧱 Developer Advocate | Agora.io
**11/2021 - 9/2023**  
- Made Agora’s Web-Based SDK more accessible through tutorials and educational content.  
- Doubled Web SDK’s monthly usage minutes from 15 million to 30 million in 4 months.  

---

##### 🧱 Instructor | YouTube, Udemy, Teachable
**11/2019 - Present**  
- Produced content showcasing new tech and tutorials.  
- 210k+ YouTube Subscribers, 30k course copies sold, 12M+ YouTube views.  

---

##### 🧱 Senior Developer | FOI Labs
**10/2017 - 10/2019**  
- Designed and developed a laboratory management system.  
- Onboarded and trained customers through webinars and conferences.  

---

##### 🧱 Digital Marketer | Unifive Digital
**2014 - 2017**  
- Organized SEO & SEM campaigns on local and global scales.  
- Built 70+ websites with a small team of developers."""
    )




# Skills
with st.container():
    st.header("Skills & Qualifications")
    st.markdown(
        """- ✔️ 10 Years experience in fullstack development
- ✔️ Tech educator & online instructor (YouTube & Udemy)
- ✔️ Technical writing & Blogging
- ✔️ SEO & paid ad campaigns (Google Adwords)"""
    )


# Tech stack
with st.container():
    st.header("Tech Stack")
    st.markdown(
        """- **🕹️ Languages**: Python, JavaScript, NodeJS
- **🕹️ Frameworks**: Django, Express, Flask, FastAPI
- **🕹️ Frontend**: React, Next JS
- **🕹️ Databases**: Postgres, MongoDB, MySQL"""
    )



# Projects and accomplishments
with st.container():
    st.header("Projects & Accomplishments")
    st.markdown(
        """- 🏆 Built a Laboratory management system for forensics lab
- 🏆 Documentation website - Led team to re-build docs for Agora.io
- 🏆 E-commerce platform using PayPal and Stripe API for payment integration
- 🏆 Social Network - Open source project"""
    )

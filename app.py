import streamlit as st
import re

st.set_page_config(
    page_title="Password Strength Checker",
    page_icon="🔐",
    layout="centered"
)

# ------------------- CSS --------------------

st.markdown("""
<style>

/* Background - light, subtle gradient */
.stApp{
    background: linear-gradient(120deg,#070617 0%, #0f172a 40%, #4527a0 70%, #021b79 100%);
    background-attachment: fixed;
    background-size: 200% 200%;
    animation: gradient 12s ease infinite;
}

@keyframes gradient{
0%{background-position:0% 50%;}
50%{background-position:100% 50%;}
100%{background-position:0% 50%;}
}

/* Main Card */
.main-card{
    background: transparent;
    padding:36px;
    border-radius:16px;
    backdrop-filter: blur(6px);
    border:1px solid rgba(124,58,237,0.12);
    box-shadow: none;
}

/* Title */
.title{
text-align:center;
    font-size:48px;
    font-weight:800;
    color:#7ef9ff;
    letter-spacing:1px;
    margin-bottom:8px;
    text-shadow:0 2px 18px rgba(126,249,255,0.12);
}

/* Subtitle */
.subtitle{
    text-align:center;
    font-size:16px;
    color:#94a3b8;
    margin-bottom:18px;
}

/* Text */
p,label,span{
    /* body text */
    font-size:16px !important;
    color:#cbd5e1;
}

/* Input Box */
.stTextInput>div>div>input{
    background: rgba(255,255,255,0.03);
    color: #ffffff;
    border-radius:10px;
    border:1px solid rgba(99,102,241,0.12);
    padding:12px;
    font-size:15px;
}

/* Button */
.stButton>button{
    width:100%;
    background: linear-gradient(90deg,#7c3aed,#06b6d4);
    color:#030712;
    font-size:15px;
    font-weight:800;
    border:none;
    border-radius:28px;
    padding:12px;
    transition: transform .14s ease, box-shadow .14s ease;
}

.stButton>button:hover{
    transform:translateY(-3px) scale(1.01);
    box-shadow:0 12px 40px rgba(99,102,241,0.18), 0 0 36px rgba(14,165,233,0.08);
}

/* Progress Bar */
.stProgress>div>div{
    background:linear-gradient(90deg,#06b6d4,#7c3aed);
    height:10px;
    border-radius:8px;
}

/* Success Message */
.success{
color:#059669;
font-size:14px;
}

/* Suggestions */
li{
font-size:14px;
color:#ffffff;
}

/* Cyber left panel */
.cyber-panel{
    background: transparent;
    color:#9be7ff;
    padding:20px;
    border-radius:12px;
    border:1px solid rgba(124,58,237,0.12);
    box-shadow: 0 6px 30px rgba(124,58,237,0.03), inset 0 0 30px rgba(124,58,237,0.01);
    font-family: 'Source Code Pro', monospace;
}

.cyber-panel .score{
    font-size:24px;
    color:#ffffff;
    margin-bottom:8px;
}
.score-num{
    font-weight:900;
    color:#ffffff;
    font-size:24px;
    padding:6px 10px;
    background:rgba(255,255,255,0.1);
    border-radius:8px;
    border:1px solid rgba(255,255,255,0.12);
    box-shadow:0 8px 22px rgba(255,255,255,0.08);
}

.status{
font-weight:700;
padding:8px 10px;
border-radius:8px;
text-align:center;
}
.status.weak{background:rgba(239,68,68,0.08);color:#dc2626}
.status.medium{background:rgba(250,204,21,0.08);color:#b45309}
.status.strong{background:rgba(16,185,129,0.08);color:#059669}

.suggest{color:#ffffff;margin:4px 0}

.suggestions strong{color:#ffffff}

/* emphasize suggestions */
.suggest{font-size:15px}

/* Rules card */
.rules-card{
    background: transparent;
    padding:18px;
    border-radius:12px;
    border:1px solid rgba(124,58,237,0.08);
    box-shadow:0 6px 22px rgba(124,58,237,0.03);
    color:#ffffff;
}
.entered-pass{background:linear-gradient(90deg, rgba(6,182,212,0.06), rgba(124,58,237,0.04));padding:10px;border-radius:8px;border:1px solid rgba(124,58,237,0.08);margin-top:8px;color:#a7f3d0}

.entered-pass.muted{color:#94a3b8;background:transparent;border:1px dashed rgba(124,58,237,0.06)}

/* make the input label bright white */
.stTextInput>div>label, .stTextInput label{ color: #ffffff !important; font-weight:600 }

/* make rules list items bright white and bigger */
.rules-card h4{color:#ffffff; font-size:18px; margin-bottom:8px;}
.rules-card ul li{ color: #ffffff; font-size:16px; line-height:1.6;}

/* hint text when password is empty */
.hint{color:#ffffff; font-size:18px; font-weight:600; margin-top:12px;}

/* make rules list items bright white and larger */
.rules-card h4{ color:#ffffff; font-size:18px; margin-bottom:8px }
.rules-card ul li{ color: #ffffff; font-size:16px; line-height:1.6 }

</style>
""", unsafe_allow_html=True)

# ------------------ CARD -------------------

st.markdown('<div class="main-card">', unsafe_allow_html=True)

cols = st.columns([2, 1])

with cols[0]:
    st.markdown(
        '<div class="title">🔐 Password Strength Checker</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">Create a secure password and check its strength instantly.</div>',
        unsafe_allow_html=True
    )

    password = st.text_input(
        "Enter Password",
        type="password",
        placeholder="Type your password..."
    )

    # Cyber-style status area
    st.markdown('<div class="cyber-panel">', unsafe_allow_html=True)

    if password:
        score = 0
        feedback = []

        if len(password) >= 8:
            score += 1
        else:
            feedback.append("Minimum 8 characters")

        if re.search(r"[A-Z]", password):
            score += 1
        else:
            feedback.append("Add one uppercase letter")

        if re.search(r"[a-z]", password):
            score += 1
        else:
            feedback.append("Add one lowercase letter")

        if re.search(r"\d", password):
            score += 1
        else:
            feedback.append("Add one number")

        if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
            score += 1
        else:
            feedback.append("Add one special character")

        # Visual score (cyber style)
        left, right = st.columns([3,1])
        with left:
            st.markdown(f"<div class='score'>Score: <span class='score-num'>{score}/5</span></div>", unsafe_allow_html=True)
            st.progress(score/5)
        with right:
            if score <= 2:
                st.markdown("<div class='status weak'>🔴 Weak</div>", unsafe_allow_html=True)
            elif score <= 4:
                st.markdown("<div class='status medium'>🟡 Medium</div>", unsafe_allow_html=True)
            else:
                st.markdown("<div class='status strong'>🟢 Strong</div>", unsafe_allow_html=True)
                st.balloons()

        if feedback:
            st.markdown('<div class="suggestions"><strong>Suggestions</strong></div>', unsafe_allow_html=True)
            for item in feedback:
                st.markdown(f"<div class='suggest'>✔ {item}</div>", unsafe_allow_html=True)

    else:
        st.markdown("<div class='hint'>Enter a password to see strength analysis...</div>", unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

with cols[1]:
    st.markdown('<div class="rules-card">', unsafe_allow_html=True)
    st.markdown('<h4 style="margin-top:0">Password Rules</h4>', unsafe_allow_html=True)
    st.markdown('''
    <ul>
      <li>Minimum 8 characters</li>
      <li>At least one uppercase letter (A-Z)</li>
      <li>At least one lowercase letter (a-z)</li>
      <li>At least one number (0-9)</li>
      <li>At least one special character (!@#$%)</li>
    </ul>
    ''', unsafe_allow_html=True)

    # Show entered password plainly in the rules card (as requested)
    st.markdown('<div class="entered"><strong>Entered:</strong></div>', unsafe_allow_html=True)
    if password:
        st.markdown(f"<div class='entered-pass'>{password}</div>", unsafe_allow_html=True)
    else:
        st.markdown("<div class='entered-pass muted'>No password entered</div>", unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
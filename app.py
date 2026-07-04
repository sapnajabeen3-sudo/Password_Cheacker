import streamlit as st

st.set_page_config(page_title="IQ Quiz", page_icon="🧠")

st.title("🧠 Simple IQ Quiz")
st.write("Answer the following questions and see your IQ score!")

score = 0

# Question 1
q1 = st.radio(
    "1. Which number comes next?\n2, 4, 8, 16, ?",
    ["18", "24", "32", "30"]
)

if q1 == "32":
    score += 1

# Question 2
q2 = st.radio(
    "2. Which shape has 4 equal sides?",
    ["Rectangle", "Triangle", "Square", "Circle"]
)

if q2 == "Square":
    score += 1

# Question 3
q3 = st.radio(
    "3. What is 15 + 27?",
    ["40", "42", "45", "44"]
)

if q3 == "42":
    score += 1

# Question 4
q4 = st.radio(
    "4. Which animal is known as the King of the Jungle?",
    ["Tiger", "Lion", "Elephant", "Leopard"]
)

if q4 == "Lion":
    score += 1

# Question 5
q5 = st.radio(
    "5. Which one is an even number?",
    ["17", "23", "26", "19"]
)

if q5 == "26":
    score += 1

if st.button("Calculate IQ Score"):
    st.success(f"Your Score: {score}/5")

    if score == 5:
        st.balloons()
        st.write("🧠 Excellent! Your logical thinking is outstanding.")
    elif score >= 3:
        st.write("😊 Good job! You have good reasoning skills.")
    else:
        st.write("📚 Keep practicing logical puzzles!")
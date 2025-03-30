# import streamlit as st
# import pandas as pd
# import joblib
# import matplotlib.pyplot as plt

# # Page Configuration
# st.set_page_config(page_title="AI-Powered Expense Tracker", page_icon="💰", layout="wide")

# # Load the Model and dataset:
# @st.cache_resource
# def load_model():
#     return joblib.load("expense_model.pkl")

# @st.cache_data
# def load_dataset():
#     return pd.read_csv("cleaned_personal_expenses.csv")

# # Load resources
# model = load_model()
# df = load_dataset()

# # App Title and Sidebar
# st.title("💸 AI-Powered Personal Expense Tracker")
# st.sidebar.title("Navigation")
# option = st.sidebar.radio("Choose an option:", ["Home", "Predict Expenses", "Visualize Data"])

# # Home Section
# if option == "Home":
#     st.subheader("Welcome to the Expense Tracker!")
#     st.write("This app helps you analyze and predict your personal expenses efficiently using AI.")
#     st.markdown("""
#         - **Predict Expenses**: Use the prediction tool to estimate your monthly expenses.
#         - **Visualize Data**: View trends and insights from the dataset.
#         - **Easy & Reliable**: Use AI-powered predictions to make better financial decisions.
#     """)
#     st.write("📊 Below is a preview of the dataset used:")
#     st.dataframe(df.head())

# # Predict Expenses Section
# elif option == "Predict Expenses":
#     st.subheader("🔮 Predict Your Monthly Expenses")
#     st.write("Fill in the details below to predict your total expenses.")

#     # User Input
#     housing = st.number_input("Housing ($)", min_value=0, value=1000, step=50)
#     bills = st.number_input("Bills & Utilities ($)", min_value=0, value=200, step=10)
#     food = st.number_input("Food & Dining ($)", min_value=0, value=300, step=10)
#     personal = st.number_input("Personal ($)", min_value=0, value=150, step=10)
#     transport = st.number_input("Auto & Transport ($)", min_value=0, value=100, step=10)
#     health = st.number_input("Health & Fitness ($)", min_value=0, value=50, step=10)

#     # Prediction Button
#     if st.button("Predict Total Expenses"):
#         # Combine inputs into a DataFrame
#         input_data = pd.DataFrame({
#             "Housing": [housing],
#             "Bills & Utilities": [bills],
#             "Food & Dining": [food],
#             "Personal": [personal],
#             "Auto & Transport": [transport],
#             "Health & Fitness": [health]
#         })

#         # Predict using the loaded model
#         prediction = model.predict(input_data)
#         st.success(f"Your predicted total monthly expenses are: **${prediction[0]:.2f}**")

# # Visualize Data Section
# elif option == "Visualize Data":
#     st.subheader("📈 Visualize Trends in Personal Expenses")

#     # Select Expense Category
#     category = st.selectbox("Choose a category to visualize:", df.columns[1:])

#     # Plot the selected category
#     if category:
#         st.write(f"### Monthly Trend for: {category}")
#         plt.figure(figsize=(10, 5))
#         plt.plot(df['Month'], df[category], marker='o', color='skyblue')
#         plt.xlabel("Month")
#         plt.ylabel(f"Expenses in {category} ($)")
#         plt.title(f"{category} Expenses Over Time")
#         st.pyplot(plt)

#     # Display the full dataset as a table
#     st.write("### Full Dataset:")
#     st.dataframe(df)



#Ye THODI BETTER TRY KI HAI LETS CHECK :

# import streamlit as st
# import pandas as pd
# import joblib
# import matplotlib.pyplot as plt
# import seaborn as sns

# # Page Configuration
# st.set_page_config(page_title="💸 Personal Expense Tracker", page_icon="📊", layout="wide")

# # Load Model and Dataset
# @st.cache_resource
# def load_model():
#     return joblib.load("expense_model.pkl")

# @st.cache_data
# def load_dataset():
#     return pd.read_csv("cleaned_personal_expenses.csv")

# model = load_model()
# df = load_dataset()

# # App Title and Sidebar
# st.title("💸 AI-Powered Personal Expense Tracker")
# st.sidebar.title("Navigation")
# option = st.sidebar.radio("Choose an option:", ["Home", "Predict Expenses", "Visualize Data", "Expense Insights"])

# # Apply custom styles using Markdown
# st.markdown("""
#     <style>
#     .main {
#         background-color: #f0f2f6;
#     }
#     .stButton>button {
#         background-color: #008CBA;
#         color: white;
#         border-radius: 5px;
#         padding: 8px 16px;
#     }
#     .stButton>button:hover {
#         background-color: #005f7f;
#     }
#     </style>
#     """, unsafe_allow_html=True)

# # Home Section
# if option == "Home":
#     st.subheader("Welcome to the AI-Powered Expense Tracker! 💡")
#     st.write("Analyze, predict, and visualize your monthly expenses with ease.")
#     st.markdown("""
#     - **Smart Predictions**: AI-based total monthly expense forecasting.
#     - **Data Insights**: Visualize trends and understand your spending patterns.
#     - **Interactive Design**: User-friendly and colorful UI for better engagement.
#     """)
#     st.write("📊 **Preview of the dataset used:**")
#     st.dataframe(df.head())

# # Predict Expenses Section
# elif option == "Predict Expenses":
#     st.subheader("🔮 Predict Your Monthly Expenses")
#     st.write("Fill in the details below to forecast your total monthly expense.")

#     # User Input
#     housing = st.number_input("Housing ($)", min_value=0, value=1000, step=50)
#     bills = st.number_input("Bills & Utilities ($)", min_value=0, value=200, step=10)
#     food = st.number_input("Food & Dining ($)", min_value=0, value=300, step=10)
#     personal = st.number_input("Personal ($)", min_value=0, value=150, step=10)
#     transport = st.number_input("Auto & Transport ($)", min_value=0, value=100, step=10)
#     health = st.number_input("Health & Fitness ($)", min_value=0, value=50, step=10)

#     # Prediction Button
#     if st.button("Predict Total Expenses"):
#         input_data = pd.DataFrame({
#             "Housing": [housing],
#             "Bills & Utilities": [bills],
#             "Food & Dining": [food],
#             "Personal": [personal],
#             "Auto & Transport": [transport],
#             "Health & Fitness": [health]
#         })

#         # Predict using the loaded model
#         prediction = model.predict(input_data)
#         st.success(f"Your predicted total monthly expenses are: **${prediction[0]:.2f}**")

#         # Pie Chart for User Inputs
#         st.write("### Your Spending Distribution:")
#         user_expenses = [housing, bills, food, personal, transport, health]
#         categories = ["Housing", "Bills", "Food", "Personal", "Transport", "Health"]
#         fig, ax = plt.subplots()
#         ax.pie(user_expenses, labels=categories, autopct="%1.1f%%", startangle=90, colors=sns.color_palette("pastel"))
#         ax.axis("equal")
#         st.pyplot(fig)

# # Visualize Data Section
# elif option == "Visualize Data":
#     st.subheader("📊 Visualize Trends in Personal Expenses")
#     st.write("Explore monthly trends across different expense categories.")

#     # Select Category to Visualize
#     category = st.selectbox("Choose a category to visualize:", df.columns[1:])

#     # Line Plot for Trends
#     if category:
#         st.write(f"### Monthly Trend for: {category}")
#         plt.figure(figsize=(10, 5))
#         sns.lineplot(data=df, x="Month", y=category, marker="o", color="green", linewidth=2)
#         plt.xlabel("Month")
#         plt.ylabel(f"Expenses in {category} ($)")
#         plt.title(f"{category} Expenses Over Time")
#         plt.grid(True)
#         st.pyplot(plt)

# # Expense Insights Section
# elif option == "Expense Insights":
#     st.subheader("💡 Expense Insights & Summary")
#     st.write("Analyze your overall spending habits and get actionable insights.")

#     # Total Expenses Per Category
#     st.write("### Total Expenses by Category:")
#     total_expenses = df.iloc[:, 1:].sum()
#     fig, ax = plt.subplots(figsize=(10, 5))
#     sns.barplot(x=total_expenses.index, y=total_expenses.values, palette="coolwarm", ax=ax)
#     ax.set_ylabel("Total Amount ($)")
#     ax.set_title("Total Expenses by Category")
#     st.pyplot(fig)

#     # Highlight the biggest expense
#     max_expense = total_expenses.idxmax()
#     max_value = total_expenses.max()
#     st.info(f"💡 You spend the most on **{max_expense}**, totaling **${max_value:.2f}**.")

#     # Progress Bars for Category Spending
#     st.write("### Progress Bars for Each Category:")
#     for category in total_expenses.index:
#         st.write(f"{category}: ${total_expenses[category]:.2f}")
#         st.progress(total_expenses[category] / total_expenses.sum())

#kal kuch naya try karungi : 


import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt

# Page Configuration
st.set_page_config(page_title="💸 Personal Expense Tracker", page_icon="📊", layout="wide")

# Load Model and Dataset
@st.cache_resource
def load_model():
    return joblib.load("expense_model.pkl")

@st.cache_data
def load_dataset():
    return pd.read_csv("cleaned_personal_expenses.csv")

model = load_model()
df = load_dataset()

# App Title and Sidebar
st.title("💸 AI-Powered Personal Expense Tracker")
st.sidebar.title("Navigation")
option = st.sidebar.radio("Choose an option:", ["Home", "Predict Expenses", "Visualize Data", "Expense Insights"])

# Apply custom styles using Markdown
st.markdown("""
    <style>
    .main {
        background-color: #f0f2f6;
    }
    .stButton>button {
        background-color: #008CBA;
        color: white;
        border-radius: 5px;
        padding: 8px 16px;
    }
    .stButton>button:hover {
        background-color: #005f7f;
    }
    </style>
    """, unsafe_allow_html=True)

# Home Section
if option == "Home":
    st.subheader("Welcome to the AI-Powered Expense Tracker! 💡")
    st.write("Analyze, predict, and visualize your monthly expenses with ease.")
    st.markdown("""
    - **Smart Predictions**: AI-based total monthly expense forecasting.
    - **Data Insights**: Visualize trends and understand your spending patterns.
    - **Interactive Design**: User-friendly and colorful UI for better engagement.
    """)
    st.write("📊 **Preview of the dataset used:**")
    st.dataframe(df.head())

# Predict Expenses Section
elif option == "Predict Expenses":
    st.subheader("🔮 Predict Your Monthly Expenses")
    st.write("Fill in the details below to forecast your total monthly expense.")

    # User Input
    housing = st.number_input("Housing ($)", min_value=0, value=1000, step=50)
    bills = st.number_input("Bills & Utilities ($)", min_value=0, value=200, step=10)
    food = st.number_input("Food & Dining ($)", min_value=0, value=300, step=10)
    personal = st.number_input("Personal ($)", min_value=0, value=150, step=10)
    transport = st.number_input("Auto & Transport ($)", min_value=0, value=100, step=10)
    health = st.number_input("Health & Fitness ($)", min_value=0, value=50, step=10)

    # Prediction Button
    if st.button("Predict Total Expenses"):
        input_data = pd.DataFrame({
            "Housing": [housing],
            "Bills & Utilities": [bills],
            "Food & Dining": [food],
            "Personal": [personal],
            "Auto & Transport": [transport],
            "Health & Fitness": [health]
        })

        # Predict using the loaded model
        prediction = model.predict(input_data)
        st.success(f"Your predicted total monthly expenses are: **${prediction[0]:.2f}**")

        # Bar Chart for User Inputs
        st.write("### Your Spending Distribution:")
        user_expenses = [housing, bills, food, personal, transport, health]
        categories = ["Housing", "Bills", "Food", "Personal", "Transport", "Health"]
        fig, ax = plt.subplots()
        ax.bar(categories, user_expenses, color=['blue', 'orange', 'green', 'red', 'purple', 'brown'])
        ax.set_ylabel("Expense Amount ($)")
        ax.set_title("User Expense Breakdown")
        st.pyplot(fig)

# Visualize Data Section
elif option == "Visualize Data":
    st.subheader("📊 Visualize Trends in Personal Expenses")
    st.write("Explore monthly trends across different expense categories.")

    # Select Category to Visualize
    category = st.selectbox("Choose a category to visualize:", df.columns[1:])

    # Line Plot for Trends
    if category:
        st.write(f"### Monthly Trend for: {category}")
        fig, ax = plt.subplots()
        ax.plot(df["Month"], df[category], marker="o", linestyle="-", color="green")
        ax.set_xlabel("Month")
        ax.set_ylabel(f"Expenses in {category} ($)")
        ax.set_title(f"{category} Expenses Over Time")
        ax.grid(True)
        st.pyplot(fig)

# Expense Insights Section
elif option == "Expense Insights":
    st.subheader("💡 Expense Insights & Summary")
    st.write("Analyze your overall spending habits and get actionable insights.")

    # Total Expenses Per Category
    st.write("### Total Expenses by Category:")
    total_expenses = df.iloc[:, 1:].sum()
    fig, ax = plt.subplots()
    ax.bar(total_expenses.index, total_expenses.values, color="dodgerblue")
    ax.set_ylabel("Total Amount ($)")
    ax.set_title("Total Expenses by Category")
    st.pyplot(fig)

    # Highlight the biggest expense
    max_expense = total_expenses.idxmax()
    max_value = total_expenses.max()
    st.info(f"💡 You spend the most on **{max_expense}**, totaling **${max_value:.2f}**.")

    # Progress Bars for Category Spending
    st.write("### Progress Bars for Each Category:")
    for category in total_expenses.index:
        st.write(f"{category}: ${total_expenses[category]:.2f}")
        st.progress(total_expenses[category] / total_expenses.sum())

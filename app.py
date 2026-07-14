import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

st.set_page_config(
    page_title="Student Budget Planner",
    page_icon="🎓",
    layout="wide"
)

st.title("🎓 Student Budget Planner")

st.markdown("""
### A budgeting tool designed to help student manage their educational expenses.
  
Fill in the details below to analyse your monthly spending and receive personalised budeting advice.
""")

st.divider()

st.header("👤 Student Information")

student_name = st.text_input("Student Name")

monthly_budget = st.number_input(
    "Monthly Budget (PKR)",
    min_value=0.0,
    step=500.0
)

st.divider()

st.header("💰 Monthly Expenses")

tuition = st.number_input("Tuition Fee", min_value=0.0)

books = st.number_input("Books and Stationery", min_value=0.0)

transport = st.number_input("Transport", min_value=0.0)

internet = st.number_input("Internet", min_value=0.0)

academy = st.number_input("Academy/Tuition", min_value=0.0)

exam = st.number_input("Examination Fees", min_value=0.0)

other = st.number_input("Other Expenses", min_value=0.0)

if st.button("📊 Calculate Budget"):

    total_expenses = (
        tuition
        + books
        + transport
        + internet
        + academy
        + exam
        + other
    )

    remaining = monthly_budget - total_expenses

    if monthly_budget > 0:
        percentage = (total_expenses / monthly_budget) * 100
    else:
        percentage = 0

    st.divider()

    st.header("📈 Budget Analysis")

    st.write(f"**Student:** {student_name}")

    st.write(f"**Total Expenses:** PKR {total_expenses:,.2f}")

    st.write(f"**Remaining Budget:** PKR {remaining:,.2f}")

    st.write(f"**Percentage Spent:** {percentage:.1f}%")

    st.divider()

    st.header("📌 Budget Status")

    if percentage <= 80:
        st.success("🟢 Healthy Budget")
    elif percentage <= 100:
        st.warning("🟡 Nearly at Budget Limit")
    else:
        st.error("🔴 Over Budget")

    st.divider()

    st.header("💡 Personalised Budget Advice")

    if percentage > 100:
        st.error("Your expenses exceed your monthly budget. Try reducing non-essential spending and prioritise educational expenses.")

    elif percentage > 80:
        st.warning("You are very close to your budget limit. Monitor your spending carefully this month.")

    else:
        st.success("Excellent! You are managing your budget well. Consider saving part of your remaining money for future educational expenses.")

    if tuition > monthly_budget * 0.50:
        st.info("📚 Tuition fee consumes more than 50% of your monthly budget.")

    if books > monthly_budget * 0.10:
        st.info("📖 Consider buying second-hand books or borrowing from libraries to reduce costs.")

    if transport > monthly_budget * 0.15:
        st.info("🚌 Transport costs are relatively high. Consider student transport discounts or public transport.")

    if internet > monthly_budget * 0.10:
        st.info("🌐 Internet expenses are higher than average. Compare available packages to reduce costs.")

    if other > monthly_budget * 0.10:
        st.info("🛍️ Your miscellaneous expenses are quite high. Review optional spending.")


    st.header("💡 Money Saving Tips")

    tips = [
        "Create a monthly budget before spending.",
        "Track every expense regularly.",
        "Use student discounts whenever available.",
        "Borrow or buy second-hand books.",
        "Avoid unnecessary online shopping.",
        "Keep an emergency savings fund."
    ]

    for tip in tips:
        st.write("✅", tip) 

    st.divider()

    st.header("📋 Budget Summary")

    st.write(f"💰 Monthly Budget: PKR {monthly_budget:,.0f}")
    st.write(f"💸 Total Expenses: PKR {total_expenses:,.0f}")
    st.write(f"💵 Remaining Budget: PKR {remaining:,.0f}")

    if remaining >= 0:
        st.success("✅ You are within your budget.")
    else:
        st.error("❌ You have exceeded your budget.")

    st.divider()

st.header("🥧 Expense Distribution")
labels = [
    "Tuition",
    "Books",
    "Transport",
    "Internet",
    "Academy",
    "Exams",
    "Other"
]

sizes = [
    tuition,
    books,
    transport,
    internet,
    academy,
    exam,
    other
]

fig, ax = plt.subplots()
ax.pie(
    sizes,
    labels=labels,
    autopct="%1.1f%%",
    startangle=90,
    shadow=True
)
ax.axis("equal")

st.pyplot(fig) 

st.divider()
st.header("📋 Expense Breakdown")
expense_data = {
    "Expense Category": [
        "Tuition",
        "Books & Stationery",
        "Transport",
        "Internet",
        "Academy",
        "Examination Fees",
        "Other"
    ],
     "Amount (PKR)": [
        tuition,
        books,
        transport,
        internet,
        academy,
        exam,
        other
    ]
}
st.table(expense_data)

df = pd.DataFrame(expense_data)
csv = df.to_csv(index=False).encode("utf-8")
st.download_button(
    label="📥 Download Budget Report",
    data=csv,
    file_name="student_budget_report.csv",
    mime="text/csv"
)
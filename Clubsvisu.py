import streamlit as st
import pandas as pd
import json
import matplotlib.pyplot as plt


def main():
    # Load data
    clubs_data = json.load(open("shsg.clubs.json"))

    # Convert JSON data to a DataFrame
    df = pd.DataFrame(clubs_data)
    df['followers'] = pd.to_numeric(df['followers'], errors='coerce')
    df_sorted = df.sort_values(by='followers', ascending=False).copy()
    df_sorted['Rank'] = range(1, len(df_sorted) + 1)

    st.header("Club Overview")

    # First row of charts
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Clubs by Category")
        category_counts = df['categoryName'].value_counts()
        fig1, ax1 = plt.subplots(figsize=(6, 6))
        ax1.pie(category_counts, labels=category_counts.index, autopct='%1.1f%%', startangle=90)
        plt.style.use('bmh')
        ax1.set_title("Clubs by Category")
        st.pyplot(fig1)

    with col2:
        st.subheader("Recruitment Status")
        recruit_counts = df['isRecruiting'].value_counts()
        fig2, ax2 = plt.subplots(figsize=(6, 6))
        ax2.pie(recruit_counts, labels=recruit_counts.index, autopct='%1.1f%%', startangle=90)
        ax2.set_title("Recruitment Status Distribution")
        plt.style.use('bmh')
        st.pyplot(fig2)

    # Second row of charts
    col3, col4 = st.columns(2)

    with col3:
        st.subheader("Member Size Distribution")
        members_counts = df['numberOfMembers'].value_counts()
        fig3, ax3 = plt.subplots(figsize=(6, 6))
        ax3.pie(members_counts, labels=members_counts.index, autopct='%1.1f%%', startangle=90)
        plt.style.use('bmh')
        ax3.set_title("Distribution by Member Size")
        st.pyplot(fig3)

    with col4:
        st.subheader("Member Size vs. Recruitment Status")
        # Define ordered categories
        cat_order = pd.api.types.CategoricalDtype(
            categories=["1-10", "11-30", "31-50", "51-100", "101 & more"],
            ordered=True
        )
        df['orderedMembers'] = df['numberOfMembers'].astype(cat_order)
        ct = pd.crosstab(df['orderedMembers'], df['isRecruiting'])

        fig4, ax4 = plt.subplots(figsize=(6, 6))
        ct.plot(kind='bar', ax=ax4)
        ax4.set_xlabel("Number of Members")
        ax4.set_ylabel("Number of Clubs")
        ax4.set_title("Member Size vs. Recruitment Status")
        plt.style.use('bmh')
        ax4.legend(title="Recruiting ?")
        st.pyplot(fig4)

    st.header("Club Details")

    # Filters
    search_query = st.text_input("Search club by name:")
    recruit_filter = st.selectbox("Filter by Recruiting Status:", options=["All", "Yes", "No"])
    category_options = ["All"] + sorted(df['categoryName'].unique())
    category_filter = st.selectbox("Filter by Category:", options=category_options)

    filtered_df = df_sorted.copy()

    if search_query:
        filtered_df = filtered_df[filtered_df['name'].str.contains(search_query, case=False, na=False)]
    if recruit_filter != "All":
        filtered_df = filtered_df[filtered_df['isRecruiting'] == recruit_filter]
    if category_filter != "All":
        filtered_df = filtered_df[filtered_df['categoryName'] == category_filter]

    if filtered_df.empty:
        st.write("No clubs found matching the selected filters.")
    else:
        for _, row in filtered_df.iterrows():
            with st.container():
                st.markdown(f"### {row['name']} (Followers Rank #{row['Rank']})")
                st.write(f"**Category:** {row['categoryName']}")
                st.write(f"**Number of Members:** {row['numberOfMembers']}")
                st.write(f"**Followers:** {row['followers']}")
                st.write(f"**Recruiting:** {row['isRecruiting']}")
                st.write(f"**Description:** {row['description']}")
                st.write("---")

if __name__ == "__main__":
    main()

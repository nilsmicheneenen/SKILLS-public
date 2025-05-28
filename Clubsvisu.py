# Import necessary libraries
import streamlit as st              # necessary to built the web app
import pandas as pd                # For data manipulation and analysis
import json                        # For loading JSON data files
import matplotlib.pyplot as plt    # For plotting graphs

def main():
    # Step 1: Load data from a JSON file containing club information
    clubs_data = json.load(open("shsg.clubs.json"))

    # Step 2: Convert the loaded JSON data into a pandas DataFrame for easier manipulation
    df = pd.DataFrame(clubs_data)

    # Step 3: Convert the 'followers' column to numeric, turning non-numeric values into NaN
    df['followers'] = pd.to_numeric(df['followers'], errors='coerce')

    # Step 4: Sort the DataFrame by follower count in descending order (most popular clubs first)
    df_sorted = df.sort_values(by='followers', ascending=False).copy()

    # Step 5: Assign a rank to each club based on its number of followers
    df_sorted['Rank'] = range(1, len(df_sorted) + 1)

    # Step 6: Display a header for the dashboard
    st.header("Club Overview")

    # Step 7: Create the first row of visualizations
    col1, col2 = st.columns(2)  # Two side-by-side charts

    # on the left column we create a pie chart of club categories
    with col1:
        st.subheader("Clubs by Category")
        category_counts = df['categoryName'].value_counts()  # Count how many clubs per category
        fig1, ax1 = plt.subplots(figsize=(6, 6))
        ax1.pie(category_counts, labels=category_counts.index, autopct='%1.1f%%', startangle=90)
        plt.style.use('bmh')  # Use a clean matplotlib style
        ax1.set_title("Clubs by Category")
        st.pyplot(fig1)       # Render the plot in the Streamlit app

    #on the right column we create a pie chart of recruitment status
    with col2:
        st.subheader("Recruitment Status")
        recruit_counts = df['isRecruiting'].value_counts()  # Count clubs by recruitment status
        fig2, ax2 = plt.subplots(figsize=(6, 6))
        ax2.pie(recruit_counts, labels=recruit_counts.index, autopct='%1.1f%%', startangle=90)
        ax2.set_title("Recruitment Status Distribution")
        plt.style.use('bmh')
        st.pyplot(fig2)

    # Step 8: Create the second row of visualizations
    col3, col4 = st.columns(2)

    # on the left column of the second row we visualise the member size distribution
    with col3:
        st.subheader("Member Size Distribution")
        members_counts = df['numberOfMembers'].value_counts()
        fig3, ax3 = plt.subplots(figsize=(6, 6))
        ax3.pie(members_counts, labels=members_counts.index, autopct='%1.1f%%', startangle=90)
        plt.style.use('bmh')
        ax3.set_title("Distribution by Member Size")
        st.pyplot(fig3)

    # on the right column we create a bar chart comparing member size with recruitment status
    with col4:
        st.subheader("Member Size vs. Recruitment Status")

        # create ordered member size categories for consistent display
        cat_order = pd.api.types.CategoricalDtype(
            categories=["1-10", "11-30", "31-50", "51-100", "101 & more"],
            ordered=True
        )
        #  onvert 'numberOfMembers' to categorical type using our defined order
        df['orderedMembers'] = df['numberOfMembers'].astype(cat_order)

        # create a cross-tab (pivot table) to count recruitment status per member size category
        ct = pd.crosstab(df['orderedMembers'], df['isRecruiting'])

        fig4, ax4 = plt.subplots(figsize=(6, 6))
        ct.plot(kind='bar', ax=ax4)  # Bar chart
        ax4.set_xlabel("Number of Members")
        ax4.set_ylabel("Number of Clubs")
        ax4.set_title("Member Size vs. Recruitment Status")
        plt.style.use('bmh')
        ax4.legend(title="Recruiting ?")
        st.pyplot(fig4)

    # Step 9: Section to display detailed club info
    st.header("Club Details")

    # Step 10: Add filtering options for the user
    search_query = st.text_input("Search club by name:")
    recruit_filter = st.selectbox("Filter by Recruiting Status:", options=["All", "Yes", "No"])
    category_options = ["All"] + sorted(df['categoryName'].unique())  # Generate a sorted list of all categories
    category_filter = st.selectbox("Filter by Category:", options=category_options)

    # Make a copy of the sorted data for filtering
    filtered_df = df_sorted.copy()

    # Step 11: Apply text search filter
    if search_query:
        filtered_df = filtered_df[filtered_df['name'].str.contains(search_query, case=False, na=False)]

    # Step 12: Apply recruitment filter
    if recruit_filter != "All":
        filtered_df = filtered_df[filtered_df['isRecruiting'] == recruit_filter]

    # Step 13: Apply category filter
    if category_filter != "All":
        filtered_df = filtered_df[filtered_df['categoryName'] == category_filter]

    # Step 14: Display either a "no results" message or the filtered club details
    if filtered_df.empty:
        st.write("No clubs found matching the selected filters.")
    else:
        # Iterate through each filtered club and display its details nicely
        for _, row in filtered_df.iterrows():
            with st.container():
                st.markdown(f"### {row['name']} (Followers Rank #{row['Rank']})")
                st.write(f"**Category:** {row['categoryName']}")
                st.write(f"**Number of Members:** {row['numberOfMembers']}")
                st.write(f"**Followers:** {row['followers']}")
                st.write(f"**Recruiting:** {row['isRecruiting']}")
                st.write(f"**Description:** {row['description']}")
                st.write("---")  # Horizontal rule to separate clubs

# Entry point: Run the main function if this file is executed directly
if __name__ == "__main__":
    main()

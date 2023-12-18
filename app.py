import streamlit as st
import pandas as pd
import base64
from io import BytesIO

def main():
    st.title("Excel Report Generator")

    # File upload
    uploaded_file = st.file_uploader("Upload an Excel file", type=["xls", "xlsx"])

    if uploaded_file is not None:
        # Read Excel file into DataFrame
        df = pd.read_excel(uploaded_file)

        # Display uploaded data
        st.subheader("Uploaded Data:")
        st.dataframe(df)

        # Generate a simple report
        st.subheader("Generated Report:")
        report_data = df.head()  # You can customize this part based on your requirements
        st.dataframe(report_data)

        # Export button to download the report as Excel
        st.subheader("Export Report:")
        export_button = st.button("Export Report as Excel")
        if export_button:
            export_filename = "generated_report.xlsx"
            st.markdown(get_table_download_link(report_data, export_filename), unsafe_allow_html=True)

def get_table_download_link(df, filename):
    """Generate a download link for the DataFrame as an Excel file."""
    excel_buffer = BytesIO()
    df.to_excel(excel_buffer, index=False, header=True, engine="openpyxl")
    excel_data = excel_buffer.getvalue()
    excel_buffer.close()
    b64 = base64.b64encode(excel_data).decode()
    href = f'<a href="data:application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;base64,{b64}" download="{filename}">Download Excel file</a>'
    return href

if __name__ == "__main__":
    main()

import streamlit as st
#https://docs.google.com/spreadsheets/d/e/2PACX-1vSXr-fUgTz_OOWDXHqMMNKCYu8lHUM_DwHPuKpEzn4kQUQkLfKIm2rrlZG8v6iRR8dOP168pKSikja-/pubhtml
def embed_google_sheet(sheet_url, width=1000, height=600, sendlink="x"):
    """Function to embed a published Google Sheet"""
    st.markdown(f'<a href="{sendlink}">Click here to be taken to a filterable and searchable sheet</a>', unsafe_allow_html=True)
    iframe = f'<iframe src="{sheet_url}" width="{width}%" height="{height}" frameborder="0"></iframe>'
    return iframe

def main():
    # Set page configuration
    st.set_page_config(
        page_title="@JonPGH Reports Viewer",
        page_icon="📊",
        layout="wide"
    )

    # Title
    st.title("@JonPGH Reports Viewer")

    # Define your Google Sheets URLs and their custom heights
    # Replace these with your actual sheet URLs and adjust heights as needed
    sheets = {
        "Yesterday SP": {
            "url": "https://docs.google.com/spreadsheets/d/e/2PACX-1vSXr-fUgTz_OOWDXHqMMNKCYu8lHUM_DwHPuKpEzn4kQUQkLfKIm2rrlZG8v6iRR8dOP168pKSikja-/pubhtml",
            "height": 1000,
            "width": 100,
            "sendlink": "https://docs.google.com/spreadsheets/d/1LfkPerLCt5jwtnhz4DwxSruo88CU6JnJRrjBSVnYETo/edit?gid=0#gid=0"
        },
        "Automated SP Ranks": {
            "url": "https://docs.google.com/spreadsheets/d/e/2PACX-1vSlQ4AFKZHaxRJJrfLIOlh2kjwaA6P65NqM4bRLcryZ_i4ClcuJYrCNt1l_52fN-IYDfrtb1d_pBav8/pubhtml",
            "height": 1200,
            "width": 100,
            "sendlink": "https://docs.google.com/spreadsheets/d/1UXv49REVrYX4CNPaWE9f_ZrPa4BwYliduQbt5XWfS08/edit?usp=sharing"
        },
        "Player Checklist": {
            "url": "https://docs.google.com/spreadsheets/d/e/2PACX-1vT4vzpvmqcxEiRPEJpRzfxZaquIKs0bLVVtU0-Ft6KB9AI-HyvLgaWKnzVliyNW76DTKC61zgsLZdeN/pubhtml",
            "height": 1200,
            "width": 100,
            "sendlink": "https://docs.google.com/spreadsheets/d/1WYeOMCzyMb1OK1P1Z3g4HFtIIpqtPx465hA8eO2pO9k/edit?gid=1165302100#gid=1165302100"
        },
        "Start Ranks": {
            "url": "https://docs.google.com/spreadsheets/d/e/2PACX-1vRAyYm2-WI12f2LvT7hspejRcUVuqdcTCipOw7AJlNzZMughxVkRWJFVG39gXcf8xJgQk7iG1660yn9/pubhtml",
            "height": 1200,
            "width": 100,
            "sendlink": "https://docs.google.com/spreadsheets/d/1yZfWaVJtVwtu8Mgdt1nAJJ8chBnSYL1U1DTrsQUtQ9Y/edit?gid=0#gid=0"
        },
        "Bullpen Data": {
            "url": "https://docs.google.com/spreadsheets/d/e/2PACX-1vRL1UJ_X4SjTnG083RAMEhec_3LDZ7WerQmCGpzdZ0rtzIGX7fNgeThbs6Lqg9V_SEiFuZUa3PzRvMj/pubhtml",
            "height": 1200,
            "width": 100,
            "sendlink": "https://docs.google.com/spreadsheets/d/1UXv49REVrYX4CNPaWE9f_ZrPa4BwYliduQbt5XWfS08/edit?usp=sharing"
        },
        "Daily Matchup Cheat Sheet": {
            "url": "https://docs.google.com/spreadsheets/d/e/2PACX-1vT0Pv08UyK4mUUWdD1Qgb_0mtBh5CGn8r6cIN5uCGxuoMpwo-oKJdPMPK0Dp-HLEs7bQSgYL_5s6uRo/pubhtml",
            "height": 1200,
            "width": 100,
            "sendlink": "https://docs.google.com/spreadsheets/d/1TWawMcNVrI-pQg2XK4XBT5rBVtjJIiDTWIoiIqeOHL4/edit?usp=sharing"
        },
        "Upcoming Probable Pitchers": {
            "url": "https://docs.google.com/spreadsheets/d/e/2PACX-1vQBhezcgx6C7owN2rvoUehvlppLsxJNd2u-nfQpI7pMmvs_uEYTf-245ez2AyMF6JoekkgMnrMwCuul/pubhtml",
            "height": 1200,
            "width": 100,
            "sendlink": "https://docs.google.com/spreadsheets/d/1cen29W7B_lK12A_u_4lvwYg-pljg9Vcc24QsVy0sL6Y/edit?usp=sharing"
        }
    }

    # Sidebar with radio buttons
    st.sidebar.title("Select a Sheet")
    selected_sheet = st.sidebar.radio(
        "Choose a sheet to view:",
        list(sheets.keys())
    )

    # Display the selected sheet
    st.header(selected_sheet)
    sheet_info = sheets[selected_sheet]
    st.markdown(
        embed_google_sheet(sheet_info["url"], height=sheet_info["height"], width=sheet_info["width"], sendlink=sheet_info["sendlink"]),
        unsafe_allow_html=True
    )

    # Add custom CSS for better styling
    st.markdown("""
        <style>
        iframe {
            border: 1px solid #cccccc;
            border-radius: 5px;
            overflow: hidden;
        }
        .stRadio > label {
            font-size: 16px;
            padding: 8px;
        }
        </style>
    """, unsafe_allow_html=True)

    # Footer
    st.sidebar.markdown("---")
    st.sidebar.write("Switch between sheets using the options above.")

if __name__ == "__main__":
    main()
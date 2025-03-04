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
            "sendlink": "https://docs.google.com/spreadsheets/d/1NcQ62cP1Sebe628iLLmAhh7O9ZU54FvvsUpylOpNFkw/edit?usp=sharing"
        },
        "Player Checklist": {
            "url": "https://docs.google.com/spreadsheets/d/e/2PACX-1vT4vzpvmqcxEiRPEJpRzfxZaquIKs0bLVVtU0-Ft6KB9AI-HyvLgaWKnzVliyNW76DTKC61zgsLZdeN/pubhtml",
            "height": 1200,
            "width": 100,
            "sendlink": "https://docs.google.com/spreadsheets/d/1WYeOMCzyMb1OK1P1Z3g4HFtIIpqtPx465hA8eO2pO9k/edit?usp=sharing"
        },
        "Player Rater": {
            "url": "https://docs.google.com/spreadsheets/d/e/2PACX-1vT3c3eUbG_JbBh3U4d8-L89Ee7GVanIAWwUwNrEfcivqD7C66bTs2F0pjoJfdYSGHypfFFa8QtKY0Mz/pubhtml",
            "height": 1200,
            "width": 100,
            "sendlink": "https://docs.google.com/spreadsheets/d/1QxshtWnbruCr73TygDoYW60qXgcC6H94ylPP44uW4os/edit?usp=sharing"
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
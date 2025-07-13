import streamlit as st

class MultiPage:
    """Framework for combining multiple streamlit applications."""
    
    def __init__(self):
        self.pages = []
    
    def add_page(self, title, func):
        """Add a new page to the app"""
        self.pages.append({
            "title": title,
            "function": func
        })
    
    def run(self):
        """Run the app"""
        # Create sidebar navigation
        st.sidebar.markdown("## Navigation")
        
        # Create page selection
        page = st.sidebar.selectbox(
            "Select Page",
            self.pages,
            format_func=lambda page: page["title"]
        )
        
        # Display page info in sidebar
        st.sidebar.markdown("---")
        st.sidebar.markdown(f"**Current Page:** {page['title']}")
        
        # Add some styling
        st.sidebar.markdown("---")
        st.sidebar.markdown("### About")
        st.sidebar.info(
            "This dashboard demonstrates a brain tumor classification model "
            "with interactive visualizations and business value analysis."
        )
        
        # Run the selected page
        page["function"]()
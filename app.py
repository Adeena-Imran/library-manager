import streamlit as st
from book import Book
from library import Library

FILENAME = "my_library.json"


lib = Library()
lib.load_file(FILENAME)



st.title("📚 Personal Library Manager")




tab1, tab2, tab3, tab4 = st.tabs(["➕ Add Book", "📖 View All", "🔍 Search", "❌ Remove Book"])

with tab1:
    st.header("Add a New Book📕")
    title = st.text_input("Title")
    author = st.text_input("Author")
    year = st.text_input("Year")
    genre = st.text_input("Genre")

    if st.button("Add Book"):
        if title and author and year and genre:
            lib.add_books(Book(title, author, year, genre))
            lib.save_to_file(FILENAME)
            st.success("Book added successfully!")
        else:
            st.warning("Please fill in all fields.")

with tab2:
    st.header("All Books📚")
    books = lib.list_books()
    if books:
        for book in books:
            st.write(book)
    else:
        st.info("No books in your library yet.")

with tab3:
    st.header("Search for a Book")
    keyword = st.text_input("Enter a title or author to search")
    if keyword:
        results = lib.search_books(keyword)
        if results:
            for book in results:
                st.write(book)
        else:
            st.warning("No matching books found.")

with tab4:
    st.header("Remove a Book by ISBN")
    genre_to_remove = st.text_input("Enter Genre")
    if st.button("Remove Book"):
        lib.remove_books(genre_to_remove)
        lib.save_to_file(FILENAME)
        st.success("Book removed if it existed.")

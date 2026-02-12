"""Unsubscribe page for removing a user and their subscriptions."""

import streamlit as st

from database_connection import fetch_dataframe, run_change
from subscribe_page import is_valid_email


def find_customer_id(email: str) -> int | None:
    """Find the customer id for an email or return None."""
    result = fetch_dataframe("""
    SELECT customer_id
    FROM customer
    WHERE customer_email = %s
    LIMIT 1;
    """, values=(email,))
    if result is None or result.empty:
        return None

    return int(result.iloc[0]["customer_id"])


def remove_customer(customer_id: int) -> None:
    """Remove a customer and any subscriptions linked to them."""
    run_change("""
    DELETE FROM subscription
    WHERE customer_id = %s;
    """, values=(customer_id,))
    
    run_change("""
    DELETE FROM customer
    WHERE customer_id = %s;
    """, values=(customer_id,))


def render_unsubscribe_page() -> None:
    """Render the unsubscribe page and handle the form submit."""
    st.title("Unsubscribe")
    st.write("Enter your email to remove all subscriptions.")

    with st.form("unsubscribe_form"):
        email = st.text_input("Email address", placeholder="name@example.com")
        submitted = st.form_submit_button("Unsubscribe")

    if not submitted:
        st.markdown("<a href='?'>Back</a>", unsafe_allow_html=True)
        return

    cleaned_email = (email or "").strip().lower()
    if not is_valid_email(cleaned_email):
        st.error("Please enter a valid email address.")
        st.markdown("<a href='?'>Back</a>", unsafe_allow_html=True)
        return

    try:
        customer_id = find_customer_id(cleaned_email)
        if customer_id is None:
            st.warning("No customer found with that email.")
            st.markdown("<a href='?'>Back</a>", unsafe_allow_html=True)
            return

        remove_customer(customer_id)
        st.success("You have been unsubscribed.")
        st.markdown("<a href='?'>Return to dashboard</a>",
                    unsafe_allow_html=True)

    except Exception:  
        st.error("Something went wrong while unsubscribing.")
        st.markdown("<a href='?'>Back</a>", unsafe_allow_html=True)

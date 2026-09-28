import streamlit as st
from contracts import Ticket
from triage import run

st.title("Ticket Triage")
st.write("One ticket. Four categories.")

text = st.text_area("Support ticket", "You took my money twice.")
mode = st.radio("Where to classify", ["mock", "live"], horizontal=True)

if st.button("Classify ticket"):
    ticket = Ticket(id="DEMO", text=text)
    st.session_state["record"] = run(ticket, mode)

record = st.session_state.get("record")
if record:
    prediction = record["prediction"]
    usage = record["usage"] or {}
    st.subheader(prediction["category"])
    st.write(prediction["reason"])
    st.caption(
        f"mode {record['mode']} · "
        f"model {record['model'] or 'none'} · "
        f"tokens {usage.get('input_tokens', 0)} in / {usage.get('output_tokens', 0)} out · "
        f"{record['latency_ms']} ms"
    )

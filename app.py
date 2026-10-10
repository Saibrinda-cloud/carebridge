import streamlit as st
from datetime import date, datetime

# ---------------- PAGE SETTINGS ----------------
st.set_page_config(
    page_title="CareBridge",
    page_icon="🏥",
    layout="wide"
)

st.title("🏥 CareBridge")
st.caption("One patient. One connected medical history.")
st.info(
    "DEMO ONLY: All patient information is fictional. "
    "This prototype does not provide real medical security."
)

# ---------------- SAMPLE DATA ----------------
SAMPLE_PATIENTS = [
    {
        "id": "CB1001",
        "name": "Aarav Sharma",
        "dob": "2002-04-12"
    },
    {
        "id": "CB1002",
        "name": "Meera Iyer",
        "dob": "1999-09-23"
    },
    {
        "id": "CB1003",
        "name": "Rahul Kumar",
        "dob": "2001-01-05"
    },
]

SAMPLE_RECORDS = [
    {
        "patient_id": "CB1001",
        "record_type": "Consultation",
        "record_date": "2026-10-02",
        "title": "General health checkup",
        "notes": "Fictional demo entry. Routine checkup."
    },
    {
        "patient_id": "CB1001",
        "record_type": "Lab Report",
        "record_date": "2026-10-04",
        "title": "Blood test",
        "notes": "Fictional demo entry. Sample report recorded."
    },
    {
        "patient_id": "CB1002",
        "record_type": "Prescription",
        "record_date": "2026-10-01",
        "title": "Sample prescription",
        "notes": "Fictional demo entry. No real medication advice."
    },
]

# ---------------- INITIALIZE APP DATA ----------------
if "patients" not in st.session_state:
    st.session_state.patients = [p.copy() for p in SAMPLE_PATIENTS]

if "records" not in st.session_state:
    st.session_state.records = [r.copy() for r in SAMPLE_RECORDS]

if "access_requests" not in st.session_state:
    st.session_state.access_requests = []

if "audit_logs" not in st.session_state:
    st.session_state.audit_logs = [
        {
            "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "action": "Demo application opened",
            "details": "Sample data loaded"
        }
    ]

def log_action(action, details):
    st.session_state.audit_logs.insert(
        0,
        {
            "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "action": action,
            "details": details,
        },
    )

# ---------------- SIDEBAR ----------------
st.sidebar.title("CareBridge Menu")
page = st.sidebar.radio(
    "Choose a page",
    [
        "Dashboard",
        "Patient Records",
        "Add Medical Record",
        "Access & Consent",
        "Activity Log",
    ],
)

st.sidebar.caption("CareBridge ID is a demo identifier.")
st.sidebar.caption("No Aadhaar or real patient data is used.")

# ---------------- DASHBOARD ----------------
if page == "Dashboard":
    st.header("Dashboard")
    st.write("A simple place to find patient histories and manage demo records.")

    col1, col2, col3 = st.columns(3)
    col1.metric("Patients", len(st.session_state.patients))
    col2.metric("Medical records", len(st.session_state.records))
    col3.metric("Access requests", len(st.session_state.access_requests))

    st.subheader("Find a patient")
    search = st.text_input(
        "Enter a CareBridge ID or patient name",
        placeholder="Example: CB1001"
    ).strip().lower()

    matches = [
        p for p in st.session_state.patients
        if search == ""
        or search in p["id"].lower()
        or search in p["name"].lower()
    ]

    if matches:
        for patient in matches:
            with st.container(border=True):
                st.write("**" + patient["name"] + "**")
                st.write("CareBridge ID: " + patient["id"])
                st.write("Date of birth: " + patient["dob"])
                if st.button(
                    "View patient records",
                    key="dashboard_" + patient["id"]
                ):
                    st.session_state.selected_patient = patient["id"]
                    st.session_state.open_patient_records = True
                    st.rerun()
    else:
        st.warning("No matching patient found.")

    if st.session_state.get("open_patient_records", False):
        st.divider()
        selected_id = st.session_state.get("selected_patient", "")
        patient = next(
            (p for p in st.session_state.patients if p["id"] == selected_id),
            None
        )
        if patient:
            st.subheader("Medical timeline: " + patient["name"])
            patient_records = [
                r for r in st.session_state.records
                if r["patient_id"] == selected_id
            ]
            patient_records.sort(
                key=lambda r: r["record_date"], reverse=True
            )
            if patient_records:
                for record in patient_records:
                    st.markdown(
                        "**" + record["record_date"] + " — "
                        + record["title"] + "**"
                    )
                    st.write("Type: " + record["record_type"])
                    st.write(record["notes"])
                    st.divider()
            else:
                st.write("No records have been added yet.")

# ---------------- PATIENT RECORDS ----------------
elif page == "Patient Records":
    st.header("Patient Records")
    search = st.text_input(
        "Search by CareBridge ID or name",
        placeholder="Example: Meera or CB1002"
    ).strip().lower()

    matches = [
        p for p in st.session_state.patients
        if search == ""
        or search in p["id"].lower()
        or search in p["name"].lower()
    ]

    if not matches:
        st.warning("No matching patient found.")
    else:
        options = {
            p["name"] + " (" + p["id"] + ")": p["id"]
            for p in matches
        }
        selected_label = st.selectbox(
            "Select a patient",
            list(options.keys())
        )
        patient_id = options[selected_label]
        patient = next(
            p for p in st.session_state.patients
            if p["id"] == patient_id
        )

        st.subheader(patient["name"])
        st.write("**CareBridge ID:** " + patient["id"])
        st.write("**Date of birth:** " + patient["dob"])
        st.subheader("Medical timeline")

        records = [
            r for r in st.session_state.records
            if r["patient_id"] == patient_id
        ]
        records.sort(key=lambda r: r["record_date"], reverse=True)

        if not records:
            st.info("No records are available for this patient.")
        else:
            for record in records:
                with st.container(border=True):
                    st.write(
                        "**" + record["record_date"] + " — "
                        + record["title"] + "**"
                    )
                    st.caption(record["record_type"])
                    st.write(record["notes"])

# ---------------- ADD A MEDICAL RECORD ----------------
elif page == "Add Medical Record":
    st.header("Add a Medical Record")
    st.write("Use fictional information for this demonstration.")

    patient_options = {
        p["name"] + " (" + p["id"] + ")": p["id"]
        for p in st.session_state.patients
    }

    with st.form("add_record_form"):
        patient_label = st.selectbox(
            "Choose patient",
            list(patient_options.keys())
        )
        record_type = st.selectbox(
            "Record type",
            ["Consultation", "Lab Report", "Prescription", "Diagnosis", "Other"]
        )
        record_date = st.date_input("Record date", value=date.today())
        title = st.text_input(
            "Record title",
            placeholder="Example: Follow-up consultation"
        )
        notes = st.text_area(
            "Notes",
            placeholder="Enter fictional demo notes"
        )
        submitted = st.form_submit_button("Save record")

    if submitted:
        if not title.strip() or not notes.strip():
            st.error("Please enter both a title and notes.")
        else:
            patient_id = patient_options[patient_label]
            st.session_state.records.append(
                {
                    "patient_id": patient_id,
                    "record_type": record_type,
                    "record_date": record_date.isoformat(),
                    "title": title.strip(),
                    "notes": notes.strip(),
                }
            )
            log_action(
                "Medical record added",
                title.strip() + " for " + patient_id
            )
            st.success("Demo record added to the timeline!")

# ---------------- ACCESS AND CONSENT ----------------
elif page == "Access & Consent":
    st.header("Access & Consent")
    st.warning(
        "Simulation only: selecting an action here does not authenticate "
        "a doctor or enforce real data permissions."
    )

    patient_options = {
        p["name"] + " (" + p["id"] + ")": p["id"]
        for p in st.session_state.patients
    }

    with st.form("access_request_form"):
        patient_label = st.selectbox(
            "Patient",
            list(patient_options.keys())
        )
        doctor = st.selectbox(
            "Requesting doctor",
            ["Dr. Ananya Rao", "Dr. Vikram Patel", "Dr. Sara Thomas"]
        )
        purpose = st.selectbox(
            "Reason for access",
            [
                "Follow-up consultation",
                "Second opinion",
                "Emergency care demonstration",
                "Routine review",
            ]
        )
        request_submitted = st.form_submit_button("Request access")

    if request_submitted:
        patient_id = patient_options[patient_label]
        st.session_state.access_requests.append(
            {
                "patient_id": patient_id,
                "doctor": doctor,
                "purpose": purpose,
                "status": "Pending",
            }
        )
        log_action(
            "Access requested",
            doctor + " requested access to " + patient_id
        )
        st.success("Access request created.")
        st.rerun()

    st.subheader("Requests")
    if not st.session_state.access_requests:
        st.info("No access requests yet.")
    else:
        for i, request in enumerate(st.session_state.access_requests):
            patient_name = next(
                (
                    p["name"] for p in st.session_state.patients
                    if p["id"] == request["patient_id"]
                ),
                request["patient_id"]
            )
            with st.container(border=True):
                st.write("**" + patient_name + "**")
                st.write("Doctor: " + request["doctor"])
                st.write("Purpose: " + request["purpose"])
                st.write("Status: **" + request["status"] + "**")

                if request["status"] == "Pending":
                    col1, col2 = st.columns(2)
                    if col1.button("Approve", key="approve_" + str(i)):
                        request["status"] = "Approved"
                        log_action(
                            "Demo access approved",
                            request["doctor"] + " / " + request["patient_id"]
                        )
                        st.rerun()
                    if col2.button("Reject", key="reject_" + str(i)):
                        request["status"] = "Rejected"
                        log_action(
                            "Demo access rejected",
                            request["doctor"] + " / " + request["patient_id"]
                        )
                        st.rerun()

                elif request["status"] == "Approved":
                    if st.button("Revoke access", key="revoke_" + str(i)):
                        request["status"] = "Revoked"
                        log_action(
                            "Demo access revoked",
                            request["doctor"] + " / " + request["patient_id"]
                        )
                        st.rerun()

# ---------------- ACTIVITY LOG ----------------
elif page == "Activity Log":
    st.header("Activity Log")
    st.write("Recent actions in this running demo session.")

    if not st.session_state.audit_logs:
        st.info("No activity recorded yet.")
    else:
        for entry in st.session_state.audit_logs:
            with st.container(border=True):
                st.caption(entry["time"])
                st.write("**" + entry["action"] + "**")
                st.write(entry["details"])

st.divider()
st.caption(
    "CareBridge prototype • Fictional data only • "
    "Demo state may reset when the app restarts."
)

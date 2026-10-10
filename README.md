# CareBridge

## Live Demo

https://carebridge-djeayk34a8bsafhrodwfsl.streamlit.app/

## Problem
Medical information can be scattered across different clinics and
providers. This can make it difficult to understand a patient's medical
history and maintain continuity of care.

## Our solution
CareBridge is a web application prototype that demonstrates how a
patient's medical history could be organized in one timeline, with a
consent workflow for requesting and managing access.

## Features
- Search patients using a CareBridge ID or name
- View medical records in chronological order
- Add fictional medical records
- Demonstrate access requests, approval, rejection, and revocation
- View an activity log

## Technology
- Python
- Streamlit
- GitHub
- Streamlit Community Cloud
- Open-Source Libraries and API Disclosure
Python: Programming language used to build the application.
Streamlit: Open-source Python library used to create the web interface.
GitHub: Used to store and manage the project's source code.
Streamlit Community Cloud: Used to deploy the application.
The application uses Streamlit and does not intentionally integrate with external healthcare APIs. The dependency list is provided in requirements.txt.

## Run locally

Requirements: Python 3.9 or newer.

1. Clone this repository:

```bash
git clone https://github.com/Saibrinda-cloud/carebridge.git
cd carebridge
```

2. Install the dependencies:

```bash
pip install -r requirements.txt
```

3. Start the application:

```bash
streamlit run app.py
```

## Important limitations
This is a hackathon prototype using fictional sample data.
The current version does not use a persistent database or real
authentication. Its access and consent workflow is simulated.
It must not be used for real patient data or clinical decisions.

## Future improvements
- Persistent database
- Verified doctor and patient accounts
- Real permission enforcement
- Secure document storage
- Integration with approved healthcare systems

import streamlit as st

st.set_page_config(
    page_title="Head & Neck Quick Reminder",
    page_icon="🩺",
    layout="centered"
)

st.title("Head & Neck Region")
st.caption("Doctor quick reminder • Red flags & differential diagnoses • Rule-based only")

st.warning(
    "This page is a concise clinical reminder, not a diagnostic tool. "
    "Use clinical judgment and local referral protocols."
)

tab1, tab2 = st.tabs(["🚩 Red Flags", "🧠 Differential Diagnoses"])

with tab1:
    st.subheader("Red Flags: Head & Neck")

    st.markdown("""
### General
- Fever, toxic appearance, sepsis concern
- Rapidly progressive swelling
- Severe pain out of proportion
- Immunocompromised state
- Recent trauma, bite, procedure, or foreign body

### Airway / Deep Neck
- Stridor, dyspnea, drooling
- Dysphagia or odynophagia
- Trismus
- Muffled “hot potato” voice
- Neck stiffness or floor-of-mouth swelling

### Neurologic / Vascular
- New focal neurologic deficit
- Severe sudden headache
- Altered mental status
- Syncope
- Horner syndrome
- Pulsatile neck mass

### Eye / Orbit
- Eye pain with reduced vision
- Proptosis
- Painful or restricted eye movement
- Diplopia
- Periorbital swelling with fever

### Ear
- Sudden sensorineural hearing loss
- Vertigo with hearing loss or neurologic signs
- Mastoid tenderness/swelling
- Facial nerve palsy
- Severe otalgia in diabetic/immunocompromised patient

### Oral / Neck Mass
- Non-healing ulcer > 2 weeks
- Unexplained neck mass > 2–3 weeks
- Hard, fixed, enlarging lymph node
- Weight loss, night sweats
- Hoarseness > 3 weeks
- Hemoptysis
""")

with tab2:
    st.subheader("Differential Diagnoses: Head & Neck Lesions")

    st.markdown("""
### Skin / Scalp / Face
- Acne, folliculitis, furuncle
- Cellulitis, erysipelas, abscess
- Impetigo
- Herpes simplex, herpes zoster
- Contact dermatitis, atopic dermatitis
- Seborrheic dermatitis
- Tinea faciei / capitis
- Insect bite reaction
- Benign tumor: cyst, lipoma, nevus
- Malignancy: BCC, SCC, melanoma

### Ear Region
- Otitis externa
- Acute otitis media
- Cerumen impaction
- Perichondritis
- Mastoiditis
- Ramsay Hunt syndrome
- Sudden sensorineural hearing loss
- Foreign body / trauma

### Eye / Periorbital
- Conjunctivitis
- Hordeolum / chalazion
- Preseptal cellulitis
- Orbital cellulitis
- Herpes zoster ophthalmicus
- Corneal abrasion / keratitis
- Acute glaucoma

### Nose / Sinus
- Allergic rhinitis
- Acute rhinosinusitis
- Nasal vestibulitis
- Epistaxis causes
- Nasal polyp
- Foreign body
- Facial trauma

### Oral Cavity / Throat
- Aphthous ulcer
- Herpes simplex
- Oral candidiasis
- Dental abscess
- Gingivitis / periodontitis
- Tonsillitis / pharyngitis
- Peritonsillar abscess
- Ludwig angina
- Oral cancer

### Neck Mass / Lymph Node
- Reactive lymphadenopathy
- Bacterial lymphadenitis
- Tuberculosis lymphadenitis
- Thyroid nodule / goiter
- Salivary gland disease
- Branchial cleft cyst
- Thyroglossal duct cyst
- Lymphoma
- Metastatic head & neck cancer

### Pain Syndromes
- Tension headache
- Migraine
- Cervicogenic headache
- Temporomandibular disorder
- Trigeminal neuralgia
- Occipital neuralgia
- Myofascial pain syndrome
- Cervical radiculopathy
""")

st.divider()

st.caption(
    "KU KPS Pain Consult • QR doctor reminder • No AI • No data collection"
)

import streamlit as st
from io import BytesIO
from datetime import datetime
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle

from translations import option_label, translate

st.set_page_config(layout="wide")

# Language options are defined locally so the selector always displays them,
# independently of the contents or cache state of translations.py.
LANGUAGE_OPTIONS = {
    "English": "en",
    "Español": "es",
    "Deutsch": "de",
    "Português": "pt",
    "Français": "fr",
}

# Canonical internal values remain in English so translations never alter scoring.
xerop = {"Never": 0, "Sometimes": 1, "Always": 2}
medop = {"No": 0, "Yes": 1}
diabop = {"No": 0, "Yes": 1}
halop = {"0": 1, "1": 1, "2": 2, "3": 2, "4": 3, "5": 3}
candop = {"No": 0, "Yes": 2}
lendop = {"No": 0, "Yes": 1}
perdop = {"None": 0, "Moderate": 1, "Severe": 2}
ckdop = {"0": 0, "1": 0, "2": 0, "3": 1, "4": 2, "5": 2, "Dialysis": 3}

CONTAINER_HEIGHT = 560
IMAGE_DIR = Path(__file__).parent / "images"

INDICATOR_IDS = (
    "xerostomia", "medication", "diabetes", "halitosis",
    "candidiasis", "tongue", "periodontal", "ckd",
)

SPECIFIC_RECOMMENDATION_KEYS = {
    indicator_id: [
        f"recommendation.{indicator_id}.1",
        f"recommendation.{indicator_id}.2",
        f"recommendation.{indicator_id}.3",
    ]
    for indicator_id in INDICATOR_IDS
}

GENERAL_RECOMMENDATION_KEYS = [f"general.{index}" for index in range(1, 9)]

if "calculated" not in st.session_state:
    st.session_state.calculated = False
    st.session_state.total_points = 0



def update_language():
    selected_name = st.session_state.get("language_name", "English")
    st.session_state.language_code = LANGUAGE_OPTIONS[selected_name]
    st.session_state.calculated = False

def tr(key: str, **kwargs) -> str:
    """Translate using the language currently selected in the interface."""
    return translate(st.session_state.get("language_code", "en"), key, **kwargs)


def get_risk_id(points: int) -> str:
    if points <= 3:
        return "low"
    if points <= 6:
        return "moderate"
    return "high"


def get_risk_level(points: int, language_code: str) -> str:
    return translate(language_code, f"risk.{get_risk_id(points)}")


def get_risk_message(points: int, language_code: str) -> str:
    return translate(language_code, f"pdf.{get_risk_id(points)}_message")


def build_patient_report_pdf(
    patient_name: str,
    patient_data: list[dict],
    total_points: int,
    language_code: str,
) -> BytesIO:
    buffer = BytesIO()
    doc = SimpleDocTemplate(
        buffer,
        pagesize=A4,
        rightMargin=40,
        leftMargin=40,
        topMargin=40,
        bottomMargin=40,
    )

    styles = getSampleStyleSheet()
    title_style = ParagraphStyle(
        "TitleStyle", parent=styles["Title"], fontSize=18,
        leading=22, spaceAfter=16,
    )
    heading_style = ParagraphStyle(
        "HeadingStyle", parent=styles["Heading2"], fontSize=13,
        leading=16, spaceBefore=12, spaceAfter=8,
    )
    normal_style = ParagraphStyle(
        "NormalStyle", parent=styles["Normal"], fontSize=10, leading=14,
    )
    small_style = ParagraphStyle(
        "SmallStyle", parent=styles["Normal"], fontSize=8,
        leading=11, textColor=colors.grey,
    )

    t = lambda key: translate(language_code, key)
    elements = [
        Paragraph(t("pdf.title"), title_style),
        Paragraph(f"<b>{t('pdf.patient_name')}:</b> {patient_name}", normal_style),
        Paragraph(
            f"{t('pdf.generated')}: {datetime.now().strftime('%Y-%m-%d %H:%M')}",
            normal_style,
        ),
        Spacer(1, 12),
    ]

    summary_data = [[t("pdf.risk_category"), get_risk_level(total_points, language_code)]]
    summary_table = Table(summary_data, colWidths=[2.2 * inch, 3.8 * inch])
    summary_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), colors.whitesmoke),
        ("BOX", (0, 0), (-1, -1), 0.8, colors.black),
        ("INNERGRID", (0, 0), (-1, -1), 0.5, colors.grey),
        ("FONTNAME", (0, 0), (0, -1), "Helvetica-Bold"),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("PADDING", (0, 0), (-1, -1), 8),
    ]))

    elements.extend([
        Paragraph(t("pdf.risk_summary"), heading_style),
        summary_table,
        Spacer(1, 10),
        Paragraph(get_risk_message(total_points, language_code), normal_style),
        Spacer(1, 14),
        Paragraph(t("pdf.patient_responses"), heading_style),
    ])

    table_data = [[t("pdf.indicator"), t("pdf.response")]]
    for item in patient_data:
        table_data.append([
            Paragraph(t(f"indicator.{item['id']}"), normal_style),
            Paragraph(option_label(language_code, str(item["response"])), normal_style),
        ])

    indicator_table = Table(table_data, colWidths=[2.7 * inch, 3.3 * inch])
    indicator_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.black),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("BOX", (0, 0), (-1, -1), 0.8, colors.black),
        ("INNERGRID", (0, 0), (-1, -1), 0.5, colors.grey),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("PADDING", (0, 0), (-1, -1), 6),
    ]))
    elements.extend([indicator_table, Spacer(1, 14)])
    elements.append(Paragraph(t("pdf.indicator_meaning"), heading_style))

    for item in patient_data:
        indicator_id = item["id"]
        elements.append(Paragraph(
            f"<b>{t(f'indicator.{indicator_id}')}</b>", normal_style
        ))
        elements.append(Paragraph(t(f"explanation.{indicator_id}"), normal_style))
        elements.append(Spacer(1, 6))

    elements.append(Paragraph(t("pdf.suggestions"), heading_style))
    added_any_specific = False
    for item in patient_data:
        if item["score"] > 0:
            added_any_specific = True
            indicator_id = item["id"]
            elements.append(Paragraph(
                f"<b>{t(f'indicator.{indicator_id}')}</b>", normal_style
            ))
            for key in SPECIFIC_RECOMMENDATION_KEYS[indicator_id]:
                elements.append(Paragraph(f"- {t(key)}", normal_style))
            elements.append(Spacer(1, 6))

    if not added_any_specific:
        elements.append(Paragraph(t("pdf.no_specific"), normal_style))

    elements.append(Paragraph(t("pdf.general_advice"), heading_style))
    for key in GENERAL_RECOMMENDATION_KEYS:
        elements.append(Paragraph(f"- {t(key)}", normal_style))

    elements.extend([
        Spacer(1, 14),
        Paragraph(t("pdf.reminder"), heading_style),
        Paragraph(t("pdf.disclaimer"), small_style),
    ])

    doc.build(elements)
    buffer.seek(0)
    return buffer


# Language is selected before any translated content is rendered.
language_names = list(LANGUAGE_OPTIONS.keys())
current_language_name = st.session_state.get("language_name", language_names[0])
if current_language_name not in LANGUAGE_OPTIONS:
    current_language_name = language_names[0]
st.session_state.language_code = LANGUAGE_OPTIONS[current_language_name]

col_main_left, col_final_right = st.columns([3, 1])

with col_main_left:
    st.markdown(
        f'<h1 class="main-app-title">{tr("app.title")}</h1>',
        unsafe_allow_html=True,
    )
    st.write(tr("app.intro"))

    with st.expander(tr("settings.title")):
        col_lang, col_theme, col_font = st.columns(3)

        with col_lang:
            st.subheader(tr("settings.language"))
            selected_language_name = st.selectbox(
                tr("settings.choose_language"),
                language_names,
                index=language_names.index(current_language_name),
                key="language_name",
                on_change=update_language,
            )
            st.session_state.language_code = LANGUAGE_OPTIONS[selected_language_name]

        with col_theme:
            st.subheader(tr("settings.theme"))
            theme_option = st.selectbox(
                tr("settings.choose_theme"),
                ["Clear", "Dark"],
                format_func=lambda value: tr(
                    "theme.clear" if value == "Clear" else "theme.dark"
                ),
                key="theme_option",
            )

        with col_font:
            st.subheader(tr("settings.font_size"))
            font_option = st.selectbox(
                tr("settings.choose_font_size"),
                ["Small", "Medium", "Large"],
                index=1,
                format_func=lambda value: tr(f"font.{value.lower()}"),
                key="font_size",
            )

    font_sizes = {"Small": "13px", "Medium": "16px", "Large": "19px"}
    selected_size = font_sizes[font_option]

    if theme_option == "Dark":
        theme = {
            "background": "#0E1117",
            "secondary_background": "#161B22",
            "surface": "#1F2630",
            "surface_hover": "#29313D",
            "text": "#F3F4F6",
            "muted_text": "#B8C0CC",
            "border": "#3A4554",
            "input_background": "#11161D",
            "button_background": "#263140",
            "button_hover": "#334155",
            "accent": "#7DB7FF",
            "shadow": "rgba(0, 0, 0, 0.45)",
        }
    else:
        theme = {
            "background": "#FFFFFF",
            "secondary_background": "#F6F8FA",
            "surface": "#FFFFFF",
            "surface_hover": "#F1F5F9",
            "text": "#17202A",
            "muted_text": "#5F6B7A",
            "border": "#D6DCE5",
            "input_background": "#FFFFFF",
            "button_background": "#F8FAFC",
            "button_hover": "#EEF2F7",
            "accent": "#1F6FEB",
            "shadow": "rgba(15, 23, 42, 0.12)",
        }

    st.markdown(
        f"""
        <style>
        :root {{
            color-scheme: {"dark" if theme_option == "Dark" else "light"};
        }}

        /* Main application background */
        .stApp,
        [data-testid="stAppViewContainer"],
        [data-testid="stMain"],
        [data-testid="stMainBlockContainer"] {{
            background-color: {theme["background"]} !important;
            color: {theme["text"]} !important;
        }}

        [data-testid="stHeader"] {{
            background-color: {theme["background"]} !important;
        }}

        /* Global text */
        .stApp,
        .stApp p,
        .stApp li,
        .stApp label,
        .stApp span,
        .stApp div,
        .stApp h1,
        .stApp h2,
        .stApp h3,
        .stApp h4,
        .stApp h5,
        .stApp h6,
        [data-testid="stText"],
        [data-testid="stCaptionContainer"] {{
            color: {theme["text"]};
        }}

        [data-testid="stCaptionContainer"],
        [data-testid="stCaptionContainer"] p,
        .stApp small {{
            color: {theme["muted_text"]} !important;
        }}

        /* Preserve font-size customization for body/interface text */
        [data-testid="stMarkdownContainer"] p,
        [data-testid="stMarkdownContainer"] li,
        [data-testid="stText"],
        [data-testid="stCaptionContainer"],
        label {{
            font-size: {selected_size} !important;
        }}

        [data-baseweb="select"] *,
        [data-baseweb="popover"] * {{
            font-size: {selected_size} !important;
        }}

        [data-testid="stButton"] button,
        [data-testid="stDownloadButton"] button {{
            font-size: {selected_size} !important;
        }}

        [data-testid="stTextInput"] input,
        [data-testid="stNumberInput"] input,
        textarea {{
            font-size: {selected_size} !important;
        }}

        [data-testid="stCheckbox"] *,
        [data-testid="stToggle"] * {{
            font-size: {selected_size} !important;
        }}

        /* Bordered containers and expanders */
        [data-testid="stVerticalBlockBorderWrapper"] {{
            background-color: {theme["surface"]} !important;
            border-color: {theme["border"]} !important;
            box-shadow: 0 1px 4px {theme["shadow"]};
        }}

        [data-testid="stExpander"] {{
            background-color: {theme["surface"]} !important;
            border: 1px solid {theme["border"]} !important;
            border-radius: 0.5rem;
        }}

        [data-testid="stExpander"] summary,
        [data-testid="stExpander"] details,
        [data-testid="stExpander"] div {{
            color: {theme["text"]} !important;
        }}

        /* Selectboxes and popup menus */
        [data-baseweb="select"] > div {{
            background-color: {theme["input_background"]} !important;
            border-color: {theme["border"]} !important;
            color: {theme["text"]} !important;
        }}

        [data-baseweb="select"] input,
        [data-baseweb="select"] svg {{
            color: {theme["text"]} !important;
            fill: {theme["text"]} !important;
        }}

        [data-baseweb="popover"],
        [data-baseweb="popover"] > div,
        [role="listbox"],
        [role="option"] {{
            background-color: {theme["surface"]} !important;
            color: {theme["text"]} !important;
        }}

        [role="option"]:hover,
        [aria-selected="true"] {{
            background-color: {theme["surface_hover"]} !important;
        }}

        /* Text and number inputs */
        [data-testid="stTextInput"] input,
        [data-testid="stNumberInput"] input,
        textarea {{
            background-color: {theme["input_background"]} !important;
            border-color: {theme["border"]} !important;
            color: {theme["text"]} !important;
            -webkit-text-fill-color: {theme["text"]} !important;
        }}

        [data-testid="stNumberInput"] button {{
            background-color: {theme["button_background"]} !important;
            border-color: {theme["border"]} !important;
            color: {theme["text"]} !important;
        }}

        /* Standard and download buttons */
        [data-testid="stButton"] button,
        [data-testid="stDownloadButton"] button {{
            background-color: {theme["button_background"]} !important;
            border: 1px solid {theme["border"]} !important;
            color: {theme["text"]} !important;
        }}

        [data-testid="stButton"] button:hover,
        [data-testid="stDownloadButton"] button:hover {{
            background-color: {theme["button_hover"]} !important;
            border-color: {theme["accent"]} !important;
            color: {theme["text"]} !important;
        }}

        [data-testid="stButton"] button:focus,
        [data-testid="stDownloadButton"] button:focus {{
            border-color: {theme["accent"]} !important;
            box-shadow: 0 0 0 0.15rem color-mix(in srgb, {theme["accent"]} 25%, transparent);
        }}

        /* Dialogs */
        [data-testid="stDialog"] > div,
        [role="dialog"] {{
            background-color: {theme["surface"]} !important;
            color: {theme["text"]} !important;
            border: 1px solid {theme["border"]} !important;
        }}

        [role="dialog"] header,
        [role="dialog"] section,
        [role="dialog"] div {{
            background-color: {theme["surface"]};
            color: {theme["text"]};
        }}

        /* Dividers and links */
        hr {{
            border-color: {theme["border"]} !important;
        }}

        .stApp a {{
            color: {theme["accent"]} !important;
        }}

        /* Toggle and checkbox labels */
        [data-testid="stCheckbox"] label,
        [data-testid="stToggle"] label {{
            color: {theme["text"]} !important;
        }}

        /* Keep status boxes legible in both modes */
        [data-testid="stAlert"] {{
            border-color: {theme["border"]} !important;
        }}

        /* Main title should not be affected by the font-size selector */
        .main-app-title {{
            color: {theme["text"]} !important;
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )

    with st.expander(tr("instructions.title")):
        st.markdown(tr("instructions.body"))

    with st.expander(tr("evidence.title")):
        st.markdown(tr("evidence.body"))

    sub_col1, sub_col2, sub_col3 = st.columns(3)

    with sub_col1:
        with st.container(height=CONTAINER_HEIGHT, border=True):
            st.header(tr("section.about_you"))

            @st.dialog(tr("dialog.xerostomia.title"))
            def show_xerostomia_popup():
                st.write(tr("dialog.xerostomia.body"))
                image_path = IMAGE_DIR / "1.jpg"
                if image_path.exists():
                    st.image(str(image_path), use_container_width=True)

            col1, col2 = st.columns([8, 1])
            with col1:
                xer = st.selectbox(
                    tr("question.xerostomia"),
                    list(xerop.keys()),
                    format_func=lambda value: option_label(
                        st.session_state.language_code, value
                    ),
                    key="xer",
                )
            with col2:
                st.markdown("<br>", unsafe_allow_html=True)
                if st.button("ℹ️", key="xer_info"):
                    show_xerostomia_popup()

            @st.dialog(tr("dialog.medication.title"))
            def show_med_popup():
                st.write(tr("dialog.medication.body"))

            col1, col2 = st.columns([8, 1])
            with col1:
                med = st.selectbox(
                    tr("question.medication"),
                    list(medop.keys()),
                    format_func=lambda value: option_label(
                        st.session_state.language_code, value
                    ),
                    key="med",
                )
            with col2:
                st.markdown("<br>", unsafe_allow_html=True)
                if st.button("ℹ️", key="med_info"):
                    show_med_popup()

            @st.dialog(tr("dialog.diabetes.title"))
            def show_diabetes_popup():
                st.write(tr("dialog.diabetes.body"))

            col1, col2 = st.columns([8, 1])
            with col1:
                diab = st.selectbox(
                    tr("question.diabetes"),
                    list(diabop.keys()),
                    format_func=lambda value: option_label(
                        st.session_state.language_code, value
                    ),
                    key="diab",
                )
            with col2:
                st.markdown("<br>", unsafe_allow_html=True)
                if st.button("ℹ️", key="diab_info"):
                    show_diabetes_popup()

    with sub_col2:
        with st.container(height=CONTAINER_HEIGHT, border=True):
            st.header(tr("section.oral_health"))

            @st.dialog(tr("dialog.halitosis.title"))
            def show_halitosis_popup():
                st.write(tr("dialog.halitosis.body"))

            col1, col2 = st.columns([8, 1])
            with col1:
                hal = st.selectbox(
                    tr("question.halitosis"),
                    list(halop.keys()),
                    key="hal",
                )
            with col2:
                st.markdown("<br>", unsafe_allow_html=True)
                if st.button("ℹ️", key="hal_info"):
                    show_halitosis_popup()

            @st.dialog(tr("dialog.candidiasis.title"))
            def show_candidiasis_popup():
                st.write(tr("dialog.candidiasis.body"))
                image_path = IMAGE_DIR / "2.jpg"
                if image_path.exists():
                    st.image(str(image_path), use_container_width=True)

            col1, col2 = st.columns([8, 1])
            with col1:
                cand = st.selectbox(
                    tr("question.candidiasis"),
                    list(candop.keys()),
                    format_func=lambda value: option_label(
                        st.session_state.language_code, value
                    ),
                    key="cand",
                )
            with col2:
                st.markdown("<br>", unsafe_allow_html=True)
                if st.button("ℹ️", key="cand_info"):
                    show_candidiasis_popup()

            @st.dialog(tr("dialog.tongue.title"))
            def show_tongue_popup():
                st.write(tr("dialog.tongue.body"))
                image_path = IMAGE_DIR / "3.jpg"
                if image_path.exists():
                    st.image(str(image_path), use_container_width=True)

            col1, col2 = st.columns([8, 1])
            with col1:
                tongue = st.selectbox(
                    tr("question.tongue"),
                    list(lendop.keys()),
                    format_func=lambda value: option_label(
                        st.session_state.language_code, value
                    ),
                    key="tongue",
                )
            with col2:
                st.markdown("<br>", unsafe_allow_html=True)
                if st.button("ℹ️", key="tongue_info"):
                    show_tongue_popup()

            @st.dialog(tr("dialog.periodontal.title"))
            def show_periodontal_popup():
                st.write(tr("dialog.periodontal.body"))
                image_path = IMAGE_DIR / "4.jpg"
                if image_path.exists():
                    st.image(str(image_path), use_container_width=True)

            col1, col2 = st.columns([8, 1])
            with col1:
                per = st.selectbox(
                    tr("question.periodontal"),
                    list(perdop.keys()),
                    format_func=lambda value: option_label(
                        st.session_state.language_code, value
                    ),
                    key="per",
                )
            with col2:
                st.markdown("<br>", unsafe_allow_html=True)
                if st.button("ℹ️", key="per_info"):
                    show_periodontal_popup()

    with sub_col3:
        with st.container(height=CONTAINER_HEIGHT, border=True):
            st.header(tr("section.kidney_health"))

            @st.dialog(tr("dialog.ckd.title"))
            def show_ckd_popup():
                st.write(tr("dialog.ckd.body"))

            col1, col2 = st.columns([8, 1])
            with col1:
                ckd = st.selectbox(
                    tr("question.ckd"),
                    list(ckdop.keys()),
                    format_func=lambda value: option_label(
                        st.session_state.language_code, value
                    ),
                    key="ckd",
                )
            with col2:
                st.markdown("<br>", unsafe_allow_html=True)
                if st.button("ℹ️", key="ckd_info"):
                    show_ckd_popup()


def calculate_risk():
    total = (
        xerop[xer] + medop[med] + diabop[diab] + halop[hal]
        + candop[cand] + lendop[tongue] + perdop[per] + ckdop[ckd]
    )
    st.session_state.total_points = total
    st.session_state.calculated = True


with col_final_right:
    with st.container(height=CONTAINER_HEIGHT + 340, border=True):
        st.header(tr("section.results"))
        st.write(tr("results.intro"))

        if st.button(tr("results.calculate"), use_container_width=True):
            calculate_risk()

        st.divider()

        if st.session_state.calculated:
            points = st.session_state.total_points
            risk_id = get_risk_id(points)
            result_text = (
                f"## { {'low': '🟢', 'moderate': '🟡', 'high': '🔴'}[risk_id] } "
                f"{tr(f'risk.{risk_id}')}\n"
                f"**{tr('results.score')}:** {points}"
            )

            if risk_id == "low":
                st.success(result_text)
            elif risk_id == "moderate":
                st.warning(result_text)
            else:
                st.error(result_text)

            st.write("---")
            st.write(f"**{tr('results.interpretation')}**")
            st.markdown(tr(f"risk.{risk_id}.interpretation"))
            st.write(f"**{tr('results.actions')}**")
            st.markdown(tr(f"risk.{risk_id}.actions"))

            with st.expander(tr("results.disclaimer.title")):
                st.caption(tr("results.disclaimer.body"))

            if points >= 4:
                st.write("---")
                generate_report = st.toggle(tr("report.toggle"))

                if generate_report:
                    st.subheader(tr("report.patient_information"))
                    name = st.text_input(tr("report.full_name"))
                    age = st.number_input(
                        tr("report.age"), min_value=1, max_value=120, step=1
                    )
                    sex = st.selectbox(
                        tr("report.sex"),
                        ["", "Male", "Female", "Other"],
                        format_func=lambda value: (
                            "" if value == "" else option_label(
                                st.session_state.language_code, value
                            )
                        ),
                    )
                    data_consent = st.checkbox(tr("report.consent"))
                    st.write("---")

                    ready_to_generate = (
                        bool(name.strip()) and sex != "" and age > 0 and data_consent
                    )

                    if ready_to_generate:
                        patient_data = [
                            {"id": "xerostomia", "response": xer, "score": xerop[xer]},
                            {"id": "medication", "response": med, "score": medop[med]},
                            {"id": "diabetes", "response": diab, "score": diabop[diab]},
                            {"id": "halitosis", "response": hal, "score": halop[hal]},
                            {"id": "candidiasis", "response": cand, "score": candop[cand]},
                            {"id": "tongue", "response": tongue, "score": lendop[tongue]},
                            {"id": "periodontal", "response": per, "score": perdop[per]},
                            {"id": "ckd", "response": ckd, "score": ckdop[ckd]},
                        ]
                        pdf_file = build_patient_report_pdf(
                            name,
                            patient_data,
                            points,
                            st.session_state.language_code,
                        )
                        st.download_button(
                            label=tr("report.download"),
                            data=pdf_file,
                            file_name=tr("report.filename"),
                            mime="application/pdf",
                            use_container_width=True,
                        )
                    else:
                        st.button(
                            tr("report.download"),
                            disabled=True,
                            use_container_width=True,
                        )
                else:
                    st.info(tr("report.activate"))
        else:
            st.markdown(
                f'<p style="color: gray;"><i>{tr("results.waiting")}</i></p>',
                unsafe_allow_html=True,
            )

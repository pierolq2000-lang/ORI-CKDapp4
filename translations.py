"""
Translation catalogue for the Oral Health Index & CKD Risk Calculator.

To add a language:
1. Add it to LANGUAGES, for example: "Español": "es".
2. Add a TRANSLATIONS["es"] dictionary containing the same keys as English.
3. The application will automatically show it in the language selector.
"""

LANGUAGES = {
    "English": "en",
    "Español": "es",
    "Deutsch": "de",
    "Português": "pt",
    "Français": "fr",
}
TRANSLATIONS = {
    "en": {
        # General interface
        "app.title": "Oral Health Index & CKD Risk Calculator",
        "app.intro": (
            "This calculator estimates how a patient’s oral health status may be associated "
            "with the development or progression of chronic kidney disease (CKD). We invite "
            "you to complete this brief questionnaire and calculate your risk level in the "
            "final section."
        ),
        "settings.title": "Settings Preferences",
        "settings.language": "Language",
        "settings.choose_language": "Choose language:",
        "settings.theme": "Theme",
        "settings.choose_theme": "Choose theme:",
        "settings.font_size": "Font Size",
        "settings.choose_font_size": "Choose font size:",
        "theme.clear": "Clear",
        "theme.dark": "Dark",
        "font.small": "Small",
        "font.medium": "Medium",
        "font.large": "Large",

        # Instructions and evidence
        "instructions.title": "Instructions",
        "instructions.body": (
            "**How to use this tool:**\n\n"
            "1. Select the appropriate option for your case in each of the three sections below.  \n"
            "2. Use the information icons next to the questions for explanations and visual guidance.  \n"
            "3. After completing all questions, press **Calculate Risk Score** in the right-side section.  \n"
            "4. The platform will display your score, risk category, interpretation, and recommended actions.  \n"
            "5. For moderate or high risk, you may optionally generate a detailed report after entering "
            "the required personal information."
        ),
        "evidence.title": "Evidence and Model Disclaimer",
        "evidence.body": (
            "This calculator is informed by current evidence describing the association between oral "
            "disease and chronic kidney disease (CKD), including systematic reviews and meta-analyses "
            "that consistently demonstrate a relationship between periodontitis and CKD.\n\n"
            "However, the numerical weighting and overall risk score used here have **not** been derived "
            "from, nor validated against, any single published prediction model or prospective cohort study.\n\n"
            "Therefore, the scoring algorithm should be understood as an **evidence-informed clinical "
            "framework**, rather than a validated risk-prediction model."
        ),

        # Section headings
        "section.about_you": "About You",
        "section.oral_health": "Your Oral Health",
        "section.kidney_health": "Your Kidney Health",
        "section.results": "Calculator Results",

        # Questions
        "question.xerostomia": "Does your mouth often feel dry or sticky?",
        "question.medication": "Do you take any medication that causes dry mouth?",
        "question.diabetes": "Have you been diagnosed with diabetes?",
        "question.halitosis": (
            "Do you or people close to you notice bad breath? How bad is it from "
            "0 (none) to 5 (very severe)?"
        ),
        "question.candidiasis": (
            "Have you noticed white patches, soreness, or a cotton-like feeling in your mouth?"
        ),
        "question.tongue": "Does your tongue have deep lines, cracks, or grooves?",
        "question.periodontal": (
            "Do your gums bleed or feel swollen, or do any teeth feel loose?"
        ),
        "question.ckd": "What is your chronic kidney disease stage?",

        # Selectbox options
        "option.never": "Never",
        "option.sometimes": "Sometimes",
        "option.always": "Always",
        "option.no": "No",
        "option.yes": "Yes",
        "option.none": "None",
        "option.moderate": "Moderate",
        "option.severe": "Severe",
        "option.dialysis": "Dialysis",
        "option.male": "Male",
        "option.female": "Female",
        "option.other": "Other",

        # Informational dialogs
        "dialog.xerostomia.title": "What is dry mouth?",
        "dialog.xerostomia.body": (
            "Dry mouth (xerostomia) is the feeling that your mouth is unusually dry, sticky, "
            "or lacks saliva.\n\nIt may make speaking, eating, swallowing, or wearing dentures "
            "more difficult.\n\nCompare your symptoms with the reference image below."
        ),
        "dialog.medication.title": "Why are we asking this?",
        "dialog.medication.body": (
            "Some medications may reduce saliva production and contribute to dry mouth.\n\n"
            "Common examples include some blood pressure medications, diuretics, antidepressants, "
            "and antihistamines."
        ),
        "dialog.diabetes.title": "Why is diabetes important?",
        "dialog.diabetes.body": (
            "Diabetes can affect oral health by increasing the risk of gum disease, oral infections, "
            "delayed healing, and dry mouth.\n\nGood oral health is especially important for people "
            "living with diabetes."
        ),
        "dialog.halitosis.title": "What is bad breath?",
        "dialog.halitosis.body": (
            "Bad breath, also called halitosis, means an unpleasant smell coming from the mouth.\n\n"
            "It may be related to dry mouth, tongue coating, gum disease, tooth decay, or oral infection."
        ),
        "dialog.candidiasis.title": "What is oral candidiasis?",
        "dialog.candidiasis.body": (
            "Oral candidiasis is a fungal infection that can appear inside the mouth.\n\n"
            "It may cause white patches, redness, soreness, burning, or a cotton-like feeling.\n\n"
            "Compare your symptoms with the reference image below."
        ),
        "dialog.tongue.title": "What is tongue fissuring?",
        "dialog.tongue.body": (
            "Tongue fissuring means having deep lines, cracks, or grooves on the surface of the tongue.\n\n"
            "Food or bacteria may remain in these grooves and cause discomfort, irritation, or bad breath.\n\n"
            "Compare your symptoms with the reference image below."
        ),
        "dialog.periodontal.title": "What is periodontal disease?",
        "dialog.periodontal.body": (
            "Periodontal disease, also called gum disease, affects the gums and tissues supporting "
            "the teeth.\n\nSigns may include bleeding or swollen gums, bad breath, loose teeth, "
            "or pain when chewing.\n\nCompare your symptoms with the reference image below."
        ),
        "dialog.ckd.title": "What do CKD stages mean?",
        "dialog.ckd.body": (
            "CKD means chronic kidney disease. It is commonly classified into stages from 1 to 5 "
            "according to how well the kidneys filter blood.\n\n"
            "**Stage 1:** Kidney damage is present, but kidney function is normal or nearly normal.\n\n"
            "**Stage 2:** Mild decrease in kidney function.\n\n"
            "**Stage 3:** Moderate decrease in kidney function. Medical follow-up becomes especially important.\n\n"
            "**Stage 4:** Severe decrease in kidney function. Preparation for advanced treatment may be needed.\n\n"
            "**Stage 5:** Kidney failure. Dialysis or kidney transplantation may be needed.\n\n"
            "**Dialysis:** Treatment that removes waste and excess fluid from the blood when the kidneys "
            "can no longer do so adequately."
        ),

        # Results
        "results.intro": "Complete all fields and press the button below to see the risk assessment.",
        "results.calculate": "Calculate Risk Score",
        "results.waiting": "Waiting for calculation...",
        "results.score": "Score",
        "results.interpretation": "Interpretation",
        "results.actions": "Recommended Actions",
        "risk.low": "Low Risk",
        "risk.moderate": "Moderate Risk",
        "risk.high": "High Risk",
        "risk.low.interpretation": (
            "Your responses suggest a **low level of oral health-related risk**. "
            "No major oral findings associated with CKD were identified based on your answers."
        ),
        "risk.moderate.interpretation": (
            "Your responses indicate **oral health findings that may require further attention**. "
            "A professional dental evaluation is recommended to prevent progression and support overall health."
        ),
        "risk.high.interpretation": (
            "Your responses suggest **multiple oral health findings or advanced systemic factors** "
            "that may be associated with an increased oral health burden. Although this is "
            "**not a diagnosis**, prompt professional evaluation is recommended."
        ),
        "risk.low.actions": (
            "- Maintain good daily oral hygiene.\n"
            "- Attend routine dental check-ups.\n"
            "- Repeat the assessment if new symptoms develop."
        ),
        "risk.moderate.actions": (
            "- Schedule a dental appointment.\n"
            "- Monitor symptoms such as dry mouth, bleeding gums, or persistent bad breath.\n"
            "- Share your report with your healthcare providers if appropriate."
        ),
        "risk.high.actions": (
            "- Arrange a dental evaluation as soon as reasonably possible.\n"
            "- Inform your dentist about your CKD stage and current medications.\n"
            "- Discuss persistent oral symptoms with your nephrologist."
        ),
        "results.disclaimer.title": "⚠️ Important Disclaimer",
        "results.disclaimer.body": (
            "The assigned numerical score is based on **evidence-informed clinical judgement and "
            "literature synthesis**. It should **not** be interpreted as a validated estimate of CKD "
            "risk or disease progression.\n\nIndividual score components are supported by published "
            "evidence, but the combined scoring system has **not** yet undergone formal derivation, "
            "calibration, or external validation.\n\nThis calculator is intended solely for educational "
            "and risk-awareness purposes and does **not** replace professional advice from a dentist, "
            "nephrologist, physician, or other qualified healthcare provider."
        ),

        # Report form
        "report.toggle": "Generate detailed PDF report",
        "report.patient_information": "Patient Information",
        "report.full_name": "Full Name",
        "report.age": "Age",
        "report.sex": "Sex",
        "report.consent": "I accept the processing of my personal data",
        "report.download": "📄 Get My Report",
        "report.activate": "Activate the switch above to generate a personalized report.",
        "report.filename": "oral_ckd_risk_report.pdf",

        # PDF
        "pdf.title": "Oral Health & CKD Risk Calculator Report",
        "pdf.patient_name": "Patient Name",
        "pdf.generated": "Report generated on",
        "pdf.risk_category": "Risk Category",
        "pdf.risk_summary": "Risk Assessment Summary",
        "pdf.patient_responses": "Patient Responses",
        "pdf.indicator": "Indicator",
        "pdf.response": "Patient Response",
        "pdf.indicator_meaning": "What Each Indicator Means",
        "pdf.suggestions": "Personalized Suggestions",
        "pdf.general_advice": "General Oral Health Advice",
        "pdf.reminder": "Important Reminder",
        "pdf.no_specific": (
            "No major risk-related answers were selected. Please continue maintaining good daily oral hygiene."
        ),
        "pdf.disclaimer": (
            "This report is for educational and self-awareness purposes only. It does not provide a "
            "medical diagnosis and should not replace professional advice from a dentist, physician, "
            "nephrologist, or other healthcare provider."
        ),
        "pdf.low_message": (
            "Your current score suggests a low level of oral health-related risk. However, maintaining "
            "good daily oral hygiene and regular dental check-ups is still important."
        ),
        "pdf.moderate_message": (
            "Your current score suggests a moderate level of oral health-related risk. Some oral health "
            "signs may need more attention. Improve daily oral care and consider visiting a dentist "
            "for further evaluation."
        ),
        "pdf.high_message": (
            "Your current score suggests a high level of oral health-related risk. Several oral health "
            "or medical factors may require professional attention. Consult a dentist and discuss your "
            "oral health with your healthcare team."
        ),

        # Indicator labels and explanations
        "indicator.xerostomia": "Dry mouth / Xerostomia",
        "indicator.medication": "Medications causing dry mouth",
        "indicator.diabetes": "Diabetes",
        "indicator.halitosis": "Bad breath / Halitosis",
        "indicator.candidiasis": "Oral candidiasis",
        "indicator.tongue": "Tongue fissuring / Fissured tongue",
        "indicator.periodontal": "Periodontal disease",
        "indicator.ckd": "CKD stage",
        "explanation.xerostomia": (
            "Dry mouth means your mouth often feels dry, sticky, or uncomfortable. "
            "It may make it harder to speak, chew, swallow, or taste food."
        ),
        "explanation.medication": (
            "Some medicines, such as diuretics or antihypertensive drugs, may reduce saliva "
            "and make your mouth feel dry."
        ),
        "explanation.diabetes": (
            "Diabetes may increase the risk of gum disease, oral infection, delayed healing, and dry mouth."
        ),
        "explanation.halitosis": (
            "Bad breath is an unpleasant smell from the mouth. It may be related to dry mouth, tongue "
            "coating, gum disease, tooth decay, or oral infection."
        ),
        "explanation.candidiasis": (
            "Oral candidiasis is a fungal infection in the mouth. It may appear as white patches, "
            "redness, soreness, burning, or a cotton-like feeling."
        ),
        "explanation.tongue": (
            "A fissured tongue has deep lines, cracks, or grooves. Food or bacteria may remain in "
            "them and cause discomfort or bad breath."
        ),
        "explanation.periodontal": (
            "Periodontal disease affects the gums and tissues supporting the teeth. Signs may include "
            "bleeding or swollen gums, bad breath, loose teeth, or pain when chewing."
        ),
        "explanation.ckd": (
            "CKD stage describes the severity of chronic kidney disease. A higher stage generally "
            "means more severe kidney disease and may be associated with more oral-health concerns."
        ),

        # Indicator-specific recommendations
        "recommendation.xerostomia.1": "Sip water frequently if this is allowed by your kidney doctor.",
        "recommendation.xerostomia.2": "Use sugar-free chewing gum or lozenges to help stimulate saliva.",
        "recommendation.xerostomia.3": "Ask your dentist or doctor about saliva substitutes or dry-mouth products.",
        "recommendation.medication.1": "Do not stop any medication by yourself.",
        "recommendation.medication.2": "Ask your doctor whether your medication may be contributing to dry mouth.",
        "recommendation.medication.3": "Tell your dentist about all medications you currently take.",
        "recommendation.diabetes.1": "Maintain good blood sugar control as advised by your healthcare provider.",
        "recommendation.diabetes.2": "Check your gums regularly for bleeding, swelling, or signs of infection.",
        "recommendation.diabetes.3": "Schedule regular dental visits because diabetes may increase the risk of gum disease.",
        "recommendation.halitosis.1": "Brush your teeth and tongue gently every day.",
        "recommendation.halitosis.2": "Clean between your teeth with floss or interdental brushes.",
        "recommendation.halitosis.3": "If bad breath continues, visit a dentist to check for gum disease, tooth decay, or infection.",
        "recommendation.candidiasis.1": "Visit a dentist or doctor if you notice white patches, soreness, burning, or a cotton-like feeling.",
        "recommendation.candidiasis.2": "Avoid self-medication without professional advice.",
        "recommendation.candidiasis.3": "Keep dentures, retainers, or oral appliances clean if you use them.",
        "recommendation.tongue.1": "Clean your tongue gently to remove trapped food or debris.",
        "recommendation.tongue.2": "Avoid spicy, acidic, or irritating foods if your tongue feels sore.",
        "recommendation.tongue.3": "Ask a dentist to examine your tongue if pain, swelling, or persistent discomfort occurs.",
        "recommendation.periodontal.1": "Visit a dentist or periodontist for a gum evaluation.",
        "recommendation.periodontal.2": "Professional cleaning may be needed to remove plaque and calculus.",
        "recommendation.periodontal.3": "Seek dental care if your gums bleed, swell, hurt, or your teeth feel loose.",
        "recommendation.ckd.1": "Keep both your kidney doctor and dentist informed about your health condition.",
        "recommendation.ckd.2": "Ask your healthcare team before major dental procedures if you have advanced CKD or receive dialysis.",
        "recommendation.ckd.3": "Maintain regular oral care because oral infection may affect general health.",

        # General recommendations
        "general.1": "Brush your teeth gently at least twice a day using fluoride toothpaste.",
        "general.2": "Clean between your teeth daily with dental floss or interdental brushes.",
        "general.3": "Drink enough water if permitted by your kidney doctor, especially if your mouth feels dry.",
        "general.4": "Avoid smoking and limit alcohol, as they may worsen dry mouth, gum problems, and bad breath.",
        "general.5": "Visit a dentist regularly for oral examination and professional cleaning.",
        "general.6": "Tell your dentist if you have chronic kidney disease, diabetes, or take long-term medication.",
        "general.7": "Do not ignore bleeding gums, loose teeth, white patches, mouth pain, or persistent bad breath.",
        "general.8": "If you receive dialysis or have advanced CKD, discuss dental-treatment timing with your healthcare team.",
    }
}


# Temporary fallbacks. These entries make every language visible now.
# Their text will remain in English until each dictionary is translated.
for _language_code in ("es", "de", "pt", "fr"):
    if _language_code not in TRANSLATIONS:
        TRANSLATIONS[_language_code] = dict(TRANSLATIONS["en"])



SPANISH_TRANSLATIONS = {
    "app.title": "Índice de Salud Oral y Calculadora de Riesgo de ERC",
    "app.intro": (
        "Esta calculadora estima cómo el estado de salud oral de un paciente puede asociarse "
        "con el desarrollo o la progresión de la enfermedad renal crónica (ERC). Le invitamos "
        "a completar este breve cuestionario y calcular su nivel de riesgo en la sección final."
    ),
    "settings.title": "Preferencias",
    "settings.language": "Idioma",
    "settings.choose_language": "Seleccione un idioma:",
    "settings.theme": "Tema",
    "settings.choose_theme": "Seleccione un tema:",
    "settings.font_size": "Tamaño de fuente",
    "settings.choose_font_size": "Seleccione el tamaño de fuente:",
    "theme.clear": "Claro",
    "theme.dark": "Oscuro",
    "font.small": "Pequeño",
    "font.medium": "Mediano",
    "font.large": "Grande",

    "instructions.title": "Instrucciones",
    "instructions.body": (
        "**Cómo utilizar esta herramienta:**\n\n"
        "1. Seleccione la opción adecuada para su caso en cada una de las tres secciones.  \n"
        "2. Utilice los iconos de información junto a las preguntas para consultar explicaciones y orientación visual.  \n"
        "3. Después de completar todas las preguntas, pulse **Calcular puntuación de riesgo**.  \n"
        "4. La plataforma mostrará su puntuación, categoría de riesgo, interpretación y acciones recomendadas.  \n"
        "5. Para riesgo moderado o alto, podrá generar opcionalmente un informe detallado."
    ),
    "evidence.title": "Evidencia y limitaciones del modelo",
    "evidence.body": (
        "Esta calculadora se basa en evidencia actual sobre la asociación entre las enfermedades orales "
        "y la enfermedad renal crónica (ERC), incluidas revisiones sistemáticas y metaanálisis.\n\n"
        "Sin embargo, la ponderación numérica y la puntuación global utilizadas aquí **no** proceden de "
        "un único modelo predictivo publicado ni han sido validadas en una cohorte prospectiva.\n\n"
        "Por lo tanto, el algoritmo debe entenderse como un **marco clínico basado en evidencia**, "
        "y no como un modelo validado de predicción de riesgo."
    ),

    "section.about_you": "Sobre usted",
    "section.oral_health": "Su salud oral",
    "section.kidney_health": "Su salud renal",
    "section.results": "Resultados de la calculadora",

    "question.xerostomia": "¿Siente con frecuencia la boca seca o pegajosa?",
    "question.medication": "¿Toma algún medicamento que le cause sequedad bucal?",
    "question.diabetes": "¿Le han diagnosticado diabetes?",
    "question.halitosis": "¿Usted o personas cercanas notan mal aliento? ¿Qué intensidad tiene de 0 a 5?",
    "question.candidiasis": "¿Ha notado placas blancas, dolor o sensación algodonosa en la boca?",
    "question.tongue": "¿Su lengua presenta líneas profundas, grietas o surcos?",
    "question.periodontal": "¿Le sangran o se le inflaman las encías, o siente algún diente flojo?",
    "question.ckd": "¿Cuál es el estadio de su enfermedad renal crónica?",

    "option.never": "Nunca",
    "option.sometimes": "A veces",
    "option.always": "Siempre",
    "option.no": "No",
    "option.yes": "Sí",
    "option.none": "Ninguna",
    "option.moderate": "Moderada",
    "option.severe": "Severa",
    "option.dialysis": "Diálisis",
    "option.male": "Masculino",
    "option.female": "Femenino",
    "option.other": "Otro",

    "dialog.xerostomia.title": "¿Qué es la boca seca?",
    "dialog.xerostomia.body": (
        "La boca seca o xerostomía es la sensación de que la boca está anormalmente seca, "
        "pegajosa o con poca saliva.\n\nPuede dificultar hablar, comer, tragar o usar prótesis dentales.\n\n"
        "Compare sus síntomas con la imagen de referencia."
    ),
    "dialog.medication.title": "¿Por qué preguntamos esto?",
    "dialog.medication.body": (
        "Algunos medicamentos pueden reducir la producción de saliva y contribuir a la sequedad bucal.\n\n"
        "Entre los ejemplos se incluyen ciertos antihipertensivos, diuréticos, antidepresivos y antihistamínicos."
    ),
    "dialog.diabetes.title": "¿Por qué es importante la diabetes?",
    "dialog.diabetes.body": (
        "La diabetes puede aumentar el riesgo de enfermedad periodontal, infecciones orales, "
        "cicatrización tardía y sequedad bucal.\n\nMantener una buena salud oral es especialmente importante."
    ),
    "dialog.halitosis.title": "¿Qué es el mal aliento?",
    "dialog.halitosis.body": (
        "El mal aliento, también llamado halitosis, es un olor desagradable procedente de la boca.\n\n"
        "Puede relacionarse con sequedad bucal, recubrimiento lingual, enfermedad periodontal, caries o infección."
    ),
    "dialog.candidiasis.title": "¿Qué es la candidiasis oral?",
    "dialog.candidiasis.body": (
        "La candidiasis oral es una infección por hongos que puede aparecer dentro de la boca.\n\n"
        "Puede causar placas blancas, enrojecimiento, dolor, ardor o sensación algodonosa."
    ),
    "dialog.tongue.title": "¿Qué es la lengua fisurada?",
    "dialog.tongue.body": (
        "La lengua fisurada presenta líneas profundas, grietas o surcos en su superficie.\n\n"
        "Los alimentos o las bacterias pueden quedar retenidos y causar molestias o mal aliento."
    ),
    "dialog.periodontal.title": "¿Qué es la enfermedad periodontal?",
    "dialog.periodontal.body": (
        "La enfermedad periodontal afecta las encías y los tejidos que sostienen los dientes.\n\n"
        "Puede causar sangrado, inflamación, mal aliento, movilidad dental o dolor al masticar."
    ),
    "dialog.ckd.title": "¿Qué significan los estadios de ERC?",
    "dialog.ckd.body": (
        "La ERC es la enfermedad renal crónica. Se clasifica habitualmente del estadio 1 al 5 según la función renal.\n\n"
        "**Estadio 1:** Daño renal con función normal o casi normal.\n\n"
        "**Estadio 2:** Disminución leve de la función renal.\n\n"
        "**Estadio 3:** Disminución moderada.\n\n"
        "**Estadio 4:** Disminución grave.\n\n"
        "**Estadio 5:** Insuficiencia renal; puede requerirse diálisis o trasplante.\n\n"
        "**Diálisis:** Tratamiento que elimina residuos y exceso de líquido de la sangre."
    ),

    "results.intro": "Complete todos los campos y pulse el botón para ver la evaluación de riesgo.",
    "results.calculate": "Calcular puntuación de riesgo",
    "results.waiting": "Esperando el cálculo...",
    "results.score": "Puntuación",
    "results.interpretation": "Interpretación",
    "results.actions": "Acciones recomendadas",
    "risk.low": "Riesgo bajo",
    "risk.moderate": "Riesgo moderado",
    "risk.high": "Riesgo alto",
    "risk.low.interpretation": (
        "Sus respuestas sugieren un **nivel bajo de riesgo relacionado con la salud oral**. "
        "No se identificaron hallazgos orales importantes asociados con ERC."
    ),
    "risk.moderate.interpretation": (
        "Sus respuestas indican **hallazgos de salud oral que pueden requerir mayor atención**. "
        "Se recomienda una evaluación dental profesional."
    ),
    "risk.high.interpretation": (
        "Sus respuestas sugieren **múltiples hallazgos orales o factores sistémicos avanzados**. "
        "Aunque esto **no es un diagnóstico**, se recomienda una evaluación profesional pronta."
    ),
    "risk.low.actions": (
        "- Mantenga una buena higiene oral diaria.\n"
        "- Acuda a controles dentales rutinarios.\n"
        "- Repita la evaluación si aparecen nuevos síntomas."
    ),
    "risk.moderate.actions": (
        "- Programe una cita dental.\n"
        "- Vigile síntomas como boca seca, sangrado de encías o mal aliento persistente.\n"
        "- Comparta el informe con sus profesionales sanitarios cuando corresponda."
    ),
    "risk.high.actions": (
        "- Organice una evaluación dental lo antes posible.\n"
        "- Informe a su dentista sobre su estadio de ERC y medicamentos actuales.\n"
        "- Comente los síntomas orales persistentes con su nefrólogo."
    ),
    "results.disclaimer.title": "⚠️ Aviso importante",
    "results.disclaimer.body": (
        "La puntuación numérica se basa en **criterio clínico informado por evidencia y síntesis de literatura**. "
        "No debe interpretarse como una estimación validada del riesgo o progresión de ERC.\n\n"
        "El sistema combinado aún no ha sido sometido a derivación, calibración o validación externa formal.\n\n"
        "Esta calculadora tiene fines educativos y de concienciación y no sustituye el consejo profesional."
    ),

    "report.toggle": "Generar informe PDF detallado",
    "report.patient_information": "Información del paciente",
    "report.full_name": "Nombre completo",
    "report.age": "Edad",
    "report.sex": "Sexo",
    "report.consent": "Acepto el tratamiento de mis datos personales",
    "report.download": "📄 Obtener mi informe",
    "report.activate": "Active el interruptor anterior para generar un informe personalizado.",
    "report.filename": "informe_riesgo_oral_erc.pdf",

    "pdf.title": "Informe de salud oral y riesgo de ERC",
    "pdf.patient_name": "Nombre del paciente",
    "pdf.generated": "Informe generado el",
    "pdf.risk_category": "Categoría de riesgo",
    "pdf.risk_summary": "Resumen de la evaluación de riesgo",
    "pdf.patient_responses": "Respuestas del paciente",
    "pdf.indicator": "Indicador",
    "pdf.response": "Respuesta del paciente",
    "pdf.indicator_meaning": "Significado de cada indicador",
    "pdf.suggestions": "Recomendaciones personalizadas",
    "pdf.general_advice": "Consejos generales de salud oral",
    "pdf.reminder": "Recordatorio importante",
    "pdf.no_specific": "No se seleccionaron respuestas asociadas con un riesgo importante.",
    "pdf.disclaimer": (
        "Este informe tiene únicamente fines educativos y de concienciación. No constituye un diagnóstico "
        "médico ni sustituye el consejo profesional."
    ),
    "pdf.low_message": "La puntuación actual sugiere un nivel bajo de riesgo relacionado con la salud oral.",
    "pdf.moderate_message": "La puntuación actual sugiere un nivel moderado de riesgo relacionado con la salud oral.",
    "pdf.high_message": "La puntuación actual sugiere un nivel alto de riesgo relacionado con la salud oral.",

    "indicator.xerostomia": "Boca seca / Xerostomía",
    "indicator.medication": "Medicamentos que causan sequedad bucal",
    "indicator.diabetes": "Diabetes",
    "indicator.halitosis": "Mal aliento / Halitosis",
    "indicator.candidiasis": "Candidiasis oral",
    "indicator.tongue": "Lengua fisurada",
    "indicator.periodontal": "Enfermedad periodontal",
    "indicator.ckd": "Estadio de ERC",

    "explanation.xerostomia": "La boca seca puede dificultar hablar, masticar, tragar o saborear.",
    "explanation.medication": "Algunos medicamentos pueden reducir la saliva y causar sequedad bucal.",
    "explanation.diabetes": "La diabetes puede aumentar el riesgo de enfermedad periodontal e infección oral.",
    "explanation.halitosis": "El mal aliento puede relacionarse con sequedad, caries, enfermedad periodontal o infección.",
    "explanation.candidiasis": "La candidiasis oral es una infección por hongos que puede causar placas blancas o ardor.",
    "explanation.tongue": "La lengua fisurada presenta grietas donde pueden acumularse alimentos o bacterias.",
    "explanation.periodontal": "La enfermedad periodontal afecta las encías y tejidos de soporte dental.",
    "explanation.ckd": "El estadio de ERC describe la gravedad de la enfermedad renal crónica.",
}

TRANSLATIONS["es"].update(SPANISH_TRANSLATIONS)

GERMAN_TRANSLATIONS = {'app.title': 'Index der Mundgesundheit & CKD-Risikorechner', 'app.intro': 'Dieser Rechner schätzt, wie der Mundgesundheitszustand einer Person mit der Entstehung oder dem Fortschreiten einer chronischen Nierenerkrankung (CKD) zusammenhängen könnte. Bitte füllen Sie den kurzen Fragebogen aus und berechnen Sie im letzten Abschnitt Ihre Risikostufe.', 'settings.title': 'Einstellungen', 'settings.language': 'Sprache', 'settings.choose_language': 'Sprache auswählen:', 'settings.theme': 'Design', 'settings.choose_theme': 'Design auswählen:', 'settings.font_size': 'Schriftgröße', 'settings.choose_font_size': 'Schriftgröße auswählen:', 'theme.clear': 'Hell', 'theme.dark': 'Dunkel', 'font.small': 'Klein', 'font.medium': 'Mittel', 'font.large': 'Groß', 'instructions.title': 'Anleitung', 'instructions.body': '**So verwenden Sie dieses Werkzeug:**\n\n1. Wählen Sie in jedem der drei Abschnitte die passende Antwort aus.  \n2. Nutzen Sie die Informationssymbole neben den Fragen für Erklärungen und Bildhinweise.  \n3. Klicken Sie nach Beantwortung aller Fragen auf **Risikopunktzahl berechnen**.  \n4. Die Anwendung zeigt Punktzahl, Risikokategorie, Interpretation und empfohlene Maßnahmen.  \n5. Bei mittlerem oder hohem Risiko können Sie optional einen ausführlichen Bericht erstellen.', 'evidence.title': 'Evidenz und Einschränkungen des Modells', 'evidence.body': 'Dieser Rechner berücksichtigt aktuelle Evidenz zum Zusammenhang zwischen oralen Erkrankungen und chronischer Nierenerkrankung (CKD), einschließlich systematischer Übersichtsarbeiten und Metaanalysen.\n\nDie numerische Gewichtung und die Gesamtpunktzahl wurden jedoch **nicht** aus einem einzelnen veröffentlichten Vorhersagemodell oder einer prospektiven Kohortenstudie abgeleitet oder daran validiert.\n\nDer Algorithmus ist daher als **evidenzinformierter klinischer Rahmen** und nicht als validiertes Risikovorhersagemodell zu verstehen.', 'section.about_you': 'Über Sie', 'section.oral_health': 'Ihre Mundgesundheit', 'section.kidney_health': 'Ihre Nierengesundheit', 'section.results': 'Ergebnisse', 'question.xerostomia': 'Fühlt sich Ihr Mund häufig trocken oder klebrig an?', 'question.medication': 'Nehmen Sie Medikamente ein, die Mundtrockenheit verursachen?', 'question.diabetes': 'Wurde bei Ihnen Diabetes diagnostiziert?', 'question.halitosis': 'Bemerken Sie oder Ihnen nahestehende Personen Mundgeruch? Wie stark ist er von 0 bis 5?', 'question.candidiasis': 'Haben Sie weiße Beläge, Schmerzen oder ein watteartiges Gefühl im Mund bemerkt?', 'question.tongue': 'Hat Ihre Zunge tiefe Linien, Risse oder Furchen?', 'question.periodontal': 'Blutet oder schwillt Ihr Zahnfleisch an, oder fühlen sich Zähne locker an?', 'question.ckd': 'In welchem Stadium befindet sich Ihre chronische Nierenerkrankung?', 'option.never': 'Nie', 'option.sometimes': 'Manchmal', 'option.always': 'Immer', 'option.no': 'Nein', 'option.yes': 'Ja', 'option.none': 'Keine', 'option.moderate': 'Mittelgradig', 'option.severe': 'Schwer', 'option.dialysis': 'Dialyse', 'option.male': 'Männlich', 'option.female': 'Weiblich', 'option.other': 'Andere', 'dialog.xerostomia.title': 'Was ist Mundtrockenheit?', 'dialog.xerostomia.body': 'Mundtrockenheit (Xerostomie) ist das Gefühl, dass der Mund ungewöhnlich trocken oder klebrig ist oder zu wenig Speichel vorhanden ist.\n\nDadurch können Sprechen, Essen, Schlucken oder das Tragen von Zahnersatz erschwert werden.\n\nVergleichen Sie Ihre Beschwerden mit dem Referenzbild.', 'dialog.medication.title': 'Warum fragen wir danach?', 'dialog.medication.body': 'Einige Medikamente können die Speichelproduktion verringern und Mundtrockenheit begünstigen.\n\nDazu gehören unter anderem bestimmte Blutdruckmedikamente, Diuretika, Antidepressiva und Antihistaminika.', 'dialog.diabetes.title': 'Warum ist Diabetes wichtig?', 'dialog.diabetes.body': 'Diabetes kann das Risiko für Zahnfleischerkrankungen, orale Infektionen, verzögerte Heilung und Mundtrockenheit erhöhen.\n\nEine gute Mundgesundheit ist für Menschen mit Diabetes besonders wichtig.', 'dialog.halitosis.title': 'Was ist Mundgeruch?', 'dialog.halitosis.body': 'Mundgeruch, auch Halitosis genannt, ist ein unangenehmer Geruch aus dem Mund.\n\nEr kann mit Mundtrockenheit, Zungenbelag, Zahnfleischerkrankungen, Karies oder einer oralen Infektion zusammenhängen.', 'dialog.candidiasis.title': 'Was ist orale Candidose?', 'dialog.candidiasis.body': 'Orale Candidose ist eine Pilzinfektion im Mund.\n\nSie kann weiße Beläge, Rötung, Schmerzen, Brennen oder ein watteartiges Gefühl verursachen.\n\nVergleichen Sie Ihre Beschwerden mit dem Referenzbild.', 'dialog.tongue.title': 'Was ist eine Fissurenzunge?', 'dialog.tongue.body': 'Eine Fissurenzunge weist tiefe Linien, Risse oder Furchen auf der Oberfläche auf.\n\nSpeisereste oder Bakterien können sich darin ansammeln und Beschwerden oder Mundgeruch verursachen.\n\nVergleichen Sie Ihre Beschwerden mit dem Referenzbild.', 'dialog.periodontal.title': 'Was ist eine Parodontalerkrankung?', 'dialog.periodontal.body': 'Parodontalerkrankungen betreffen das Zahnfleisch und das Gewebe, das die Zähne stützt.\n\nAnzeichen können Zahnfleischbluten, Schwellung, Mundgeruch, lockere Zähne oder Schmerzen beim Kauen sein.\n\nVergleichen Sie Ihre Beschwerden mit dem Referenzbild.', 'dialog.ckd.title': 'Was bedeuten die CKD-Stadien?', 'dialog.ckd.body': 'CKD bedeutet chronische Nierenerkrankung. Sie wird meist anhand der Nierenfunktion in die Stadien 1 bis 5 eingeteilt.\n\n**Stadium 1:** Nierenschädigung bei normaler oder nahezu normaler Funktion.\n\n**Stadium 2:** Leichte Einschränkung der Nierenfunktion.\n\n**Stadium 3:** Mäßige Einschränkung; regelmäßige ärztliche Kontrolle ist besonders wichtig.\n\n**Stadium 4:** Schwere Einschränkung; eine Vorbereitung auf weiterführende Behandlung kann erforderlich sein.\n\n**Stadium 5:** Nierenversagen; Dialyse oder Nierentransplantation kann erforderlich sein.\n\n**Dialyse:** Behandlung zur Entfernung von Abfallstoffen und überschüssiger Flüssigkeit aus dem Blut.', 'results.intro': 'Füllen Sie alle Felder aus und klicken Sie auf die Schaltfläche, um die Risikobewertung anzuzeigen.', 'results.calculate': 'Risikopunktzahl berechnen', 'results.waiting': 'Warten auf die Berechnung...', 'results.score': 'Punktzahl', 'results.interpretation': 'Interpretation', 'results.actions': 'Empfohlene Maßnahmen', 'risk.low': 'Niedriges Risiko', 'risk.moderate': 'Mittleres Risiko', 'risk.high': 'Hohes Risiko', 'risk.low.interpretation': 'Ihre Antworten sprechen für ein **niedriges mundgesundheitsbezogenes Risiko**. Auf Grundlage Ihrer Angaben wurden keine wesentlichen mit CKD verbundenen oralen Befunde erkannt.', 'risk.moderate.interpretation': 'Ihre Antworten weisen auf **orale Befunde hin, die weitere Aufmerksamkeit erfordern könnten**. Eine professionelle zahnärztliche Untersuchung wird empfohlen.', 'risk.high.interpretation': 'Ihre Antworten deuten auf **mehrere orale Befunde oder fortgeschrittene systemische Faktoren** hin. Obwohl dies **keine Diagnose** darstellt, wird eine zeitnahe professionelle Abklärung empfohlen.', 'risk.low.actions': '- Achten Sie auf eine gute tägliche Mundhygiene.\n- Nehmen Sie regelmäßige zahnärztliche Kontrollen wahr.\n- Wiederholen Sie die Bewertung, wenn neue Beschwerden auftreten.', 'risk.moderate.actions': '- Vereinbaren Sie einen Zahnarzttermin.\n- Beobachten Sie Beschwerden wie Mundtrockenheit, Zahnfleischbluten oder anhaltenden Mundgeruch.\n- Teilen Sie den Bericht gegebenenfalls mit Ihrem Behandlungsteam.', 'risk.high.actions': '- Vereinbaren Sie möglichst bald eine zahnärztliche Untersuchung.\n- Informieren Sie Ihre Zahnärztin oder Ihren Zahnarzt über Ihr CKD-Stadium und Ihre Medikamente.\n- Besprechen Sie anhaltende orale Beschwerden mit Ihrer Nephrologin oder Ihrem Nephrologen.', 'results.disclaimer.title': '⚠️ Wichtiger Hinweis', 'results.disclaimer.body': 'Die numerische Punktzahl basiert auf **evidenzinformierter klinischer Beurteilung und Literaturauswertung**. Sie darf **nicht** als validierte Schätzung des CKD-Risikos oder des Krankheitsverlaufs verstanden werden.\n\nDas kombinierte Bewertungssystem wurde noch nicht formal abgeleitet, kalibriert oder extern validiert.\n\nDieser Rechner dient ausschließlich Bildungs- und Sensibilisierungszwecken und ersetzt keine professionelle Beratung.', 'report.toggle': 'Ausführlichen PDF-Bericht erstellen', 'report.patient_information': 'Patientenangaben', 'report.full_name': 'Vollständiger Name', 'report.age': 'Alter', 'report.sex': 'Geschlecht', 'report.consent': 'Ich stimme der Verarbeitung meiner personenbezogenen Daten zu', 'report.download': '📄 Bericht herunterladen', 'report.activate': 'Aktivieren Sie den Schalter oben, um einen personalisierten Bericht zu erstellen.', 'report.filename': 'mundgesundheit_ckd_risikobericht.pdf', 'pdf.title': 'Bericht zum Mundgesundheits- und CKD-Risiko', 'pdf.patient_name': 'Name der Patientin/des Patienten', 'pdf.generated': 'Bericht erstellt am', 'pdf.risk_category': 'Risikokategorie', 'pdf.risk_summary': 'Zusammenfassung der Risikobewertung', 'pdf.patient_responses': 'Antworten', 'pdf.indicator': 'Indikator', 'pdf.response': 'Antwort', 'pdf.indicator_meaning': 'Bedeutung der einzelnen Indikatoren', 'pdf.suggestions': 'Personalisierte Empfehlungen', 'pdf.general_advice': 'Allgemeine Hinweise zur Mundgesundheit', 'pdf.reminder': 'Wichtiger Hinweis', 'pdf.no_specific': 'Es wurden keine Antworten ausgewählt, die auf ein wesentliches Risiko hinweisen. Bitte behalten Sie eine gute tägliche Mundhygiene bei.', 'pdf.disclaimer': 'Dieser Bericht dient ausschließlich Bildungs- und Sensibilisierungszwecken. Er stellt keine medizinische Diagnose dar und ersetzt keine professionelle Beratung.', 'pdf.low_message': 'Ihre aktuelle Punktzahl spricht für ein niedriges mundgesundheitsbezogenes Risiko. Eine gute tägliche Mundhygiene und regelmäßige Kontrollen bleiben dennoch wichtig.', 'pdf.moderate_message': 'Ihre aktuelle Punktzahl spricht für ein mittleres mundgesundheitsbezogenes Risiko. Einige Anzeichen sollten genauer abgeklärt werden.', 'pdf.high_message': 'Ihre aktuelle Punktzahl spricht für ein hohes mundgesundheitsbezogenes Risiko. Mehrere orale oder medizinische Faktoren können professionelle Aufmerksamkeit erfordern.', 'indicator.xerostomia': 'Mundtrockenheit / Xerostomie', 'indicator.medication': 'Medikamente, die Mundtrockenheit verursachen', 'indicator.diabetes': 'Diabetes', 'indicator.halitosis': 'Mundgeruch / Halitosis', 'indicator.candidiasis': 'Orale Candidose', 'indicator.tongue': 'Fissurenzunge', 'indicator.periodontal': 'Parodontalerkrankung', 'indicator.ckd': 'CKD-Stadium', 'explanation.xerostomia': 'Mundtrockenheit bedeutet, dass sich der Mund häufig trocken, klebrig oder unangenehm anfühlt. Sprechen, Kauen, Schlucken oder Schmecken kann erschwert sein.', 'explanation.medication': 'Einige Medikamente, etwa Diuretika oder Blutdrucksenker, können den Speichelfluss verringern.', 'explanation.diabetes': 'Diabetes kann das Risiko für Zahnfleischerkrankungen, orale Infektionen, verzögerte Heilung und Mundtrockenheit erhöhen.', 'explanation.halitosis': 'Mundgeruch kann mit Mundtrockenheit, Zungenbelag, Zahnfleischerkrankungen, Karies oder Infektionen zusammenhängen.', 'explanation.candidiasis': 'Orale Candidose ist eine Pilzinfektion, die weiße Beläge, Rötung, Schmerzen oder Brennen verursachen kann.', 'explanation.tongue': 'Eine Fissurenzunge hat tiefe Linien oder Furchen, in denen sich Speisereste und Bakterien ansammeln können.', 'explanation.periodontal': 'Parodontalerkrankungen betreffen Zahnfleisch und Zahnhalteapparat und können Blutungen, Schwellung oder lockere Zähne verursachen.', 'explanation.ckd': 'Das CKD-Stadium beschreibt den Schweregrad der chronischen Nierenerkrankung.', 'recommendation.xerostomia.1': 'Trinken Sie regelmäßig kleine Mengen Wasser, sofern Ihre Nierenärztin oder Ihr Nierenarzt dies erlaubt.', 'recommendation.xerostomia.2': 'Zuckerfreier Kaugummi oder zuckerfreie Lutschpastillen können den Speichelfluss anregen.', 'recommendation.xerostomia.3': 'Fragen Sie nach Speichelersatzmitteln oder Produkten gegen Mundtrockenheit.', 'recommendation.medication.1': 'Setzen Sie Medikamente nicht eigenständig ab.', 'recommendation.medication.2': 'Fragen Sie, ob Ihre Medikamente zur Mundtrockenheit beitragen könnten.', 'recommendation.medication.3': 'Informieren Sie Ihre Zahnarztpraxis über alle Medikamente.', 'recommendation.diabetes.1': 'Achten Sie entsprechend der ärztlichen Empfehlung auf eine gute Blutzuckereinstellung.', 'recommendation.diabetes.2': 'Kontrollieren Sie Ihr Zahnfleisch auf Blutungen, Schwellungen oder Infektionszeichen.', 'recommendation.diabetes.3': 'Nehmen Sie regelmäßige zahnärztliche Kontrollen wahr.', 'recommendation.halitosis.1': 'Putzen Sie täglich sanft Zähne und Zunge.', 'recommendation.halitosis.2': 'Reinigen Sie die Zahnzwischenräume mit Zahnseide oder Interdentalbürsten.', 'recommendation.halitosis.3': 'Lassen Sie anhaltenden Mundgeruch zahnärztlich abklären.', 'recommendation.candidiasis.1': 'Suchen Sie bei weißen Belägen, Brennen oder Schmerzen eine Zahn- oder Arztpraxis auf.', 'recommendation.candidiasis.2': 'Vermeiden Sie Selbstmedikation ohne fachliche Beratung.', 'recommendation.candidiasis.3': 'Reinigen Sie Zahnersatz und andere orale Hilfsmittel sorgfältig.', 'recommendation.tongue.1': 'Reinigen Sie die Zunge vorsichtig.', 'recommendation.tongue.2': 'Meiden Sie reizende Speisen, wenn die Zunge empfindlich ist.', 'recommendation.tongue.3': 'Lassen Sie anhaltende Schmerzen oder Schwellungen untersuchen.', 'recommendation.periodontal.1': 'Lassen Sie Ihr Zahnfleisch zahnärztlich oder parodontologisch untersuchen.', 'recommendation.periodontal.2': 'Eine professionelle Zahnreinigung kann erforderlich sein.', 'recommendation.periodontal.3': 'Suchen Sie bei Blutungen, Schwellung, Schmerzen oder lockeren Zähnen zahnärztliche Hilfe.', 'recommendation.ckd.1': 'Informieren Sie sowohl Ihr Nieren- als auch Ihr zahnärztliches Behandlungsteam.', 'recommendation.ckd.2': 'Besprechen Sie größere zahnärztliche Eingriffe bei fortgeschrittener CKD oder Dialyse vorher mit Ihrem Behandlungsteam.', 'recommendation.ckd.3': 'Achten Sie auf regelmäßige Mundpflege, da orale Infektionen die Allgemeingesundheit beeinflussen können.', 'general.1': 'Putzen Sie Ihre Zähne mindestens zweimal täglich vorsichtig mit fluoridhaltiger Zahnpasta.', 'general.2': 'Reinigen Sie täglich die Zahnzwischenräume.', 'general.3': 'Trinken Sie ausreichend Wasser, sofern dies nierenärztlich erlaubt ist.', 'general.4': 'Vermeiden Sie Rauchen und begrenzen Sie Alkohol.', 'general.5': 'Nehmen Sie regelmäßige zahnärztliche Untersuchungen und professionelle Reinigungen wahr.', 'general.6': 'Informieren Sie Ihre Zahnarztpraxis über CKD, Diabetes und Dauermedikamente.', 'general.7': 'Ignorieren Sie Zahnfleischbluten, lockere Zähne, weiße Beläge, Schmerzen oder anhaltenden Mundgeruch nicht.', 'general.8': 'Besprechen Sie bei Dialyse oder fortgeschrittener CKD den Zeitpunkt zahnärztlicher Behandlungen mit Ihrem Behandlungsteam.'}
PORTUGUESE_TRANSLATIONS = {'app.title': 'Índice de Saúde Oral e Calculadora de Risco de DRC', 'app.intro': 'Esta calculadora estima como o estado de saúde oral de uma pessoa pode estar associado ao desenvolvimento ou à progressão da doença renal crónica (DRC). Preencha este breve questionário e calcule o seu nível de risco na secção final.', 'settings.title': 'Preferências', 'settings.language': 'Idioma', 'settings.choose_language': 'Escolha o idioma:', 'settings.theme': 'Tema', 'settings.choose_theme': 'Escolha o tema:', 'settings.font_size': 'Tamanho da letra', 'settings.choose_font_size': 'Escolha o tamanho da letra:', 'theme.clear': 'Claro', 'theme.dark': 'Escuro', 'font.small': 'Pequeno', 'font.medium': 'Médio', 'font.large': 'Grande', 'instructions.title': 'Instruções', 'instructions.body': '**Como utilizar esta ferramenta:**\n\n1. Selecione a opção adequada ao seu caso em cada uma das três secções.  \n2. Utilize os ícones de informação junto às perguntas para consultar explicações e orientação visual.  \n3. Depois de responder a todas as perguntas, clique em **Calcular pontuação de risco**.  \n4. A aplicação apresentará a pontuação, a categoria de risco, a interpretação e as ações recomendadas.  \n5. Em caso de risco moderado ou elevado, poderá gerar opcionalmente um relatório detalhado.', 'evidence.title': 'Evidência e limitações do modelo', 'evidence.body': 'Esta calculadora considera evidência atual sobre a associação entre doenças orais e doença renal crónica (DRC), incluindo revisões sistemáticas e meta-análises.\n\nNo entanto, a ponderação numérica e a pontuação global **não** foram derivadas nem validadas com base num único modelo de previsão publicado ou estudo de coorte prospetivo.\n\nAssim, o algoritmo deve ser entendido como um **quadro clínico informado pela evidência**, e não como um modelo de previsão de risco validado.', 'section.about_you': 'Sobre si', 'section.oral_health': 'A sua saúde oral', 'section.kidney_health': 'A sua saúde renal', 'section.results': 'Resultados', 'question.xerostomia': 'Sente frequentemente a boca seca ou pegajosa?', 'question.medication': 'Toma algum medicamento que provoque boca seca?', 'question.diabetes': 'Foi-lhe diagnosticada diabetes?', 'question.halitosis': 'Você ou pessoas próximas notam mau hálito? Qual é a intensidade de 0 a 5?', 'question.candidiasis': 'Notou placas brancas, dor ou sensação de algodão na boca?', 'question.tongue': 'A sua língua apresenta linhas profundas, fissuras ou sulcos?', 'question.periodontal': 'As suas gengivas sangram ou estão inchadas, ou algum dente parece solto?', 'question.ckd': 'Qual é o estádio da sua doença renal crónica?', 'option.never': 'Nunca', 'option.sometimes': 'Às vezes', 'option.always': 'Sempre', 'option.no': 'Não', 'option.yes': 'Sim', 'option.none': 'Nenhuma', 'option.moderate': 'Moderada', 'option.severe': 'Grave', 'option.dialysis': 'Diálise', 'option.male': 'Masculino', 'option.female': 'Feminino', 'option.other': 'Outro', 'dialog.xerostomia.title': 'O que é boca seca?', 'dialog.xerostomia.body': 'A boca seca, ou xerostomia, é a sensação de que a boca está anormalmente seca, pegajosa ou com pouca saliva.\n\nPode dificultar falar, comer, engolir ou utilizar próteses dentárias.\n\nCompare os seus sintomas com a imagem de referência.', 'dialog.medication.title': 'Por que fazemos esta pergunta?', 'dialog.medication.body': 'Alguns medicamentos podem reduzir a produção de saliva e contribuir para a boca seca.\n\nExemplos incluem certos anti-hipertensivos, diuréticos, antidepressivos e anti-histamínicos.', 'dialog.diabetes.title': 'Por que a diabetes é importante?', 'dialog.diabetes.body': 'A diabetes pode aumentar o risco de doença gengival, infeções orais, cicatrização lenta e boca seca.\n\nUma boa saúde oral é especialmente importante para pessoas com diabetes.', 'dialog.halitosis.title': 'O que é mau hálito?', 'dialog.halitosis.body': 'O mau hálito, também chamado halitose, é um odor desagradável proveniente da boca.\n\nPode estar relacionado com boca seca, saburra lingual, doença gengival, cárie ou infeção oral.', 'dialog.candidiasis.title': 'O que é candidíase oral?', 'dialog.candidiasis.body': 'A candidíase oral é uma infeção fúngica que pode surgir na boca.\n\nPode causar placas brancas, vermelhidão, dor, ardor ou sensação de algodão.\n\nCompare os seus sintomas com a imagem de referência.', 'dialog.tongue.title': 'O que é língua fissurada?', 'dialog.tongue.body': 'A língua fissurada apresenta linhas profundas, fissuras ou sulcos na superfície.\n\nAlimentos ou bactérias podem ficar retidos e causar desconforto ou mau hálito.\n\nCompare os seus sintomas com a imagem de referência.', 'dialog.periodontal.title': 'O que é doença periodontal?', 'dialog.periodontal.body': 'A doença periodontal afeta as gengivas e os tecidos que sustentam os dentes.\n\nOs sinais podem incluir sangramento, inchaço, mau hálito, dentes soltos ou dor ao mastigar.\n\nCompare os seus sintomas com a imagem de referência.', 'dialog.ckd.title': 'O que significam os estádios da DRC?', 'dialog.ckd.body': 'DRC significa doença renal crónica. É geralmente classificada em estádios de 1 a 5 de acordo com a função renal.\n\n**Estádio 1:** Lesão renal com função normal ou quase normal.\n\n**Estádio 2:** Redução ligeira da função renal.\n\n**Estádio 3:** Redução moderada; o acompanhamento médico torna-se especialmente importante.\n\n**Estádio 4:** Redução grave; pode ser necessária preparação para tratamento avançado.\n\n**Estádio 5:** Falência renal; pode ser necessária diálise ou transplante renal.\n\n**Diálise:** Tratamento que remove resíduos e excesso de líquidos do sangue.', 'results.intro': 'Preencha todos os campos e clique no botão para ver a avaliação de risco.', 'results.calculate': 'Calcular pontuação de risco', 'results.waiting': 'A aguardar o cálculo...', 'results.score': 'Pontuação', 'results.interpretation': 'Interpretação', 'results.actions': 'Ações recomendadas', 'risk.low': 'Risco baixo', 'risk.moderate': 'Risco moderado', 'risk.high': 'Risco elevado', 'risk.low.interpretation': 'As suas respostas sugerem um **baixo nível de risco relacionado com a saúde oral**. Não foram identificados achados orais importantes associados à DRC.', 'risk.moderate.interpretation': 'As suas respostas indicam **achados de saúde oral que podem exigir maior atenção**. Recomenda-se uma avaliação dentária profissional.', 'risk.high.interpretation': 'As suas respostas sugerem **múltiplos achados orais ou fatores sistémicos avançados**. Embora isto **não seja um diagnóstico**, recomenda-se avaliação profissional atempada.', 'risk.low.actions': '- Mantenha uma boa higiene oral diária.\n- Realize consultas dentárias de rotina.\n- Repita a avaliação se surgirem novos sintomas.', 'risk.moderate.actions': '- Marque uma consulta dentária.\n- Vigie sintomas como boca seca, sangramento gengival ou mau hálito persistente.\n- Partilhe o relatório com os seus profissionais de saúde quando apropriado.', 'risk.high.actions': '- Procure uma avaliação dentária assim que possível.\n- Informe o dentista sobre o seu estádio de DRC e os medicamentos atuais.\n- Discuta sintomas orais persistentes com o nefrologista.', 'results.disclaimer.title': '⚠️ Aviso importante', 'results.disclaimer.body': 'A pontuação numérica baseia-se em **julgamento clínico informado pela evidência e síntese da literatura**. Não deve ser interpretada como uma estimativa validada do risco ou da progressão da DRC.\n\nO sistema combinado ainda não foi formalmente derivado, calibrado ou validado externamente.\n\nEsta calculadora destina-se apenas a fins educativos e de sensibilização e não substitui aconselhamento profissional.', 'report.toggle': 'Gerar relatório PDF detalhado', 'report.patient_information': 'Informações do paciente', 'report.full_name': 'Nome completo', 'report.age': 'Idade', 'report.sex': 'Sexo', 'report.consent': 'Aceito o tratamento dos meus dados pessoais', 'report.download': '📄 Obter o meu relatório', 'report.activate': 'Ative o interruptor acima para gerar um relatório personalizado.', 'report.filename': 'relatorio_risco_oral_drc.pdf', 'pdf.title': 'Relatório de saúde oral e risco de DRC', 'pdf.patient_name': 'Nome do paciente', 'pdf.generated': 'Relatório gerado em', 'pdf.risk_category': 'Categoria de risco', 'pdf.risk_summary': 'Resumo da avaliação de risco', 'pdf.patient_responses': 'Respostas do paciente', 'pdf.indicator': 'Indicador', 'pdf.response': 'Resposta', 'pdf.indicator_meaning': 'Significado de cada indicador', 'pdf.suggestions': 'Sugestões personalizadas', 'pdf.general_advice': 'Conselhos gerais de saúde oral', 'pdf.reminder': 'Lembrete importante', 'pdf.no_specific': 'Não foram selecionadas respostas associadas a risco importante. Continue a manter uma boa higiene oral diária.', 'pdf.disclaimer': 'Este relatório destina-se apenas a fins educativos e de sensibilização. Não fornece um diagnóstico médico nem substitui aconselhamento profissional.', 'pdf.low_message': 'A sua pontuação atual sugere um baixo nível de risco relacionado com a saúde oral.', 'pdf.moderate_message': 'A sua pontuação atual sugere um nível moderado de risco relacionado com a saúde oral.', 'pdf.high_message': 'A sua pontuação atual sugere um nível elevado de risco relacionado com a saúde oral.', 'indicator.xerostomia': 'Boca seca / Xerostomia', 'indicator.medication': 'Medicamentos que causam boca seca', 'indicator.diabetes': 'Diabetes', 'indicator.halitosis': 'Mau hálito / Halitose', 'indicator.candidiasis': 'Candidíase oral', 'indicator.tongue': 'Língua fissurada', 'indicator.periodontal': 'Doença periodontal', 'indicator.ckd': 'Estádio da DRC', 'explanation.xerostomia': 'A boca seca pode dificultar falar, mastigar, engolir ou sentir o sabor dos alimentos.', 'explanation.medication': 'Alguns medicamentos podem reduzir a saliva e provocar boca seca.', 'explanation.diabetes': 'A diabetes pode aumentar o risco de doença gengival, infeção oral, atraso na cicatrização e boca seca.', 'explanation.halitosis': 'O mau hálito pode estar associado a boca seca, saburra lingual, doença gengival, cárie ou infeção.', 'explanation.candidiasis': 'A candidíase oral é uma infeção fúngica que pode causar placas brancas, vermelhidão, dor ou ardor.', 'explanation.tongue': 'A língua fissurada apresenta sulcos onde alimentos e bactérias podem acumular-se.', 'explanation.periodontal': 'A doença periodontal afeta as gengivas e os tecidos de suporte dos dentes.', 'explanation.ckd': 'O estádio da DRC descreve a gravidade da doença renal crónica.', 'recommendation.xerostomia.1': 'Beba pequenos goles de água com frequência, se o nefrologista o permitir.', 'recommendation.xerostomia.2': 'Utilize pastilha elástica ou pastilhas sem açúcar para estimular a saliva.', 'recommendation.xerostomia.3': 'Pergunte sobre substitutos de saliva ou produtos para boca seca.', 'recommendation.medication.1': 'Não interrompa nenhum medicamento por iniciativa própria.', 'recommendation.medication.2': 'Pergunte se os seus medicamentos podem contribuir para a boca seca.', 'recommendation.medication.3': 'Informe o dentista sobre todos os medicamentos que toma.', 'recommendation.diabetes.1': 'Mantenha um bom controlo da glicemia conforme orientação clínica.', 'recommendation.diabetes.2': 'Observe as gengivas quanto a sangramento, inchaço ou sinais de infeção.', 'recommendation.diabetes.3': 'Realize consultas dentárias regulares.', 'recommendation.halitosis.1': 'Escove suavemente os dentes e a língua todos os dias.', 'recommendation.halitosis.2': 'Limpe entre os dentes com fio dentário ou escovas interdentárias.', 'recommendation.halitosis.3': 'Procure avaliação dentária se o mau hálito persistir.', 'recommendation.candidiasis.1': 'Consulte um dentista ou médico se notar placas brancas, ardor ou dor.', 'recommendation.candidiasis.2': 'Evite automedicação sem orientação profissional.', 'recommendation.candidiasis.3': 'Mantenha limpas as próteses e outros aparelhos orais.', 'recommendation.tongue.1': 'Limpe a língua suavemente.', 'recommendation.tongue.2': 'Evite alimentos irritantes se a língua estiver sensível.', 'recommendation.tongue.3': 'Procure avaliação se houver dor ou inchaço persistente.', 'recommendation.periodontal.1': 'Consulte um dentista ou periodontologista para avaliar as gengivas.', 'recommendation.periodontal.2': 'Pode ser necessária uma limpeza profissional.', 'recommendation.periodontal.3': 'Procure cuidados dentários em caso de sangramento, inchaço, dor ou dentes soltos.', 'recommendation.ckd.1': 'Mantenha o nefrologista e o dentista informados sobre a sua condição.', 'recommendation.ckd.2': 'Antes de procedimentos dentários importantes, consulte a equipa de saúde se tiver DRC avançada ou fizer diálise.', 'recommendation.ckd.3': 'Mantenha cuidados orais regulares, pois infeções orais podem afetar a saúde geral.', 'general.1': 'Escove os dentes suavemente pelo menos duas vezes por dia com pasta fluoretada.', 'general.2': 'Limpe diariamente os espaços entre os dentes.', 'general.3': 'Beba água suficiente se o nefrologista o permitir.', 'general.4': 'Evite fumar e limite o álcool.', 'general.5': 'Consulte regularmente um dentista para exame e limpeza profissional.', 'general.6': 'Informe o dentista se tiver DRC, diabetes ou usar medicamentos de longa duração.', 'general.7': 'Não ignore sangramento gengival, dentes soltos, placas brancas, dor ou mau hálito persistente.', 'general.8': 'Se fizer diálise ou tiver DRC avançada, discuta o momento do tratamento dentário com a equipa de saúde.'}
FRENCH_TRANSLATIONS = {'app.title': 'Indice de santé bucco-dentaire et calculateur de risque de MRC', 'app.intro': 'Ce calculateur estime dans quelle mesure l’état de santé bucco-dentaire d’une personne peut être associé au développement ou à la progression d’une maladie rénale chronique (MRC). Remplissez ce court questionnaire et calculez votre niveau de risque dans la dernière section.', 'settings.title': 'Préférences', 'settings.language': 'Langue', 'settings.choose_language': 'Choisissez la langue :', 'settings.theme': 'Thème', 'settings.choose_theme': 'Choisissez le thème :', 'settings.font_size': 'Taille de police', 'settings.choose_font_size': 'Choisissez la taille de police :', 'theme.clear': 'Clair', 'theme.dark': 'Sombre', 'font.small': 'Petite', 'font.medium': 'Moyenne', 'font.large': 'Grande', 'instructions.title': 'Instructions', 'instructions.body': '**Comment utiliser cet outil :**\n\n1. Sélectionnez l’option correspondant à votre situation dans chacune des trois sections.  \n2. Utilisez les icônes d’information pour consulter les explications et les repères visuels.  \n3. Après avoir répondu à toutes les questions, cliquez sur **Calculer le score de risque**.  \n4. L’application affichera votre score, la catégorie de risque, l’interprétation et les actions recommandées.  \n5. En cas de risque modéré ou élevé, vous pourrez générer facultativement un rapport détaillé.', 'evidence.title': 'Données probantes et limites du modèle', 'evidence.body': 'Ce calculateur s’appuie sur les données actuelles concernant l’association entre les maladies bucco-dentaires et la maladie rénale chronique (MRC), notamment des revues systématiques et des méta-analyses.\n\nCependant, la pondération numérique et le score global **n’ont pas** été dérivés d’un modèle prédictif publié unique ni validés dans une cohorte prospective.\n\nL’algorithme doit donc être compris comme un **cadre clinique fondé sur les données disponibles**, et non comme un modèle validé de prédiction du risque.', 'section.about_you': 'À propos de vous', 'section.oral_health': 'Votre santé bucco-dentaire', 'section.kidney_health': 'Votre santé rénale', 'section.results': 'Résultats', 'question.xerostomia': 'Votre bouche vous semble-t-elle souvent sèche ou collante ?', 'question.medication': 'Prenez-vous un médicament qui provoque une sécheresse buccale ?', 'question.diabetes': 'Un diabète vous a-t-il été diagnostiqué ?', 'question.halitosis': 'Vous-même ou vos proches remarquez-vous une mauvaise haleine ? Quelle est son intensité de 0 à 5 ?', 'question.candidiasis': 'Avez-vous remarqué des plaques blanches, une douleur ou une sensation cotonneuse dans la bouche ?', 'question.tongue': 'Votre langue présente-t-elle des lignes profondes, des fissures ou des sillons ?', 'question.periodontal': 'Vos gencives saignent-elles ou sont-elles gonflées, ou certaines dents semblent-elles mobiles ?', 'question.ckd': 'Quel est le stade de votre maladie rénale chronique ?', 'option.never': 'Jamais', 'option.sometimes': 'Parfois', 'option.always': 'Toujours', 'option.no': 'Non', 'option.yes': 'Oui', 'option.none': 'Aucune', 'option.moderate': 'Modérée', 'option.severe': 'Sévère', 'option.dialysis': 'Dialyse', 'option.male': 'Masculin', 'option.female': 'Féminin', 'option.other': 'Autre', 'dialog.xerostomia.title': 'Qu’est-ce que la sécheresse buccale ?', 'dialog.xerostomia.body': 'La sécheresse buccale, ou xérostomie, correspond à la sensation d’une bouche anormalement sèche, collante ou manquant de salive.\n\nElle peut rendre plus difficiles la parole, l’alimentation, la déglutition ou le port d’une prothèse dentaire.\n\nComparez vos symptômes à l’image de référence.', 'dialog.medication.title': 'Pourquoi posons-nous cette question ?', 'dialog.medication.body': 'Certains médicaments peuvent réduire la production de salive et favoriser la sécheresse buccale.\n\nParmi les exemples figurent certains antihypertenseurs, diurétiques, antidépresseurs et antihistaminiques.', 'dialog.diabetes.title': 'Pourquoi le diabète est-il important ?', 'dialog.diabetes.body': 'Le diabète peut augmenter le risque de maladie gingivale, d’infection buccale, de retard de cicatrisation et de sécheresse buccale.\n\nUne bonne santé bucco-dentaire est particulièrement importante chez les personnes diabétiques.', 'dialog.halitosis.title': 'Qu’est-ce que la mauvaise haleine ?', 'dialog.halitosis.body': 'La mauvaise haleine, ou halitose, est une odeur désagréable provenant de la bouche.\n\nElle peut être liée à la sécheresse buccale, à un dépôt sur la langue, à une maladie gingivale, à une carie ou à une infection.', 'dialog.candidiasis.title': 'Qu’est-ce que la candidose buccale ?', 'dialog.candidiasis.body': 'La candidose buccale est une infection fongique de la bouche.\n\nElle peut provoquer des plaques blanches, des rougeurs, des douleurs, des brûlures ou une sensation cotonneuse.\n\nComparez vos symptômes à l’image de référence.', 'dialog.tongue.title': 'Qu’est-ce qu’une langue fissurée ?', 'dialog.tongue.body': 'Une langue fissurée présente des lignes profondes, des fissures ou des sillons à sa surface.\n\nDes aliments ou des bactéries peuvent s’y accumuler et provoquer une gêne ou une mauvaise haleine.\n\nComparez vos symptômes à l’image de référence.', 'dialog.periodontal.title': 'Qu’est-ce qu’une maladie parodontale ?', 'dialog.periodontal.body': 'La maladie parodontale touche les gencives et les tissus qui soutiennent les dents.\n\nLes signes peuvent inclure des saignements, un gonflement, une mauvaise haleine, des dents mobiles ou une douleur à la mastication.\n\nComparez vos symptômes à l’image de référence.', 'dialog.ckd.title': 'Que signifient les stades de la MRC ?', 'dialog.ckd.body': 'MRC signifie maladie rénale chronique. Elle est généralement classée du stade 1 au stade 5 selon la fonction rénale.\n\n**Stade 1 :** Atteinte rénale avec fonction normale ou presque normale.\n\n**Stade 2 :** Légère diminution de la fonction rénale.\n\n**Stade 3 :** Diminution modérée ; le suivi médical devient particulièrement important.\n\n**Stade 4 :** Diminution sévère ; une préparation à un traitement avancé peut être nécessaire.\n\n**Stade 5 :** Insuffisance rénale ; une dialyse ou une transplantation peut être nécessaire.\n\n**Dialyse :** Traitement qui élimine les déchets et l’excès de liquide du sang.', 'results.intro': 'Remplissez tous les champs puis cliquez sur le bouton pour afficher l’évaluation du risque.', 'results.calculate': 'Calculer le score de risque', 'results.waiting': 'En attente du calcul...', 'results.score': 'Score', 'results.interpretation': 'Interprétation', 'results.actions': 'Actions recommandées', 'risk.low': 'Risque faible', 'risk.moderate': 'Risque modéré', 'risk.high': 'Risque élevé', 'risk.low.interpretation': 'Vos réponses suggèrent un **faible niveau de risque lié à la santé bucco-dentaire**. Aucun signe bucco-dentaire majeur associé à la MRC n’a été identifié.', 'risk.moderate.interpretation': 'Vos réponses indiquent des **signes bucco-dentaires pouvant nécessiter une attention supplémentaire**. Une évaluation dentaire professionnelle est recommandée.', 'risk.high.interpretation': 'Vos réponses suggèrent **plusieurs signes bucco-dentaires ou facteurs systémiques avancés**. Bien qu’il ne s’agisse **pas d’un diagnostic**, une évaluation professionnelle rapide est recommandée.', 'risk.low.actions': '- Maintenez une bonne hygiène bucco-dentaire quotidienne.\n- Consultez régulièrement un dentiste.\n- Répétez l’évaluation si de nouveaux symptômes apparaissent.', 'risk.moderate.actions': '- Prenez rendez-vous chez le dentiste.\n- Surveillez la sécheresse buccale, le saignement des gencives ou la mauvaise haleine persistante.\n- Partagez le rapport avec vos professionnels de santé si nécessaire.', 'risk.high.actions': '- Organisez une évaluation dentaire dès que possible.\n- Informez votre dentiste de votre stade de MRC et de vos médicaments.\n- Discutez des symptômes buccaux persistants avec votre néphrologue.', 'results.disclaimer.title': '⚠️ Avertissement important', 'results.disclaimer.body': 'Le score numérique repose sur un **jugement clinique éclairé par les données disponibles et une synthèse de la littérature**. Il ne doit **pas** être interprété comme une estimation validée du risque ou de la progression de la MRC.\n\nLe système combiné n’a pas encore fait l’objet d’une dérivation, d’un étalonnage ou d’une validation externe formels.\n\nCe calculateur est destiné uniquement à l’éducation et à la sensibilisation et ne remplace pas un avis professionnel.', 'report.toggle': 'Générer un rapport PDF détaillé', 'report.patient_information': 'Informations du patient', 'report.full_name': 'Nom complet', 'report.age': 'Âge', 'report.sex': 'Sexe', 'report.consent': 'J’accepte le traitement de mes données personnelles', 'report.download': '📄 Obtenir mon rapport', 'report.activate': 'Activez l’interrupteur ci-dessus pour générer un rapport personnalisé.', 'report.filename': 'rapport_risque_oral_mrc.pdf', 'pdf.title': 'Rapport sur la santé bucco-dentaire et le risque de MRC', 'pdf.patient_name': 'Nom du patient', 'pdf.generated': 'Rapport généré le', 'pdf.risk_category': 'Catégorie de risque', 'pdf.risk_summary': 'Résumé de l’évaluation du risque', 'pdf.patient_responses': 'Réponses du patient', 'pdf.indicator': 'Indicateur', 'pdf.response': 'Réponse', 'pdf.indicator_meaning': 'Signification de chaque indicateur', 'pdf.suggestions': 'Suggestions personnalisées', 'pdf.general_advice': 'Conseils généraux de santé bucco-dentaire', 'pdf.reminder': 'Rappel important', 'pdf.no_specific': 'Aucune réponse associée à un risque important n’a été sélectionnée. Continuez à maintenir une bonne hygiène bucco-dentaire.', 'pdf.disclaimer': 'Ce rapport est destiné uniquement à l’éducation et à la sensibilisation. Il ne fournit pas de diagnostic médical et ne remplace pas un avis professionnel.', 'pdf.low_message': 'Votre score actuel suggère un faible niveau de risque lié à la santé bucco-dentaire.', 'pdf.moderate_message': 'Votre score actuel suggère un niveau modéré de risque lié à la santé bucco-dentaire.', 'pdf.high_message': 'Votre score actuel suggère un niveau élevé de risque lié à la santé bucco-dentaire.', 'indicator.xerostomia': 'Sécheresse buccale / Xérostomie', 'indicator.medication': 'Médicaments provoquant une sécheresse buccale', 'indicator.diabetes': 'Diabète', 'indicator.halitosis': 'Mauvaise haleine / Halitose', 'indicator.candidiasis': 'Candidose buccale', 'indicator.tongue': 'Langue fissurée', 'indicator.periodontal': 'Maladie parodontale', 'indicator.ckd': 'Stade de la MRC', 'explanation.xerostomia': 'La sécheresse buccale peut rendre plus difficiles la parole, la mastication, la déglutition ou la perception du goût.', 'explanation.medication': 'Certains médicaments peuvent réduire la salive et provoquer une sécheresse buccale.', 'explanation.diabetes': 'Le diabète peut augmenter le risque de maladie gingivale, d’infection buccale, de retard de cicatrisation et de sécheresse.', 'explanation.halitosis': 'La mauvaise haleine peut être liée à la sécheresse, à un dépôt lingual, à une maladie gingivale, à une carie ou à une infection.', 'explanation.candidiasis': 'La candidose buccale est une infection fongique pouvant provoquer des plaques blanches, des rougeurs, des douleurs ou des brûlures.', 'explanation.tongue': 'Une langue fissurée comporte des sillons où des aliments et des bactéries peuvent s’accumuler.', 'explanation.periodontal': 'La maladie parodontale touche les gencives et les tissus de soutien des dents.', 'explanation.ckd': 'Le stade de la MRC décrit la gravité de la maladie rénale chronique.', 'recommendation.xerostomia.1': 'Buvez régulièrement de petites quantités d’eau si votre néphrologue l’autorise.', 'recommendation.xerostomia.2': 'Utilisez un chewing-gum ou des pastilles sans sucre pour stimuler la salive.', 'recommendation.xerostomia.3': 'Demandez conseil au sujet des substituts salivaires ou des produits contre la sécheresse buccale.', 'recommendation.medication.1': 'N’arrêtez aucun médicament de votre propre initiative.', 'recommendation.medication.2': 'Demandez si vos médicaments peuvent contribuer à la sécheresse buccale.', 'recommendation.medication.3': 'Informez votre dentiste de tous les médicaments que vous prenez.', 'recommendation.diabetes.1': 'Maintenez un bon équilibre glycémique selon les recommandations de votre professionnel de santé.', 'recommendation.diabetes.2': 'Surveillez les saignements, le gonflement ou les signes d’infection des gencives.', 'recommendation.diabetes.3': 'Effectuez des contrôles dentaires réguliers.', 'recommendation.halitosis.1': 'Brossez doucement vos dents et votre langue chaque jour.', 'recommendation.halitosis.2': 'Nettoyez les espaces interdentaires avec du fil ou des brossettes.', 'recommendation.halitosis.3': 'Consultez un dentiste si la mauvaise haleine persiste.', 'recommendation.candidiasis.1': 'Consultez un dentiste ou un médecin en présence de plaques blanches, de brûlures ou de douleurs.', 'recommendation.candidiasis.2': 'Évitez l’automédication sans avis professionnel.', 'recommendation.candidiasis.3': 'Nettoyez soigneusement les prothèses et appareils buccaux.', 'recommendation.tongue.1': 'Nettoyez doucement votre langue.', 'recommendation.tongue.2': 'Évitez les aliments irritants si la langue est sensible.', 'recommendation.tongue.3': 'Consultez en cas de douleur ou de gonflement persistant.', 'recommendation.periodontal.1': 'Consultez un dentiste ou un parodontiste pour évaluer vos gencives.', 'recommendation.periodontal.2': 'Un nettoyage professionnel peut être nécessaire.', 'recommendation.periodontal.3': 'Consultez en cas de saignement, gonflement, douleur ou mobilité dentaire.', 'recommendation.ckd.1': 'Tenez votre néphrologue et votre dentiste informés de votre état de santé.', 'recommendation.ckd.2': 'Avant une intervention dentaire importante, consultez votre équipe soignante en cas de MRC avancée ou de dialyse.', 'recommendation.ckd.3': 'Maintenez des soins bucco-dentaires réguliers, car une infection orale peut affecter la santé générale.', 'general.1': 'Brossez doucement vos dents au moins deux fois par jour avec un dentifrice fluoré.', 'general.2': 'Nettoyez chaque jour les espaces entre les dents.', 'general.3': 'Buvez suffisamment d’eau si votre néphrologue l’autorise.', 'general.4': 'Évitez le tabac et limitez l’alcool.', 'general.5': 'Consultez régulièrement un dentiste pour un examen et un nettoyage professionnel.', 'general.6': 'Informez votre dentiste si vous avez une MRC, un diabète ou un traitement au long cours.', 'general.7': 'N’ignorez pas les saignements gingivaux, les dents mobiles, les plaques blanches, la douleur ou la mauvaise haleine persistante.', 'general.8': 'En cas de dialyse ou de MRC avancée, discutez du calendrier des soins dentaires avec votre équipe soignante.'}
TRANSLATIONS["de"].update(GERMAN_TRANSLATIONS)
TRANSLATIONS["pt"].update(PORTUGUESE_TRANSLATIONS)
TRANSLATIONS["fr"].update(FRENCH_TRANSLATIONS)

def translate(language_code: str, key: str, **kwargs) -> str:
    """Return a localized string, falling back to English and then to the key."""
    text = TRANSLATIONS.get(language_code, {}).get(
        key,
        TRANSLATIONS["en"].get(key, key),
    )
    if kwargs:
        try:
            return text.format(**kwargs)
        except (KeyError, ValueError):
            return text
    return text


OPTION_KEYS = {
    "Never": "option.never",
    "Sometimes": "option.sometimes",
    "Always": "option.always",
    "No": "option.no",
    "Yes": "option.yes",
    "None": "option.none",
    "Moderate": "option.moderate",
    "Severe": "option.severe",
    "Dialysis": "option.dialysis",
    "Male": "option.male",
    "Female": "option.female",
    "Other": "option.other",
}


def option_label(language_code: str, value: str) -> str:
    """Translate a displayed option without changing its internal canonical value."""
    key = OPTION_KEYS.get(str(value))
    return translate(language_code, key) if key else str(value)

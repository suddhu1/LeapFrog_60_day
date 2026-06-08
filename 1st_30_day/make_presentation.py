from pptx import Presentation
from pptx.util import Pt

# Create presentation object
prs = Presentation()

# --- Slide 1: Title Slide ---
title_slide_layout = prs.slide_layouts[0]
slide = prs.slides.add_slide(title_slide_layout)
title = slide.shapes.title
subtitle = slide.placeholders[1]
title.text = "SathyKoAchar"
subtitle.text = "\"From Our Roots, To Your Table\"\n\nBalmiki Lincoln College, Birtamode, Jhapa\nAffiliated to Lincoln University, Malaysia"

# --- Helper function for bullet slides ---
def add_bullet_slide(prs, title_text, bullet_points):
    bullet_slide_layout = prs.slide_layouts[1]
    slide = prs.slides.add_slide(bullet_slide_layout)
    shapes = slide.shapes
    title_shape = shapes.title
    body_shape = shapes.placeholders[1]
    
    title_shape.text = title_text
    tf = body_shape.text_frame
    
    for i, point in enumerate(bullet_points):
        if i == 0:
            tf.text = point
        else:
            p = tf.add_paragraph()
            p.text = point
            p.level = 0

# --- Slide Data ---
slides_data = [
    ("Executive Summary", [
        "The Concept: Handcrafted, organic, preservative-free pickles using traditional Nepali recipes.",
        "Key Differentiator: QR code traceability (Farm-to-Jar) and 100% pure mustard oil.",
        "Location: Surunga, Jhapa, Nepal.",
        "Financial Viability: Low startup cost (NPR 65,000) with immediate profitability potential."
    ]),
    ("The Problem & The Solution", [
        "The Problem: 69.4% dislike artificial tastes; 59.5% rely on homemade pickles due to lack of trust.",
        "The Solution (SathyKoAchar):",
        " - Zero chemicals, MSG, or synthetic colors.",
        " - Eco-friendly glass packaging (preferred by 81.1%).",
        " - Authentic 'Grandmother’s Recipe' taste profile."
    ]),
    ("Market Insights (The Data)", [
        "Daily Consumption: 64.9% of respondents eat pickles daily.",
        "Oil Preference: 78.4% demand pure mustard oil (Toriko Tel).",
        "Trust Factor: 83.7% would trust the brand more with a QR code showing the ingredient source."
    ]),
    ("The Product Line", [
        "Mula (Radish): NPR 300 (400g)",
        "Mix Vegetable: NPR 325 (400g)",
        "Masu (Meat/Chicken): NPR 700 (400g)",
        "Sidra (Dried Fish): NPR 700 (400g)",
        "Chilli Garlic Paste: NPR 500",
        "Premium Festive Gift Boxes: NPR 600 - 1,800"
    ]),
    ("Business & Revenue Model", [
        "Revenue Streams:",
        " - Direct-to-Consumer (D2C) via Social Media (55%)",
        " - Retail/Kirana Stores (25%)",
        " - B2B/Restaurants (8%)",
        " - Festive Hampers (12%)",
        "Operational Plan: Cloud Kitchen (Phase 1) -> Rental Unit (Phase 2) -> Export (Phase 3)"
    ]),
    ("Marketing & Sales Strategy", [
        "Positioning: 'The only pickle brand that shows you exactly where every ingredient comes from.'",
        "Channels:",
        " - Content: Behind-the-scenes reels on Instagram/TikTok.",
        " - Engagement: 'Gift a Jar' referral programs.",
        " - Physical: Weekend sample tasting at supermarkets."
    ]),
    ("Financial Projections", [
        "Startup Investment: NPR 65,000 (Self-funded + Soft Loans).",
        "Break-Even Point: 24 Jars per month.",
        "Growth: Net Profit grows from NPR 38,000 (Year 1) to NPR 670,000 (Year 5).",
        "Profitability: Net Margin reaching ~78% by Year 5."
    ]),
    ("Legal & Organizational Structure", [
        "Legal Status: Registered Partnership Firm (Nepal Partnership Act 2020 BS).",
        "Compliance:",
        " - DFTQC Food License & Hygiene Certification.",
        " - PAN Registration.",
        " - Food Labeling Regulation 2067 BS.",
        "Team: 7 Core Partners managing Strategy, Production, Marketing, and Logistics."
    ]),
    ("SWOT Analysis", [
        "Strengths: High consumer demand for organic and mustard oil base.",
        "Weaknesses: Limited initial production capacity.",
        "Opportunities: Growing Nepal pickle export market.",
        "Threats: Price fluctuation of raw materials (Mustard oil/spices)."
    ]),
    ("Conclusion", [
        "Feasibility: Confirmed through primary data and low-cost entry model.",
        "Impact: Supports local farmers, promotes eco-friendly packaging, and preserves heritage.",
        "Final Word: SathyKoAchar is ready for launch!"
    ])
]

# Generate slides
for title, points in slides_data:
    add_bullet_slide(prs, title, points)

# Save the file
prs.save("SathyKoAchar_Presentation.pptx")
print("Presentation successfully generated as 'SathyKoAchar_Presentation.pptx'!")
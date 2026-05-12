"""
Inflatable 3D Illustrations — Landing Page Clone
Built with Reflex (Python) + Poetry
Reference: https://inflatable.wannathis.one/
"""
import reflex as rx

from landing_page.components.navbar import navbar
from landing_page.components.hero import hero
from landing_page.components.features import features_purple, features_one_click, features_use_cases
from landing_page.components.gallery import gallery
from landing_page.components.pricing import pricing
from landing_page.components.footer import footer
from landing_page.components.login import login_page


# ── Global styles ──────────────────────────────────────────────────────────────
GLOBAL_STYLE = {
    # Google Fonts
    "@import": "url('https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&family=DM+Sans:ital,opsz,wght@0,9..40,300;0,9..40,400;0,9..40,600;0,9..40,700;1,9..40,300&display=swap')",
    "body": {
        "margin": "0",
        "padding": "0",
        "background_color": "#F0EFF5",
        "font_family": "'DM Sans', sans-serif",
        "overflow_x": "hidden",
    },
    "*": {
        "box_sizing": "border-box",
    },
    # Keyframe animations (injected via hero component style prop)
    "@keyframes float1": {
        "0%": {"transform": "translateY(0px) rotate(-3deg)"},
        "50%": {"transform": "translateY(-20px) rotate(2deg)"},
        "100%": {"transform": "translateY(0px) rotate(-3deg)"},
    },
    "@keyframes float2": {
        "0%": {"transform": "translateY(0px) rotate(5deg)"},
        "50%": {"transform": "translateY(-15px) rotate(-2deg)"},
        "100%": {"transform": "translateY(0px) rotate(5deg)"},
    },
    "@keyframes float3": {
        "0%": {"transform": "translateY(0px) rotate(-5deg)"},
        "50%": {"transform": "translateY(-12px) rotate(3deg)"},
        "100%": {"transform": "translateY(0px) rotate(-5deg)"},
    },
}


def index() -> rx.Component:
    """Main landing page combining all sections."""
    return rx.box(
        # Fixed navbar
        navbar(),
        # Page sections stacked vertically
        rx.vstack(
            hero(),
            features_purple(),
            features_use_cases(),
            features_one_click(),
            gallery(),
            pricing(),
            footer(),
            spacing="0",
            width="100%",
            padding="0",
            align_items="stretch",
            gap="12px",
            padding_x=["0.5rem", "0.75rem", "1rem"],
            padding_bottom="0",
        ),
        width="100%",
        min_height="100vh",
        background="#E8E5F0",
    )


# ── App ────────────────────────────────────────────────────────────────────────
app = rx.App(
    style=GLOBAL_STYLE,
    stylesheets=[
        "https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&family=DM+Sans:ital,opsz,wght@0,9..40,300;0,9..40,400;0,9..40,600;0,9..40,700;1,9..40,300&display=swap",
    ],
)

app.add_page(
    index,
    route="/",
    title="Inflatable — Abstract 3D Illustrations for Figma & Blender",
    description="Stay creative with Inflatable. Premium 3D inflatable abstract illustrations with realistic materials for Figma and Blender. 30+ objects.",
)

app.add_page(
    login_page,
    route="/login",
    title="Login — Inflatable",
    description="Login to your Inflatable account.",
)

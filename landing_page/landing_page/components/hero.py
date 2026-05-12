"""Hero section for the Inflatable landing page."""
import reflex as rx


def hero() -> rx.Component:
    return rx.box(
        # Background gradient border
        rx.box(
            # Left floating 3D object
            rx.box(
                rx.image(
                    src="/hero_yellow_donut.png",
                    width="100%",
                    height="100%",
                    object_fit="contain",
                    alt="Inflatable yellow donut",
                    style={"filter": "drop-shadow(0 20px 40px rgba(200,180,50,0.3))", "mix-blend-mode": "multiply"},
                ),
                position="absolute",
                left="-30px",
                top="30px",
                width=["200px", "280px", "380px"],
                height=["200px", "280px", "380px"],
                z_index="2",
                animation="float1 6s ease-in-out infinite",
                overflow="hidden",
                background="transparent",
            ),
            # Right floating 3D object
            rx.box(
                rx.image(
                    src="/hero_silver_flower.png",
                    width="100%",
                    height="100%",
                    object_fit="contain",
                    alt="Inflatable silver flower",
                    style={"filter": "drop-shadow(0 20px 40px rgba(150,150,200,0.3))", "mix-blend-mode": "multiply"},
                ),
                position="absolute",
                right="-20px",
                top="20px",
                width=["200px", "260px", "360px"],
                height=["200px", "260px", "360px"],
                z_index="2",
                animation="float2 7s ease-in-out infinite",
                overflow="hidden",
                background="transparent",
            ),
            # Bottom-left purple blob
            rx.box(
                rx.image(
                    src="/hero_purple_blob.png",
                    width="100%",
                    height="100%",
                    object_fit="contain",
                    alt="Inflatable purple blob",
                    style={"filter": "drop-shadow(0 15px 30px rgba(100,80,200,0.25))", "mix-blend-mode": "multiply"},
                ),
                position="absolute",
                left="80px",
                bottom="-80px",
                width=["130px", "170px", "220px"],
                height=["130px", "170px", "220px"],
                z_index="2",
                animation="float3 8s ease-in-out infinite",
                overflow="hidden",
                background="transparent",
            ),
            # Hero text centered
            rx.vstack(
                rx.text(
                    "Stay creative with",
                    font_family="'DM Sans', sans-serif",
                    font_size=["0.9rem", "1rem", "1.1rem"],
                    color="#555",
                    letter_spacing="0.02em",
                ),
                rx.heading(
                    "INFLATABLE",
                    rx.box(as_="br"),
                    "ABSTRACT 3D",
                    rx.box(as_="br"),
                    "ILLUSTRATIONS",
                    font_family="'DM Serif Display', serif",
                    font_size=["3rem", "5rem", "7.5rem", "9rem"],
                    font_weight="900",
                    color="#0a0a0a",
                    text_align="center",
                    line_height="1",
                    letter_spacing="-0.02em",
                    as_="h1",
                ),
                spacing="4",
                align_items="center",
                z_index="5",
                position="relative",
                padding_top="2rem",
            ),
            position="relative",
            width="100%",
            height=["600px", "700px", "800px"],
            display="flex",
            align_items="center",
            justify_content="center",
            overflow="hidden",
        ),
        width="100%",
        background="linear-gradient(180deg, #F0EFF5 0%, #E8E5F0 100%)",
        border="4px solid #C5C8E8",
        border_radius="0 0 1rem 1rem",
        padding_top="80px",  # navbar offset
        style={
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
        },
    )

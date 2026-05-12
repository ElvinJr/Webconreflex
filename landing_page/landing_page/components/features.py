"""Features sections for the Inflatable landing page."""
import reflex as rx


def features_purple() -> rx.Component:
    """Purple section: GRAB ATTENTION WITH REALISTIC MATERIALS AND TEXTURES."""
    return rx.box(
        rx.vstack(
            rx.heading(
                "GRAB ATTENTION WITH REALISTIC MATERIALS AND TEXTURES",
                font_family="'DM Serif Display', serif",
                font_size=["2.5rem", "3.5rem", "5rem", "6rem"],
                font_weight="900",
                color="#F5C842",
                text_align="center",
                line_height="1.05",
                letter_spacing="-0.01em",
                max_width="1000px",
                as_="h2",
            ),
            # Big 3D image
            rx.box(
                rx.image(
                    src="/feature_pink_blob.png",
                    width="100%",
                    max_width="600px",
                    height="auto",
                    object_fit="contain",
                    alt="Inflatable pink and purple blob",
                    style={"filter": "drop-shadow(0 30px 60px rgba(0,0,0,0.4))", "mix-blend-mode": "multiply"},
                ),
                width="100%",
                display="flex",
                justify_content="center",
                margin_top="2rem",
            ),
            # Description text
            rx.text(
                "We've carefully selected materials and textures that capture the essence "
                "of the inflatable style. They add a tactility to your designs, making "
                "them feel more interactive and engaging.",
                font_family="'DM Sans', sans-serif",
                font_size=["0.95rem", "1rem", "1.1rem"],
                color="rgba(255,255,255,0.85)",
                text_align="center",
                max_width="600px",
                line_height="1.7",
            ),
            spacing="6",
            align_items="center",
            padding_x=["1.5rem", "2rem", "3rem"],
            padding_y=["4rem", "6rem", "8rem"],
        ),
        width="100%",
        background="linear-gradient(160deg, #8B5ECA 0%, #6B3FA8 50%, #7C5CBF 100%)",
        border="4px solid #C5C8E8",
        border_radius="1rem",
        overflow="hidden",
    )


def features_one_click() -> rx.Component:
    """Dark section: CHANGE COLORS IN 1 CLICK."""
    return rx.box(
        rx.grid(
            # Left: Blender screenshot mockup
            rx.box(
                rx.box(
                    # Color picker mockup
                    rx.vstack(
                        rx.box(
                            rx.text(
                                "🎨 Color Picker",
                                font_size="0.75rem",
                                color="#ccc",
                                font_family="'DM Sans', sans-serif",
                            ),
                            rx.box(
                                width="180px",
                                height="180px",
                                border_radius="50%",
                                background="conic-gradient(from 0deg, #ff0000, #ffff00, #00ff00, #00ffff, #0000ff, #ff00ff, #ff0000)",
                                margin_top="0.5rem",
                            ),
                            rx.grid(
                                rx.box(rx.text("Hue", font_size="0.65rem", color="#aaa", font_family="'DM Sans', sans-serif")),
                                rx.box(rx.text("0.684", font_size="0.65rem", color="#fff", font_family="'DM Sans', sans-serif")),
                                rx.box(rx.text("Saturation", font_size="0.65rem", color="#aaa", font_family="'DM Sans', sans-serif")),
                                rx.box(rx.text("0.699", font_size="0.65rem", color="#fff", font_family="'DM Sans', sans-serif")),
                                rx.box(rx.text("Value", font_size="0.65rem", color="#aaa", font_family="'DM Sans', sans-serif")),
                                rx.box(rx.text("0.982", font_size="0.65rem", color="#fff", font_family="'DM Sans', sans-serif")),
                                columns="2",
                                spacing="2",
                                margin_top="0.75rem",
                                padding="0.5rem",
                                background="rgba(255,255,255,0.1)",
                                border_radius="6px",
                            ),
                            padding="1rem",
                            background="rgba(0,0,0,0.5)",
                            border_radius="10px",
                            border="1px solid rgba(255,255,255,0.15)",
                            width="220px",
                        ),
                        # Purple 3D fist/object below
                        rx.box(
                            rx.box(
                                width="200px",
                                height="200px",
                                border_radius="50%",
                                background="radial-gradient(circle at 40% 35%, #A889E0, #7B5CBF 60%, #4A2D8A)",
                                style={"filter": "blur(0px) drop-shadow(0 10px 30px rgba(100,60,180,0.5))"},
                            ),
                            margin_top="1rem",
                        ),
                        align_items="center",
                    ),
                    position="relative",
                ),
                display="flex",
                align_items="center",
                justify_content="center",
                padding="3rem",
            ),
            # Right: Text
            rx.vstack(
                rx.text(
                    "CHANGE COLORS IN",
                    font_family="'DM Serif Display', serif",
                    font_size=["2rem", "3rem", "4rem"],
                    font_weight="900",
                    color="#5B9CF6",
                    letter_spacing="-0.01em",
                    line_height="1",
                ),
                rx.text(
                    "1 CLICK",
                    font_family="'DM Serif Display', serif",
                    font_size=["3rem", "5rem", "7rem"],
                    font_weight="900",
                    color="#5B9CF6",
                    letter_spacing="-0.02em",
                    line_height="0.9",
                ),
                rx.text(
                    "Adjust colors according to your brand book or client needs with just one click in Blender.",
                    font_family="'DM Sans', sans-serif",
                    font_size=["0.9rem", "1rem", "1.1rem"],
                    color="rgba(255,255,255,0.75)",
                    line_height="1.7",
                    max_width="400px",
                    margin_top="1rem",
                ),
                spacing="2",
                align_items="flex-start",
                justify_content="center",
                padding=["2rem", "3rem"],
            ),
            columns="2",
            gap="0",
            width="100%",
        ),
        width="100%",
        background="linear-gradient(135deg, #080810 0%, #0D0D1A 50%, #060610 100%)",
        border="4px solid #C5C8E8",
        border_radius="1rem",
        overflow="hidden",
        min_height="450px",
    )


def features_use_cases() -> rx.Component:
    """Light section about use cases."""
    return rx.box(
        rx.vstack(
            rx.text(
                "PERFECT FOR",
                font_family="'DM Serif Display', serif",
                font_size=["2rem", "3rem", "4.5rem"],
                font_weight="900",
                color="#0a0a0a",
                letter_spacing="-0.01em",
                text_align="center",
            ),
            rx.hstack(
                *[
                    rx.box(
                        rx.vstack(
                            rx.text(icon, font_size="2rem"),
                            rx.text(
                                title,
                                font_family="'DM Sans', sans-serif",
                                font_weight="700",
                                font_size="1rem",
                                color="#0a0a0a",
                                text_align="center",
                            ),
                            rx.text(
                                desc,
                                font_family="'DM Sans', sans-serif",
                                font_size="0.85rem",
                                color="#666",
                                text_align="center",
                                line_height="1.6",
                            ),
                            spacing="2",
                            align_items="center",
                        ),
                        padding="2rem 1.5rem",
                        background="#fff",
                        border_radius="1rem",
                        border="1px solid rgba(0,0,0,0.08)",
                        flex="1",
                        min_width="180px",
                        style={
                            "box_shadow": "0 4px 20px rgba(0,0,0,0.06)",
                            "_hover": {"transform": "translateY(-4px)", "transition": "all 0.2s ease"},
                            "transition": "all 0.2s ease",
                        },
                    )
                    for icon, title, desc in [
                        ("🌐", "Websites", "Landing pages, portfolios, and marketing sites"),
                        ("📱", "Mobile Apps", "UI illustrations, onboarding screens"),
                        ("🎨", "Presentations", "Slides, pitch decks, and reports"),
                        ("✉️", "Social Media", "Posts, stories, and brand content"),
                    ]
                ],
                spacing="4",
                flex_wrap="wrap",
                justify_content="center",
            ),
            spacing="8",
            align_items="center",
            padding_x=["1.5rem", "2rem", "4rem"],
            padding_y=["4rem", "6rem"],
        ),
        width="100%",
        background="#F0EFF5",
        border="4px solid #C5C8E8",
        border_radius="1rem",
    )

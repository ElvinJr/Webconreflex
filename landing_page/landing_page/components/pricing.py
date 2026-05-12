"""Pricing section for the Inflatable landing page."""
import reflex as rx


def pricing_card_full_set() -> rx.Component:
    features = [
        "30 illustrations",
        "Inflatable trending style",
        "Stylish materials",
        "Blender source file",
        "Figma file",
        "PNG files",
    ]
    return rx.box(
        rx.vstack(
            rx.text(
                "FULL SET",
                font_family="'DM Serif Display', serif",
                font_size=["2rem", "2.5rem", "3rem"],
                font_weight="900",
                color="#fff",
                letter_spacing="-0.01em",
            ),
            rx.vstack(
                *[
                    rx.hstack(
                        rx.text("✳", color="#dbb9ff", font_size="1rem"),
                        rx.text(
                            f,
                            font_family="'DM Sans', sans-serif",
                            font_size="0.95rem",
                            color="rgba(255,255,255,0.9)",
                        ),
                        spacing="2",
                        align_items="center",
                    )
                    for f in features
                ],
                spacing="2",
                align_items="flex-start",
            ),
            # 3D object decoration
            rx.box(
                rx.box(
                    width="180px",
                    height="180px",
                    border_radius="50%",
                    background="radial-gradient(circle at 35% 30%, #C9A0FF, #9B6EE8 55%, #6B3FA8)",
                    style={"filter": "blur(1px) drop-shadow(0 10px 30px rgba(100,40,200,0.6))"},
                ),
                display="flex",
                justify_content="flex-end",
                margin_top="1rem",
                padding_right="1rem",
            ),
            rx.button(
                "PURCHASE, $36",
                width="100%",
                background="transparent",
                border="2px solid rgba(255,255,255,0.7)",
                border_radius="999px",
                color="#fff",
                font_family="'DM Sans', sans-serif",
                font_weight="700",
                font_size="0.85rem",
                letter_spacing="0.08em",
                padding_y="1em",
                cursor="pointer",
                _hover={
                    "background": "rgba(255,255,255,0.15)",
                    "transition": "all 0.2s ease",
                },
                transition="all 0.2s ease",
                margin_top="auto",
            ),
            spacing="4",
            align_items="stretch",
            height="100%",
        ),
        background="linear-gradient(145deg, #A87DE0 0%, #8B5CBF 50%, #7040A0 100%)",
        border_radius="1.2rem",
        padding=["1.5rem", "2rem", "2.5rem"],
        flex="1",
        min_width="280px",
        position="relative",
        overflow="hidden",
    )


def pricing_card_pro() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.text(
                "Pro Access",
                font_family="'DM Sans', sans-serif",
                font_size="0.85rem",
                color="#666",
                letter_spacing="0.02em",
            ),
            rx.text(
                "GET ACCESS TO HUGE LIBRARY OF 3D ILLUSTRATIONS & MOCKUPS. 5000+ ASSETS AND REGULAR RELEASES",
                font_family="'DM Serif Display', serif",
                font_size=["1.5rem", "2rem", "2.5rem"],
                font_weight="900",
                color="#0a0a0a",
                letter_spacing="-0.01em",
                line_height="1.1",
            ),
            rx.button(
                "TRY, $12/MONTH",
                width="100%",
                background="#0a0a0a",
                border="none",
                border_radius="999px",
                color="#fff",
                font_family="'DM Sans', sans-serif",
                font_weight="700",
                font_size="0.85rem",
                letter_spacing="0.08em",
                padding_y="1em",
                cursor="pointer",
                _hover={
                    "background": "#333",
                    "transition": "all 0.2s ease",
                },
                transition="all 0.2s ease",
                margin_top="auto",
            ),
            spacing="4",
            align_items="stretch",
            height="100%",
        ),
        background="#F5F3EF",
        border_radius="1.2rem",
        padding=["1.5rem", "2rem", "2.5rem"],
        flex="1",
        min_width="280px",
    )


def demo_banner() -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.text(
                "DEMO",
                font_family="'DM Serif Display', serif",
                font_size=["1.5rem", "2rem"],
                font_weight="900",
                color="#fff",
                letter_spacing="-0.01em",
            ),
            rx.text(
                "Not sure about Inflatable set? Give it a free try!",
                font_family="'DM Sans', sans-serif",
                font_size=["0.85rem", "1rem"],
                color="rgba(255,255,255,0.8)",
                flex="1",
            ),
            rx.button(
                "DOWNLOAD",
                background="transparent",
                border="1.5px solid rgba(255,255,255,0.6)",
                border_radius="999px",
                color="#fff",
                font_family="'DM Sans', sans-serif",
                font_weight="700",
                font_size="0.8rem",
                letter_spacing="0.08em",
                padding_x="1.5em",
                padding_y="0.7em",
                cursor="pointer",
                white_space="nowrap",
                _hover={
                    "background": "rgba(255,255,255,0.15)",
                    "transition": "all 0.2s ease",
                },
                transition="all 0.2s ease",
            ),
            spacing="6",
            align_items="center",
            flex_wrap="wrap",
        ),
        background="rgba(255,255,255,0.06)",
        border="1px solid rgba(255,255,255,0.15)",
        border_radius="0.8rem",
        padding=["1.5rem", "2rem"],
        margin_top="1.5rem",
    )


def pricing() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.text(
                "DESIGN WITH SPEED AND QUALITY",
                font_family="'DM Serif Display', serif",
                font_size=["2.5rem", "3.5rem", "5rem"],
                font_weight="900",
                color="#fff",
                text_align="center",
                letter_spacing="-0.02em",
                line_height="1",
                max_width="800px",
            ),
            rx.hstack(
                pricing_card_full_set(),
                pricing_card_pro(),
                spacing="4",
                align_items="stretch",
                flex_wrap="wrap",
                width="100%",
            ),
            demo_banner(),
            spacing="8",
            align_items="center",
            padding_x=["1.5rem", "2rem", "4rem"],
            padding_y=["4rem", "6rem"],
            width="100%",
            max_width="1000px",
            margin="0 auto",
        ),
        width="100%",
        background="linear-gradient(180deg, #090912 0%, #0D0D1E 100%)",
        border="4px solid #C5C8E8",
        border_radius="1rem",
        overflow="hidden",
    )

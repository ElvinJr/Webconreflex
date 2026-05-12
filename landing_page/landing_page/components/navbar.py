"""Navbar component for the Inflatable landing page."""
import reflex as rx


def navbar() -> rx.Component:
    return rx.box(
        rx.hstack(
            # Logo
            rx.link(
                rx.hstack(
                    rx.text(
                        "INFLATABLE",
                        font_size="0.9rem",
                        font_weight="700",
                        letter_spacing="0.08em",
                        color="#0a0a0a",
                        font_family="'DM Sans', sans-serif",
                    ),
                    rx.text(
                        "by",
                        font_size="0.75rem",
                        color="#555",
                        font_family="'DM Sans', sans-serif",
                        margin_x="4px",
                    ),
                    rx.box(
                        rx.text("👾", font_size="1.1rem"),
                        background="#0a0a0a",
                        border_radius="50%",
                        width="26px",
                        height="26px",
                        display="flex",
                        align_items="center",
                        justify_content="center",
                    ),
                    spacing="1",
                    align_items="center",
                ),
                href="/",
                text_decoration="none",
                _hover={"opacity": 0.8},
                transition="opacity 0.2s ease",
            ),
            # CTA Buttons
            rx.hstack(
                rx.link(
                    rx.button(
                        "LOGIN",
                        background="transparent",
                        border="1.5px solid rgba(0,0,0,0.1)",
                        border_radius="999px",
                        color="#555",
                        font_family="'DM Sans', sans-serif",
                        font_size="0.7rem",
                        font_weight="600",
                        letter_spacing="0.06em",
                        padding_x="1.5em",
                        padding_y="0.6em",
                        cursor="pointer",
                        _hover={
                            "background": "rgba(0,0,0,0.05)",
                            "color": "#0a0a0a",
                            "border": "1.5px solid #0a0a0a",
                        },
                        transition="all 0.2s ease",
                    ),
                    href="/login",
                    text_decoration="none",
                ),
                rx.button(
                    "DOWNLOAD, FOR FIGMA AND BLENDER",
                    background="transparent",
                    border="1.5px solid #0a0a0a",
                    border_radius="999px",
                    color="#0a0a0a",
                    font_family="'DM Sans', sans-serif",
                    font_size="0.7rem",
                    font_weight="600",
                    letter_spacing="0.06em",
                    padding_x="1.2em",
                    padding_y="0.6em",
                    cursor="pointer",
                    _hover={
                        "background": "#0a0a0a",
                        "color": "#fff",
                        "transition": "all 0.2s ease",
                    },
                    transition="all 0.2s ease",
                ),
                spacing="3",
                align_items="center",
            ),
            justify_content="space-between",
            align_items="center",
            width="100%",
            padding_x=["1.5rem", "2rem", "3rem"],
            padding_y="1.2rem",
        ),
        position="fixed",
        top="0",
        left="0",
        right="0",
        z_index="100",
        background="rgba(240, 239, 245, 0.85)",
        backdrop_filter="blur(12px)",
        border_bottom="1px solid rgba(0,0,0,0.06)",
    )

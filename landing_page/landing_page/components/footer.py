"""Footer component for the Inflatable landing page."""
import reflex as rx

FOOTER_LINKS = {
    "Products": ["Mockups", "Abstract", "Freebies", "Characters", "Themes", "⚡ Pro Access"],
    "Legal info": ["License", "Affiliate program", "Blog", "Order custom", "Terms of Use", "help@wannathis.one"],
}

SOCIAL_ICONS = ["📷", "🅱", "📌", "🐦"]


def footer_link(text: str, highlight: bool = False) -> rx.Component:
    return rx.link(
        text,
        href="#",
        font_family="'DM Sans', sans-serif",
        font_size="0.9rem",
        color="#F5C842" if highlight else "rgba(255,255,255,0.6)",
        text_decoration="none",
        _hover={"color": "#fff", "transition": "color 0.15s ease"},
        transition="color 0.15s ease",
    )


def footer() -> rx.Component:
    return rx.box(
        # Main footer content
        rx.grid(
            # Brand
            rx.vstack(
                rx.hstack(
                    rx.text(
                        "MADE BY",
                        font_family="'DM Sans', sans-serif",
                        font_size="0.8rem",
                        font_weight="700",
                        color="#fff",
                        letter_spacing="0.08em",
                    ),
                    rx.box(
                        rx.text("👾", font_size="1rem"),
                        background="#333",
                        border_radius="50%",
                        width="28px",
                        height="28px",
                        display="flex",
                        align_items="center",
                        justify_content="center",
                    ),
                    spacing="2",
                    align_items="center",
                ),
                spacing="2",
                align_items="flex-start",
            ),
            # Empty spacer column
            rx.box(),
            # Products links
            rx.vstack(
                rx.text(
                    "Products",
                    font_family="'DM Sans', sans-serif",
                    font_size="0.85rem",
                    font_weight="700",
                    color="#fff",
                    margin_bottom="0.75rem",
                ),
                *[
                    footer_link(link, highlight=(link.startswith("⚡")))
                    for link in FOOTER_LINKS["Products"]
                ],
                spacing="3",
                align_items="flex-start",
            ),
            # Legal links
            rx.vstack(
                rx.text(
                    "Legal info",
                    font_family="'DM Sans', sans-serif",
                    font_size="0.85rem",
                    font_weight="700",
                    color="#fff",
                    margin_bottom="0.75rem",
                ),
                *[footer_link(link) for link in FOOTER_LINKS["Legal info"]],
                spacing="3",
                align_items="flex-start",
            ),
            # Follow us
            rx.vstack(
                rx.text(
                    "Follow us",
                    font_family="'DM Sans', sans-serif",
                    font_size="0.85rem",
                    font_weight="700",
                    color="#fff",
                    margin_bottom="0.75rem",
                ),
                rx.hstack(
                    *[
                        rx.link(
                            rx.box(
                                rx.text(social["icon"], font_size="1rem"),
                                width="36px",
                                height="36px",
                                border_radius="50%",
                                background="rgba(255,255,255,0.1)",
                                display="flex",
                                align_items="center",
                                justify_content="center",
                                cursor="pointer",
                                _hover={"background": "rgba(255,255,255,0.2)", "transition": "all 0.15s ease"},
                                transition="all 0.15s ease",
                            ),
                            href=social["link"],
                            is_external=True,
                        )
                        for social in [
                            {"icon": "📷", "link": "https://www.instagram.com/elvinjr_?igsh=MWFtaWE1amN3bzEzcw=="},
                            {"icon": "💡", "link": "https://www.landingfolio.com/inspiration/post/inflatable?category=landing-page"},
                            {"icon": "📌", "link": "https://br.pinterest.com/wannathisone/"},
                            {"icon": "🐦", "link": "https://x.com/wannathis3d"},
                        ]
                    ],
                    spacing="2",
                ),
                spacing="3",
                align_items="flex-start",
            ),
            columns="4",
            gap="3rem",
            width="100%",
        ),
        # Bottom bar
        rx.box(
            rx.text(
                "© 2026 All Rights Reserved",
                font_family="'DM Sans', sans-serif",
                font_size="0.8rem",
                color="rgba(255,255,255,0.35)",
            ),
            margin_top="4rem",
            padding_top="2rem",
            border_top="1px solid rgba(255,255,255,0.08)",
        ),
        padding_x=["1.5rem", "2rem", "4rem"],
        padding_y=["4rem", "5rem"],
        background="linear-gradient(180deg, #090912 0%, #0A0A14 100%)",
        border="4px solid #C5C8E8",
        border_radius="1rem 1rem 0 0",
    )

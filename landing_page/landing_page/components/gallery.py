"""Gallery section for the Inflatable landing page."""
import reflex as rx

GALLERY_ITEMS = [
    {
        "src": "/gallery_yellow_flower.png",
        "alt": "Yellow puffy flower",
        "label": "Yellow Flower",
        "color": "#FFF9E0",
    },
    {
        "src": "/gallery_green_stick.png",
        "alt": "Green inflatable stick",
        "label": "Green Stick",
        "color": "#E8F5E8",
    },
    {
        "src": "/hero_purple_blob.png",
        "alt": "Purple inflatable cube",
        "label": "Purple Cube",
        "color": "#EDE8F8",
    },
    {
        "src": "/feature_pink_blob.png",
        "alt": "Pink abstract blob",
        "label": "Pink Blob",
        "color": "#FDE8F0",
    },
    {
        "src": "/hero_silver_flower.png",
        "alt": "Iridescent flower",
        "label": "Silver Flower",
        "color": "#E8EEF8",
    },
    {
        "src": "/hero_yellow_donut.png",
        "alt": "Yellow donut",
        "label": "Yellow Donut",
        "color": "#FFF5DC",
    },
]


def gallery_card(item: dict) -> rx.Component:
    return rx.box(
        rx.box(
            rx.image(
                src=item["src"],
                width="100%",
                height="100%",
                object_fit="contain",
                alt=item["alt"],
                padding="1rem",
                style={"mix-blend-mode": "multiply"},
            ),
            width="100%",
            height="220px",
            display="flex",
            align_items="center",
            justify_content="center",
            background=item["color"],
            border_radius="0.8rem 0.8rem 0 0",
        ),
        rx.box(
            rx.text(
                item["label"],
                font_family="'DM Sans', sans-serif",
                font_size="0.85rem",
                font_weight="600",
                color="#0a0a0a",
            ),
            padding="0.75rem 1rem",
            background="#fff",
            border_radius="0 0 0.8rem 0.8rem",
        ),
        border_radius="0.8rem",
        overflow="hidden",
        border="1px solid rgba(0,0,0,0.08)",
        style={
            "box_shadow": "0 4px 20px rgba(0,0,0,0.07)",
            "transition": "all 0.25s ease",
            "_hover": {
                "transform": "translateY(-6px) scale(1.02)",
                "box_shadow": "0 12px 40px rgba(0,0,0,0.14)",
            },
        },
        cursor="pointer",
    )


def gallery() -> rx.Component:
    return rx.box(
        rx.vstack(
            # Section header
            rx.hstack(
                rx.vstack(
                    rx.text(
                        "30 OBJECTS",
                        font_family="'DM Serif Display', serif",
                        font_size=["3rem", "5rem", "7rem"],
                        font_weight="900",
                        color="#0a0a0a",
                        letter_spacing="-0.03em",
                        line_height="1",
                    ),
                    rx.text(
                        "LOTS OF DIFFERENT SHAPES AND FORMS",
                        font_family="'DM Sans', sans-serif",
                        font_size=["0.9rem", "1rem", "1.1rem"],
                        font_weight="600",
                        color="#555",
                        letter_spacing="0.05em",
                    ),
                    spacing="2",
                    align_items="flex-start",
                ),
                justify_content="center",
                width="100%",
                padding_x=["1.5rem", "2rem", "4rem"],
            ),
            # Gallery grid
            rx.grid(
                *[gallery_card(item) for item in GALLERY_ITEMS],
                columns="3",
                gap="1.25rem",
                width="100%",
                padding_x=["1.5rem", "2rem", "4rem"],
            ),
            spacing="8",
            align_items="stretch",
            padding_y=["4rem", "6rem"],
        ),
        width="100%",
        background="#F0EFF5",
        border="4px solid #C5C8E8",
        border_radius="1rem",
    )

"""Login page component for the Inflatable landing page."""
import reflex as rx
from landing_page.components.navbar import navbar


def login_page() -> rx.Component:
    """The login page of the application."""
    return rx.box(
        # Include the navbar for consistent navigation
        navbar(),
        
        # Main login container
        rx.center(
            rx.vstack(
                # Header
                rx.vstack(
                    rx.heading(
                        "Welcome Back",
                        font_size="2.5rem",
                        font_weight="700",
                        color="#0a0a0a",
                        font_family="'DM Serif Display', serif",
                    ),
                    rx.text(
                        "Enter your credentials to access your account",
                        font_size="1rem",
                        color="#666",
                        font_family="'DM Sans', sans-serif",
                    ),
                    align_items="center",
                    spacing="2",
                    margin_bottom="2.5rem",
                ),
                
                # Form
                rx.vstack(
                    rx.input(
                        placeholder="Email Address",
                        type="email",
                        width="100%",
                        padding_y="1.5rem",
                        padding_x="1rem",
                        border_radius="16px",
                        background="white",
                        border="1px solid rgba(0,0,0,0.08)",
                        _focus={
                            "border": "1.5px solid #0a0a0a",
                            "box_shadow": "none",
                        },
                    ),
                    rx.input(
                        placeholder="Password",
                        type="password",
                        width="100%",
                        padding_y="1.5rem",
                        padding_x="1rem",
                        border_radius="16px",
                        background="white",
                        border="1px solid rgba(0,0,0,0.08)",
                        _focus={
                            "border": "1.5px solid #0a0a0a",
                            "box_shadow": "none",
                        },
                    ),
                    rx.button(
                        "LOG IN",
                        width="100%",
                        background="#0a0a0a",
                        color="white",
                        padding_y="1.6rem",
                        border_radius="16px",
                        font_weight="700",
                        letter_spacing="0.1em",
                        font_size="0.8rem",
                        cursor="pointer",
                        _hover={
                            "background": "#333",
                            "transform": "translateY(-2px)",
                            "box_shadow": "0 10px 20px rgba(0,0,0,0.1)",
                        },
                        transition="all 0.2s ease",
                        margin_top="1rem",
                    ),
                    spacing="4",
                    width="100%",
                ),
                
                # Footer links
                rx.vstack(
                    rx.link(
                        "Forgot your password?",
                        href="#",
                        font_size="0.85rem",
                        color="#888",
                        _hover={"color": "#0a0a0a"},
                        transition="color 0.2s ease",
                    ),
                    rx.divider(margin_y="1.5rem", border_color="rgba(0,0,0,0.05)"),
                    rx.hstack(
                        rx.text("Don't have an account?", font_size="0.85rem", color="#666"),
                        rx.link(
                            "Create one",
                            href="#",
                            font_size="0.85rem",
                            font_weight="700",
                            color="#0a0a0a",
                            _hover={"text_decoration": "underline"},
                        ),
                        spacing="2",
                    ),
                    rx.link(
                        "← Volver a la página principal",
                        href="/",
                        font_size="0.85rem",
                        color="#666",
                        margin_top="1.5rem",
                        _hover={"color": "#0a0a0a", "text_decoration": "none"},
                        transition="color 0.2s ease",
                    ),
                    align_items="center",
                    width="100%",
                ),
                
                # Card Styling
                padding="3.5rem",
                background="rgba(255, 255, 255, 0.7)",
                backdrop_filter="blur(20px)",
                border_radius="32px",
                box_shadow="0 25px 50px -12px rgba(0, 0, 0, 0.08)",
                border="1px solid rgba(255, 255, 255, 0.8)",
                width=["90%", "450px"],
                align_items="center",
            ),
            width="100%",
            height="100vh",
            padding_top="80px", # Space for fixed navbar
        ),
        width="100%",
        min_height="100vh",
        background="#E8E5F0",
    )

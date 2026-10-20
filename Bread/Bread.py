import reflex as rx

class State(rx.State):
    pass  # Add any interactive state later (cart, modals, etc.)

def promo_banner() -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.text("TESTING TESTING TESTING", weight="bold", color="white"),
            rx.text("3 Months of Mojo for Just $99", weight="bold", color="#f97316"),
            rx.link("Subscribe & Save", href="#", color="white", underline="always"),
            spacing="2",
            justify="center",
            width="100%",
        ),
        bg="#111827",
        padding="0.6rem",
        width="100%",
    )

def navbar() -> rx.Component:
    return rx.hstack(
        rx.heading("Books", size="6", weight="bold"),
        rx.spacer(),
        rx.hstack(
            rx.link("Learn", href="#"),
            rx.link("App", href="#"),
            rx.link("Founder", href="#"),
            rx.link("Shop", href="#"),
            spacing="6",
        ),
        rx.hstack(
            rx.icon("search"),
            rx.icon("user"),
            spacing="4",
        ),
        padding="1rem 2rem",
        bg="#0f172a",
        color="white",
        width="100%",
        position="sticky",
        top="0",
        z_index="1000",
    )

def hero() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.heading(
                "Your 90-Day Comeback",
                size="9",
                weight="bold",
                text_align="center",
            ),
            rx.heading(
                "Starts at $99",
                size="9",
                weight="bold",
                color="#f97316",
                text_align="center",
            ),
            rx.text(
                "The most complete natural testosterone formula on the market. "
                "More testosterone produced. More of it unlocked.",
                size="5",
                color="#94a3b8",
                text_align="center",
                max_width="600px",
            ),
            rx.button(
                "Shop Kino Mojo",
                size="4",
                bg="#f97316",
                color="white",
                _hover={"bg": "#ea580c"},
                padding="1.2rem 2.5rem",
            ),
            spacing="5",
            align="center",
            padding="6rem 2rem",
        ),
        bg="linear-gradient(180deg, #0f172a 0%, #111827 100%)",
        width="100%",
        min_height="70vh",
    )

def product_card(title: str, description: str, button_text: str) -> rx.Component:
    return rx.card(
        rx.vstack(
            rx.heading(title, size="6"),
            rx.text(description, color="#94a3b8", size="3"),
            rx.button(button_text, variant="outline", color_scheme="orange"),
            spacing="3",
            align="start",
        ),
        width="100%",
        bg="#1e293b",
        border="1px solid #334155",
    )

def products_section() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.heading("Elite formulas for the high-performance life.", size="8", text_align="center"),
            rx.text(
                "Experience the difference of premium ingredients clinically dosed to support lean muscle, "
                "healthy testosterone, and sustained focus.",
                color="#94a3b8",
                text_align="center",
                max_width="700px",
            ),
            rx.grid(
                product_card(
                    "The Mojo Stack",
                    "Two supplements. One goal. Free testosterone + blood flow & performance.",
                    "Shop The Mojo Stack",
                ),
                product_card(
                    "Boost Testosterone",
                    "7 clinically dosed natural ingredients to restore healthy testosterone and drive.",
                    "Shop Kino Mojo",
                ),
                product_card(
                    "Fuel Your Training",
                    "Clean pre-workout with smooth energy and sharp focus — no jitters or crash.",
                    "Shop Kino Octane",
                ),
                columns="3",
                spacing="4",
                width="100%",
            ),
            spacing="6",
            align="center",
            padding="5rem 2rem",
        ),
        bg="#0f172a",
        width="100%",
    )

def info_columns() -> rx.Component:
    return rx.grid(
        rx.vstack(
            rx.heading("Our Mission", size="5"),
            rx.text(
                "Kinobody isn't about grinding 5–6 days a week. Build a lean, powerful, movie-star physique "
                "with just 2–3 focused workouts a week.",
                color="#94a3b8",
            ),
            rx.button("Learn More", variant="ghost", color_scheme="orange"),
            spacing="3",
            align="start",
        ),
        rx.vstack(
            rx.heading("Natural Ingredients", size="5"),
            rx.text(
                "All natural, clinically dosed, manufactured at a GMP-certified facility. "
                "Third-party tested. Never underdosed.",
                color="#94a3b8",
            ),
            rx.button("Learn More", variant="ghost", color_scheme="orange"),
            spacing="3",
            align="start",
        ),
        rx.vstack(
            rx.heading("Guarantee", size="5"),
            rx.text(
                "Every product is backed by a 30-day money-back guarantee. Try it risk-free. "
                "If you're not satisfied, get a full refund.",
                color="#94a3b8",
            ),
            spacing="3",
            align="start",
        ),
        columns="3",
        spacing="6",
        padding="4rem 2rem",
        bg="#111827",
        width="100%",
    )

def app_promo() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.heading("Kinobody Fitness App", size="7"),
            rx.text("Transform into movie star shape.", size="5", color="#94a3b8"),
            rx.button("Get the App", size="3", bg="#f97316", color="white"),
            spacing="4",
            align="center",
            padding="4rem 2rem",
        ),
        bg="#0f172a",
        width="100%",
    )

def index() -> rx.Component:
    return rx.box(
        promo_banner(),
        navbar(),
        hero(),
        products_section(),
        info_columns(),
        app_promo(),
        width="100%",
        bg="#0f172a",
        color="white",
        font_family="Inter, sans-serif",
    )

app = rx.App(
    theme=rx.theme(
        appearance="dark",
        accent_color="orange",
        radius="medium",
    )
)
app.add_page(index)

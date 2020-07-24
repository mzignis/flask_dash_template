import dash_bootstrap_components as dbc

navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink('Home', href='/dash/')),
        dbc.DropdownMenu(
            children=[
                dbc.DropdownMenuItem("Pages", header=True),
                dbc.DropdownMenuItem("Page 1", href="/dash/page1"),
                dbc.DropdownMenuItem("Page 2", href="/dash/page2"),
                dbc.DropdownMenuItem(divider=True),
                dbc.DropdownMenuItem("Logout", href='/dash/logout')
            ],
            nav=True,
            in_navbar=True,
            label="Profile",
        ),
    ],
    brand="Login Page Template",
    brand_href="/dash/",
    color="#337ab7",
    dark=True,
)
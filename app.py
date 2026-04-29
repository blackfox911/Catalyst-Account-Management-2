import os
from datetime import datetime

import pandas as pd
import plotly.express as px
import streamlit as st


st.set_page_config(
    page_title="CATALYST BRAND Pro",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown(
    """
    <style>
    :root {
        --bg: #0b0b0c;
        --panel: #141416;
        --panel-soft: #1b1b1f;
        --line: #2a2b31;
        --text: #f4f4f5;
        --muted: #9f9fa8;
        --accent: #ff6a2f;
        --accent-soft: rgba(255, 106, 47, 0.18);
        --success: #5fd19b;
    }
    .stApp {
        background:
            radial-gradient(circle at top right, rgba(255,106,47,0.12), transparent 22%),
            linear-gradient(180deg, #0a0a0b 0%, #111214 100%);
        color: var(--text);
    }
    [data-testid="stHeader"] { background: rgba(0,0,0,0); }
    section[data-testid="stSidebar"] {
        background: #111113;
        border-right: 1px solid var(--line);
    }
    section[data-testid="stSidebar"] > div {
        padding-top: 1rem;
    }
    .block-container {
        padding-top: 1rem;
        padding-bottom: 2rem;
        max-width: 1400px;
    }
    .topbar, .glass-card, .table-shell, .wallet-shell, .chart-shell {
        background: linear-gradient(180deg, rgba(32,33,39,0.92), rgba(21,22,25,0.98));
        border: 1px solid var(--line);
        border-radius: 22px;
        box-shadow: 0 14px 40px rgba(0,0,0,0.28);
    }
    .topbar {
        padding: 16px 20px;
        margin-bottom: 12px;
    }
    .topbar-title {
        font-size: 1.35rem;
        font-weight: 700;
        color: var(--text);
    }
    .muted {
        color: var(--muted);
        font-size: 0.88rem;
    }
    .hero-card {
        border-radius: 22px;
        padding: 20px;
        min-height: 152px;
        border: 1px solid rgba(255,255,255,0.06);
        background: linear-gradient(145deg, #ff5b1f 0%, #ff7f45 52%, #fff0e9 100%);
        color: white;
        box-shadow: 0 18px 40px rgba(255,106,47,0.28);
    }
    .kpi-card {
        border-radius: 22px;
        padding: 20px;
        min-height: 152px;
        border: 1px solid var(--line);
        background:
            linear-gradient(180deg, rgba(255,255,255,0.06), rgba(255,255,255,0.01)),
            linear-gradient(145deg, #2a2b30 0%, #191a1f 100%);
        color: var(--text);
    }
    .card-eyebrow {
        font-size: 0.8rem;
        color: rgba(255,255,255,0.72);
        margin-bottom: 8px;
    }
    .hero-card .card-eyebrow { color: rgba(255,255,255,0.86); }
    .card-title {
        font-size: 1.05rem;
        font-weight: 600;
        margin-bottom: 2px;
    }
    .card-subtitle {
        font-size: 0.82rem;
        color: var(--muted);
        margin-bottom: 22px;
    }
    .hero-card .card-subtitle { color: rgba(255,255,255,0.78); }
    .card-value {
        font-size: 2rem;
        font-weight: 800;
        line-height: 1.05;
        margin-bottom: 12px;
    }
    .card-chip {
        display: inline-block;
        padding: 6px 10px;
        border-radius: 999px;
        font-size: 0.76rem;
        background: rgba(255,255,255,0.18);
        color: white;
    }
    .wallet-shell, .chart-shell, .table-shell { padding: 16px 18px; }
    .wallet-shell, .chart-shell { margin-bottom: 4px; }
    .section-title {
        font-size: 1.05rem;
        font-weight: 700;
        margin-bottom: 4px;
    }
    .wallet-card {
        border-radius: 18px;
        padding: 14px;
        background: linear-gradient(180deg, #1f2025 0%, #18191d 100%);
        border: 1px solid rgba(255,255,255,0.06);
        margin-bottom: 8px;
    }
    .wallet-card .currency {
        color: var(--muted);
        font-size: 0.8rem;
        margin-bottom: 10px;
    }
    .wallet-card .amount {
        font-size: 1.2rem;
        font-weight: 700;
    }
    .wallet-card .status {
        margin-top: 8px;
        font-size: 0.75rem;
        color: var(--success);
    }
    div[data-testid="stTabs"] {
        margin-top: 18px;
    }
    .stTabs [data-baseweb="tab-list"] {
        gap: 10px;
        background: transparent;
    }
    .stTabs [data-baseweb="tab"] {
        background: #1a1b20;
        border: 1px solid var(--line);
        border-radius: 12px 12px 0 0;
        padding: 10px 16px;
        color: var(--muted);
    }
    .stTabs [aria-selected="true"] {
        background: linear-gradient(180deg, #ff6a2f 0%, #ff7b42 100%) !important;
        color: white !important;
        border-color: transparent !important;
    }
    [data-testid="stDataFrame"], [data-testid="stTable"] {
        border: 1px solid var(--line);
        border-radius: 16px;
        overflow: hidden;
    }
    [data-testid="stMetric"] {
        background: transparent !important;
    }
    .stButton > button, .stDownloadButton > button, [data-testid="baseButton-secondary"] {
        border-radius: 12px;
        border: 1px solid rgba(255,255,255,0.08);
    }
    .stButton > button[kind="primary"] {
        background: linear-gradient(180deg, #ff6a2f 0%, #ff854f 100%);
        color: white;
        border: none;
    }
    .sidebar-brand {
        padding: 10px 12px 16px 12px;
        border-bottom: 1px solid rgba(255,255,255,0.06);
        margin-bottom: 12px;
    }
    .sidebar-brand-title {
        font-size: 1.2rem;
        font-weight: 800;
    }
    .sidebar-pill {
        display: inline-block;
        margin-top: 6px;
        padding: 4px 10px;
        border-radius: 999px;
        background: var(--accent-soft);
        color: #ffc6b0;
        font-size: 0.74rem;
    }
    div[data-testid="stHorizontalBlock"] {
        gap: 0.85rem;
    }
    div[data-testid="stVerticalBlock"] > div:has(.hero-card),
    div[data-testid="stVerticalBlock"] > div:has(.kpi-card),
    div[data-testid="stVerticalBlock"] > div:has(.wallet-shell),
    div[data-testid="stVerticalBlock"] > div:has(.chart-shell) {
        margin-bottom: 0.15rem !important;
    }
    div[data-testid="stVerticalBlock"] > div:has(.wallet-shell) + div,
    div[data-testid="stVerticalBlock"] > div:has(.chart-shell) + div {
        margin-top: 0 !important;
    }
    div[data-testid="stPlotlyChart"] {
        margin-top: -10px;
    }
    div[data-testid="stPlotlyChart"] > div {
        border-radius: 18px;
        overflow: hidden;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

DEFAULT_USERNAME = "Admin"
DEFAULT_PASSWORD = "Letmein@420kid"


def normalize_credential(value):
    return str(value).strip()


def render_login():
    st.markdown(
        """
        <style>
        section[data-testid="stSidebar"] { display: none !important; }
        [data-testid="stHeader"] { display: none !important; }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div style="max-width: 520px; margin: 10vh auto 0 auto;">
            <div class="kpi-card" style="min-height: unset;">
                <div class="card-title" style="font-size: 1.25rem; font-weight: 800;">CATALYST ™ Accounts</div>
                <div class="muted" style="margin-top: 6px; margin-bottom: 18px;">Sign in to continue</div>
        """,
        unsafe_allow_html=True,
    )
    with st.form("login_form", clear_on_submit=False):
        username = st.text_input("Username", value="", placeholder="Admin")
        password = st.text_input("Password", value="", placeholder="Password", type="password")
        show_password_hint = st.checkbox("Show default login help")
        if show_password_hint:
            st.caption("Username: Admin")
            st.caption("Password: Letmein@420kid")
        submitted = st.form_submit_button("Login", use_container_width=True)

    if submitted:
        typed_username = normalize_credential(username)
        typed_password = normalize_credential(password)
        valid_username = typed_username.lower() == DEFAULT_USERNAME.lower()
        valid_password = typed_password == DEFAULT_PASSWORD or typed_password.lower() == DEFAULT_PASSWORD.lower()

        if valid_username and valid_password:
            st.session_state["is_authenticated"] = True
            st.rerun()
        else:
            st.error("Invalid credentials. Check spelling, case, and extra spaces.")

    st.markdown("</div></div></div>", unsafe_allow_html=True)


if "is_authenticated" not in st.session_state:
    st.session_state["is_authenticated"] = False

if not st.session_state["is_authenticated"]:
    render_login()
    st.stop()

INVENTORY_COLUMNS = ["Product Name", "Quantity", "Cost Price", "Sale Price"]
SALES_COLUMNS = ["Date", "Product Name", "Quantity Sold", "Price Per Item", "Total Revenue"]
ASSET_COLUMNS = ["Asset Name", "Quantity", "Price Per Asset"]
LIABILITY_COLUMNS = ["Liability Name", "Amount"]
CASH_COLUMNS = ["Cash at Hand", "Amount"]


def load_data(file_path, default_data, columns):
    if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
        df = pd.read_csv(file_path)
    else:
        df = pd.DataFrame(default_data)
        df.to_csv(file_path, index=False)
    for column in columns:
        if column not in df.columns:
            df[column] = ""
    return df[columns].copy()


def clean_text(value):
    if pd.isna(value):
        return ""
    return str(value).strip()


def clean_inventory(df):
    df = df.copy()
    for col in INVENTORY_COLUMNS:
        if col not in df.columns:
            df[col] = ""

    df["Product Name"] = df["Product Name"].apply(clean_text)
    for col in ["Quantity", "Cost Price", "Sale Price"]:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    df = df.dropna(subset=["Quantity", "Cost Price", "Sale Price"])
    df = df[df["Product Name"] != ""]
    df = df[(df["Quantity"] >= 0) & (df["Cost Price"] >= 0) & (df["Sale Price"] >= 0)]
    df["Quantity"] = df["Quantity"].astype(int)
    df = df.drop_duplicates(subset=["Product Name"], keep="last")
    return df.reset_index(drop=True)


def clean_assets(df):
    df = df.copy()
    for col in ASSET_COLUMNS:
        if col not in df.columns:
            df[col] = ""
    df["Asset Name"] = df["Asset Name"].apply(clean_text)
    for col in ["Quantity", "Price Per Asset"]:
        df[col] = pd.to_numeric(df[col], errors="coerce")
    df = df.dropna(subset=["Quantity", "Price Per Asset"])
    df = df[df["Asset Name"] != ""]
    df = df[(df["Quantity"] >= 0) & (df["Price Per Asset"] >= 0)]
    df["Quantity"] = df["Quantity"].astype(int)
    return df.reset_index(drop=True)


def clean_liabilities(df):
    df = df.copy()
    for col in LIABILITY_COLUMNS:
        if col not in df.columns:
            df[col] = ""
    df["Liability Name"] = df["Liability Name"].apply(clean_text)
    df["Amount"] = pd.to_numeric(df["Amount"], errors="coerce")
    df = df.dropna(subset=["Amount"])
    df = df[df["Liability Name"] != ""]
    df = df[df["Amount"] >= 0]
    return df.reset_index(drop=True)


def clean_cash(df):
    df = df.copy()
    for col in CASH_COLUMNS:
        if col not in df.columns:
            df[col] = ""
    df["Cash at Hand"] = df["Cash at Hand"].apply(clean_text)
    df["Amount"] = pd.to_numeric(df["Amount"], errors="coerce")
    df = df.dropna(subset=["Amount"])
    df = df[df["Cash at Hand"] != ""]
    df = df[df["Amount"] >= 0]
    return df.reset_index(drop=True)


def clean_sales(df):
    df = df.copy()
    for col in SALES_COLUMNS:
        if col not in df.columns:
            df[col] = ""
    df["Product Name"] = df["Product Name"].apply(clean_text)
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
    for col in ["Quantity Sold", "Price Per Item", "Total Revenue"]:
        df[col] = pd.to_numeric(df[col], errors="coerce")
    df = df.dropna(subset=["Date", "Quantity Sold", "Price Per Item", "Total Revenue"])
    df = df[df["Product Name"] != ""]
    df = df[(df["Quantity Sold"] > 0) & (df["Price Per Item"] >= 0) & (df["Total Revenue"] >= 0)]
    df["Quantity Sold"] = df["Quantity Sold"].astype(int)
    return df.sort_values("Date").reset_index(drop=True)


def save_inventory(df):
    cleaned = clean_inventory(df)
    cleaned.to_csv("inventory.csv", index=False)
    return cleaned


def save_assets(df):
    cleaned = clean_assets(df)
    cleaned.to_csv("assets.csv", index=False)
    return cleaned


def save_liabilities(df):
    cleaned = clean_liabilities(df)
    cleaned.to_csv("liabilities.csv", index=False)
    return cleaned


def save_cash(df):
    cleaned = clean_cash(df)
    cleaned.to_csv("cash_at_hand.csv", index=False)
    return cleaned


def format_sale_label(row):
    sale_date = pd.to_datetime(row["Date"], errors="coerce")
    date_text = sale_date.strftime("%Y-%m-%d %H:%M") if pd.notna(sale_date) else "Unknown date"
    return (
        f'{date_text} | {row["Product Name"]} | '
        f'Qty: {int(row["Quantity Sold"])} | Revenue: ${float(row["Total Revenue"]):,.2f}'
    )


def format_money(value, prefix="$", decimals=2):
    return f"{prefix}{float(value):,.{decimals}f}"


def render_kpi_card(title, subtitle, value, footer, highlighted=False):
    card_class = "hero-card" if highlighted else "kpi-card"
    st.markdown(
        f"""
        <div class="{card_class}">
            <div class="card-eyebrow">Overview</div>
            <div class="card-title">{title}</div>
            <div class="card-subtitle">{subtitle}</div>
            <div class="card-value">{value}</div>
            <div class="card-chip">{footer}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_wallet_card(currency, amount, status):
    st.markdown(
        f"""
        <div class="wallet-card">
            <div class="currency">{currency}</div>
            <div class="amount">{amount}</div>
            <div class="status">{status}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


inventory = clean_inventory(
    load_data(
        "inventory.csv",
        [{"Product Name": "Gadget Pro", "Quantity": 50, "Cost Price": 100.0, "Sale Price": 250.0}],
        INVENTORY_COLUMNS,
    )
)
sales = clean_sales(
    load_data(
        "sales.csv",
        {"Date": [], "Product Name": [], "Quantity Sold": [], "Price Per Item": [], "Total Revenue": []},
        SALES_COLUMNS,
    )
)
assets = clean_assets(
    load_data(
        "assets.csv",
        [{"Asset Name": "Office Studio", "Quantity": 1, "Price Per Asset": 15000.0}],
        ASSET_COLUMNS,
    )
)
liabilities = clean_liabilities(
    load_data(
        "liabilities.csv",
        [{"Liability Name": "Business Loan", "Amount": 5000.0}],
        LIABILITY_COLUMNS,
    )
)

default_cash_on_hand = float(sales["Total Revenue"].sum()) if not sales.empty else 10000.0
cash_at_hand_entries = clean_cash(
    load_data(
        "cash_at_hand.csv",
        [{"Cash at Hand": "Default", "Amount": default_cash_on_hand}],
        CASH_COLUMNS,
    )
)
cash_on_hand = float(cash_at_hand_entries["Amount"].sum()) if not cash_at_hand_entries.empty else 0.0
inventory_val = float((inventory["Quantity"] * inventory["Cost Price"]).sum()) if not inventory.empty else 0.0
fixed_assets_val = float((assets["Quantity"] * assets["Price Per Asset"]).sum()) if not assets.empty else 0.0
total_liabilities = float(liabilities["Amount"].sum()) if not liabilities.empty else 0.0
net_worth = (cash_on_hand + inventory_val + fixed_assets_val) - total_liabilities

sales_count = len(sales)
products_count = len(inventory)
recent_sales = sales.sort_values("Date", ascending=False).copy() if not sales.empty else pd.DataFrame(columns=SALES_COLUMNS)

with st.sidebar:
    st.markdown(
        """
        <div class="sidebar-brand">
            <div class="sidebar-brand-title">CATALYST ™ Accounts</div>
            <div class="sidebar-pill">Pro Dashboard</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    if st.button("Logout", use_container_width=True):
        st.session_state["is_authenticated"] = False
        st.rerun()
    st.text_input("Search", placeholder="Search")
    st.markdown("##### Navigation")
    selected_page = st.radio(
        "Navigation",
        ["Dashboard", "Inventory", "Sales Entry", "Fixed Assets", "Liabilities", "Balance Sheet"],
        index=0,
        label_visibility="collapsed",
    )
    st.divider()
    st.markdown("##### Workspace")
    st.caption(f"{products_count} active products")
    st.caption(f"{sales_count} sales entries")
    st.caption(f"{len(assets)} fixed assets")
    st.caption(f"{len(liabilities)} liabilities")

st.markdown(
    f"""
    <div class="topbar">
        <div class="muted">CATALYST BRAND / {selected_page}</div>
        <div class="topbar-title">{selected_page}</div>
        <div class="muted">Track inventory, cash flow, refunds, assets, and liabilities in one place.</div>
    </div>
    """,
    unsafe_allow_html=True,
)

if selected_page == "Dashboard":
    row1, row2, row3 = st.columns(3, gap="small")
    with row1:
        render_kpi_card(
            "My balance",
            "Your current revenue-backed cash position",
            format_money(cash_on_hand),
            f"{sales_count} sales recorded",
            highlighted=True,
        )
    with row2:
        render_kpi_card(
            "Inventory value",
            "Current stock value at cost",
            format_money(inventory_val),
            f"{products_count} products tracked",
        )
    with row3:
        render_kpi_card(
            "Net worth",
            "Assets minus liabilities",
            format_money(net_worth),
            f"Liabilities {format_money(total_liabilities)}",
        )

    col_left, col_right = st.columns([1.05, 1.8], gap="small")

    with col_left:
        st.markdown(
            """
            <div class="wallet-shell">
                <div class="section-title">My Wallet</div>
                <div class="muted">Estimated balances across your key currencies</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        wallet_cols = st.columns(2, gap="small")
        with wallet_cols[0]:
            render_wallet_card("USD", format_money(cash_on_hand), "Base currency")
            render_wallet_card("EUR", format_money(cash_on_hand * 0.92, prefix="EUR "), "Estimated rate")
        with wallet_cols[1]:
            render_wallet_card("GBP", format_money(cash_on_hand * 0.78, prefix="GBP "), "Estimated rate")
            render_wallet_card("KES", f"KES {cash_on_hand * 130:,.0f}", "Estimated rate")

    with col_right:
        st.markdown(
            """
            <div class="chart-shell">
                <div class="section-title">Dashboard Insights</div>
                <div class="muted">Asset mix and revenue trend</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        charts_cols = st.columns(2, gap="small")

        # Pie chart: composition of assets (cash vs inventory vs fixed assets).
        with charts_cols[0]:
            total_assets = cash_on_hand + inventory_val + fixed_assets_val
            st.markdown(
                """
                <div class="section-title" style="margin-bottom: 2px;">Asset Mix</div>
                <div class="muted" style="margin-bottom: 10px;">Cash, inventory, and fixed assets</div>
                """,
                unsafe_allow_html=True,
            )
            if total_assets > 0:
                pie_df = pd.DataFrame(
                    {
                        "Asset": ["Cash at hand", "Inventory", "Fixed assets"],
                        "Value": [cash_on_hand, inventory_val, fixed_assets_val],
                    }
                )
                fig_pie = px.pie(
                    pie_df,
                    names="Asset",
                    values="Value",
                    template="plotly_dark",
                    hole=0.35,
                )
                fig_pie.update_layout(
                    paper_bgcolor="rgba(0,0,0,0)",
                    plot_bgcolor="rgba(0,0,0,0)",
                    margin=dict(l=0, r=0, t=0, b=0),
                    font=dict(color="#f4f4f5"),
                    legend_title_text="",
                )
                st.plotly_chart(fig_pie, use_container_width=True)
            else:
                st.info("Add cash, inventory, or fixed assets to see your mix.")

        # Line graph: cumulative revenue over time.
        with charts_cols[1]:
            st.markdown(
                """
                <div class="section-title" style="margin-bottom: 2px;">Revenue Trend</div>
                <div class="muted" style="margin-bottom: 10px;">Cumulative sales revenue</div>
                """,
                unsafe_allow_html=True,
            )
            if not sales.empty:
                chart_data = sales.sort_values("Date").copy()
                chart_data["Cumulative Revenue"] = chart_data["Total Revenue"].cumsum()
                fig_line = px.line(
                    chart_data,
                    x="Date",
                    y="Cumulative Revenue",
                    template="plotly_dark",
                    markers=True,
                    color_discrete_sequence=["#FE6A35"],
                )
                fig_line.update_layout(
                    paper_bgcolor="rgba(0,0,0,0)",
                    plot_bgcolor="rgba(0,0,0,0)",
                    margin=dict(l=0, r=0, t=0, b=0),
                    font=dict(color="#f4f4f5"),
                    xaxis_title="",
                    yaxis_title="",
                )
                st.plotly_chart(fig_line, use_container_width=True)
            else:
                st.info("Start recording sales to see the revenue trend.")

    st.divider()

    st.markdown('<div class="table-shell">', unsafe_allow_html=True)
    st.markdown("### Recent Activities")
    st.caption("Latest sales transactions and revenue activity.")
    if recent_sales.empty:
        st.info("No recent sales activity yet.")
    else:
        activity_table = recent_sales[["Product Name", "Quantity Sold", "Date", "Total Revenue"]].copy()
        activity_table["Date"] = activity_table["Date"].dt.strftime("%d %b, %Y %I:%M %p")
        activity_table["Total Revenue"] = activity_table["Total Revenue"].map(lambda x: format_money(x))
        activity_table = activity_table.rename(
            columns={
                "Product Name": "Activity",
                "Quantity Sold": "Units",
                "Date": "Date",
                "Total Revenue": "Revenue",
            }
        )
        st.dataframe(activity_table.head(8), use_container_width=True, hide_index=True)
    st.markdown("</div>", unsafe_allow_html=True)

if selected_page == "Inventory":
    st.subheader("Edit Inventory Stocks")
    st.caption("Product names now accept normal text. Empty names, duplicates, and negative values are cleaned before saving.")
    edited_inv = st.data_editor(
        inventory,
        num_rows="dynamic",
        use_container_width=True,
        key="ed_inv",
        column_config={
            "Product Name": st.column_config.TextColumn("Product Name", required=True, help="Enter letters or mixed product names."),
            "Quantity": st.column_config.NumberColumn("Quantity", min_value=0, step=1, format="%d"),
            "Cost Price": st.column_config.NumberColumn("Cost Price", min_value=0.0, step=1.0, format="%.2f"),
            "Sale Price": st.column_config.NumberColumn("Sale Price", min_value=0.0, step=1.0, format="%.2f"),
        },
    )
    if st.button("Update Inventory"):
        cleaned_inventory = save_inventory(edited_inv)
        if cleaned_inventory.empty:
            st.error("Add at least one valid product with a name, quantity, and prices.")
        else:
            st.success("Inventory updated successfully.")
            st.rerun()

    st.markdown("#### Delete Inventory Entry")
    if inventory.empty:
        st.info("No inventory entries available to delete.")
    else:
        inventory_options = {
            f'{row["Product Name"]} | Qty: {int(row["Quantity"])} | Sale: ${float(row["Sale Price"]):,.2f}': idx
            for idx, row in inventory.iterrows()
        }
        selected_inventory_label = st.selectbox(
            "Choose inventory item to delete",
            list(inventory_options.keys()),
            key="delete_inventory_select",
        )
        if st.button("Delete Inventory Entry", type="secondary"):
            updated_inventory = inventory.drop(index=inventory_options[selected_inventory_label]).reset_index(drop=True)
            save_inventory(updated_inventory)
            st.success("Inventory entry deleted.")
            st.rerun()

if selected_page == "Sales Entry":
    col_s1, col_s2 = st.columns([1, 2])
    product_names = inventory["Product Name"].tolist()
    with col_s1:
        st.subheader("New Sale")
        if not product_names:
            st.warning("Add inventory items first before recording sales.")
        else:
            with st.form("sale_form", clear_on_submit=True):
                prod = st.selectbox("Product", product_names)
                stock_qty = int(inventory.loc[inventory["Product Name"] == prod, "Quantity"].iloc[0])
                price_item = float(inventory.loc[inventory["Product Name"] == prod, "Sale Price"].iloc[0])
                st.caption(f"Available stock: {stock_qty} | Unit price: ${price_item:,.2f}")
                qty = int(st.number_input("Qty Sold", min_value=1, step=1))
                submitted = st.form_submit_button("Finalize Transaction")

            if submitted:
                if qty > stock_qty:
                    st.error(f"Not enough stock for {prod}. Available: {stock_qty}.")
                else:
                    updated_inventory = inventory.copy()
                    idx = updated_inventory.index[updated_inventory["Product Name"] == prod][0]
                    updated_inventory.at[idx, "Quantity"] = stock_qty - qty

                    new_row = pd.DataFrame(
                        [
                            {
                                "Date": datetime.now(),
                                "Product Name": prod,
                                "Quantity Sold": qty,
                                "Price Per Item": price_item,
                                "Total Revenue": qty * price_item,
                            }
                        ]
                    )
                    updated_sales = clean_sales(pd.concat([sales, new_row], ignore_index=True))

                    save_inventory(updated_inventory)
                    updated_sales.to_csv("sales.csv", index=False)
                    st.balloons()
                    st.success("Sale recorded successfully.")
                    st.rerun()

    with col_s2:
        st.subheader("History")
        if sales.empty:
            st.info("No sales recorded yet.")
        else:
            history = sales.sort_values("Date", ascending=False).copy()
            history["Date"] = history["Date"].dt.strftime("%Y-%m-%d %H:%M")
            st.dataframe(history.head(10), use_container_width=True)

            st.markdown("#### Delete Sale / Process Refund")
            sales_view = sales.sort_values("Date", ascending=False).reset_index()
            sales_options = {format_sale_label(row): int(row["index"]) for _, row in sales_view.iterrows()}
            selected_sale_label = st.selectbox(
                "Choose sale entry to delete or refund",
                list(sales_options.keys()),
                key="delete_sale_select",
            )
            if st.button("Delete Sale And Restore Stock", type="secondary"):
                sale_idx = sales_options[selected_sale_label]
                sale_row = sales.loc[sale_idx]

                updated_sales = sales.drop(index=sale_idx).reset_index(drop=True)
                updated_inventory = inventory.copy()
                product_match = updated_inventory["Product Name"] == sale_row["Product Name"]

                if product_match.any():
                    inventory_idx = updated_inventory.index[product_match][0]
                    updated_inventory.at[inventory_idx, "Quantity"] = (
                        int(updated_inventory.at[inventory_idx, "Quantity"]) + int(sale_row["Quantity Sold"])
                    )
                    save_inventory(updated_inventory)
                    updated_sales.to_csv("sales.csv", index=False)
                    st.success("Sale deleted and stock restored.")
                else:
                    updated_sales.to_csv("sales.csv", index=False)
                    st.warning("Sale deleted, but stock was not restored because the product no longer exists in inventory.")
                st.rerun()

if selected_page == "Fixed Assets":
    st.subheader("Fixed Assets")
    edited_ast = st.data_editor(
        assets,
        num_rows="dynamic",
        use_container_width=True,
        key="ed_ast",
        column_config={
            "Asset Name": st.column_config.TextColumn("Asset Name", required=True),
            "Quantity": st.column_config.NumberColumn("Quantity", min_value=0, step=1, format="%d"),
            "Price Per Asset": st.column_config.NumberColumn("Price Per Asset", min_value=0.0, step=1.0, format="%.2f"),
        },
    )
    if st.button("Save Assets"):
        save_assets(edited_ast)
        st.success("Assets saved.")
        st.rerun()

    st.markdown("#### Delete Asset Entry")
    if assets.empty:
        st.info("No asset entries available to delete.")
    else:
        asset_options = {
            f'{row["Asset Name"]} | Qty: {int(row["Quantity"])} | Price: ${float(row["Price Per Asset"]):,.2f}': idx
            for idx, row in assets.iterrows()
        }
        selected_asset_label = st.selectbox(
            "Choose asset entry to delete",
            list(asset_options.keys()),
            key="delete_asset_select",
        )
        if st.button("Delete Asset Entry", type="secondary"):
            updated_assets = assets.drop(index=asset_options[selected_asset_label]).reset_index(drop=True)
            save_assets(updated_assets)
            st.success("Asset entry deleted.")
            st.rerun()

if selected_page == "Liabilities":
    st.subheader("Liabilities")
    edited_lb = st.data_editor(
        liabilities,
        num_rows="dynamic",
        use_container_width=True,
        key="ed_lb",
        column_config={
            "Liability Name": st.column_config.TextColumn("Liability Name", required=True),
            "Amount": st.column_config.NumberColumn("Amount", min_value=0.0, step=1.0, format="%.2f"),
        },
    )
    if st.button("Save Liabilities"):
        save_liabilities(edited_lb)
        st.success("Liabilities saved.")
        st.rerun()

    st.markdown("#### Delete Liability Entry")
    if liabilities.empty:
        st.info("No liability entries available to delete.")
    else:
        liability_options = {
            f'{row["Liability Name"]} | Amount: ${float(row["Amount"]):,.2f}': idx
            for idx, row in liabilities.iterrows()
        }
        selected_liability_label = st.selectbox(
            "Choose liability entry to delete",
            list(liability_options.keys()),
            key="delete_liability_select",
        )
        if st.button("Delete Liability Entry", type="secondary"):
            updated_liabilities = liabilities.drop(index=liability_options[selected_liability_label]).reset_index(drop=True)
            save_liabilities(updated_liabilities)
            st.success("Liability entry deleted.")
            st.rerun()

if selected_page == "Balance Sheet":
    tabs = st.tabs(["Financial Position", "Cash at Hand"])
    with tabs[0]:
        st.header("Financial Position")
        st.table(
            pd.DataFrame(
                {
                    "Category": [
                        "Total Cash Assets",
                        "Inventory Valuation",
                        "Fixed Assets",
                        "LESS: Liabilities",
                        "OWNER EQUITY",
                    ],
                    "Amount": [
                        f"${cash_on_hand:,.2f}",
                        f"${inventory_val:,.2f}",
                        f"${fixed_assets_val:,.2f}",
                        f"-${total_liabilities:,.2f}",
                        f"${net_worth:,.2f}",
                    ],
                }
            )
        )

    with tabs[1]:
        st.subheader("Cash at Hand Entries")
        st.caption("Add one or more cash amounts (e.g., petty cash, main cash). These values are used in the Balance Sheet.")

        edited_cash = st.data_editor(
            cash_at_hand_entries,
            num_rows="dynamic",
            use_container_width=True,
            key="ed_cash",
            column_config={
                "Cash at Hand": st.column_config.TextColumn("Cash at Hand", required=True),
                "Amount": st.column_config.NumberColumn("Amount", min_value=0.0, step=1.0, format="%.2f"),
            },
        )

        if st.button("Save Cash at Hand"):
            save_cash(edited_cash)
            st.success("Cash at hand saved.")
            st.rerun()

        st.markdown("#### Delete Cash Entry")
        if cash_at_hand_entries.empty:
            st.info("No cash at hand entries available to delete.")
        else:
            cash_options = {
                f'{row["Cash at Hand"]} | Amount: ${float(row["Amount"]):,.2f}': idx
                for idx, row in cash_at_hand_entries.iterrows()
            }
            selected_cash_label = st.selectbox(
                "Choose cash entry to delete",
                list(cash_options.keys()),
                key="delete_cash_select",
            )
            if st.button("Delete Cash Entry", type="secondary"):
                updated_cash = cash_at_hand_entries.drop(index=cash_options[selected_cash_label]).reset_index(drop=True)
                save_cash(updated_cash)
                st.success("Cash entry deleted.")
                st.rerun()
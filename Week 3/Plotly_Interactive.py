# ==============================================================================
# INTERACTIVE DATA VISUALIZATIONS WITH PLOTLY EXPRESS
# ==============================================================================
# Plotly Express (px) is a high-level Python visualization library designed for
# creating rich, interactive, publication-quality figures with simple syntax.
#
# Unlike static libraries (Matplotlib/Seaborn), Plotly figures are interactive:
# - Zoom and Pan smoothly across data points
# - Hover tooltips that reveal exact underlying values
# - Toggle traces and categories on/off in the legend
# - Export figures as PNG images directly from the browser viewer
# - Save interactive figures to standalone HTML files
#
# Visualizations covered in this file:
# 1. Geographic Choropleth Map (Gapminder Global GDP per Capita)
# 2. Interactive Time-Series Line Plot (USD vs INR Currency Exchange Rates)
# ==============================================================================

import pandas as pd
import plotly.express as px

# ------------------------------------------------------------------------------
# 1. GEOGRAPHIC CHOROPLETH MAP: Global GDP per Capita
# ------------------------------------------------------------------------------
# A Choropleth map is a thematic map where geographic areas (e.g. countries)
# are shaded or patterned in proportion to a statistical variable (e.g. GDP).

print("Fetching Gapminder dataset from GitHub...")
gapminder_url = 'https://raw.githubusercontent.com/plotly/datasets/master/gapminder_with_codes.csv'

try:
    data = pd.read_csv(gapminder_url)
    print("Dataset preview:")
    print(data.head(3))

    # Create the choropleth map
    # - locations: Column containing country identifiers (3-letter ISO Alpha-3 codes, e.g. USA, IND, BRA)
    # - color: Numerical column determining fill color intensity
    # - hover_name: Field shown in bold at the top of the tooltip when hovering over a country
    # - projection: Map projection type ('natural earth', 'orthographic', 'mercator', etc.)
    # - title: Title displayed above the map
    fig_map = px.choropleth(
        data,
        locations='iso_alpha',
        color='gdpPercap',
        hover_name='country',
        projection='natural earth',
        title='GDP per Capita by Country (Gapminder)',
        color_continuous_scale=px.colors.sequential.Plasma
    )

    # Optional: Save standalone HTML for offline viewing
    fig_map.write_html("choropleth_map.html")
    print("Saved interactive map to 'choropleth_map.html'")

    # fig.show() launches your default browser with the interactive plot
    print("Launching interactive Choropleth Map...")
    fig_map.show()

except Exception as e:
    print(f"Error fetching Gapminder data: {e}")


# ------------------------------------------------------------------------------
# 2. INTERACTIVE TIME-SERIES LINE PLOT: Dollar vs Rupee Exchange Rate
# ------------------------------------------------------------------------------
# Plotly's line charts allow instant date zooming, range selection, and point inspection.

print("\nFetching Currency Exchange Rates dataset...")
exchange_url = 'https://raw.githubusercontent.com/datasets/currency-exchange-rates/master/data/currency-exchange-rates.csv'

try:
    dollar_conv = pd.read_csv(exchange_url)
    print("Currency dataset preview:")
    print(dollar_conv.head(3))

    # Create interactive line plot
    # - x: Date / Time column for the horizontal axis
    # - y: Currency rate for the vertical axis
    # - title: Plot title
    fig_line = px.line(
        dollar_conv,
        x='DATE',
        y='RATE',
        title='Dollar vs Rupee Historical Exchange Rate'
    )

    # Enhance layout with range sliders and unified hovermode
    fig_line.update_layout(
        xaxis_title="Date",
        yaxis_title="Exchange Rate (INR per USD)",
        hovermode="x unified"
    )

    # Optional: Save standalone HTML
    fig_line.write_html("dollar_vs_rupee.html")
    print("Saved interactive line chart to 'dollar_vs_rupee.html'")

    # Display interactive figure
    print("Launching interactive Line Plot...")
    fig_line.show()

except Exception as e:
    print(f"Error fetching currency exchange data: {e}")

